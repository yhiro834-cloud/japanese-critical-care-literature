from src.classifier import classify
from src.models import Article


def test_japanese_keyword():
    categories, hits = classify(Article(title_ja="人工呼吸器の管理"))
    assert "人工呼吸" in categories and "人工呼吸" in hits


def test_multiple_categories():
    categories, _ = classify(Article(title_ja="救急看護におけるせん妄ケア"))
    assert {"救急看護", "せん妄"} <= set(categories)


def test_case_insensitive_english():
    categories, _ = classify(Article(title_en="ECMO and ARDS"))
    assert {"ECMO", "呼吸管理"} <= set(categories)
