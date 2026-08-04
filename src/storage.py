from __future__ import annotations

import json
import os
import tempfile
from collections import Counter
from datetime import date
from pathlib import Path

from src.models import Article, NA


def load_articles(path: Path) -> list[Article]:
    if not path.exists() or not path.read_text(encoding="utf-8").strip():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return [Article.from_dict(item) for item in data]


def _atomic_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
        temporary = stream.name
    os.replace(temporary, path)


def append_articles(path: Path, articles: list[Article]) -> None:
    current = load_articles(path)
    _atomic_json(path, [a.to_dict() for a in current + articles])


def save_processed(path: Path, articles: list[Article]) -> None:
    _atomic_json(path, [a.to_dict() for a in articles])


def report_path(root: Path, day: date) -> Path:
    return root / "literature" / f"{day:%Y}" / f"{day:%m}" / f"{day:%Y-%m-%d}.md"


def render_markdown(articles: list[Article], day: date) -> str:
    source = Counter(s for a in articles for s in a.source_databases)
    cats = Counter(c for a in articles for c in a.categories)
    top = sorted(articles, key=lambda a: a.importance_score, reverse=True)[:3]
    lines = [f"# 国内集中治療・救急文献レポート｜{day:%Y-%m-%d}", "", "## 本日の概要", "",
             f"- 新規文献数：{len(articles)}", f"- J-STAGEからの取得数：{source['J-STAGE']}",
             f"- CiNii Researchからの取得数：{source['CiNii Research']}",
             f"- 日本語抄録ありの文献数：{sum(a.abstract_ja != '日本語抄録なし' for a in articles)}",
             f"- 無料全文ありの文献数：{sum(a.free_full_text for a in articles)}",
             f"- 重要度5の文献数：{sum(a.importance_score == 5 for a in articles)}",
             f"- 重要度4の文献数：{sum(a.importance_score == 4 for a in articles)}",
             f"- 注目カテゴリー：{'、'.join(c for c, _ in cats.most_common(3)) or '該当なし'}",
             f"- 最重要文献3件：{'／'.join(a.title_ja for a in top) or '該当なし'}", "", "## 注意事項", "",
             "- このレポートは日本語文献を対象としています。",
             "- カテゴリーと重要度はプログラムによる機械的な一次分類です。",
             "- 文献の質や臨床への適用可能性を保証するものではありません。",
             "- 抄録だけでなく、原著論文や公式ガイドライン本文を確認してください。",
             "- このレポートは医学的判断の代替ではありません。", "", "## 文献一覧", ""]
    if not articles:
        lines += ["本日の新規文献はありません。", ""]
    for index, a in enumerate(articles, 1):
        lines += [f"### {index}. {a.title_ja}", "", f"- 英語タイトル：{a.title_en}",
                  f"- 著者：{'、'.join(a.authors) or NA}", f"- 所属：{'、'.join(a.affiliations) or NA}",
                  f"- 掲載誌：{a.journal}", f"- 発行年：{a.publication_year}",
                  f"- 巻・号・ページ：{a.volume}・{a.issue}・{a.start_page}-{a.end_page}", f"- DOI：{a.doi}",
                  f"- 資料種別：{a.article_type}", f"- カテゴリー：{'、'.join(a.categories)}",
                  f"- 一致キーワード：{'、'.join(a.matched_keywords) or NA}", f"- 重要度：{a.importance_score}",
                  f"- 重要度の判定理由：{a.importance_reason}", f"- 取得元：{'、'.join(a.source_databases)}",
                  f"- J-STAGE：{a.jstage_url}", f"- CiNii Research：{a.cinii_url}", f"- DOI URL：{a.doi_url}",
                  f"- 無料全文：{'あり' if a.free_full_text else '確認できず'}", f"- PDF：{a.pdf_url}", f"- HTML全文：{a.html_url}",
                  "", "#### 日本語抄録", "", a.abstract_ja, "", "#### 著者キーワード", ""]
        lines += [f"- {keyword}" for keyword in a.keywords] or ["- 記載なし"]
        lines += ["", "#### 手動確認欄", "", "- 研究目的：未確認", "- 研究デザイン：未確認", "- 対象者・施設：未確認",
                  "- 主な結果：未確認", "- 研究の限界：未確認", "- 救命ICU看護への応用：未評価", "- フライトナースへの応用：未評価",
                  "- 確認状況：未確認", ""]
    return "\n".join(lines)


def write_report(root: Path, articles: list[Article], day: date) -> Path:
    path = report_path(root, day)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_markdown(articles, day), encoding="utf-8")
    return path
