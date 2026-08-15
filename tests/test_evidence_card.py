from datetime import date

from src.content_analyzer import analyze
from src.evidence_card import render, write_cards
from src.models import Article


def test_evidence_card_renders_and_writes(tmp_path):
    article = analyze(Article(article_key="doi:10.1234/example", title_ja="架空研究", abstract_ja="目的：目的を確認した。結果：結果を確認した。"))
    paths = write_cards(tmp_path, [article], date(2026, 8, 13))
    assert paths[0].exists()
    assert "原文由来の基本情報" in paths[0].read_text(encoding="utf-8")
    assert article.evidence_card_path.startswith("evidence/2026/08/")
    assert "全文：未確認" in render(article, date.today())
