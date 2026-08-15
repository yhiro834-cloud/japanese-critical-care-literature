from __future__ import annotations

import re

from src.models import Article, NA

MISSING_ABSTRACTS = {"", NA, "日本語抄録なし"}

DESIGNS = [
    ("診療ガイドライン", r"診療ガイドライン|clinical practice guideline"),
    ("指針", r"指針"), ("声明", r"声明|statement"), ("コンセンサス", r"コンセンサス|consensus"),
    ("システマティックレビュー", r"システマティックレビュー|systematic review"),
    ("メタアナリシス", r"メタアナリシス|meta[ -]analysis"),
    ("非ランダム化比較試験", r"非ランダム化|non[- ]randomi[sz]ed"),
    ("ランダム化比較試験", r"無作為化|ランダム化|randomi[sz]ed"),
    ("前向きコホート研究", r"前向き.{0,20}コホート|prospective.{0,20}cohort"),
    ("後ろ向きコホート研究", r"後ろ向き.{0,20}コホート|retrospective.{0,20}cohort"),
    ("症例対照研究", r"症例対照|case[- ]control"), ("横断研究", r"横断研究|cross[- ]sectional"),
    ("質的研究", r"質的研究|半構造化面接|インタビュー"), ("混合研究法", r"混合研究法|mixed methods"),
    ("アンケート調査", r"アンケート|質問紙"), ("症例シリーズ", r"症例シリーズ|case series"),
    ("症例報告", r"症例報告|case report"), ("総説", r"総説|review article"),
    ("会議録", r"会議録"), ("学会抄録", r"学会抄録"),
]

ATTRIBUTES = [("多施設研究", r"多施設|multicenter|multi-center"), ("単施設研究", r"単施設|single[- ]center"),
              ("観察研究", r"観察研究|observational"), ("前向き", r"前向き|prospective"),
              ("後ろ向き", r"後ろ向き|retrospective")]

RELEVANCE = {
    "ICU看護": ["ICU", "集中治療室", "クリティカルケア"], "救急看護": ["救急看護", "救急外来"],
    "初療": ["初療", "初期診療"], "集中治療": ["集中治療", "重症患者"],
    "フライトナース": ["フライトナース", "ドクターヘリ"], "病院前救護": ["病院前", "救急救命士"],
    "看護教育": ["看護教育", "教育"], "医療安全": ["医療安全", "有害事象"],
    "家族看護": ["家族看護", "家族"], "倫理": ["倫理", "終末期"],
}


def sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[。！？])\s*|(?<=[.!?])\s+(?=[A-Z])", text) if s.strip()]


def _section_sentence(text: str, labels: str) -> str | None:
    pattern = rf"(?:^|[。\n])\s*(?:{labels})\s*[:：]\s*([^。\n]+[。]?)"
    match = re.search(pattern, text, re.I)
    return match.group(1).strip() if match else None


def detect_design(text: str) -> tuple[str, list[str]]:
    primary = next((name for name, pattern in DESIGNS if re.search(pattern, text, re.I)), "判定不能")
    attrs = [name for name, pattern in ATTRIBUTES if re.search(pattern, text, re.I)]
    if primary == "判定不能" and re.search(r"前向き|prospective", text, re.I):
        primary = "観察研究"
    if primary == "判定不能" and re.search(r"後ろ向き|retrospective", text, re.I):
        primary = "観察研究"
    return primary, attrs


