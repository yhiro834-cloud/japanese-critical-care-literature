from __future__ import annotations

from src.models import Article

CATEGORY_KEYWORDS = {
    "人工呼吸": ["人工呼吸", "人工呼吸器", "ventilat"],
    "呼吸管理": ["呼吸管理", "nppv", "hfnc", "ards", "抜管", "再挿管"],
    "鎮痛": ["鎮痛", "疼痛", "cpot", "nrs"],
    "鎮静": ["鎮静", "rass", "sedation"],
    "せん妄": ["せん妄", "cam-icu", "delirium"],
    "早期離床": ["早期離床", "リハビリテーション"],
    "PICS・ICU-AW": ["pics", "icu-aw", "集中治療後症候群"],
    "敗血症": ["敗血症", "sepsis"],
    "循環管理": ["循環管理", "ショック", "昇圧薬"],
    "心停止・蘇生後管理": ["心停止", "心肺蘇生", "蘇生後", "pcas", "cpr"],
    "ECMO": ["ecmo", "ecpr"],
    "外傷": ["外傷", "大量輸血", "trauma"],
    "神経集中治療": ["頭部外傷", "脳出血", "脳梗塞", "神経集中治療", "tbi"],
    "感染管理": ["感染管理", "院内感染", "vap", "clabsi"],
    "栄養管理": ["栄養管理", "経腸栄養"],
    "腎・血液浄化": ["血液浄化", "持続的腎代替", "crrt"],
    "救急看護": ["救急看護", "救急外来", "トリアージ"],
    "フライトナース": ["フライトナース", "ドクターヘリ", "航空医療"],
    "病院前救護": ["病院前救護", "プレホスピタル", "救急救命士"],
    "医療安全": ["医療安全", "有害事象"],
    "家族看護": ["家族看護", "家族支援"],
    "倫理": ["倫理", "意思決定支援"],
    "終末期看護": ["終末期", "end-of-life"],
    "看護教育": ["看護教育", "新人教育", "シミュレーション教育"],
}


def classify(article: Article) -> tuple[list[str], list[str]]:
    text = " ".join([article.title_ja, article.title_en, article.abstract_ja, article.abstract_en,
                     article.journal, *article.keywords]).casefold()
    categories, matched = [], []
    for category, words in CATEGORY_KEYWORDS.items():
        hits = [word for word in words if word.casefold() in text]
        if hits:
            categories.append(category)
            matched.extend(hits)
    return categories or ["その他"], list(dict.fromkeys(matched))
