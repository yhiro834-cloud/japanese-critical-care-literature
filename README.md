# 国内集中治療・救急文献の自動収集

J-STAGEと、任意でCiNii Researchの公式APIを毎日検索し、日本語の集中治療・救急・救急看護関連文献をMarkdownとJSONへ保存する仕組みです。GitHub Actionsが毎朝7時（日本時間）に動きます。外部生成AI、有料文献データベース、有料APIは使いません。

> [!IMPORTANT]
> 分類と重要度は単純なキーワード規則による一次選別です。論文の質、臨床への適用可能性、医学的判断を保証しません。必ず原文を確認してください。

## できること／できないこと

- 直近7日を目安に、日本語タイトルまたは日本語抄録を持つ文献を最大20件収集します。
- DOI、各データベースID、正規化タイトル等で過去分と重複排除します。
- タイトル、抄録、キーワード、誌名から複数カテゴリーと重要度1〜5を機械的に付与します。
- `literature/YYYY/MM/YYYY-MM-DD.md` と `data/articles.json` に保存します。
- APIが提供する書誌情報をそのまま保存し、欠損値は推測しません。AI要約、臨床応用の生成、PDF自動ダウンロード、医中誌Web検索、PubMed検索はしません。

J-STAGEは科学技術振興機構（JST）が運営する国内学術刊行物の公開基盤です。CiNii Researchは国立情報学研究所（NII）が提供する国内学術情報検索サービスです。医中誌Webは有料契約が必要なため、無料運用という本プロジェクトの条件に合わせて使用しません。

## 全体の仕組み

1. `src/config.py` の11領域を、領域ごとに公式APIで検索します。
2. 公開日等をPythonでも確認し、日本語文字を含まない文献を除外します。
3. `data/processed_articles.json` と照合し、同一文献を除きます。
4. `src/classifier.py` と `src/scorer.py` の規則を適用します。
5. 新規文献がある日だけJSONとMarkdownを更新し、GitHub Actionsがcommit/pushします。

利用するのはPython 3.12、通常の`ubuntu-latest`、標準`GITHUB_TOKEN`、`requests`、`python-dotenv`、`pytest`だけです。外部データベースや生成AI APIはありません。GitHub Actionsには公開リポジトリでは原則無料、非公開リポジトリではプランごとの無料枠・課金条件があります。GitHubの「Settings → Billing and licensing」で利用量と支出上限を確認してください。

## GitHubで最初に行う設定

1. このフォルダーの内容をGitHubリポジトリの既定ブランチへpushします。
2. リポジトリの「Settings → Actions → General → Workflow permissions」で「Read and write permissions」を選び、保存します。組織ポリシーで変更できない場合は管理者へ確認します。
3. CiNiiも使う場合だけ、[CiNii API利用登録](https://support.nii.ac.jp/ja/cinii/api/developer)からアプリケーションIDを取得します。登録画面の案内と利用条件に従い、短時間の大量アクセスを避けてください。
4. 「Settings → Secrets and variables → Actions → Secrets → New repository secret」で、名前を`CINII_APP_ID`、値を発行されたIDとして保存します。IDをコードやIssueに貼らないでください。

必須Secretはありません。`GITHUB_TOKEN`はGitHubが実行ごとに自動発行します。任意Secretは`CINII_APP_ID`だけです。未登録なら警告後、J-STAGEだけで正常に動きます。

ActionsのVariables（Secretsと同じ画面の「Variables」）は必要な場合だけ設定します。

| 名前 | 初期値 | 用途 |
|---|---:|---|
| `MAX_ARTICLES` | `20` | 1日最大件数（プログラム上限100） |
| `DRY_RUN` | `false` | `true`なら検索・解析だけ行い、保存しない |
| `ENABLE_CINII` | `true` | CiNii検索を使うか |
| `ENABLE_PUBMED_JAPANESE` | `false` | 将来拡張用。初期版では`true`でも検索しない |

## 実行方法

### 手動実行

GitHubで「Actions → Daily Japanese literature → Run workflow → Run workflow」を押します。結果は同じ画面の実行履歴を開き、失敗した赤いステップをクリックして確認できます。ログにはSecretを出しません。

自動実行のcronは`0 22 * * *`です。UTC（世界の基準時）の22時は、日本標準時（UTC+9）の翌朝7時です。GitHubの混雑時には開始が多少遅れる場合があります。

### ローカル実行

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
python -m pytest
python -m src.main
```

Windows PowerShellでは有効化を`.venv\Scripts\Activate.ps1`で行います。CiNiiを使う場合だけ`.env`の`CINII_APP_ID=`の右側に自分のIDを書きます。`.env`はGitに保存されません。

`DRY_RUN=true python -m src.main`なら、保存予定件数と文献IDだけ確認し、Markdown・JSON・重複管理ファイルを一切変更しません。

## 調整する場所

- 検索領域・検索語：`src/config.py`の`SEARCH_GROUPS`
- カテゴリー用語：`src/classifier.py`の`CATEGORY_KEYWORDS`
- 重要度：`src/scorer.py`の`BASE_RULES`、`BONUS`、`PENALTY`
- 最大件数：GitHub Variableまたは`.env`の`MAX_ARTICLES`

検索語を増やしすぎるとAPIアクセス数が増えます。まず少数を追加し、公式の[J-STAGE WebAPI利用規約](https://www.jstage.jst.go.jp/static/pages/WebAPI/-char/ja)、[J-STAGE WebAPIマニュアル](https://www.jstage.jst.go.jp/static/files/ja/manual_api.pdf)、[CiNii Research OpenSearch仕様](https://support.nii.ac.jp/ja/cir/r_opensearch)と利用条件を確認してください。本実装はHTML画面をスクレイピングせず、User-Agent、20秒のタイムアウト、最大3回の指数バックオフ、リクエスト間隔を設定しています。

## 保存結果と手動評価

日別レポートは`literature`以下、全件JSONは`data/articles.json`、重複判定履歴は`data/processed_articles.json`です。日別Markdownの「手動確認欄」を読みながら編集し、研究デザイン、主な結果、限界、看護への応用、確認状況を記録できます。自動処理はこの欄を推測しません。

## よくあるトラブル

- **CiNiiが検索されない**：`CINII_APP_ID`の名前、Secretの保存先、`ENABLE_CINII`を確認します。IDなしでもJ-STAGEは動きます。
- **pushが403で失敗**：Workflow permissionsが書き込み許可か、ブランチ保護がActionsの直接pushを禁じていないか確認します。
- **新規ファイルがない**：直近7日・日本語・領域語・重複排除の条件に該当しない日は正常です。
- **APIエラー**：一時障害なら次回実行を待つか手動再実行します。継続する場合は公式サービス状況・仕様変更・利用制限を確認します。
- **pytestが失敗**：Actionsの失敗ステップを開き、最初の`FAILED`行とその直前のエラーを確認します。
- **請求が心配**：SettingsのBillingでActions使用量と予算を確認します。本workflowは標準ランナーを最大15分だけ使いますが、アカウントの契約条件はGitHubの最新表示が優先です。

## ファイル構成

`src/jstage_client.py`と`src/cinii_client.py`が公式API、`classifier.py`が分類、`scorer.py`が重要度、`deduplicator.py`が重複排除、`storage.py`が安全なJSON追記とMarkdown生成、`main.py`が全体を担当します。テストは`tests/`、毎日実行の設定は`.github/workflows/daily_japanese_literature.yml`です。
