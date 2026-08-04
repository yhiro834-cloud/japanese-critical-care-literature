from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

NA = "記載なし"


@dataclass
class Article:
    article_key: str = NA
    jstage_article_id: str = NA
    cinii_id: str = NA
    doi: str = NA
    title_ja: str = NA
    title_en: str = NA
    abstract_ja: str = "日本語抄録なし"
    abstract_en: str = NA
    authors: list[str] = field(default_factory=list)
    affiliations: list[str] = field(default_factory=list)
    journal: str = NA
    issn: str = NA
    volume: str = NA
    issue: str = NA
    start_page: str = NA
    end_page: str = NA
    publication_year: str = NA
    publication_date: str = NA
    online_date: str = NA
    updated_date: str = NA
    article_type: str = NA
    keywords: list[str] = field(default_factory=list)
    categories: list[str] = field(default_factory=list)
    matched_keywords: list[str] = field(default_factory=list)
    importance_score: int = 1
    importance_reason: str = NA
    source_databases: list[str] = field(default_factory=list)
    jstage_url: str = NA
    cinii_url: str = NA
    doi_url: str = NA
    pdf_url: str = NA
    html_url: str = NA
    free_full_text: bool = False
    retrieved_at: str = NA
    manual_review_status: str = "未確認"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Article":
        allowed = cls.__dataclass_fields__
        return cls(**{key: value for key, value in data.items() if key in allowed})
