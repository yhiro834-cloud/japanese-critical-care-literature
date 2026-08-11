# Changelog

医学的内容・分類・運用に関する重要変更を記録します。単純な誤字修正は省略できます。

## Unreleased

### 2026-08-12 — Nutrition / Refeeding Depth Phase 23

- **テーマ:** critical-care nutrition delivery、route safety、EN intolerance、organ support、refeeding prevention/response
- **変更内容:** Nutrition/Refeeding SSOTと既存症例を、実投与量・hidden carbohydrate・monitoring・handoff中心に深化
- **新しいEvidence:** ASPEN adult critical care guideline/library、ESPEN ICU nutrition practical guideline 2023、ASPEN refeeding consensus
- **臨床的に何が変わったか:** prescribed rate＝delivery、gastric residual＝intolerance、normal baseline electrolyte＝low risk、electrolyte補正＝解決という短絡を防ぐloopを追加
- **影響ページ:** `docs/14_Nutrition/`、refeeding case
- **要確認:** dietitian/pharmacy/critical care review、local tube/EN/PN/electrolyte/thiamine protocolとの整合

### 2026-08-12 — Fundamentals Depth Phase 22

- **テーマ:** critical-care physiology、clinical reasoning、systematic ICU assessment、human factors/communication
- **変更内容:** 4 SSOTをベッドサイド実用レベルへ深化し、conflicting signals症例、CQ、基礎/中級/上級/症例Quiz、30分教材を追加
- **新しいEvidence:** AHRQ Diagnostic Safety/TeamSTEPPS、SCCM CCUS 2024 focused update、WHO Patient Safety
- **臨床的に何が変わったか:** oxygenation＝delivery、MAP＝perfusion、陰性検査＝除外、alarm＝artifact、再教育＝安全対策という短絡を防ぎ、measurement-to-action、diagnostic timeout、daily goals、closed loopを実装
- **影響ページ:** `docs/00_Fundamentals/`、Cases、Clinical Questions、Quiz、Slide Ready
- **要確認:** multidisciplinary clinical review、施設のrapid response/handoff/POCUS/incident policyとの整合

### 2026-08-11 — Final Requirements Audit Phase 21

- **テーマ:** Fundamentals、教材再構成、portal/status、全要件監査
- **変更内容:** physiology/reasoning/ICU assessment/human factors本体、ABCDE handoff、5/10/20/30分×3対象の教材workflowとshock例、Implementation Statusを追加し、学習・運用ページのreview metadataを統一
- **新しいEvidence:** WHO/ICRC Basic Emergency Care、AHRQ TeamSTEPPS、WHO Patient Safety。既存領域Evidenceは変更なし
- **臨床的に何が変わったか:** 単一値中心の生理理解、premature closure、非系統的round、memory依存の安全対策を補い、完成範囲と専門家review未完了を明確に分離
- **影響ページ:** `README.md`、`docs/00_Fundamentals/`、Teaching Materials、Topic Map、Documentation Portal、Implementation Status
- **要確認:** multidisciplinary specialist sign-off、local protocol alignment、継続Evidence surveillance

### 2026-08-11 — Special Populations / Toxicology / Safety Systems Phase 20

- **テーマ:** 小児・妊産婦・complex adults、中毒・環境急変、shared decision/end-of-life、human factors/搬送/災害/QI
- **変更内容:** 6本体SSOT、unknown poisoning症例、CQ、Quiz、30分教材を追加
- **新しいEvidence:** WHO pediatric ETAT/BEC/IITT、ACOG Critical Care in Pregnancy、AHA toxicology/drowning、SCCM family-centered care、AHRQ TeamSTEPPS
- **臨床的に何が変わったか:** 成人基準の無批判な外挿、toxidromeの確定診断化、原因同定待ち、DNARの自動拡張、個人責任だけのincident review、無計画搬送を防ぐframeworkを追加
- **影響ページ:** `docs/30_Special_Populations/`、`docs/31_Toxicology_Environmental/`、`docs/32_Ethics_Safety_Systems/`、Cases、CQ、Quiz、Slide Ready
- **要確認:** pediatric/obstetric/toxicology/geriatrics/ethics/organ donation/safety specialists、local legal・transport・disaster protocolとの整合

### 2026-08-11 — Bedside Systems / Nursing Phase 19

