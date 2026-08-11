# Automated Literature Inbox

## 位置づけ

既存のGitHub ActionsはCiNii ResearchとJ-STAGEから日本語の集中治療・救急関連文献候補を集め、`literature/YYYY/MM/` に保存します。

これは以下を意味しません。

- 論文の質が確認済み
- Knowledge Baseに採用済み
- 診療推奨を支持
- 書誌情報・要約が原文と照合済み

## 採用フロー

`literature/ candidate` → 重複確認 → 原文/公式record確認 → 批判的吟味 → Reference registry登録 → Knowledge本文へ紐づけ → review

## 既存自動化の実行

- 定期実行: `.github/workflows/daily_japanese_literature.yml`
- 手動実行: GitHubのActions画面からworkflow dispatch
- 保存済み重複管理: `data/processed_articles.json`
- 詳細な検索期間や件数: workflowの入力値と環境変数を確認

自動分類・スコアはtriage支援であり、医学的妥当性の判定ではありません。

初心者向けの設定、手動実行、変数、トラブル対応は[自動文献収集 設定・実行ガイド](LITERATURE_AUTOMATION_GUIDE.md)にあります。
