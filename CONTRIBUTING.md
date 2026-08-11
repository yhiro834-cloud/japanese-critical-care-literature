# Contributing and Update Rules

## 1. 新規Knowledgeページ

1. [Topic Map](docs/TOPIC_MAP.md)で本体ページ（SSOT）を決める
2. [_templates](docs/_templates/knowledge-page.md)をコピーする
3. metadataを埋め、初稿は `status: draft` とする
4. 推奨、一般的臨床慣行、専門家意見を本文で区別する
5. Referencesを一次情報で検証する
6. Clinical、Evidence、Nursingの観点でレビューする
7. レビュー完了条件を満たした場合のみ `status: reviewed` とする

## 2. Evidence優先順位

1. 最新の公式診療ガイドライン
2. 国際Consensus Statement
3. 国内学会ガイドライン
4. Systematic review / meta-analysis
5. RCT
6. Landmark trial
7. 信頼性の高いreview

検索順位は質の保証ではありません。対象集団、介入、比較、アウトカム、限界、公開後の更新を確認します。

## 3. 捏造防止ルール

- DOI、PMID、URL、推奨文、Evidence levelを記憶や推測で埋めない
- DOIは出版社/Crossref等、PMIDはPubMed、ガイドラインは発行組織の公式ページで照合する
- URLがアクセス可能でも、題名・版・発行主体・年が一致するか確認する
- 確認できない欄は `要確認` または `Evidence unclear` とする
- 自動収集レポートだけを根拠に本文へ採用しない
- 二次資料を参照した場合も、推奨の引用は可能な限り原典へ遡る

詳細は[Evidence workflow](docs/29_References/EVIDENCE_WORKFLOW.md)を参照してください。

## 4. レビュー完了条件

- [ ] Scopeと対象者が明確
- [ ] 生理・病態から臨床推論へつながる
- [ ] 診断基準・推奨に版と対象集団がある
- [ ] 高リスク介入に安全上の注意と再評価がある
- [ ] 看護観察、Red Flags、escalationがある
- [ ] 重要主張とReferenceの対応が追跡できる
- [ ] 書誌情報とリンクを原典で確認した
- [ ] 重複せずSSOTへリンクしている
- [ ] `Evidence Reviewed` と `Next Review` を更新した
- [ ] 臨床的変更をCHANGELOGへ記録した

## 5. 定期更新

- 通常: 12か月ごとを目安に再確認
- 高変化領域・新ガイドライン予告あり: 3〜6か月
- Safety alert、主要ガイドライン、practice-changing trial: 期限を待たず確認
- 期限切れページは削除せず `status: update-needed` と明示

## 6. Pull Request

PR本文に目的、対象ページ、Evidence、臨床的変更、安全上の影響、未確認事項を記載してください。医学的内容を含むPRは、可能なら領域専門家と看護実践者の双方がレビューします。