- **テーマ:** monitoring、device lifecycle、急変・alarm troubleshooting、系統的ICU看護、家族・終末期支援
- **変更内容:** 4本体SSOT、偽alarm/真の急変症例、CQ、Quiz、30分教材を追加
- **新しいEvidence:** FDA pulse oximeter safety、AARC blood gas guidance、AACN monitoring resources、SCCM family-centered care guidance
- **臨床的に何が変わったか:** monitor値だけの治療、artifact決めつけ、line追跡不足、backup不在、device-first troubleshooting、handoff/comfort/家族支援の分断を防ぐ共通loopを追加
- **影響ページ:** `docs/19_Monitoring/`、`docs/20_Devices/`、`docs/21_Emergency_Troubleshooting/`、`docs/22_Nursing/`、Cases、CQ、Quiz、Slide Ready
- **要確認:** bedside nursing/clinical engineering/palliative care、local alarm/device/transport/escalation/end-of-life policyとの整合

### 2026-08-11 — Infection Control / Procedures Phase 18

- **テーマ:** standard/transmission precautions、職業曝露、CLABSI/CAUTI/VAP、手技安全
- **変更内容:** 4本体SSOT、line break/曝露症例、CQ、Quiz、30分教材を追加
- **新しいEvidence:** CDC Core/Isolation/Injection Safety、SHEA Compendium CLABSI/CAUTI/VAP 2022、WHO procedure safety
- **臨床的に何が変わったか:** glovesによるhand hygiene代替、病原体確定待ち、device culture短絡、timeout省略、placement後確認漏れ、曝露報告遅延を防ぐ構造を追加
- **影響ページ:** `docs/17_Infection_Control/`、`docs/18_Procedures/`、Cases、CQ、Quiz、Slide Ready、Guidelines registry
- **要確認:** IPC/occupational health/procedure specialists、local PPE/PEP/device/procedure policyとの整合

### 2026-08-11 — PADIS / Rehabilitation / PICS Phase 17

- **テーマ:** pain、sedation、delirium、sleep/withdrawal、early mobility、ICU-AW、PICS/PICS-F
- **変更内容:** 3本体SSOT、agitation/回復症例、CQ、Quiz、30分教材を追加
- **新しいEvidence:** SCCM PADIS 2018 + 2025 focused update、ICU Liberation A–F
- **臨床的に何が変わったか:** agitationへの反射的深鎮静、NMBA中の苦痛見逃し、delirium薬物偏重、一律bed rest、退院＝回復という誤認を防ぐ構造を追加
- **影響ページ:** `docs/15_Pain_Sedation_Delirium/`、`docs/16_Rehabilitation_PICS/`、Cases、CQ、Quiz、Slide Ready、Guidelines registry
- **要確認:** nursing/pharmacy/PT/OT/SLT/psychology、local assessment/mobility/follow-up pathwayとの整合

### 2026-08-11 — Pharmacology / Nutrition Phase 16

- **テーマ:** critical-care PK/PD、CRRT/ECMO dose、high-alert infusion、EN/PN、refeeding
- **変更内容:** 4本体SSOT、refeeding症例、CQ、Quiz、30分教材を追加
- **新しいEvidence:** ASPEN nutrition 2022、ESPEN ICU nutrition 2023、ASPEN refeeding 2020、ISMP 2024–2025、critical-care TDM position paper
- **臨床的に何が変わったか:** organ supportでの固定dose、濃度/単位/dead-space error、goal rate偏重、refeeding見逃しを防ぐ再評価loopを追加
- **影響ページ:** `docs/13_Pharmacology/`、`docs/14_Nutrition/`、Cases、CQ、Quiz、Slide Ready、Guidelines registry
- **要確認:** ICU pharmacist/dietitian/laboratory、local pump library/TDM/nutrition protocolとの整合

### 2026-08-11 — Hematology Phase 15

- **テーマ:** DIC、血小板減少、輸血/PBM、抗凝固/拮抗、VTE
- **変更内容:** 3本体SSOT、急性血小板低下症例、CQ、Quiz、30分教材を追加
- **新しいEvidence:** AABB RBC 2023、AABB/ICTMG platelet 2025、ASH VTE 2018、ISTH DIC communications、ACC bleeding pathway 2020
- **臨床的に何が変わったか:** DICへの早期固定、HIT/TTP見逃し、閾値だけの製剤投与、輸血反応見逃し、agent非特異的拮抗、VTE予防更新漏れを防ぐ構造を追加
- **影響ページ:** `docs/12_Hematology/`、Cases、CQ、Quiz、Slide Ready、Guidelines registry
- **要確認:** hematology/transfusion/pharmacy/laboratory、local antidote/transfusion/VTE protocolとの整合

