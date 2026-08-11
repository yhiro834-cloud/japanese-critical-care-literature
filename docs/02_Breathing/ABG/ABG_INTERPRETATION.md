---
title: "ABG and Acid–Base Interpretation"
status: review-needed
created: 2026-08-11
last_updated: 2026-08-11
evidence_reviewed: 2026-08-11
next_review: 2027-02-11
owners: []
reviewers: [Codex evidence review]
tags: [abg, acid-base, oxygenation, ventilation]
related: [../Respiratory_Physiology/RESPIRATORY_PHYSIOLOGY.md]
ssot: true
---

# ABG and Acid–Base Interpretation

> [!CAUTION]
> ABGは採血時点のsnapshotです。数式は近似であり、患者評価・経時変化・原因診断を置き換えません。重篤なacidemia、呼吸疲弊、急速な変化は直ちに担当チームへescalationしてください。

## 1. Overview

ABGはpH、PaCO₂、PaO₂を測定し、HCO₃⁻等を算出してventilation、oxygenation、acid–baseを評価します。正しい解釈は「値を読む」だけでなく、検体、FiO₂、体位、時刻、介入との関係を確認する作業です。

## 2. Why It Matters

同じpHでも原因・緊急度は異なります。単純なラベル付けではmixed disorder、呼吸疲弊、検体error、代償限界を見逃します。

## 3. Physiology

Henderson–Hasselbalchの臨床的関係：

`pH = 6.1 + log(HCO₃⁻ / (0.03 × PaCO₂))`

- PaCO₂: respiratory component
- HCO₃⁻: metabolic componentを表す従属的指標
- kidneyとlungのcompensationはpHを正常方向へ動かすが、通常「過剰代償」で反対側へ越えない

Stewart approachはPCO₂、strong ion difference、weak acidsから説明します。traditional approachと対立する唯一の正解として扱わず、hyperchloremiaやhypoalbuminemiaを見抜く補助にします。

## 4. Pathophysiology

| Primary disorder | 主変化 | 代表原因 |
|---|---|---|
| Metabolic acidosis | HCO₃⁻低下 | lactate、ketoacid、腎不全、HCO₃ loss、toxin |
| Metabolic alkalosis | HCO₃⁻上昇 | gastric loss、diuretic、mineralocorticoid、post-hypercapnic |
| Respiratory acidosis | PaCO₂上昇 | hypoventilation、fatigue、obstruction、CNS/neuromuscular |
| Respiratory alkalosis | PaCO₂低下 | hypoxemia、pain/anxiety、sepsis、pregnancy、CNS、ventilator |

## 5. Causes / Etiology

### High anion gap metabolic acidosis

Lactate、ketoacidosis、renal failure、toxic alcohol/salicylate等を臨床文脈で評価します。Mnemonicは検査やhistoryの代替ではありません。

### Normal anion gap metabolic acidosis

GI HCO₃ loss、renal tubular acidosis、chloride-rich fluid、尿路/腸管関連等。

## 6. Assessment

ABG前に以下を確認します。

- なぜ採るか：oxygenation、ventilation、acid–base、intervention response
- FiO₂/device、PEEP、体位、採血部位、時刻
- patient–ventilator synchrony、RR/work、意識、perfusion
- 直前の吸引、体位変換、oxygen/ventilator変更
- 同時のNa、Cl、albumin、lactate、glucose、ketone、renal function

## 7. Monitoring

反復ABGは目的と採血riskを比較します。SpO₂、ETCO₂、VBG、clinical trendで代替可能な問いと、PaO₂/PaCO₂の正確なarterial measurementを要する問いを区別します。

## 8. Interpretation

### 8-step approach

