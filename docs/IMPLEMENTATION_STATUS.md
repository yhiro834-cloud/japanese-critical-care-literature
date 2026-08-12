# Implementation Status

Last audited: 2026-08-12

## Coverage achieved

- FundamentalsからAirway/Breathing/Circulation、臓器別、ECMO/MCS、全身管理、bedside systems、special populations、toxicology、ethics/safetyまで74実体SSOT入口を配置
- 各実装PhaseにCase、Clinical Question、基礎/中級/上級/症例Quiz、30分Slide Readyを配置
- 5/10/20/30分 × 新人/中堅/リーダーへ再構成する教材workflowと実例を配置
- Guidelines/References台帳、Evidence review、Next Review、CHANGELOG、SSOT更新規則を配置
- CiNii Research/J-STAGEの自動収集候補を未評価inboxとしてKnowledgeから分離

## Quality gates run at final audit

- Python test suite
- all internal Markdown links
- Markdown frontmatter/status/date coverage for SSOT pages
- V2 staged-learning marker、placeholder/stale phase language search
- `git diff --check`
- 74 SSOT（template除外）のidentity/review log/minimum-depth/新人・ベテラン導線gate
- 74 SSOTすべての直接外部Evidence identity（DOI/PMID/公式一次source）gate
- 20領域のClinical Questions・Quiz・Slide Readyの集合一致
- 20領域のSSOT・CQ・Quiz・Slide・Case・Visual/rationale同期台帳
- 67 SVGのFigure Index一意登録、XML/16:9/accessibility、日本語フォント、関連SSOT gate
- 7高精細PNGのFigure Index一意登録、PNG妥当性、最小解像度gate
- 外部URL 122件の到達性監査と、失効URLの一次論文/現行公式URLへの修正

詳細結果は[Completion Audit 2026-08-12](COMPLETION_AUDIT_2026-08-12.md)を参照。

## Important limits

`reviewed`は、編集・根拠・構造・視覚教材の内部監査を完了したという意味です。診療protocol完成や外部専門学会の認証を意味しません。

- 全本文は内部監査済み。領域専門家、ICU看護、薬剤、臨床工学等による追加の外部レビューは引き続き有用
- dose、device setting、procedure、transfer、disaster、organ donationは施設手順・法令・機種manualとの整合が必要
- EvidenceはNext Review以前でも重要な新版、訂正、撤回があれば更新する
- 自動収集文献は採用を意味せず、原文評価後にのみRegistry/Knowledgeへ反映する

## Ongoing maintenance

1. Evidence inboxをtriageする
2. overdue `next_review` とguideline新版を確認する
3. SSOTを更新し、Cases/Quiz/Slidesの影響を確認する
4. reviewerと変更理由をReview Log/CHANGELOGへ残す
5. testsとlink check後にPR reviewで公開する
