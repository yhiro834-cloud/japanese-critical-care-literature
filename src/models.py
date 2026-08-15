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
    content_review_level: str = "title_and_metadata"
    abstract_reviewed: bool = False
    fulltext_reviewed: bool = False
    study_design: str = "判定不能"
    study_design_attributes: list[str] = field(default_factory=list)
    research_objective: str = "抄録から確認できず"
    pico_applicable: bool = True
    population: str = "抄録から判定不能"
    intervention_or_exposure: str = "抄録から判定不能"
    comparison: str = "抄録から判定不能"
    primary_outcomes: list[str] = field(default_factory=list)
    secondary_outcomes: list[str] = field(default_factory=list)
    sample_size: str = NA
    number_of_facilities: str = NA
    study_setting: list[str] = field(default_factory=list)
    key_results: list[str] = field(default_factory=list)
    key_numeric_results: list[str] = field(default_factory=list)
    authors_conclusion: str = "確認できず"
    reported_limitations: list[str] = field(default_factory=list)
    automatic_cautions: list[str] = field(default_factory=list)
    extractive_summary: list[str] = field(default_factory=list)
    summary_sources: list[str] = field(default_factory=list)
    evidence_sources: dict[str, str] = field(default_factory=dict)
    extraction_confidence: str = "low"
    research_usability: str = "D"
    relevance: dict[str, str] = field(default_factory=dict)
    ranking_reason: str = NA
    literature_review_status: str = "未判定"
    exclusion_reason: str = NA
    evidence_card_path: str = NA

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Article":
        allowed = cls.__dataclass_fields__
        return cls(**{key: value for key, value in data.items() if key in allowed})
