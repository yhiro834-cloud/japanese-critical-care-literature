---
title: "Bedside Emergency and Alarm Response"
status: review-needed
created: 2026-08-11
last_updated: 2026-08-12
evidence_reviewed: 2026-08-12
next_review: 2027-02-11
owners: []
reviewers: [Codex evidence review]
tags: [emergency, alarm, desaturation, hypotension]
related: [../../19_Monitoring/Core_Monitoring/MONITORING_WAVEFORMS_ARTIFACT.md, ../../20_Devices/Lifecycle/DEVICE_LIFECYCLE_BACKUP.md]
ssot: true
---

# Bedside Emergency and Alarm Response

## 0. まず覚える

bedside emergencyでは、alarm名やmonitor値の診断より、**患者を見て応援を呼び、ABCDEを支え、患者・interface・回路・機械・供給源を切り分ける**ことが先である。

**簡単に言うと：** alarmを止めるのではなく、患者の危険を止める。改善後も原因と再発防止まで閉じる。

| 用語 | 意味 | 実践上のポイント |
|---|---|---|
| independent support | 問題deviceと別の方法で生命機能を一時的に支えること | manual ventilationやbackup pumpなどをtrained teamで行う |
| troubleshooting | 原因候補を系統的に切り分けること | 同じ失敗介入を反復せず、反応で次へ進む |
| working diagnosis | 現時点で最も疑う仮の原因 | 新情報と反応に応じて更新し、固定しない |
| nuisance alarm | 患者危険を示さない反復alarm | 無効化せずsensor、limit、delay、workflowを修正する |
| alarm fatigue | 多数のalarmにより反応性が低下する危険 | 優先度設計、個別limit、保守、event reviewで対処する |
| debrief | event後に経過・判断・改善点を振り返ること | 時刻、介入と反応、未解決事項、再発防止を共有する |

**新人看護師の到達点：** alarm時に患者の反応、pulse、呼吸、皮膚/灌流を確認して早期に応援要請し、airway、oxygen、line、circuit、電源・gasを両端まで見る。介入時刻と反応を記録し、原因不明・改善なしを即時escalateできる。

> **報告例：** 「突然SpO₂が低下し、胸郭運動も低下しています。応援要請し、airwayとcircuitを確認、manual supportを準備しています。probe artifactだけとせず、tube閉塞・脱落、気胸を含む緊急評価をお願いします。」

**ベテラン向け深掘り：** manual ventilationで改善した/しないという一所見でpatient/device causeを二分せず、technique、airway、胸郭、肺血流を再評価する。alarm limit変更には根拠、期限、戻すownerを持たせ、event後のdevice・薬剤・logを保全する。

## Visual Series：急変時の臨床推論

1. [SpO₂突然低下](../../../assets/clinical_reasoning/spo2_drop_reasoning.svg)：患者・signal・airway/breathing・device/循環を並行評価する。
2. [突然の低血圧](../../../assets/clinical_reasoning/hypotension_reasoning.svg)：測定、灌流、循環表現型、drug deliveryを分ける。
3. [急な意識変化](../../../assets/clinical_reasoning/altered_consciousness_reasoning.svg)：ABC、血糖、神経所見、薬剤、構造/電気的原因を追う。
4. [尿量低下](../../../assets/clinical_reasoning/low_urine_output_reasoning.svg)：測定/閉塞、灌流、うっ血、腎/薬剤を分ける。

図は急変対応を遅らせる順番表ではありません。応援要請と生命機能supportを先行し、複数人なら評価・支持・記録を並行します。

## Universal sequence

**患者を見る → 応援/緊急call → ABCDE → independent support → patient/device/circuit/sourceを並行確認 → 原因修正 → response確認 → debrief。** monitorだけを見ず、pulse、意識、呼吸、skin/perfusionを確認する。

## First-minute team split

- leader：priority、working threat、reassessmentを声に出す。
- A/B：airway、胸郭、oxygen/circuit、manual backup。
- C：pulse/perfusion、rhythm、bleeding、infusion/line。
- D/E：consciousness/pupil/glucose、temperature/exposure。
- recorder/runner：時刻、intervention/response、equipment/senior call。

一人しかいない場合もこの順に短く走査し、早く応援を呼ぶ。

## Sudden desaturation

airway displacement/obstruction、circuit disconnect、oxygen source、pneumothorax、atelectasis/secretions、bronchospasm、edema/aspiration/PE、artifactをDOPEに限定せず検索。必要ならventilatorから外して適切なmanual ventilationでpatient/lung mechanicsを確認し、high pressure/low volume alarmのpatient側とmachine側を分ける。

manual ventilationへ移る際はtrained clinician、oxygen source、PEEP/pressure/volume risk、ETCO₂、胸郭/pulseを確認する。manualで改善＝ventilator故障、改善なし＝patient causeと単純化せず、techniqueとairwayも再評価する。

## Sudden hypotension

true pressure/pulseを確認し、bleeding/hypovolemia、distributive、cardiogenic、obstructive、arrhythmia、drug delivery/line、measurement systemを同時に評価する。temporary perfusion supportを行いながら、POCUS/ECG/lab等で原因を絞る。

新しい低血圧では直近のposition/procedure、ventilator/PEEP、sedation/bolus、infusion交換、drain output、allergy/exposureをtimelineで確認する。fluid/vasopressor反応を原因確定とみなさず、harmと再発を追う。

## Acute neurological change

airway/oxygen/BP/glucose、pupil/GCS/focal sign、sedative/NMBA、seizure、stroke/bleed/ICP、metabolic/toxicを確認し、last-known-wellと時刻を記録する。鎮静薬で所見を隠す前に可能な評価を行う。

## Device alarm

patient dependenceを判断し、manual/backup supportを確保。両端をtraceし、kink/clamp/disconnection/position、circuit、sensor、power/gas/batteryを確認する。device固有の危険操作はtrained specialist/manualに従う。

## Alarm accountability

alarmごとに「誰が応答したか、patientへの影響、原因、修正、再発防止」を閉じる。limitを変更した場合は根拠と期限を記録する。nuisance alarmは無効化ではなくsensor/site/lead、delay/priority、patient-specific limit、maintenance、workflowを見直す。

## After stabilization

event timeline、baselineとの差、interventions and response、unresolved differential、temporary device/setting、next check、family communicationをhandoffする。薬剤/機器/検体を不用意に廃棄せず、incident reviewに必要な情報を保全する。

> [!DANGER]
> repeated reset、alarm silencing、同じfailed interventionの反復でescalationを遅らせない。改善しない/原因不明なら早い段階でsenior/specialist/OR/IR/ECMO等へ拡大する。

## References

1. AHA. 2025 Adult Advanced Life Support. https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-advanced-life-support
2. SCCM. ICU Liberation and emergency care resources. https://www.sccm.org/clinical-resources

## Review log

- 2026-08-12: V2導入、independent support/troubleshooting/alarm fatigue/debrief等の用語、新人の初動・報告を追加。AHA 2025を再確認。
- 2026-08-12: first-minute team split, manual ventilation limits, timeline triggers, alarm accountability, and post-event handoff expanded.
- 2026-08-11: Cross-domain emergency synthesis; simulation/local rapid-response validation required.
