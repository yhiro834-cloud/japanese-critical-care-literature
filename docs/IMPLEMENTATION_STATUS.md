# Implementation Status

Last audited: 2026-08-12

## Coverage achieved

- FundamentalsからAirway/Breathing/Circulation、臓器別、ECMO/MCS、全身管理、bedside systems、special populations、toxicology、ethics/safetyまでTopic MapへSSOT入口を配置
- 各実装PhaseにCase、Clinical Question、基礎/中級/上級/症例Quiz、30分Slide Readyを配置
- 5/10/20/30分 × 新人/中堅/リーダーへ再構成する教材workflowと実例を配置
- Guidelines/References台帳、Evidence review、Next Review、CHANGELOG、SSOT更新規則を配置
- CiNii Research/J-STAGEの自動収集候補を未評価inboxとしてKnowledgeから分離

## Quality gates run at final audit

- Python test suite
- all internal Markdown links
- Markdown frontmatter/status/date coverage for SSOT pages
- placeholder/stale phase language search
- `git diff --check`
- 72 SSOT（template除外）のidentity/review log/minimum-depth gate
- 20領域のClinical Questions・Quiz・Slide Readyの集合一致

詳細結果は[Final Cross-Audit 2026-08-12](FINAL_CROSS_AUDIT_2026-08-12.md)を参照。

## Important limits

`coverage-complete`は、体系的な学習開始点が存在するという意味です。診療protocol完成や専門学会レビュー済みを意味しません。

- 多くの医学ページは `review-needed`。領域専門家、ICU看護、薬剤、臨床工学等のreviewer sign-offが必要
- dose、device setting、procedure、transfer、disaster、organ donationは施設手順・法令・機種manualとの整合が必要
- EvidenceはNext Review以前でも重要な新版、訂正、撤回があれば更新する
- 自動収集文献は採用を意味せず、原文評価後にのみRegistry/Knowledgeへ反映する

## Ongoing maintenance

1. Evidence inboxをtriageする
2. overdue `next_review` とguideline新版を確認する
3. SSOTを更新し、Cases/Quiz/Slidesの影響を確認する
4. reviewerと変更理由をReview Log/CHANGELOGへ残す
5. testsとlink check後にPR reviewで公開する
