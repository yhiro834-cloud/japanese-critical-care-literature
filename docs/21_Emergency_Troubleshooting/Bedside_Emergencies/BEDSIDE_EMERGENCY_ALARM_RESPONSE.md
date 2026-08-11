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

- 2026-08-12: first-minute team split, manual ventilation limits, timeline triggers, alarm accountability, and post-event handoff expanded.
- 2026-08-11: Cross-domain emergency synthesis; simulation/local rapid-response validation required.
