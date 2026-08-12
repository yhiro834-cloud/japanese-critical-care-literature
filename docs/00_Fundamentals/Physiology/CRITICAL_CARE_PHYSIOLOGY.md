---
title: "Critical Care Physiology Foundations"
status: review-needed
created: 2026-08-11
last_updated: 2026-08-12
evidence_reviewed: 2026-08-12
next_review: 2027-02-11
owners: []
reviewers: [Codex evidence review]
tags: [physiology, oxygen-delivery, homeostasis, microcirculation]
related: [../../02_Breathing/Respiratory_Physiology/RESPIRATORY_PHYSIOLOGY.md, ../../03_Circulation/Shock/SHOCK.md]
ssot: true
---

# Critical Care Physiology Foundations

## 0. まず覚える

**酸素運搬量（oxygen delivery：DO₂）**は、血液が1分間に全身へ運ぶ酸素量の概念で、心拍出量と動脈血酸素含量の両方に左右されます。

**簡単に言うと：** SpO₂や血圧が正常でも、Hbや血流、臓器への分布が不足すれば細胞へ十分な酸素は届きません。

**新人看護師の到達点：** SpO₂、Hb、血圧、脈拍、CRT、意識、尿量、体温、呼吸仕事量を同じtimelineで確認し、介入前後の変化を報告すること。

**ベテラン向け深掘り：** macro/microcirculation、静脈うっ血、酸素需要、extraction、測定誤差、臓器補助による新たな害を統合し、単一targetの正常化を患者改善と同一視しません。

### 報告例

> 「SpO₂は○○ですが、Hb○○、MAP○○、CRT○○、尿量○○で、酸素運搬または分布不足を懸念します。介入○○後の灌流所見と呼吸・循環への害を再評価してください。」

## Oxygen pathway

```text
inspired O₂ → alveolar gas exchange → arterial O₂ content
→ cardiac output × CaO₂ = systemic DO₂
→ regional distribution/microcirculation → cellular use (VO₂)
```

CaO₂は主にhemoglobin-bound oxygenで決まり、SpO₂/PaO₂だけではoxygen deliveryを表せない。DO₂はCaO₂とcardiac outputの積であり、同じMAPでもflowと臓器灌流は異なる。

### Working equations

```text
CaO₂ ≈ (1.34 × Hb × SaO₂) + (0.003 × PaO₂)
DO₂ = cardiac output × CaO₂ × 10
VO₂ = cardiac output × (CaO₂ − CvO₂) × 10
O₂ extraction ratio = VO₂ / DO₂
```

単位、採血部位、測定時刻、FiO₂/ventilator、輸血・循環介入との時間関係を揃えて解釈する。式から得た推定値を、直接測定された精密値のように扱わない。

## Demand, extraction, and reserve

発熱、shivering、work of breathing、agitation、seizureは需要を増やす。供給低下に対しextractionで代償できる範囲を超えるとVO₂が供給依存となり、臓器機能が悪化する。ただしlactate上昇は低酸素だけでなくadrenergic drive、clearance、薬剤等でも起こる。

### Bedside question

低酸素血症、貧血、low flow、distribution failure、需要増加のどこが支配的かを分ける。全要素を同時に「正常化」するのではなく、最も危険で可逆的な制約を治療し、responseとharmを確認する。

## Macro and microcirculation

HR、MAP、COなどmacro-hemodynamicsが改善しても、microcirculatory flowやorgan congestionが同時に改善するとは限らない。CRT、皮膚、意識、尿量、lactate trajectory、organ functionを統合し、介入反応で仮説を更新する。

## Pressure, flow, volume, and venous side

- pressureはflowの代理ではない。MAPは灌流圧の一部だが、COや局所血流を保証しない。
- preloadはvolumeそのものではなく、心筋線維長/充満とresponseの概念。fluid responsivenessは「輸液が必要」を意味しない。
- afterloadは単一のSVR値だけでなく、ventricular pressure load、arterial properties、valvular/outflow条件を含む。
- organ perfusionはinflowだけでなくvenous pressure/congestionにも左右される。高いCVPを一律にpreload目標としない。

## Acid-base as physiology

pHは呼吸性成分（PaCO₂）と代謝性成分の相互作用で決まる。異常値をlabelで終えず、ventilation、strong ion/renal handling、lactate/ketone/toxin、compensation、sampling errorを病態と時間軸へ戻す。詳細は[ABG SSOT](../../02_Breathing/ABG/ABG_INTERPRETATION.md)。

## Measurement-to-action loop

```text
clinical question → valid measurement? → physiologic meaning
→ competing explanations → action threshold → intervention
→ expected response/time → observed response + harm → update
```

同じ値でも「screening」「diagnosis support」「titration」「prognosis」で意味が異なる。trendは測定条件が比較可能なときにだけ有効である。

## Homeostasis under organ support

ventilator、vasopressor、fluid、CRRT、ECMOは生理を置換・修正するが、原因治療ではない。benefitと同時にpressure/volume injury、arrhythmia、fluid overload、drug clearance変化、device complicationを作り得る。

> [!CAUTION]
> equationは思考補助であり、測定誤差・時間変化・局所循環を消さない。単一targetの正常化を患者改善と同一視しない。

## References

- [Respiratory Physiology](../../02_Breathing/Respiratory_Physiology/RESPIRATORY_PHYSIOLOGY.md)
- [Shock](../../03_Circulation/Shock/SHOCK.md)
- [Hemodynamic Monitoring](../../03_Circulation/Hemodynamics/HEMODYNAMIC_MONITORING.md)
- [ABG Interpretation](../../02_Breathing/ABG/ABG_INTERPRETATION.md)

## Review log

- 2026-08-12: equations, pressure/flow/venous physiology, acid-base, and measurement-to-action loop expanded.
- 2026-08-11: oxygen pathway and homeostasis foundation added.