def analyze(article: Article) -> Article:
    abstract = article.abstract_ja if article.abstract_ja not in MISSING_ABSTRACTS else article.abstract_en
    has_abstract = abstract not in MISSING_ABSTRACTS
    article.abstract_reviewed = has_abstract
    article.fulltext_reviewed = False  # URLの存在だけでは本文確認済みにしない。
    article.content_review_level = "abstract_reviewed" if has_abstract else ("title_and_metadata" if article.title_ja != NA else "metadata_only")
    text = " ".join([article.title_ja, abstract if has_abstract else "", " ".join(article.keywords)])
    article.study_design, article.study_design_attributes = detect_design(text)
    if not has_abstract:
        article.automatic_cautions = ["抄録しか確認できない", "全文未確認"] if article.abstract_reviewed else ["抄録未確認", "全文未確認"]
        article.relevance = relevance(text)
        return article

    objective = _section_sentence(abstract, "目的|Objective|Aim|Purpose")
    method = _section_sentence(abstract, "方法|Methods?")
    result = _section_sentence(abstract, "結果|Results?")
    conclusion = _section_sentence(abstract, "結論|Conclusions?")
    limitation = _section_sentence(abstract, "限界|研究の限界|Limitations?")
    article.research_objective = objective or "抄録から確認できず"
    article.authors_conclusion = conclusion or "確認できず"
    article.reported_limitations = [limitation] if limitation else []
    population_match = re.search(r"([^。]{0,80}?(?:患者|看護師|対象者|症例))\s*(\d+)\s*(名|例)", abstract)
    if population_match:
        article.population = population_match.group(0)
        article.sample_size = f"{population_match.group(2)}{population_match.group(3)}"
    facility_match = re.search(r"(\d+)\s*施設", abstract)
    if facility_match:
        article.number_of_facilities = f"{facility_match.group(1)}施設"
    intervention = _section_sentence(abstract, "介入|曝露|Intervention|Exposure")
    comparison = _section_sentence(abstract, "比較|対照|Comparison")
    article.intervention_or_exposure = intervention or "抄録から判定不能"
    article.comparison = comparison or "抄録から判定不能"
    article.study_setting = [x for x in ["ICU" if re.search(r"ICU|集中治療室", text, re.I) else "", "救急外来" if "救急外来" in text else "", "病院前" if "病院前" in text else ""] if x]
    article.key_results = [result] if result else []
    numeric_pattern = r"(?:p\s*[<=>]\s*\d+(?:\.\d+)?|95\s*%\s*(?:信頼区間|CI)\s*[:：]?\s*[^、。;；）)]+|(?:オッズ比|OR|ハザード比|HR)\s*[:：=]?\s*\d+(?:\.\d+)?)"
    article.key_numeric_results = [m.group(0) for m in re.finditer(numeric_pattern, result or "", re.I)]
    outcomes = [x for x in ["死亡率", "ICU死亡率", "28日死亡率", "人工呼吸器装着期間", "ICU在室日数", "入院期間", "再挿管率", "せん妄発症率", "有害事象", "感染率", "ADL", "QOL", "PICS", "疼痛", "RASS", "CAM-ICU", "患者満足度", "家族満足度"] if x.casefold() in text.casefold()]
    article.primary_outcomes = outcomes
    article.extractive_summary, article.summary_sources = [], []
    for value, source in [(objective, "abstract"), (method, "methods"), (result, "results"), (conclusion, "conclusion")]:
        if value and value not in article.extractive_summary:
            article.extractive_summary.append(value); article.summary_sources.append(source)
    article.evidence_sources = {k: "abstract" for k, v in {"research_objective": objective, "sample_size": article.sample_size != NA, "key_results": result, "authors_conclusion": conclusion}.items() if v}
    if article.study_design != "判定不能":
        article.evidence_sources["study_design"] = "abstract" if detect_design(abstract)[0] != "判定不能" else "title"
    article.automatic_cautions = [x for x in article.study_design_attributes if x in {"単施設研究", "観察研究", "後ろ向き"}]
    article.automatic_cautions.append("全文未確認")
    components = sum(bool(x) for x in [objective, method, result])
    detailed = components >= 3 and article.study_design != "判定不能" and article.sample_size != NA
    article.research_usability = "A" if detailed else ("B" if components >= 2 else "C")
    article.extraction_confidence = "high" if components >= 3 else "medium"
    article.relevance = relevance(text)
    article.pico_applicable = article.study_design not in {"質的研究", "混合研究法", "実践報告", "総説", "会議録", "学会抄録"}
    return article


def relevance(text: str) -> dict[str, str]:
    folded = text.casefold()
    result = {}
    for label, words in RELEVANCE.items():
        count = sum(word.casefold() in folded for word in words)
        result[label] = "high" if count >= 2 else ("medium" if count == 1 else "low")
    return result


def analyze_fulltext(article: Article, text: str) -> Article:
    """PDF抽出本文から、明示された文だけをEvidence Card項目へ追加する。"""
    article.fulltext_reviewed = True
    article.content_review_level = "fulltext_reviewed"
    section_patterns = {
        "research_objective": r"(?:目的|Objective|Aim|Purpose)\s*[:：]?\s*([^。\n]{10,300}[。]?)",
        "key_results": r"(?:結果|Results?)\s*[:：]?\s*([^。\n]{10,500}[。]?)",
        "authors_conclusion": r"(?:結論|Conclusions?)\s*[:：]?\s*([^。\n]{10,400}[。]?)",
        "reported_limitations": r"(?:研究の限界|限界|Limitations?)\s*[:：]?\s*([^。\n]{10,400}[。]?)",
    }
    found: list[tuple[str, str]] = []
    for field_name, pattern in section_patterns.items():
        match = re.search(pattern, text, re.I)
        if not match:
            continue
        value = match.group(1).strip()
        if field_name in {"key_results", "reported_limitations"}:
            setattr(article, field_name, [value])
        else:
            setattr(article, field_name, value)
        article.evidence_sources[field_name] = "fulltext"
        found.append((field_name, value))
    design, attributes = detect_design(text)
    if design != "判定不能":
        article.study_design = design
        article.study_design_attributes = attributes
        article.evidence_sources["study_design"] = "fulltext"
    article.extractive_summary = [value for _, value in found[:8]]
    article.summary_sources = ["results" if name == "key_results" else "conclusion" if name == "authors_conclusion" else "fulltext" for name, _ in found[:8]]
    article.extraction_confidence = "high" if len(found) >= 3 else "medium"
    article.research_usability = "A" if len(found) >= 3 else "B"
    article.automatic_cautions = [x for x in article.automatic_cautions if x != "全文未確認"]
    return article
