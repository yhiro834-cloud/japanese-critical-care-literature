from __future__ import annotations

import re
from datetime import date
from pathlib import Path

from src.models import Article, NA

LEVELS = {"metadata_only": "書誌情報のみ", "title_and_metadata": "タイトル・書誌情報確認", "abstract_reviewed": "抄録確認済み", "fulltext_partially_reviewed": "本文一部確認済み", "fulltext_reviewed": "本文確認済み"}


def safe_key(value: str) -> str:
    return re.sub(r"[^0-9A-Za-z._-]+", "_", value.replace("doi:", "")).strip("._") or "unknown"


def card_path(root: Path, article: Article, day: date) -> Path:
    return root / "evidence" / f"{day:%Y}" / f"{day:%m}" / f"{safe_key(article.article_key)}.md"


def render(article: Article, day: date) -> str:
    def joined(values: list[str]) -> str: return "、".join(values) or NA
    summary = "\n".join(f"- {x}" for x in article.extractive_summary) or "- 記載なし"
    cautions = "\n".join(f"- {x}" for x in article.automatic_cautions) or "- 記載なし"
    return f"""# {article.title_ja}

## 原文由来の基本情報

- 文献ID：{article.article_key}
- DOI：{article.doi}
- 著者：{joined(article.authors)}
- 掲載誌：{article.journal}
- 発行年：{article.publication_year}
- 資料種別：{article.article_type}
- カテゴリー：{joined(article.categories)}
- 重要度：{article.importance_score}
- 取得元：{joined(article.source_databases)}
- J-STAGE URL：{article.jstage_url}
- CiNii Research URL：{article.cinii_url}
- DOI URL：{article.doi_url}
- PDF URL：{article.pdf_url}
- PDF確認状況：{article.pdf_review_status}
- PDF確認日時：{article.pdf_checked_at}
- 本文抽出文字数：{article.fulltext_character_count}
- HTML全文URL：{article.html_url}

## 内容確認状況

- 内容確認レベル：{LEVELS.get(article.content_review_level, article.content_review_level)}
- 日本語抄録：{'確認済み' if article.abstract_ja not in {'', NA, '日本語抄録なし'} else 'なし／未確認'}
- 英語抄録：{'確認済み' if article.abstract_en not in {'', NA} else 'なし／未確認'}
- 全文：{'確認済み' if article.fulltext_reviewed else '未確認'}
- 確認日時：{article.retrieved_at}

## 自動抽出（原文確認が必要）

### 研究目的
{article.research_objective}

### 研究デザイン
{article.study_design}（属性：{joined(article.study_design_attributes)}）

### 対象
{article.population}（サンプル数：{article.sample_size}、施設数：{article.number_of_facilities}）

### 介入・曝露
{article.intervention_or_exposure}

### 比較
{article.comparison}

### 評価項目
{joined(article.primary_outcomes)}

### 主な結果
{joined(article.key_results)}

### 著者の結論
{article.authors_conclusion}

### 著者が記載した研究の限界
{joined(article.reported_limitations)}

### 自動抽出された注意点
{cautions}

### 抽出的要約
{summary}

- 抽出信頼度：{article.extraction_confidence}
- 研究利用可能性：{article.research_usability}（研究の質・エビデンスレベルではありません）

## 手動評価

- 原文確認：未確認
- 研究目的：自動抽出／要確認
- 研究デザイン：自動判定／要確認
- 対象者・施設：自動抽出／要確認
- 介入・曝露：自動抽出／要確認
- 比較対象：自動抽出／要確認
- 主要評価項目：自動抽出／要確認
- 主な結果：自動抽出／要確認
- 統計解析：未評価
- バイアスリスク：未評価
- 研究の限界：未評価
- 結果の臨床的重要性：未評価
- 救命ICU看護への応用：未評価
- 救急看護への応用：未評価
- フライトナースへの応用：未評価
- 自施設への適用可能性：未評価
- 文献採用：{article.literature_review_status}
- 確認者：未記入
- 確認日：未記入

> 自動抽出は文献検討の一次整理です。数値、統計解析、結論、因果関係、推奨・推奨度、エビデンスレベルは必ず原文で確認してください。
"""


def write_cards(root: Path, articles: list[Article], day: date) -> list[Path]:
    paths = []
    for article in articles:
        path = card_path(root, article, day)
        article.evidence_card_path = str(path.relative_to(root))
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render(article, day), encoding="utf-8")
        paths.append(path)
    return paths
