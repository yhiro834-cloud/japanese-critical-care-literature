---
title: "Textbook V2 Learning Asset Coverage"
status: reviewed
created: 2026-08-12
last_updated: 2026-08-12
evidence_reviewed: 2026-08-12
next_review: 2027-02-12
owners: []
reviewers: [Codex structural and learning-design review]
tags: [audit, cases, questions, quiz, slides, figures]
related: [TEXTBOOK_V2_MIGRATION.md, ../FIGURE_INDEX.md]
ssot: false
---

# Textbook V2 Learning Asset Coverage

本文を唯一の医学的source of truth（SSOT）とし、Clinical Questions、Quiz、Slide Ready、症例、図を本文へ戻る学習導線として管理する。表のリンクが存在するだけで医学的正しさを保証せず、SSOT更新時には同じ行の教材へ影響がないか再確認する。

## 20領域の同期台帳

| Domain ID | 代表SSOT | Clinical Questions | Quiz | Slide Ready | 代表症例 | Visual / rationale |
|---|---|---|---|---|---|---|
| CRITICAL_CARE_FUNDAMENTALS | [Clinical Reasoning](00_Fundamentals/Clinical_Reasoning/CLINICAL_REASONING.md) / [ABCDE](00_Fundamentals/ABCDE/README.md) | [CQ](24_Clinical_Questions/FUNDAMENTALS_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_CRITICAL_CARE_FUNDAMENTALS.md) | [Slide](27_Slide_Ready/CRITICAL_CARE_FUNDAMENTALS_30MIN.md) | [Conflicting signals](23_Clinical_Cases/CASE_CONFLICTING_SIGNALS_DIAGNOSTIC_TIMEOUT.md) | [ABCDE再評価loop](../assets/general/abcde_reassessment_loop.svg) |
| AIRWAY | [Airway emergencies](01_Airway/Assessment_Emergencies/AIRWAY_ASSESSMENT_EMERGENCIES.md) | [CQ](24_Clinical_Questions/AIRWAY_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_AIRWAY.md) | [Slide](27_Slide_Ready/AIRWAY_20MIN.md) | [Airway emergency](23_Clinical_Cases/CASE_AIRWAY_EMERGENCY.md) | [ABCDE Airway](../assets/general/abcde_airway_detail.svg) |
| RESPIRATORY_PHYSIOLOGY_ABG | [Respiratory physiology](02_Breathing/Respiratory_Physiology/RESPIRATORY_PHYSIOLOGY.md) / [ABG](02_Breathing/ABG/ABG_INTERPRETATION.md) | [CQ](24_Clinical_Questions/RESPIRATORY_PHYSIOLOGY_ABG_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_RESPIRATORY_PHYSIOLOGY_ABG.md) | [Slide](27_Slide_Ready/RESPIRATORY_PHYSIOLOGY_ABG_20MIN.md) | [Desaturation / hypercapnia](23_Clinical_Cases/CASE_DESATURATION_HYPERCAPNIA.md) | [肺胞gas交換](../assets/physiology/alveolar_gas_exchange.svg) |
| RESPIRATORY_SUPPORT | [Mechanical ventilation](02_Breathing/Mechanical_Ventilation/MECHANICAL_VENTILATION.md) / [ARDS](02_Breathing/ARDS/ARDS.md) | [CQ](24_Clinical_Questions/RESPIRATORY_SUPPORT_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_RESPIRATORY_SUPPORT.md) | [Slide](27_Slide_Ready/RESPIRATORY_SUPPORT_30MIN.md) | [Support escalation](23_Clinical_Cases/CASE_RESPIRATORY_SUPPORT_ESCALATION.md) | [非同調](../assets/ventilation/asynchrony_series.svg) / [ARDS](../assets/breathing/ards_alveolar_injury.svg) |
| SHOCK_SEPTIC_SHOCK | [Shock](03_Circulation/Shock/SHOCK.md) / [Septic shock](03_Circulation/Shock/SEPTIC_SHOCK.md) | [CQ](24_Clinical_Questions/SHOCK_SEPTIC_SHOCK_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_SHOCK_SEPTIC_SHOCK.md) | [Slide](27_Slide_Ready/SHOCK_SEPTIC_SHOCK_20MIN.md) | [Sudden hypotension](23_Clinical_Cases/CASE_SUDDEN_HYPOTENSION_SEPTIC_SHOCK.md) | [Shock推論loop](../assets/shock/shock_reasoning_loop.svg) / [Sepsis](../assets/sepsis/sepsis_pathophysiology.svg) |
| HEMODYNAMICS | [Hemodynamic monitoring](03_Circulation/Hemodynamics/HEMODYNAMIC_MONITORING.md) / [POCUS](03_Circulation/POCUS/HEMODYNAMIC_POCUS.md) | [CQ](24_Clinical_Questions/HEMODYNAMICS_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_HEMODYNAMICS.md) | [Slide](27_Slide_Ready/HEMODYNAMICS_30MIN.md) | [Fluid responsiveness](23_Clinical_Cases/CASE_FLUID_RESPONSIVENESS.md) | [圧・流れ・灌流](../assets/circulation/pressure_flow_perfusion.svg) / [肺POCUS](../assets/pocus/lung_ultrasound_schematic.svg) |
| NEUROCRITICAL | [Neurological assessment](04_Neurology/Assessment/NEUROLOGICAL_ASSESSMENT.md) / [ICP/CPP](04_Neurology/ICP_CPP_TBI/ICP_CPP_TBI.md) | [CQ](24_Clinical_Questions/NEUROCRITICAL_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_NEUROCRITICAL.md) | [Slide](27_Slide_Ready/NEUROCRITICAL_30MIN.md) | [Acute neurological decline](23_Clinical_Cases/CASE_ACUTE_NEUROLOGICAL_DECLINE.md) | [Monro–Kellie](../assets/neurology/monro_kellie_doctrine.svg) / [意識変化](../assets/clinical_reasoning/altered_consciousness_reasoning.svg) |
| RENAL | [AKI](05_Renal/AKI/AKI.md) / [CRRT](05_Renal/CRRT/CRRT.md) | [CQ](24_Clinical_Questions/RENAL_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_RENAL.md) | [Slide](27_Slide_Ready/RENAL_30MIN.md) | [Oliguria / CRRT alarm](23_Clinical_Cases/CASE_OLIGURIA_CRRT_ALARM.md) | [CRRT回路](../assets/crrt/crrt_circuit.svg) / [尿量低下](../assets/clinical_reasoning/low_urine_output_reasoning.svg) / [高カリウム血症](../assets/renal/hyperkalemia_actions.svg) |
| INFECTION_SEPSIS | [Infection assessment](06_Infection_Sepsis/Infection_Assessment/INFECTION_ASSESSMENT.md) / [Antimicrobial/source control](06_Infection_Sepsis/Antimicrobial_Source_Control/ANTIMICROBIAL_SOURCE_CONTROL.md) | [CQ](24_Clinical_Questions/INFECTION_SEPSIS_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_INFECTION_SEPSIS.md) | [Slide](27_Slide_Ready/INFECTION_SEPSIS_30MIN.md) | [Culture-negative sepsis](23_Clinical_Cases/CASE_CULTURE_NEGATIVE_SEPSIS.md) | [Sepsis病態](../assets/sepsis/sepsis_pathophysiology.svg) / [抗菌薬タイムアウト](../assets/infection/antibiotic_timeout.svg) |
| TRAUMA_BURNS | [Trauma assessment](07_Trauma/Initial_Assessment/TRAUMA_INITIAL_ASSESSMENT.md) / [Burns](07_Trauma/Burns/BURN_INITIAL_MANAGEMENT.md) | [CQ](24_Clinical_Questions/TRAUMA_BURNS_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_TRAUMA_BURNS.md) | [Slide](27_Slide_Ready/TRAUMA_BURNS_30MIN.md) | [Occult hemorrhage](23_Clinical_Cases/CASE_TRAUMA_OCCULT_HEMORRHAGE.md) | [外傷性大出血の並行行動](../assets/trauma/hemorrhage_parallel_actions.svg) / [ABCDE Exposure](../assets/general/abcde_exposure_detail.svg) |
| CARDIAC_CRITICAL_CARE | [Cardiac arrest](08_Cardiac_Critical_Care/Cardiac_Arrest/CARDIAC_ARREST_POST_ARREST.md) / [Cardiogenic shock](08_Cardiac_Critical_Care/Heart_Failure_Shock/ACUTE_HEART_FAILURE_CARDIOGENIC_SHOCK.md) | [CQ](24_Clinical_Questions/CARDIAC_CRITICAL_CARE_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_CARDIAC_CRITICAL_CARE.md) | [Slide](27_Slide_Ready/CARDIAC_CRITICAL_CARE_30MIN.md) | [Post-ROSC deterioration](23_Clinical_Cases/CASE_POST_ROSC_DETERIORATION.md) | [Shock表現型](../assets/shock/shock_classification.svg)（心電図実例は機器/症例sourceが必要） |
| ECMO_MCS | [ECMO foundations](09_ECMO_MCS/ECMO_Foundations/ECMO_FOUNDATIONS_DAILY_MANAGEMENT.md) / [Temporary MCS](09_ECMO_MCS/Temporary_MCS/TEMPORARY_MCS.md) | [CQ](24_Clinical_Questions/ECMO_MCS_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_ECMO_MCS.md) | [Slide](27_Slide_Ready/ECMO_MCS_30MIN.md) | [ECMO low flow](23_Clinical_Cases/CASE_ECMO_LOW_FLOW.md) | [VVとVA](../assets/ecmo/va_vs_vv_ecmo.svg) |
| ENDOCRINE_METABOLIC | [DKA/HHS](10_Endocrine_Metabolic/Hyperglycemic_Crises/DKA_HHS.md) | [CQ](24_Clinical_Questions/ENDOCRINE_METABOLIC_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_ENDOCRINE_METABOLIC.md) | [Slide](27_Slide_Ready/ENDOCRINE_METABOLIC_30MIN.md) | [Euglycemic DKA](23_Clinical_Cases/CASE_EUGLYCEMIC_DKA.md) | [高血糖緊急症の並行治療](../assets/endocrine/dka_hhs_parallel_treatment.svg)。患者別の数値推移は症例flow sheetで補完する。 |
| GI_LIVER_PANCREAS | [GI bleeding](11_GI_Liver/GI_Bleeding/ACUTE_GI_BLEEDING.md) / [IAH/ACS](11_GI_Liver/IAH_ACS/INTRA_ABDOMINAL_HYPERTENSION.md) | [CQ](24_Clinical_Questions/GI_LIVER_PANCREAS_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_GI_LIVER_PANCREAS.md) | [Slide](27_Slide_Ready/GI_LIVER_PANCREAS_30MIN.md) | [GI bleed reshock](23_Clinical_Cases/CASE_GI_BLEED_RESHOCK.md) | [低血圧推論](../assets/clinical_reasoning/hypotension_reasoning.svg)（臓器固有図は将来拡張） |
| HEMATOLOGY | [DIC/thrombocytopenia](12_Hematology/DIC_Thrombocytopenia/DIC_THROMBOCYTOPENIA.md) / [Transfusion](12_Hematology/Transfusion/TRANSFUSION_PBM.md) | [CQ](24_Clinical_Questions/HEMATOLOGY_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_HEMATOLOGY.md) | [Slide](27_Slide_Ready/HEMATOLOGY_30MIN.md) | [Acute platelet fall](23_Clinical_Cases/CASE_ACUTE_PLATELET_FALL.md) | 図より発症時刻・薬剤・検査trendの比較表を優先。 |
| PHARMACOLOGY_NUTRITION | [PK/PD](13_Pharmacology/PKPD/CRITICAL_CARE_PKPD.md) / [Nutrition](14_Nutrition/Critical_Care_Nutrition/CRITICAL_CARE_NUTRITION.md) | [CQ](24_Clinical_Questions/PHARMACOLOGY_NUTRITION_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_PHARMACOLOGY_NUTRITION.md) | [Slide](27_Slide_Ready/PHARMACOLOGY_NUTRITION_30MIN.md) | [Infusion transition](23_Clinical_Cases/CASE_INFUSION_CONCENTRATION_TRANSITION.md) / [Refeeding](23_Clinical_Cases/CASE_REFEEDED_PATIENT_DYSPNEA.md) | device/濃度依存のため固定配管図を作らず、line traceと症例timelineを優先。 |
| PADIS_REHAB_PICS | [PADIS](15_Pain_Sedation_Delirium/PADIS/PADIS_BEDSIDE_CARE.md) / [PICS](16_Rehabilitation_PICS/PICS/PICS_RECOVERY.md) | [CQ](24_Clinical_Questions/PADIS_REHAB_PICS_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_PADIS_REHAB_PICS.md) | [Slide](27_Slide_Ready/PADIS_REHAB_PICS_30MIN.md) | [Agitation / weakness / recovery](23_Clinical_Cases/CASE_AGITATION_WEAKNESS_RECOVERY.md) | 図より患者別goal・daily trajectory・家族情報の共有表を優先。 |
| INFECTION_CONTROL_PROCEDURES | [Precautions](17_Infection_Control/Precautions/STANDARD_TRANSMISSION_PRECAUTIONS.md) / [Procedure safety](18_Procedures/Safety_Framework/PROCEDURAL_SAFETY_FRAMEWORK.md) | [CQ](24_Clinical_Questions/INFECTION_CONTROL_PROCEDURES_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_INFECTION_CONTROL_PROCEDURES.md) | [Slide](27_Slide_Ready/INFECTION_CONTROL_PROCEDURES_30MIN.md) | [Line break / exposure](23_Clinical_Cases/CASE_LINE_BREAK_EXPOSURE.md) | 手順は施設PPE/曝露protocolに依存するため、固定図よりlocal checklistを優先。 |
| BEDSIDE_SYSTEMS_NURSING | [Monitoring](19_Monitoring/Core_Monitoring/MONITORING_WAVEFORMS_ARTIFACT.md) / [Nursing care](22_Nursing/Systematic_Care/SYSTEMATIC_ICU_NURSING_CARE.md) | [CQ](24_Clinical_Questions/BEDSIDE_SYSTEMS_NURSING_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_BEDSIDE_SYSTEMS_NURSING.md) | [Slide](27_Slide_Ready/BEDSIDE_SYSTEMS_NURSING_30MIN.md) | [False alarm / deterioration](23_Clinical_Cases/CASE_FALSE_ALARM_TRUE_DETERIORATION.md) | [SpO₂低下推論](../assets/clinical_reasoning/spo2_drop_reasoning.svg) |
| SPECIAL_TOXICOLOGY_SYSTEMS | [Complex adults](30_Special_Populations/Complex_Adults/COMPLEX_ADULT_POPULATIONS.md) / [Toxicology](31_Toxicology_Environmental/Toxicology/TOXICOLOGY_INITIAL_APPROACH.md) / [Ethics](32_Ethics_Safety_Systems/Ethics/GOALS_SHARED_DECISION_END_OF_LIFE.md) | [CQ](24_Clinical_Questions/SPECIAL_TOXICOLOGY_SYSTEMS_QUESTIONS.md) | [Quiz](25_Quiz/QUIZ_SPECIAL_TOXICOLOGY_SYSTEMS.md) | [Slide](27_Slide_Ready/SPECIAL_TOXICOLOGY_SYSTEMS_30MIN.md) | [Unknown poisoning](23_Clinical_Cases/CASE_UNKNOWN_POISONING_COMPLEX_PATIENT.md) | 対象・毒物・意思決定で分岐が大きく、単一図へ過度に単純化しない。 |

## 同期規則

1. SSOTの重要主張、用語、数値、推奨強度を変更したら、同じ行のCQ・Quiz・Slide・Caseを確認する。
2. Case/Quizは新しい治療内容を独自追加せず、SSOTまたは検証済みReferenceへ戻す。
3. 図がある領域は[Figure Index](../FIGURE_INDEX.md)のEvidence Sourceと確認日を同じPRで更新する。
4. 図がない領域は「不要」ではなく、表・timeline・local protocolの方が安全または有効な理由を記録する。
5. 専門家review後も、新版guideline・機器変更・施設protocol変更があれば再同期する。

## Review log

- 2026-08-12: 20領域についてSSOT、CQ、Quiz、Slide、Case、Visual/rationaleを相互監査し、同期台帳を作成。
