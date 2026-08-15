from src.content_analyzer import analyze, detect_design
from src.models import Article


ABSTRACT = ("目的：集中治療室患者に対する早期離床プロトコルの効果を検討した。"
            "方法：3施設のICU患者120名を対象とした前向きコホート研究を実施した。"
            "結果：離床群でICU在室日数が短かった（p=0.03、オッズ比 0.72、95%信頼区間 0.55-0.94）。"
            "結論：早期離床プロトコルはICU在室日数の短縮と関連した。")


def test_extracts_objective_population_numbers_and_results():
    article = analyze(Article(title_ja="早期離床", abstract_ja=ABSTRACT, pdf_url="https://example.test/a.pdf"))
    assert "効果を検討" in article.research_objective
    assert article.sample_size == "120名"
    assert article.number_of_facilities == "3施設"
    assert any("p=0.03" in x for x in article.key_numeric_results)
    assert any("95%信頼区間" in x for x in article.key_numeric_results)
    assert any("オッズ比" in x for x in article.key_numeric_results)
    assert article.authors_conclusion.startswith("早期離床")
    assert article.content_review_level == "abstract_reviewed"
    assert article.fulltext_reviewed is False
    assert article.research_usability == "A"


def test_design_patterns():
    assert detect_design("前向きコホート研究")[0] == "前向きコホート研究"
    assert detect_design("後ろ向きコホート研究")[0] == "後ろ向きコホート研究"
    assert detect_design("ランダム化比較試験")[0] == "ランダム化比較試験"
    assert detect_design("非ランダム化比較試験")[0] == "非ランダム化比較試験"
    assert "多施設研究" in detect_design("多施設共同観察研究")[1]
    assert detect_design("システマティックレビュー")[0] == "システマティックレビュー"
    assert detect_design("症例報告")[0] == "症例報告"


def test_title_only_never_invents_results():
    article = analyze(Article(title_ja="集中治療に関する研究", abstract_ja="日本語抄録なし"))
    assert article.key_results == []
    assert article.key_numeric_results == []
    assert article.research_usability == "D"


def test_empty_abstract_is_safe():
    assert analyze(Article(title_ja="題名", abstract_ja="")).content_review_level == "title_and_metadata"


def test_hazard_ratio_is_detected():
    article = analyze(Article(title_ja="研究", abstract_ja="結果：死亡率は低かった（ハザード比 0.81）。"))
    assert any("ハザード比" in x for x in article.key_numeric_results)
