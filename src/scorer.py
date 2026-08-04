from __future__ import annotations

from src.models import Article

BASE_RULES = [
    (5, ["診療ガイドライン", "指針", "声明", "コンセンサス"]),
    (4, ["システマティックレビュー", "メタアナリシス", "ランダム化", "無作為化", "多施設"]),
    (3, ["原著", "コホート", "観察研究", "総説"]),
    (2, ["実践報告", "症例報告", "1例"]),
    (1, ["会議録", "学会抄録", "巻頭言", "書評"]),
]
BONUS = ["推奨", "前向き", "死亡率", "患者予後", "看護実践", "有害事象", "医療安全"]
PENALTY = ["動物実験", "基礎的研究", "in vitro", "訂正文"]


def score(article: Article) -> tuple[int, str]:
    text = " ".join([article.article_type, article.title_ja, article.abstract_ja, article.journal]).casefold()
    value, basis = 2, "資料種別を特定できないため基礎点2"
    for candidate, words in BASE_RULES:
        hit = next((w for w in words if w.casefold() in text), None)
        if hit:
            value, basis = candidate, f"「{hit}」に一致した基礎点{candidate}"
            break
    plus = [w for w in BONUS if w.casefold() in text]
    minus = [w for w in PENALTY if w.casefold() in text]
    value = max(1, min(5, value + bool(plus) - bool(minus)))
    details = [basis]
    if plus:
        details.append("加点候補: " + "、".join(plus))
    if minus:
        details.append("減点候補: " + "、".join(minus))
    details.append("機械的な一次選別であり、論文の質を保証しません")
    return value, "。".join(details) + "。"
