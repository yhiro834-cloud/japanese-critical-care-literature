import json
from datetime import date

from src.models import Article
from src.storage import append_articles, load_articles, render_markdown, report_path


def test_empty_json(tmp_path):
    path = tmp_path / "empty.json"
    path.write_text("", encoding="utf-8")
    assert load_articles(path) == []


def test_safe_json_append_preserves_existing(tmp_path):
    path = tmp_path / "articles.json"
    path.write_text('[{"article_key":"old"}]', encoding="utf-8")
    append_articles(path, [Article(article_key="new", title_ja="日本語")])
    data = json.loads(path.read_text(encoding="utf-8"))
    assert [item["article_key"] for item in data] == ["old", "new"]
    assert "日本語" in path.read_text(encoding="utf-8")


def test_markdown_and_missing_abstract():
    text = render_markdown([Article(title_ja="テスト")], date(2026, 8, 5))
    assert "国内集中治療・救急文献レポート｜2026-08-05" in text
    assert "日本語抄録なし" in text


def test_zero_articles_markdown():
    assert "新規文献はありません" in render_markdown([], date.today())


def test_daily_path(tmp_path):
    assert report_path(tmp_path, date(2026, 8, 5)) == tmp_path / "literature/2026/08/2026-08-05.md"
