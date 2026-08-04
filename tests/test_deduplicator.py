import pytest

from src.deduplicator import duplicate_of, normalize_title
from src.models import Article


@pytest.mark.parametrize("field,value", [
    ("doi", "10.1/ABC"), ("jstage_article_id", "journal/123"), ("cinii_id", "CRID123")
])
def test_identifier_duplicates(field, value):
    old = Article(**{field: value})
    new = Article(**{field: value.lower() if field == "doi" else value})
    assert duplicate_of(new, [old]) is old


def test_title_normalization():
    assert normalize_title(" ＩＣＵ：救急 看護。 ") == normalize_title("icu 救急看護")


def test_title_and_year_duplicate_without_doi():
    old = Article(title_ja="集中治療の研究", publication_year="2026")
    new = Article(title_ja="集中治療 の研究。", publication_year="2026")
    assert duplicate_of(new, [old]) is old


def test_no_doi_is_not_automatically_duplicate():
    assert duplicate_of(Article(title_ja="論文A"), [Article(title_ja="論文B")]) is None
