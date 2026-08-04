from __future__ import annotations

import re
import unicodedata
from collections.abc import Iterable

from src.models import Article, NA


def normalize_title(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "").casefold().strip()
    value = re.sub(r"[\s\u3000]+", "", value)
    return re.sub(r"[^\w\u3040-\u30ff\u3400-\u9fff]", "", value)


def _present(value: str) -> bool:
    return bool(value and value != NA)


def duplicate_of(article: Article, existing: Iterable[Article]) -> Article | None:
    for old in existing:
        if _present(article.doi) and _present(old.doi) and article.doi.casefold() == old.doi.casefold():
            return old
        if _present(article.jstage_article_id) and article.jstage_article_id == old.jstage_article_id:
            return old
        if _present(article.cinii_id) and article.cinii_id == old.cinii_id:
            return old
        same_title = normalize_title(article.title_ja) == normalize_title(old.title_ja)
        if same_title and _present(article.publication_year) and article.publication_year == old.publication_year:
            return old
        first = article.authors[0] if article.authors else ""
        old_first = old.authors[0] if old.authors else ""
        if same_title and first == old_first and article.journal == old.journal:
            return old
    return None


def merge_articles(left: Article, right: Article) -> Article:
    """情報量の多いレコードを基礎に、欠損値と取得元を相互補完する。"""
    def richness(a: Article) -> int:
        return sum(v not in (NA, "日本語抄録なし", "", [], False) for v in a.to_dict().values())
    base, other = (left, right) if richness(left) >= richness(right) else (right, left)
    data = base.to_dict()
    for key, value in other.to_dict().items():
        if data[key] in (NA, "日本語抄録なし", "", [], False) and value not in (NA, "", []):
            data[key] = value
    for key in ("source_databases", "keywords"):
        data[key] = list(dict.fromkeys(getattr(left, key) + getattr(right, key)))
    return Article.from_dict(data)
