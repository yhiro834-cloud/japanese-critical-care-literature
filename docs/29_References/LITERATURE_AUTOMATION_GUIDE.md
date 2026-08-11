---
title: "日本語文献自動収集 設定・実行ガイド"
status: review-needed
created: 2026-08-11
last_updated: 2026-08-11
evidence_reviewed: 2026-08-11
next_review: 2027-02-11
owners: []
reviewers: [Codex evidence review]
tags: [learning-artifact]
related: []
ssot: false
---

# 日本語文献自動収集 設定・実行ガイド

J-STAGEと、任意でCiNii Researchの公式APIを毎日検索し、日本語の集中治療・救急・救急看護関連文献をMarkdownとJSONへ保存します。GitHub Actionsは毎朝7時17分（日本時間）に動きます。外部生成AI、有料文献データベース、有料APIは使いません。

> [!IMPORTANT]
> 分類と重要度は単純なキーワード規則による一次選別です。論文の質、臨床への適用可能性、医学的判断を保証しません。必ず原文を確認してください。

## できること／できないこと

- 日本語タイトルまたは日本語抄録を持つ文献を設定件数まで収集
- DOI、データベースID、正規化タイトル等で重複排除
- タイトル、抄録、キーワード、誌名からカテゴリーと重要度1〜5を機械的に付与
- `literature/YYYY/MM/YYYY-MM-DD.md` と `data/articles.json` に保存
- APIが提供する書誌情報を保存し、欠損値は推測しない
- AI要約、臨床応用の生成、PDF自動ダウンロード、医中誌Web・PubMed検索は行わない

J-STAGEは科学技術振興機構（JST）、CiNii Researchは国立情報学研究所（NII）が提供します。医中誌Webは有料契約が必要なため使用しません。

## 全体の仕組み

1. `src/config.py` の検索領域を公式APIで検索
2. 公開日等をPythonでも確認し、日本語文字を含まない文献を除外
3. `data/processed_articles.json` と照合して重複を除外
4. `src/classifier.py` と `src/scorer.py` の規則を適用
5. 新規文献がある日だけJSONとMarkdownを更新し、Actionsがcommit/push

Python 3.12、標準GitHub Actions runner、`GITHUB_TOKEN`、`requests`、`python-dotenv`、`pytest`を使います。GitHub Actionsの利用条件は契約プランにより異なるため、SettingsのBillingで確認してください。

## GitHubで最初に行う設定

1. 「Settings → Actions → General → Workflow permissions」で「Read and write permissions」を選び保存
2. CiNiiも使う場合だけ、[CiNii API利用登録](https://support.nii.ac.jp/ja/cinii/api/developer)からアプリケーションIDを取得
3. 「Settings → Secrets and variables → Actions → Secrets」で`CINII_APP_ID`を登録

必須Secretはありません。`GITHUB_TOKEN`はGitHubが自動発行します。`CINII_APP_ID`がなければJ-STAGEだけで動作します。

## Actions Variables

| 名前 | 初期値 | 用途 |
|---|---:|---|
| `MAX_ARTICLES` | `50` | 1日最大件数（プログラム上限100） |
| `DAYS_BACK` | `7` | 何日前まで検索するか（最大3650日） |
| `START_YEAR` | `2020` | この年の1月1日以降を検索。設定時は`DAYS_BACK`より優先 |
| `DRY_RUN` | `false` | `true`なら検索・解析のみで保存しない |
| `ENABLE_CINII` | `true` | CiNii検索を使うか |
| `ENABLE_PUBMED_JAPANESE` | `false` | 将来拡張用。現時点では検索しない |

## 実行方法

### GitHubで手動実行

「Actions → Daily Japanese literature → Run workflow」を押します。失敗時は実行履歴を開き、赤いステップを確認します。ログにはSecretを出しません。

cronは`17 22 * * *`です。UTCの22時17分は日本時間の翌朝7時17分です。GitHub側の状況で開始が遅れる場合があります。

### ローカル実行

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
python -m pytest
python -m src.main
```

Windows PowerShellでは`.venv\Scripts\Activate.ps1`で有効化します。CiNiiを使う場合だけ`.env`の`CINII_APP_ID=`へ自分のIDを書きます。`.env`はGitへ保存されません。

`DRY_RUN=true python -m src.main`なら、保存予定件数と文献IDだけ確認し、ファイルを変更しません。

## 調整する場所

- 検索領域・検索語: `src/config.py`の`SEARCH_GROUPS`
- カテゴリー用語: `src/classifier.py`の`CATEGORY_KEYWORDS`
- 重要度: `src/scorer.py`の`BASE_RULES`、`BONUS`、`PENALTY`
- 最大件数: `MAX_ARTICLES`
- 検索期間: `START_YEAR`（未設定時は`DAYS_BACK`）

検索語を増やすとAPIアクセス数が増えます。[J-STAGE WebAPI利用規約](https://www.jstage.jst.go.jp/static/pages/WebAPI/-char/ja)、[J-STAGE WebAPIマニュアル](https://www.jstage.jst.go.jp/static/files/ja/manual_api.pdf)、[CiNii Research OpenSearch仕様](https://support.nii.ac.jp/ja/cir/r_opensearch)と利用条件を確認してください。実装にはUser-Agent、20秒のtimeout、最大3回の指数backoff、request間隔があります。

## 保存結果と手動評価

- 日別レポート: `literature/`
- 全件JSON: `data/articles.json`
- 重複判定履歴: `data/processed_articles.json`

日別Markdownの手動確認欄へ、研究デザイン、主な結果、限界、看護への応用、確認状況を記録できます。自動処理はこれらを推測しません。

## よくあるトラブル

- **CiNiiが検索されない:** `CINII_APP_ID`、Secretの保存先、`ENABLE_CINII`を確認
- **pushが403:** Workflow permissionsとbranch protectionを確認
- **新規ファイルがない:** 期間・日本語・領域語・重複排除の条件に該当しない日は正常
- **APIエラー:** 一時障害なら次回を待つか手動再実行。継続時は公式情報を確認
- **pytestが失敗:** 最初の`FAILED`行と直前のerrorを確認
- **請求が心配:** SettingsのBillingでActions使用量と予算を確認

## ファイル構成

`jstage_client.py`と`cinii_client.py`が公式API、`classifier.py`が分類、`scorer.py`が重要度、`deduplicator.py`が重複排除、`storage.py`が保存、`main.py`が全体を担当します。テストは`tests/`、定期実行は`.github/workflows/daily_japanese_literature.yml`です。
