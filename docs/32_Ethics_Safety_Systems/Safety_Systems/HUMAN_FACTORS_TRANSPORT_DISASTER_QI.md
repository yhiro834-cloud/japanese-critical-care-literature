---
title: "Human Factors, Transport, Disaster, and Quality Improvement"
status: review-needed
created: 2026-08-11
last_updated: 2026-08-12
evidence_reviewed: 2026-08-12
next_review: 2027-02-11
owners: []
reviewers: [Codex evidence review]
tags: [human-factors, transport, disaster, quality-improvement]
related: [../../20_Devices/Lifecycle/DEVICE_LIFECYCLE_BACKUP.md, ../../21_Emergency_Troubleshooting/Bedside_Emergencies/BEDSIDE_EMERGENCY_ALARM_RESPONSE.md]
ssot: true
---

# Human Factors, Transport, Disaster, and QI

> [!NOTE]
> **図で確認：** [安全を高める学習システム](../../../assets/safety/learning_system_loop.svg) — 有害事象を個人の注意不足で終わらせず、背景要因、対策、測定、再設計へつなぐ。

## 0. まず覚える

ヒューマンファクター（human factors）は、人の能力・限界と、作業、機器、環境、チーム、組織の相互作用から安全を設計する考え方である。エラーを「注意不足」で終わらせず、再発しにくい仕組みへ変える。

**簡単に言うと：** よい人にもっと注意させるだけでなく、間違いが起こりにくく、起きても患者を守れる仕組みを作る。

| 用語 | 意味 | 実践上のポイント |
|---|---|---|
| human factors | 人とsystemの相互作用を安全・性能の観点で扱う分野 | workload、UI、環境、team、policyを含める |
| latent condition | 普段は見えにくいsystem内の潜在的危険 | staffing、設計、供給、training等をeventから探る |
| pre-brief / debrief | 実施前の計画共有 / 実施後の振り返り | 役割、threat、stop条件、学習事項を共有する |
| go / no-go | 搬送・手技等を開始できるかの判断 | benefit、安定化、backup、destination、abortを確認する |
| incident command | 災害時に役割・情報・資源を統合する指揮system | 個人判断でtriageや資源基準を変更しない |
| balancing measure | 改善策が生む別の害・負担を測る指標 | delay、workload、inequity、workaroundを監視する |

**新人看護師の到達点：** 搬送前に目的、patient threat、役割、oxygen/power/drug予備、line/device、route、受入準備、abort条件を確認し、到着後にABCDEと設定を再照合できる。near missを報告し、事実と改善案を分けて記録する。

> **報告例：** 「CT搬送予定ですが、昇圧薬増量中で酸素予備も往復＋待機時間を満たしません。現時点はno-goとし、bedside代替と安定化、予備資源を再評価してください。」

**ベテラン向け深掘り：** 災害allocationは事前承認された透明で一貫したpolicyを用い、bedside clinician一人へ倫理負担を集中させない。QIはprocess/outcome/balancing measure、denominator、時間変化を定義し、一時的before-after改善やdocumentation率を患者利益と同一視しない。

## Reliable team actions

- pre-briefでleader、roles、plan、anticipated threats、stop criteriaを共有する。
- call-out、read-back/closed-loop、graded assertiveness、cross-monitoringを用い、急変後に短いdebriefを行う。
- errorを個人の注意不足だけで終えず、task、equipment、environment、staffing、handoff、policy、latent conditionsへ展開する。

## Intrahospital transport

```text
benefit > transport risk? → stabilize → team/equipment/oxygen/power/drug reserve
→ route + destination readiness → line/tube trace + handoff
→ continuous monitoring → arrival re-check → event/deviation review
```

### Transport go/no-go brief

- purpose、expected benefit、alternative at bedside、delay consequence
- current threats and minimum stabilization target
- leader、airway、monitor/device、drug roles
- oxygen/power/drug reserveを往復+delayで計算しbackupを用意
- ventilator/pump compatibility、MRI等destination restrictions
- line/tube/drain securement、route/elevator、receiving readiness
- deterioration/abort trigger、communication、return plan

出発直前と到着直後にABCDE、dose/setting、line、gas/oxygen、battery、patient positionを再確認する。

## Disaster / mass casualty

通常時の個別最適から、incident commandと利用可能資源下の集団最適へ移行する。施設が採用するtriage system、役割、communication、PPE/decontamination、surge、resource tracking、reunificationを用い、個人判断で基準を変更しない。

## Disaster operational domains

incident command、situational report、staff safety/PPE、contamination zones、triage/re-triage、surge space/staff/stuff、oxygen/power/medication、patient tracking、laboratory/blood、communication redundancy、family reunification、continuity for existing ICU patients、recovery/debriefを確認する。triage categoryは状態と資源で変わり得るため時刻と再評価を記録する。

allocation ruleは事前に承認された透明・一貫したpolicyを用い、bedside clinician一人へ倫理的負担を集中させない。disability、年齢、社会的価値等を無批判な代理指標にせず、公平性とappeal/reviewを確保する。

## Quality improvement loop

問題をoperational definitionとbalancing measureで定義し、baseline→small test→measure→adaptを反復する。process、outcome、balancing measureを分け、報告件数の増加を直ちに安全悪化と解釈しない。学習事項をpolicy、training、equipment、auditへ戻す。

### Measurement plan

| Measure | Example role |
|---|---|
| Structure | staff/equipment/policy availability |
| Process | eligible cases receiving intended action |
| Outcome | patient-centered result/harm |
| Balancing | delay、workload、new workaround、inequity |

denominator、data source、frequency、ownerを先に定義し、run chartで時間変化を見る。before-afterの一時的改善やdocumentation率だけでpatient benefitを断定しない。重大eventには個別分析、routine careにはaggregate learningを組み合わせる。

## Resilience and downtime

EHR/network/power/oxygen/supply failure時のminimum dataset、paper order、identity、medication/infusion、lab/result return、communication channel、reconciliationを訓練する。復旧時に二重投与・未実施・誤転記を防ぐreconciliation ownerを決める。

## References

- WHO. [Interagency Integrated Triage Tool](https://www.who.int/tools/triage).
- AHRQ. [TeamSTEPPS](https://www.ahrq.gov/teamstepps-program/index.html).
- WHO. [Patient safety](https://www.who.int/teams/integrated-health-services/patient-safety).

## Review log

- 2026-08-12: V2導入、human factors/latent condition/go-no-go/incident command/QI指標等の用語、新人搬送報告を追加。
- 2026-08-12: transport go/no-go, disaster domains/allocation, measurement plan, and downtime reconciliation expanded.
- 2026-08-11: initial systems framework; local command/transport/QI policy required.
