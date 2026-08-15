from __future__ import annotations

import logging
import re
from datetime import date, datetime, timedelta, timezone

from src import cinii_client, jstage_client
from src.classifier import classify
from src.content_analyzer import analyze
from src.config import SEARCH_GROUPS, Config, jst_today
from src.deduplicator import duplicate_of, merge_articles
from src.models import Article, NA
from src.scorer import score
from src.storage import append_articles, load_articles, rank_articles, save_processed, write_report
from src.evidence_card import write_cards

LOG = logging.getLogger(__name__)


def is_japanese(article: Article) -> bool:
    text = " ".join([article.title_ja, article.abstract_ja])
    return bool(re.search(r"[\u3040-\u30ff\u3400-\u9fff]", text))


def is_recent(article: Article, days: int, today: date | None = None) -> bool:
    today = today or jst_today()
    cutoff = today - timedelta(days=days)
    for value in (article.updated_date, article.online_date, article.publication_date):
        if value == NA:
            continue
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00")).date()
            return cutoff <= parsed <= today
        except ValueError:
            pass
    # 日付が年までしかないAPI項目は当年のみ候補に残す。
    return article.publication_year == str(today.year)


def collect(config: Config) -> list[Article]:
    candidates = jstage_client.search(SEARCH_GROUPS, config.days_back, config.request_interval)
    if config.enable_cinii and config.cinii_app_id:
        candidates += cinii_client.search(SEARCH_GROUPS, config.cinii_app_id, config.request_interval)
    elif config.enable_cinii:
        LOG.warning("CINII_APP_IDが未設定のため、CiNii Researchを省略してJ-STAGEだけで実行します。")
    # PubMedは初期版では意図的に実装しない。有効化されても警告だけにする。
    if config.enable_pubmed_japanese:
        LOG.warning("ENABLE_PUBMED_JAPANESEは将来拡張用です。初期版はPubMedを検索しません。")

    merged: list[Article] = []
    for candidate in candidates:
        if not is_japanese(candidate) or not is_recent(candidate, config.days_back):
            continue
        old = duplicate_of(candidate, merged)
        if old:
            index = merged.index(old)
            merged[index] = merge_articles(old, candidate)
        else:
            merged.append(candidate)

    prior = load_articles(config.root / "data" / "processed_articles.json")
    new = [article for article in merged if duplicate_of(article, prior) is None]
    for article in new:
        article.categories, article.matched_keywords = classify(article)
        article.importance_score, article.importance_reason = score(article)
        analyze(article)
    new.sort(key=lambda a: a.importance_score, reverse=True)
    selected = new[:config.max_articles]
    rank_articles(selected)
    return selected


def run(config: Config) -> int:
    articles = collect(config)
    if config.dry_run:
        LOG.info("DRY_RUN: 保存予定 %d件", len(articles))
        for article in articles:
            LOG.info("文献ID: %s", article.article_key)
        return len(articles)
    if not articles:
        LOG.info("新規文献はありません。ファイルは変更しません。")
        return 0
    data_path = config.root / "data" / "articles.json"
    processed_path = config.root / "data" / "processed_articles.json"
    day = jst_today()
    write_cards(config.root, articles, day)
    append_articles(data_path, articles)
    save_processed(processed_path, load_articles(processed_path) + articles)
    path = write_report(config.root, articles, day)
    LOG.info("%d件を保存しました: %s", len(articles), path)
    return len(articles)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    run(Config.from_env())
