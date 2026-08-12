# Phase 1 監査報告

## What was wrong — 何が問題だったか

1. 前回の`reviewed`表示は、文章構造・リンク・描画検証を示すにとどまり、重要Claimと原典の対応、推奨強度、対象集団、例外まで保証していなかった。
2. 170ページすべてに、医学的正確性4/5以上を証明するClaim単位の査読記録がなかった。
3. Referenceは存在していても、Title・Author・Year・DOI/PMID・本文支持範囲の再検証が完了していなかった。
4. 74図は描画可能だったが、本文・Evidence・矢印・圧関係・回路方向を図ごとに独立査読した証拠が不足していた。
5. 高品質に見える7枚のAIラスター解剖図には、追跡可能な原図と専門家の解剖学的承認がなかった。
6. 酸塩基、PEEP/人工呼吸力学、混合ショック、神経疾患別ページ、MCS/CRRT詳細、薬理、産科、処置、モニタリング、ICU看護などに実質的Coverage gapがあった。
7. 既存ページはQuick/Core/Advancedに近い段階説明を持つが、Fact / Recommendation / Practice / Uncertaintyの表示が統一されていなかった。

## What was corrected — Phase 1で修正したこと

- `main`の基準点をリモートバックアップへ保存した。
- 170文書を0〜5点で保守的に再評価し、74 SSOTを`REWRITE`、96文書を`MAJOR REVISION`とした。
- 74視覚教材を全件棚卸しし、67 SVGを`CORRECT`、7 PNGを`REDRAW`とした。
- 122の外部URLをReference台帳へ抽出し、未検証事項を`REFERENCE NOT RE-VERIFIED`として可視化した。
- 指定された全領域をCoverage auditし、新規Master Page候補と優先順位を定義した。
- 74実体SSOTを、Evidence review・rewrite・figure review・cross-review・human review別に追跡する台帳を作成した。従来の75件集計はテンプレートを誤って含めていたため訂正した。
- AIだけで確証できない高リスク領域を、必要な専門職とともに明示した。

## Evidence changes — 確認した最新版・状態変化

- **Surviving Sepsis Campaign 2026**：SCCM公式ページで、2021版を更新する成人ガイドラインとして確認。全敗血症Claimの再マッピングが必要。
- **AHA CPR/ECC 2025**：公式ガイドライン群を確認。ALS・特殊状況・心停止後管理の2020/2023由来記述は継承可否を再確認する。
- **ESICM shock/hemodynamic monitoring 2025**：公式資料を確認。正確な推奨引用には全文照合が必要。
- **J-SSCG2024**：日本集中治療医学会・日本救急医学会の正式版を公式情報で確認。
- **KDIGO AKI/AKD 2026**：現時点では公開査読用ドラフトであり、最終版として採用してはいけないことを確認。
- **ELSO**：公式一覧で成人VV 2021、成人VA 2021、回路2022等の版を確認。
- **AARC**：Patient–Ventilator Assessment 2024、Spontaneous Breathing Trial 2024等を公式一覧で確認。
- **Neurocritical Care Society**：疾患別ガイドライン一覧を確認。一つの文書を神経集中治療全般へ拡張しない。
- **日本集中治療医学会**：JCCNG2024（2025公開）、J-ReCIP2023、搬送2025等を公式一覧で確認。

## Visual corrections — 図に対する判定

このPhaseでは本文確定前の再描画を行っていない。全図を未承認として棚卸しし、数値・波形・回路・矢印を持つSVGはEvidenceと新本文に合わせて修正、AIラスター解剖図は原則再作成とした。これは「描画できる＝正しい」という前回の弱い証拠を撤回する判断である。

## Remaining uncertainty — 未解決事項

- 122 Referenceの完全な書誌・実在性・Claim支持範囲
- ガイドライン本文のRecommendation strength / certainty / population
- ECMO、CRRT、神経、人工呼吸、薬剤、産科、輸血、倫理の専門家承認
- 施設固有プロトコル、法令、機種別取扱説明書との整合
- ページ間の文章類似度だけでなく、意味レベルの矛盾と不要重複

## Next priority — 次の優先作業

Phase 2で`STYLE_GUIDE.md`、Evidence label、Claim citation方式、Threshold registry、新Template、SSOT/cross-link規則、Figure Index schemaを整備する。その後、ABCDE→呼吸生理→人工呼吸/PEEP→ARDSの順で、一次情報をClaim単位に照合して書き直す。