### 2026-08-11 — GI / Liver / Pancreas Phase 14

- **テーマ:** GI bleeding、ALF/HE、acute pancreatitis、IAH/ACS
- **変更内容:** 4本体SSOT、再出血症例、CQ、Quiz、30分教材を追加
- **新しいEvidence:** ACG UGIB 2021、ALF 2023、pancreatitis 2024、WSACS 2013 current published guidance
- **臨床的に何が変わったか:** 初期Hb過信、移植相談遅延、ALF INRのroutine correction、膵炎の過剰輸液/予防的抗菌薬、IAHへのblind fluidを防ぐloopを追加
- **影響ページ:** `docs/11_GI_Liver/`、Cases、CQ、Quiz、Slide Ready、Guidelines registry
- **要確認:** GI/hepatology/transplant/surgery/nutrition、local endoscopy/transfer/IAP protocolとの整合

### 2026-08-11 — Endocrine / Metabolic Phase 13

- **テーマ:** DKA/HHS、重症患者血糖、副腎・甲状腺危機、体温異常
- **変更内容:** 3本体SSOT、euglycemic DKA症例、CQ、Quiz、30分教材を追加
- **新しいEvidence:** ADA/EASD hyperglycemic crises 2024、SCCM glycemic control 2024、Endocrine Society adrenal 2016/2024、ATA 2016
- **臨床的に何が変わったか:** glucoseだけのDKA判定、低K下insulin、栄養中断中の低血糖、adrenal crisisの結果待ち、heat strokeへの解熱薬依存を防ぐloopを追加
- **影響ページ:** `docs/10_Endocrine_Metabolic/`、Cases、CQ、Quiz、Slide Ready、Guidelines registry
- **要確認:** endocrine/pharmacy/laboratory/toxicology、local insulin/electrolyte/cooling protocolとの整合

### 2026-08-11 — ECMO / MCS Phase 12

- **テーマ:** VV/VA-ECMO、IABP、microaxial flow pump、合併症、emergency、搬送
- **変更内容:** 3本体SSOT、low-flow症例、CQ、Quiz、30分教材、Devices/Emergency cross-linkを追加
- **新しいEvidence:** ELSO VV/VA 2021、circuit/anticoagulation/transport 2022、ACC cardiogenic shock 2025
- **臨床的に何が変わったか:** flow/saturation単独判断、chatteringへのblind fluid、無訓練の回路操作、device-first MCS選択を防ぐ構造を追加
- **影響ページ:** `docs/09_ECMO_MCS/`、Devices、Emergency、Cases、CQ、Quiz、Slide Ready、Guidelines registry
- **要確認:** ECMO director/perfusion/device specialist、機種固有manual・施設emergency cardとの整合

### 2026-08-11 — Cardiac Critical Care Phase 11

- **テーマ:** ACS、急性心不全/cardiogenic shock、不整脈、心停止、PCAS、temperature control
- **変更内容:** 4本体SSOT、ROSC後悪化症例、CQ、Quiz、30分教材を追加し、神経予後SSOTへ接続
- **新しいEvidence:** ACC/AHA ACS 2025、ACC cardiogenic shock CCG 2025、AHA ALS/Post-Arrest 2025
- **臨床的に何が変わったか:** 単回ECGによるACS除外、rhythm名だけの治療、ROSC後hyperoxia/早期CAGの一律化、早期予後断定を防ぐloopを追加
- **影響ページ:** `docs/08_Cardiac_Critical_Care/`、Cases、Clinical Questions、Quiz、Slide Ready、Guidelines registry
- **要確認:** cardiology/EP/resuscitation/pharmacy、local cath/code/temperature protocolとの整合

### 2026-08-11 — Trauma / Burns Phase 10