1. **患者・検体・条件:** 本人、時刻、arterialか、FiO₂/PEEP、air bubble/delay
2. **pH:** acidemia / alkalemia / near-normal
3. **PaCO₂とHCO₃⁻:** pH方向を説明するprimary processを特定
4. **Expected compensation:** 範囲外ならmixed disorder
5. **Anion gap:** `AG = Na − (Cl + HCO₃)`（Kを含める式か確認）
6. **Albumin correction:** 低albuminでAGが隠れる。概算 `corrected AG = AG + 2.5 × (4 − albumin[g/dL])`
7. **Oxygenation:** PaO₂、P/F、A–a、FiO₂/device、SpO₂との一致
8. **臨床統合とtrend:** 原因、緊急度、次の評価、介入後再検

### Expected compensation（成人の近似）

| Primary disorder | 期待される変化の近似 |
|---|---|
| Metabolic acidosis | Winter: `PaCO₂ ≈ 1.5 × HCO₃ + 8 ±2` |
| Metabolic alkalosis | `PaCO₂ ≈ 40 + 0.7 × (HCO₃ − 24) ±5` |
| Acute respiratory acidosis | PaCO₂ +10ごとにHCO₃約+1 mmol/L |
| Chronic respiratory acidosis | PaCO₂ +10ごとにHCO₃約+3.5–4 mmol/L |
| Acute respiratory alkalosis | PaCO₂ −10ごとにHCO₃約−2 mmol/L |
| Chronic respiratory alkalosis | PaCO₂ −10ごとにHCO₃約−4–5 mmol/L |

近似値、基準値、acute/chronic境界は資料で差があります。範囲外ならmixed disorderを疑いますが、診断は臨床経過と統合します。

### Delta assessment

High AG acidosisで`ΔAG`と`ΔHCO₃`の不釣り合いは追加のmetabolic processを示唆します。baseline、albumin、測定法の影響があるため単独確定に使いません。

### VBGをどう使うか

Peripheral VBGのpH/HCO₃は特定状況でABGと概ね近いことがありますが、PvCO₂のagreementは広く、PaO₂の代用にはなりません。AARC 2013はvenous PCO₂/pHをarterial measurementの代替として一律使用しないよう記載しています。問い・患者・local validationに応じて選びます。

## 9. Diagnosis

ABGが示すのはprocessであり病名ではありません。例えばrespiratory alkalosisはpainでもPEでもsepsisでも起こります。原因診断にはhistory、exam、laboratory、imagingが必要です。

## 10. Clinical Reasoning

```text
ABG異常
→ 患者は安定か／採血条件は信頼できるか
→ oxygenation・ventilation・acid-baseのどの問いか
→ pH → primary process → expected compensation
→ AG/albumin → mixed metabolic process
→ PaO₂/PF/A-aとFiO₂/device
→ 原因仮説と緊急度
→ 介入
→ clinical statusと再検値で仮説更新
```

### 例

`pH 7.25 / PaCO₂ 24 / HCO₃ 10`

Metabolic acidosisがprimary。Winter expected PaCO₂は約23±2で、respiratory compensationは概ね期待範囲。次にAG、albumin、lactate、ketone、renal function、toxin/historyを確認します。これだけで原因は確定しません。

## 11. Treatment

数値ではなく原因と生理的脅威を治療します。airway/ventilation failure、shock、seizure、toxin、DKA、renal failure等の緊急原因を優先します。pHだけを正常化する介入には害があり得ます。

## 12. Nursing Points

- sampling前後のFiO₂、device、PEEP、体位、ventilator設定を記録
- arterial line sampleはdead-space/flush contaminationを防ぎ施設手順に従う
- syringe内airを除き、混和し、速やかに分析/搬送
- patient ID、arterial/venous source、採血時刻を確認
- critical resultはread-backし、患者所見とともに報告
- 値が臨床像と合わなければ再採血前にpreanalytical errorを検討

## 13. ICU Nursing Pearls

- HCO₃⁻は多くのanalyzerで計算値。chemistry total CO₂と完全一致しないことがある
- co-oximetryなしのcalculated saturationはdyshemoglobinを見逃し得る
- CO poisoningではPaO₂が保たれてもtissue oxygen deliveryは障害され得る
- severe anemiaではPaO₂/SaO₂が保たれてもCaO₂が低い

