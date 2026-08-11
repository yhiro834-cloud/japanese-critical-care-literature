# Visual Asset Plan

## Repository analysis

2026-08-12時点で、200 Markdown、72実体SSOT、21 Cases、20領域のCQ/Quiz/Slide Readyを確認した。既存本文は臨床推論・再評価・handoverを重視する一方、呼吸生理、人工呼吸波形、循環動態、ICP/CPP、CRRT/ECMO回路、bedside troubleshootingは文章のみではmental modelを形成しにくい。Phase 1は全領域の入口となるABCDEを6図へ分割し、以後のFigure Seriesに使うDesign Systemを確立する。

PriorityはP1（臨床推論またはmechanism理解への効果が大きい）、P2（補助的または専門領域）とする。Evidence Sourceは図の直接根拠となるKnowledge Base内SSOT/登録済みsourceを示す。

| Figure ID | Topic | Related Markdown | Learning Objective | Figure Type | Figure Content | Priority | Evidence Source | Planned File Name |
|---|---|---|---|---|---|---|---|---|
| FIG-G-ABCDE-001 | ABCDE overview | `docs/00_Fundamentals/ABCDE/README.md` | 異常発見後に介入と再評価へ戻る循環を説明 | SVG flow | safety→ABCDE→action→response→repeat | P1 | WHO/ICRC BEC 2018; ABCDE SSOT | `assets/general/abcde_reassessment_loop.svg` |
| FIG-G-ABCDE-002 | Airway pass | same | Aで見る所見・monitor・red flag・actionを区別 | SVG cards | voice/sound/patency/device/ETCO2 | P1 | Airway SSOT series | `assets/general/abcde_airway_detail.svg` |
| FIG-G-ABCDE-003 | Breathing pass | same | oxygenation・ventilation・workを分ける | SVG cards | RR/work/chest/SpO2/ETCO2/waveform | P1 | Breathing SSOT series | `assets/general/abcde_breathing_detail.svg` |
| FIG-G-ABCDE-004 | Circulation pass | same | pressureだけでなくperfusionを評価 | SVG cards | pulse/BP/CRT/skin/mentation/urine/lactate | P1 | Circulation SSOT series | `assets/general/abcde_circulation_detail.svg` |
| FIG-G-ABCDE-005 | Disability pass | same | 意識変化の即時評価を構造化 | SVG cards | GCS/JCS/pupil/motor/glucose/seizure/drug | P1 | Neurology SSOT series | `assets/general/abcde_disability_detail.svg` |
| FIG-G-ABCDE-006 | Exposure pass | same | 全身曝露と保温・尊厳を同時に扱う | SVG cards | temperature/skin/bleeding/source/trauma/device | P1 | Fundamentals/Trauma/Infection SSOT | `assets/general/abcde_exposure_detail.svg` |
| FIG-P-RESP-001 | Alveolar gas exchange | Respiratory Physiology | alveolus–capillary diffusionとdeliveryを理解 | SVG schematic | ventilation/diffusion/perfusion | P1 | Respiratory Physiology SSOT | `assets/physiology/alveolar_gas_exchange.svg` |
| FIG-P-RESP-002 | V/Q spectrum | Respiratory Physiology | shuntとdead spaceを連続体で理解 | SVG comparison | low V/Q→matched→high V/Q | P1 | Respiratory Physiology SSOT | `assets/physiology/vq_shunt_dead_space.svg` |
| FIG-P-RESP-003 | Oxyhemoglobin curve | Respiratory Physiology | curve shiftと臨床的限界を理解 | SVG graph | saturation vs PaO2, qualitative shifts | P1 | Respiratory Physiology SSOT | `assets/physiology/oxyhemoglobin_curve.svg` |
| FIG-V-VENT-001 | Pressure components | Mechanical Ventilation | PEEP・driving・peak/plateauの関係を理解 | SVG graph | airway pressure components | P1 | Mechanical Ventilation SSOT | `assets/ventilation/airway_pressure_components.svg` |
| FIG-V-VENT-002 | Peak vs plateau | Mechanical Ventilation | resistanceとcomplianceの鑑別を理解 | SVG comparison | peak↑ only vs plateau↑ | P1 | Mechanical Ventilation SSOT | `assets/ventilation/peak_vs_plateau_pressure.svg` |
| FIG-V-VENT-003 | Normal waveforms | Mechanical Ventilation | normal pressure/flow/volume time curvesを認識 | SVG waveform | synchronized normal traces | P1 | Mechanical Ventilation SSOT | `assets/ventilation/normal_time_waveforms.svg` |
| FIG-V-VENT-004 | Auto-PEEP | Mechanical Ventilation | expiratory flowがzeroへ戻らない意味を理解 | SVG waveform | air trapping | P1 | Mechanical Ventilation SSOT | `assets/ventilation/auto_peep_waveform.svg` |
| FIG-V-VENT-005 | Patient–ventilator asynchrony | Mechanical Ventilation | ineffective effort/double triggerを区別 | SVG waveform series | trigger/cycle mismatch | P1 | Mechanical Ventilation SSOT | `assets/ventilation/asynchrony_series.svg` |
| FIG-B-ARDS-001 | Normal vs injured alveolus | ARDS | edemaとaerated lung lossを理解 | SVG medical schematic | normal/injured alveoli | P1 | ATS ARDS 2024; ARDS SSOT | `assets/breathing/ards_alveolar_injury.svg` |
| FIG-B-ARDS-002 | Shunt mechanism | ARDS | perfused nonventilated unitとhypoxemiaを理解 | SVG schematic | capillary flow under flooded alveolus | P1 | ARDS/Respiratory Physiology SSOT | `assets/breathing/ards_shunt_mechanism.svg` |
| FIG-B-ARDS-003 | Prone mechanism | ARDS | recruitmentとstress distributionの概念を理解 | SVG comparison | supine vs prone schematic | P1 | ARDS SSOT; PROSEVA | `assets/breathing/prone_position_mechanism.svg` |
| FIG-C-HEMO-001 | Pressure–flow–perfusion | Hemodynamics | MAPだけでなくflow/perfusionを統合 | SVG concept map | pressure↔flow→organ signs | P1 | Hemodynamic Monitoring SSOT | `assets/circulation/pressure_flow_perfusion.svg` |
| FIG-C-HEMO-002 | Frank–Starling | Hemodynamics | responsivenessとcongestion riskを理解 | SVG graph | two operating regions | P1 | Fluid/Hemodynamics SSOT | `assets/circulation/frank_starling_concept.svg` |
| FIG-C-HEMO-003 | PLR reasoning | Hemodynamics | reversible preload challengeの解釈を理解 | SVG sequence | baseline→PLR→flow response | P1 | Fluid Therapy SSOT | `assets/circulation/plr_reasoning.svg` |
| FIG-C-SHOCK-001 | Shock classification | Shock | preload/pump/tone/obstructionの違いを比較 | SVG comparison | four phenotypes + mixed warning | P1 | Shock SSOT | `assets/shock/shock_classification.svg` |
| FIG-C-SHOCK-002 | Shock reasoning loop | Shock | phenotype→intervention→responseを循環化 | SVG algorithm | validity/flow/perfusion/reassessment | P1 | Shock SSOT | `assets/shock/shock_reasoning_loop.svg` |
| FIG-I-SEPSIS-001 | Sepsis physiology | Septic Shock | vasodilation/leak/myocardial dysfunctionを分解 | SVG mechanism | infection→dysregulated response→perfusion | P1 | SSC 2026; Septic Shock SSOT | `assets/sepsis/sepsis_pathophysiology.svg` |
| FIG-N-ICP-001 | Monro–Kellie | ICP/CPP/TBI | fixed volume内のcompensationを理解 | SVG stacked volume | brain/blood/CSF compensation | P1 | ICP/CPP/TBI SSOT | `assets/neurology/monro_kellie_doctrine.svg` |
| FIG-N-ICP-002 | ICP–CPP relationship | ICP/CPP/TBI | CPP=MAP−ICPを臨床的に解釈 | SVG graph/concept | rising ICP and CPP risk | P1 | ICP/CPP/TBI SSOT | `assets/neurology/icp_cpp_relationship.svg` |
| FIG-R-CRRT-001 | CRRT circuit | CRRT | accessからreturnまでの流れを説明 | SVG circuit | patient/pump/filter/effluent/return | P1 | CRRT SSOT | `assets/crrt/crrt_circuit.svg` |
| FIG-R-CRRT-002 | Clearance mechanisms | CRRT | diffusion/convection/UFを区別 | SVG comparison | solute/water movement | P1 | CRRT SSOT | `assets/crrt/crrt_clearance_mechanisms.svg` |
| FIG-R-CRRT-003 | Pressure alarm reasoning | CRRT | pressure patternからpatient/circuitを点検 | SVG algorithm | patient→access→filter→return | P1 | CRRT SSOT | `assets/crrt/crrt_alarm_reasoning.svg` |
| FIG-E-ECMO-001 | VV circuit | ECMO | drainage/oxygenation/returnを理解 | SVG circuit | venous→pump→oxygenator→venous | P1 | ECMO Foundations SSOT | `assets/ecmo/vv_ecmo_circuit.svg` |
| FIG-E-ECMO-002 | VA circuit | ECMO | circulatory supportのreturn方向を理解 | SVG circuit | venous→pump→oxygenator→arterial | P1 | ECMO Foundations SSOT | `assets/ecmo/va_ecmo_circuit.svg` |
| FIG-E-ECMO-003 | VA vs VV | ECMO |補助対象とmonitoringを比較 | SVG comparison | gas exchange vs gas+flow | P1 | ECMO Foundations SSOT | `assets/ecmo/va_vs_vv_ecmo.svg` |
| FIG-CR-001 | SpO2 fall reasoning | Bedside emergencies | patient-firstで原因を分解 | SVG algorithm | patient/airway/breathing/device/circulation | P1 | Bedside Alarm Response SSOT | `assets/clinical_reasoning/spo2_drop_reasoning.svg` |
| FIG-CR-002 | Hypotension reasoning | Bedside emergencies | measurement→perfusion→phenotypeを分ける | SVG algorithm | validity/preload/pump/tone/obstruction | P1 | Shock/Monitoring SSOT | `assets/clinical_reasoning/hypotension_reasoning.svg` |
| FIG-CR-003 | Altered consciousness | Bedside emergencies | immediate reversible causesを構造化 | SVG algorithm | ABC/glucose/drug/seizure/structural | P1 | Neuro Assessment SSOT | `assets/clinical_reasoning/altered_consciousness_reasoning.svg` |
| FIG-CR-004 | Low urine output | Bedside emergencies | production/obstruction/measurementを区別 | SVG algorithm | validity/perfusion/congestion/obstruction | P1 | AKI SSOT | `assets/clinical_reasoning/low_urine_output_reasoning.svg` |
| FIG-P-POCUS-001 | Lung artifacts | POCUS | 教育用模式図と実像を区別して概念理解 | SVG schematic | sliding/A-line/B-line/effusion | P2 | CCUS/Respiratory SSOT | `assets/pocus/lung_ultrasound_schematic.svg` |

## Phase order

1. Phase 1: FIG-G-ABCDE-001–006、Design System、Index、本文統合。
2. Phase 2: Respiratory physiology + normal/abnormal ventilator waveforms。
3. Phase 3: ARDS + shock/hemodynamics/sepsis。
4. Phase 4: ICP/CPP + CRRT + ECMO/MCS circuits。
5. Phase 5: emergency clinical reasoning seriesとPOCUS模式図。