- **テーマ:** primary/secondary survey、出血性shock、damage control、胸腹部・骨盤外傷、熱傷初期管理
- **変更内容:** 3本体SSOT、潜在性出血症例、CQ、Quiz、30分教材を追加し、TBIは既存神経SSOTへ接続
- **新しいEvidence:** European major trauma bleeding guideline 6th 2023、ACS TQP Best Practices、ABA burn shock resuscitation 2024、WSES pelvic trauma
- **臨床的に何が変わったか:** 単発の正常vital/Hb/eFASTによる除外、CT優先による止血遅延、MTPの漫然継続、熱傷輸液式のautopilot化を防ぐ再評価loopを追加
- **影響ページ:** `docs/07_Trauma/`、Cases、Clinical Questions、Quiz、Slide Ready、Guidelines registry
- **要確認:** trauma/burn/transfusion/surgery、local MTP・転送protocolとの整合

### 2026-08-11 — Infection / Sepsis Phase 9

- **テーマ:** 感染評価、培養、抗菌薬、source control、diagnostic/antibiotic timeout
- **変更内容:** 2本体SSOT、culture-negative sepsis症例、CQ、Quiz、30分教材を追加
- **新しいEvidence:** SSC Adult 2026、IDSA/SHEA stewardship 2016、CDC Hospital Core Elements 2019/2022
- **臨床的に何が変わったか:** 培養採取による治療遅延、低品質検体の過剰解釈、culture-negative時の漫然継続、source control遅延を防ぐ再評価loopを追加
- **影響ページ:** `docs/06_Infection_Sepsis/`、Cases、Clinical Questions、Quiz、Slide Ready、Guidelines registry
- **要確認:** ID/microbiology/pharmacy/surgery、local antibiogram・culture採取protocolとの整合

### 2026-08-11 — Renal Phase 8

- **テーマ:** AKI/尿量、electrolyte emergencies、KRT/CRRT
- **変更内容:** 3本体SSOT、乏尿/CRRT症例、CQ、Quiz、30分教材を追加
- **新しいEvidence:** KDIGO AKI 2012（現行最終版）、KDIGO controversies 2020、UKKA hyperkalemia 2023、European hyponatremia 2014、STARRT-AKI
- **臨床的に何が変わったか:** KDIGO 2026草案を未確定として分離し、oliguriaへのblind fluid、電解質補正後の再検漏れ、CRRT alarm reset反復を防ぐ構造を追加
- **影響ページ:** `docs/05_Renal/`、Cases、Clinical Questions、Quiz、Slide Ready、Guidelines/References registries
- **要確認:** KDIGO最終版公開時の更新、nephrology/CRRT/pharmacy/施設protocol review

### 2026-08-11 — Neurocritical Care Phase 7

- **テーマ:** 意識/瞳孔、stroke/ICH/SAH、TBI、ICP/CPP、seizure/NCSE、神経予後
- **変更内容:** 5本体SSOT、急性神経悪化症例、CQ、Quiz、30分教材を追加
- **新しいEvidence:** AHA/ASA AIS 2026・ICH 2022・aSAH 2023、BTF severe TBI 4th、NCS cerebral edema 2020・neuroprognostication 2023、ACNS cEEG
- **臨床的に何が変わったか:** AISを2026版へ更新し、score/ICP/単一検査の断定を避けるserial・multimodal・deconfounded reasoningを標準化
- **影響ページ:** `docs/04_Neurology/`、Cases、Clinical Questions、Quiz、Slide Ready、Guidelines/References registries
- **要確認:** neurocritical/stroke/neurosurgery/EEG専門家、施設stroke/EVD/status protocolとの整合

### 2026-08-11 — Hemodynamics Phase 6

- **テーマ:** 血行動態monitoring、fluid responsiveness/therapy、POCUS、vasopressor/inotrope
- **変更内容:** pressure–flow–perfusion、dynamic assessment、fluid phases、CCUS QA、薬剤delivery safety、症例/CQ/Quiz/30分教材を追加
- **新しいEvidence:** ESICM shock/monitoring 2025、ESICM fluid Parts 1–3、SCCM CCUS 2024、SSC 2026
- **臨床的に何が変わったか:** MAP/CVP/IVC/lactate単独判断を避け、need–responsiveness–toleranceと介入後再評価を標準化
- **影響ページ:** `docs/03_Circulation/`、Cases、Clinical Questions、Quiz、Slide Ready、Guidelines registry
- **要確認:** hemodynamics/CCUS/pharmacy専門家、施設A-line/vasoactive/fluid protocolとの整合

### 2026-08-11 — Airway Phase 5

