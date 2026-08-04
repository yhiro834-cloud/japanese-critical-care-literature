from src.models import Article
from src.scorer import score


def test_guideline_is_five():
    value, reason = score(Article(title_ja="集中治療診療ガイドライン"))
    assert value == 5 and "保証しません" in reason


def test_case_report_is_low():
    value, _ = score(Article(article_type="症例報告"))
    assert value == 2


def test_score_stays_in_range():
    value, _ = score(Article(title_ja="動物実験による基礎的研究"))
    assert 1 <= value <= 5