## 14. Red Flags

- pHの急速な悪化、severe acidemia/alkalemia
- PaCO₂上昇と意識低下/疲弊
- oxygen増量でもPaO₂/SpO₂悪化
- PaCO₂が一見正常でもsevere metabolic acidosisに対し代償不足
- salicylate等を示唆するmixed respiratory alkalosis + metabolic acidosis
- 値と患者が著しく不一致

## 15. Troubleshooting

### 結果が不自然

1. 患者・採血部位・label
2. FiO₂/device/体位/時刻
3. air bubble、delay、過剰liquid heparin、line flush contamination
4. analyzer/calculated value
5. 必要なら適切な条件で再採血

## 16. Common Pitfalls

- pH正常でacid–base disorderなしと判断
- compensationを別のprimary disorderと誤認、またはmixed disorderを見逃す
- albumin低下を無視してnormal AGと判断
- VBG PaO₂でoxygenation評価
- ABG採血条件を記録せずtrend比較
- calculated SaO₂でCOHb/MetHbを除外

## 17. Clinical Case

- [SpO₂突然低下とPaCO₂上昇](../../23_Clinical_Cases/CASE_DESATURATION_HYPERCAPNIA.md)

## 18. Clinical Questions

- [Respiratory Physiology / ABG Questions](../../24_Clinical_Questions/RESPIRATORY_PHYSIOLOGY_ABG_QUESTIONS.md)

## 19. Quiz

- [Respiratory Physiology / ABG Quiz](../../25_Quiz/QUIZ_RESPIRATORY_PHYSIOLOGY_ABG.md)

## 20. Take Home Messages

1. ABGは採血条件を含めて解釈する。
2. pH → primary → compensation → AG → oxygenation → clinical integrationの順で読む。
3. 正常pHでもmixed disorderはあり得る。
4. VBGは問いにより有用だがPaO₂代替ではなく、PaCO₂ agreementにも限界がある。
5. 数値ではなく原因を治療し、患者とtrendで再評価する。

## 21. Slide Ready Summary

[20分教材](../../27_Slide_Ready/RESPIRATORY_PHYSIOLOGY_ABG_20MIN.md)

## 22. References

| ID | Citation | DOI | PMID / official URL | Evidence type | Supports |
|---|---|---|---|---|---|
| GL-2013-001 | Davis MD, et al. AARC Clinical Practice Guideline: Blood Gas Analysis and Hemoximetry: 2013. Respir Care. | 10.4187/respcare.02786 | PMID 23901131; https://www.aarc.org/resource/clinical-practice-guidelines/ | Clinical practice guideline | indications, limitations, hemoximetry, arterial/venous distinctions |
| REF-2014-001 | Bloom BM, et al. The role of venous blood gas in the emergency department. | 10.1097/MEJ.0b013e32836437cf | PMID 23903783 | Systematic review/meta-analysis | VBG–ABG agreement and limitations |
| REF-2022-002 | Çuhadar S, et al. Detection of preanalytical errors in arterial blood gas analysis. | 10.11613/BM.2022.020708 | PMID 35799987 | Experimental study | delay/air bubble effects |
| REF-2020-001 | Sjoding MW, et al. Racial Bias in Pulse Oximetry Measurement. | 10.1056/NEJMc2029240 | PMID 33326721 | Retrospective paired-measurement study | occult hypoxemia disparity |
| FDA-2025-001 | FDA. Pulse Oximeters. | — | https://www.fda.gov/medical-devices/products-and-medical-procedures/pulse-oximeters | Regulatory safety information | device limitations and influencing factors |

Identifiers and official pages verified 2026-08-11. Compensation formulae are standard clinical approximations rather than recommendations from a single guideline.

## Review Log

| Date | Reviewer | Scope | Result |
|---|---|---|---|
| 2026-08-11 | Codex | evidence identity / equations / sample safety / nursing | Evidence reviewed; respiratory/clinical laboratory expert review needed |
