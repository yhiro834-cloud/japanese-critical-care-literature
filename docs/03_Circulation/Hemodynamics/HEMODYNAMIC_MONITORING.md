---
title: "Hemodynamic Monitoring and Fluid Responsiveness"
status: review-needed
created: 2026-08-11
last_updated: 2026-08-12
evidence_reviewed: 2026-08-12
next_review: 2027-02-11
owners: []
reviewers: [Codex evidence review]
tags: [hemodynamics, perfusion, cardiac-output, fluid-responsiveness]
related: [../Shock/SHOCK.md, ../Fluid_Therapy/FLUID_THERAPY.md, ../POCUS/HEMODYNAMIC_POCUS.md]
ssot: true
---

# Hemodynamic Monitoring and Fluid Responsiveness

> [!CAUTION]
> monitor値は診断ではありません。測定品質、適用条件、患者の灌流、介入への反応を確認し、単一のMAP・CVP・PPV・SVV・CO値で治療しないでください。

## 0. まず覚える

**血行動態（hemodynamics）**は、心臓と血管によって血液がどの圧・流れで全身を巡るかを扱う考え方です。

**簡単に言うと：** monitorの数値を集めるのではなく、「圧はあるか」「流れはあるか」「臓器へ届いているか」を確かめます。

| 用語 | 簡単な意味 | 限界 |
|---|---|---|
| MAP | 平均的な動脈圧 | 適切な目標は患者と灌流反応で異なる |
| CVP | 中心静脈圧 | volume量やfluid responsivenessを単独で示さない |
| SV/CO | 1回/1分の心拍出 | 測定法、調律、換気条件の影響を受ける |
| fluid responsiveness | 輸液でSV/COが増える可能性 | 輸液が必要・安全という意味ではない |

**新人看護師の到達点：** transducer level/zero、波形、cuffとの整合、体位、調律を確認し、患者の灌流所見と一緒に報告すること。

**ベテラン向け深掘り：** dynamic testの適用条件、RV failure、腹腔/胸腔圧、arrhythmia、spontaneous effort、測定法間差を統合します。

## 1. Overview

血行動態monitoringの目的は、shockの有無と型、酸素供給不足の機序、介入に反応する可能性、害を検出することです。ESICM 2025はserial tissue perfusion、dynamic fluid responsiveness、非反応例でのarterial pressureとCO/SV monitoring、shock type評価のfirst-line echocardiographyを強調します。

## 2. Physiology

- `MAP ≈ CO × SVR`（CVPを省略した近似）
- `CO = HR × SV`
- `DO₂ = CO × CaO₂`
- `SVR ≈ 80 × (MAP − CVP) / CO`

MAPが保たれてもCO/DO₂不足はあり、低MAPでも灌流障害の程度は患者で異なります。値ではなくflow、pressure、oxygen content、組織応答を統合します。

## 3. Bedside Perfusion

- 意識、skin temperature/mottling、capillary refill time（CRT）、尿量
- lactate値とclearance：生成、利用、肝 clearance、薬剤等の影響を考える
- HR/BP/temperature、pulse pressure、ETCO₂、呼吸循環相互作用
- central lineがある場合のScvO₂/SvO₂、veno-arterial CO₂ gapはtrend補助。単独targetではない

## 4. Pressure and Flow Monitoring

### Arterial line

level/zero、air bubble、tubing、damping、waveformを確認します。over/underdampingで収縮期/拡張期は歪みますがMAPは比較的保たれることがあります。cuffとの不一致は部位・波形・測定条件を再確認します。

### CVP

右房圧の近似で、波形・呼吸・PEEP・RV/胸腔/腹腔圧の影響を受けます。単一CVPでvolume statusやfluid responsivenessを決めません。

### CO/SV

echo、pulse contour、thermodilution等は前提・校正・不整脈・ventilation・valve/shuntの影響が異なります。絶対値だけでなく、同条件でのtrendと介入反応を重視します。

## 5. Fluid Responsiveness

fluid responsivenessは「preload増加でSV/COが増える可能性」であり、「輸液が必要」「予後が改善」「安全」の同義語ではありません。

- passive leg raise（PLR）はreversible preload challenge。CO/SVをreal time測定する
- small fluid challengeは投与量・時間・response/stop criteriaを事前定義
- PPV/SVVはcontrolled ventilation、十分なVT、規則的rhythm、自発呼吸なし等の条件に依存
- end-expiratory occlusion等も適用条件がある
- IVC径/呼吸性変動単独はfluid responsivenessの万能指標ではない

## 6. Clinical Reasoning

```text
低血圧/灌流異常 → 測定は信頼できるか → shock phenotypeと緊急原因
→ CO/SVは低いか → preload/contractility/afterload/HRに分解
→ fluidを考えるなら responsiveness + need + tolerance
→ 小さく目的を定めて介入 → SV/COと組織灌流、肺/RV/静脈うっ血を再評価
```

## 7. Nursing Points

- line level/zero、pressure bag、waveform、末梢循環、穿刺部をshift/体位変更後に確認
- PLRやchallengeはbaseline、時刻、体位、ventilator、薬剤、SV/CO、BP、CRTを揃えて記録
- urine outputは時間・体重・catheter patency・腎病態を確認
- vasopressor変更時はMAPだけでなく末梢、意識、尿量、不整脈、乳酸trendを報告
- alarmを無効化せず、artifactと真の変化を患者所見で区別

## 8. Red Flags / Pitfalls

- progressive mottling/意識低下/oliguria/lactate上昇、narrow pulse pressure、new arrhythmia
- zero/level不良、damped waveform、CVP/IVCをvolumeの答えにする
- fluid responsiveだから輸液、MAP正常だからshockなし、lactateだけを正常化

## 9. Take Home Messages

1. serial perfusion assessmentをpressureとflowに統合する。
2. fluid responsivenessはneed/toleranceと別に判断する。
3. 介入前に期待するresponseとstop criteriaを決める。

## 10. References

- Monnet X, et al. ESICM guidelines on circulatory shock and hemodynamic monitoring 2025. Intensive Care Med. DOI: 10.1007/s00134-025-08137-z; PMID: 41236566.

## Review Log

| Date | Reviewer | Scope | Result |
|---|---|---|---|
| 2026-08-12 | Codex | V2 terminology / measurement limits / nursing | Staged-learning introduction added; hemodynamics expert review needed |
| 2026-08-11 | Codex | guideline / physiology / nursing | Evidence reviewed; hemodynamics expert review needed |
