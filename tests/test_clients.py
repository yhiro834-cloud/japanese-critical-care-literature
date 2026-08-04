from src.jstage_client import parse_jstage


def test_parse_jstage_official_atom_shape():
    xml = '''<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/">
      <entry><article_title><en>English</en><ja>集中治療</ja></article_title>
      <article_link><ja>https://www.jstage.jst.go.jp/article/jsicm/33/0/33_R3/_article/-char/ja/</ja></article_link>
      <author><ja><name>山田太郎</name></ja></author>
      <material_title><ja>集中治療医学会誌</ja></material_title><pubyear>2026</pubyear>
      <prism:doi>10.1/example</prism:doi><updated>2026-08-01T00:00:00+09:00</updated></entry></feed>'''.encode()
    article = parse_jstage(xml, "now")[0]
    assert article.title_ja == "集中治療"
    assert article.title_en == "English"
    assert article.authors == ["山田太郎"]
    assert article.journal == "集中治療医学会誌"
    assert article.publication_year == "2026"
    assert article.jstage_article_id == "jsicm/33_R3"