- **テーマ:** 気道評価、閉塞、RSI/DAM、ETCO₂、ETT/カフ、気管切開、吸引、VAP、抜管
- **変更内容:** airway assessment/rescue、physiologically difficult airway、挿管確認、人工気道care、症例、CQ、Quiz、20分教材を追加
- **新しいEvidence:** SCCM RSI 2023、ASA Difficult Airway 2022、PUMA oesophageal intubation 2022、DAS extubation 2012、SHEA/IDSA/APIC VAP update 2022
- **臨床的に何が変わったか:** SpO₂低下待ち、同一手技反復、聴診のみの挿管確認、挿管後鎮静忘れ、抜管時の再確保計画不足を防ぐ構造を追加
- **影響ページ:** `docs/01_Airway/`、Cases、Clinical Questions、Quiz、Slide Ready、Guidelines registry
- **要確認:** 気道専門家、感染管理、各施設Difficult Airway/気管切開protocolとの整合

### 2026-08-11 — Respiratory Support Phase 4

- **テーマ:** 酸素療法、HFNC、NIV、人工呼吸器、ARDS、人工呼吸器離脱
- **変更内容:** support escalation、ventilator mechanics/waveform SSOT、ARDS肺保護、SBT/抜管評価、症例、CQ、Quiz、30分教材を追加
- **新しいEvidence:** BTS oxygen 2017、ERS HFNC 2022、ERS/ATS NIV 2017、ATS ARDS update 2024、ATS/CHEST liberation 2017、ARDSNet、PROSEVA、ROX validation
- **臨床的に何が変わったか:** SpO₂単独評価、NIV/HFNC failureによる挿管遅延、pressure/waveform誤読、SBTと抜管判断の混同を防ぐ再評価loopを追加
- **影響ページ:** `docs/02_Breathing/`、Cases、Clinical Questions、Quiz、Slide Ready、Guidelines/References registries
- **要確認:** 呼吸療法・集中治療専門家レビュー、各施設protocol/機種との整合

### 2026-08-11 — Respiratory Physiology / ABG Phase 3

- **テーマ:** 呼吸生理、ABG、酸塩基
- **変更内容:** Oxygenation/ventilation/delivery、V/Q、ABG 8-step、compensation、検体安全、症例、Quiz、Slide Readyを追加
- **新しいEvidence:** AARC BGA/hemoximetry CPG、VBG meta-analysis、ABG preanalytical study、FDA pulse oximeter safety information、pulse oximetry paired-measurement study
- **臨床的に何が変わったか:** SpO₂の限界、VBGの適用限界、検体条件を明示し、数値単独判断を防ぐ構造を追加
- **影響ページ:** `docs/02_Breathing/`、Cases、Quiz、Slide Ready、Guidelines/References registries
- **要確認:** 呼吸/臨床検査領域専門家レビュー、施設採血protocolとの整合

### 2026-08-11 — Shock / Septic Shock Phase 2

- **テーマ:** Shock、Septic Shock
- **変更内容:** 生理・表現型・評価・臨床推論・治療・看護・症例・Quiz・Slide Readyを追加
- **新しいEvidence:** SSC Adult Guidelines 2026、Sepsis-3、ANDROMEDA-SHOCK、CLASSIC、CLOVERS、ANDROMEDA-SHOCK-2
- **臨床的に何が変わったか:** 最新SSCを2026版として登録。初期fluid、MAP、vasopressor、抗菌薬、source controlの記述を2026推奨に合わせた
- **影響ページ:** `docs/03_Circulation/Shock/`、Cases、Quiz、Slide Ready、Guidelines/References registries
- **要確認:** 各施設protocolとの整合、領域専門家によるclinical review

### 2026-08-11 — Knowledge Base Phase 1

- **テーマ:** 全体設計
- **変更内容:** Knowledge Portal、Topic Map、各種テンプレート、Evidence台帳、更新規則を追加
- **新しいEvidence:** なし（構造整備のみ）
- **臨床的に何が変わったか:** 医学的推奨の変更なし
- **要確認:** 各TopicのEvidenceレビューはPhase 2以降

## Entry template

### YYYY-MM-DD — Topic

- **変更内容:**
- **新しいEvidence:** Title / year / DOI・PMID・official URL（確認済みのみ）
- **臨床的に何が変わったか:**
- **影響ページ:**
- **レビュー担当:**
