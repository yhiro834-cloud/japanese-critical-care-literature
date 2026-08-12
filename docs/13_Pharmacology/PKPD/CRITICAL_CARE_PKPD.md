---
title: "Critical Care Pharmacokinetics and Dose Reassessment"
status: review-needed
created: 2026-08-11
last_updated: 2026-08-12
evidence_reviewed: 2026-08-12
next_review: 2027-02-11
owners: []
reviewers: [Codex evidence review]
tags: [pharmacology, pkpd, organ-failure, tdm]
related: [../../05_Renal/CRRT/CRRT.md, ../../06_Infection_Sepsis/Antimicrobial_Source_Control/ANTIMICROBIAL_SOURCE_CONTROL.md]
ssot: true
---

# Critical Care Pharmacokinetics and Dose Reassessment

## 0. まず覚える

薬物動態（pharmacokinetics: PK）は体が薬をどう処理するか、薬力学（pharmacodynamics: PD）は薬が体や病原体へどう作用するかを扱う。重症患者では浮腫、臓器不全、CRRT、ECMOなどで通常の投与設計が外れやすい。

**簡単に言うと：** 「腎機能が悪いから減らす」だけでなく、最初に必要量を届かせるloadingと、その後に蓄積させないmaintenanceを分け、効果と毒性で調整する。

| 用語 | 意味 | 実践上のポイント |
|---|---|---|
| volume of distribution（Vd） | 薬が体内へどの程度広がるかを表す見かけの容積 | 浮腫・capillary leakで水溶性薬のloadingに影響 |
| clearance | 単位時間に薬が体から除去される能力 | 腎肝機能、KRT、臓器血流で変化する |
| loading dose | 目標濃度へ早く到達するための初回量 | 主にVdで考え、腎障害だけで自動減量しない |
| maintenance dose | 目標曝露を維持するための継続量 | clearanceと臓器機能のtrajectoryで再評価する |
| TDM | therapeutic drug monitoring、治療薬物monitoring | 採血時刻、投与時刻、部位、targetをそろえて解釈する |
| augmented renal clearance | 重症時に腎clearanceが予想以上に増える状態 | serum creatinineが低くてもunderexposureを起こしうる |

**新人看護師の到達点：** 適応、投与量・時刻、採血時刻・部位、尿量/腎肝機能、CRRT実稼働、ECMO、効果・毒性を同じtimelineで記録し、臓器support変更時に薬剤再評価を依頼できる。

> **報告例：** 「CRRTが6時間停止していましたが、薬剤は稼働中の設定で継続されています。尿量も減少し薬剤蓄積riskがあります。実際のclearanceに合わせたmaintenance doseとTDM時刻の再評価をお願いします。」

**ベテラン向け深掘り：** non-steady-state creatinine、低筋量、fluid dilution、蛋白結合、active metabolite、ECMO sequestrationを考慮する。TDM値が臨床像と合わない場合はdose変更前にline contamination、sampling window、missed dose、assay限界を検証する。

## Why usual dosing fails

critical illness changes volume of distribution、protein binding、organ perfusion、clearance。fluid resuscitation/capillary leakはhydrophilic drug exposureを下げ、AKI/acute liver injuryは蓄積を、augmented renal clearanceはunderexposureを起こし得る。ECMO、CRRT、plasma exchange、obesity、burnsが重なる。

## Separate loading, maintenance, and effect

- loading exposureは主にVdと早期target到達で考える。renal dysfunctionだけで自動減量しない。
- maintenance exposureはclearance、dose interval/infusion、organ trajectory、extracorporeal removalで考える。
- pharmacodynamic endpointはdrugごとに異なり、血中濃度だけでなくclinical effect、organism/MIC、toxicityを統合する。
- active metabolite、high protein binding、tissue penetration、nonlinear kineticsが単純式を崩し得る。

## Dose reasoning loop

```text
indication + target site/organism
→ loading need (Vd) / maintenance need (clearance)
→ weight scalar + renal/hepatic function + extracorporeal support
→ concentration/clinical effect/toxicity
→ trajectory changes → re-dose, de-escalate, stop
```

- “renal dysfunctionだからloadingも減量”を自動化しない。
- serum creatinineはnon-steady state/low muscle massでclearanceを誤る。
- CRRTはmodality、effluent、downtime、filter、residual functionを確認。
- ECMO sequestrationの影響はdrug/circuitで異なり、TDMとclinical endpointを活用。

## Dynamic renal and hepatic assessment

AKIのcreatinineは遅れて変化し、fluid balanceや低筋量で希釈/過小評価される。尿量、trajectory、KRT開始/停止、残存腎機能、nephrotoxinを併記する。肝機能は単一enzymeではなくsynthetic function、bilirubin、flow/congestion、drug extraction、encephalopathyを分ける。

## Extracorporeal support handoff

| Factor | Verify |
|---|---|
| CRRT | modality、effluent prescribed/delivered、downtime、filter age、residual urine、adsorption |
| Intermittent KRT | session timing、duration、access、post-dialysis dose |
| ECMO | circuit age/configuration、drug lipophilicity/protein binding、organ recovery、TDM |
| Plasma exchange | exchanged volume/timing、protein binding/Vd、redosing plan |

「CRRT中」とだけhandoffせず、24時間の実稼働とdose timingを同じtimelineへ置く。

## TDM and medication review

採血時刻、dose/infusion、sampling site、steady state、assay、targetを揃えて解釈する。毎日、indication、重複、interaction、QT、anticholinergic/sedative burden、renal/hepatic trajectory、stop date、enteral transitionをreviewする。

### TDM specimen integrity

同じlineから採血する場合のcontamination、infusion interruption、peak/trough/AUC sampling window、missed/delayed doseを記録する。数値が臨床像と合わないときはdose変更前に採血条件とassay limitationを確認する。

## Daily medication reconciliation

`continue / adjust / hold / stop / convert route`を全薬剤で決め、理由と次回review triggerを残す。home medicationの離脱、duplicated PRN、nutrition-feed interaction、QT/electrolyte、anticholinergic/sedative burden、antimicrobial stop/de-escalation、VTE/stress-ulcer indicationを確認する。

> [!CAUTION]
> “腎機能正常”“CRRT中”“ECMO中”だけで固定doseにしない。薬剤師とpatient/device-specific情報を確認する。

## References

1. Abdul-Aziz MH, et al. Antimicrobial therapeutic drug monitoring in critically ill adults: a Position Paper. Intensive Care Med. 2020. DOI: `10.1007/s00134-020-06050-1`; PMID: `32383061`.
2. ELSO Guidelines portal. https://www.elso.org/ecmo-resources/elso-ecmo-guidelines.aspx

## Review log

- 2026-08-12: V2導入、PK/PD、Vd、clearance、loading/maintenance、TDM等の用語、新人のtimeline報告を追加。
- 2026-08-12: loading/maintenance separation, dynamic organ assessment, extracorporeal handoff, TDM integrity, and reconciliation expanded.
- 2026-08-11: PK/PD review; ICU pharmacist/local TDM review required.
