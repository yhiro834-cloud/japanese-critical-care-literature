---
title: "Human Factors and Team Communication"
status: review-needed
created: 2026-08-11
last_updated: 2026-08-12
evidence_reviewed: 2026-08-12
next_review: 2027-02-11
owners: []
reviewers: [Codex evidence review]
tags: [human-factors, communication, safety, handoff]
related: [../../32_Ethics_Safety_Systems/Safety_Systems/HUMAN_FACTORS_TRANSPORT_DISASTER_QI.md, ../ABCDE/README.md]
ssot: true
---

# Human Factors and Team Communication

## Design for predictable limits

fatigue、interruptions、noise、workload、similar packaging、mode confusion、authority gradientは通常のhuman limitationsである。memoryと注意だけに依存せず、standardization、forcing function、independent check、labeling、workspace design、staffing/escalationで防御層を作る。

## Match the control to the hazard

| Weak alone | Stronger system control |
|---|---|
| 注意喚起・再教育だけ | workflow redesign、standardization、forcing function |
| color/記憶だけ | barcode/identity check、physical separation、hard stop |
| 「ダブルチェックした」 | 独立して計算/原情報を確認し不一致を解消 |
| 個人の熟練だけ | role、checklist、simulation、backup、escalation |

強い対策も新たなworkaroundやalarm burdenを生み得るため、実装後にbalancing measureを確認する。

## Acute team cycle

```text
brief → leader/roles/priority → call-out and closed-loop
→ cross-monitor → shared reassessment → handoff → debrief
```

- orderはpatient、action、dose/setting、route/device、timingを明確にし、受け手がread-backする。
- concernは具体的riskとrequestを付け、未解決ならgraded escalationを続ける。
- debriefは「何が起きたか、何が助けたか、次回何を変えるか」を短く記録する。

## Closed-loop communication

```text
sender: 名指し + 明確な依頼 + timing
receiver: 内容を復唱し受諾/不可能を表明
sender: 正誤を確認
receiver: 実施後の結果を報告
```

read-backは単なる「はい」ではない。urgency、dose/setting、route/device、patient identityを含める。critical resultやhandoffには質問と確認の機会を確保する。

## Brief, huddle, and debrief

- brief：開始前にgoal、roles、threats、resources、contingency。
- huddle：状況/planが変わった時にmental modelとrolesを更新。
- debrief：事実、差異、成功、防御層、owner付き改善策。責任追及会にしない。

## Speaking up

concernを観察可能な事実、予想される害、具体的requestで伝える。応答がなければ再度明確に伝え、chain of command/rapid response等へgraded escalationする。心理的安全性は「反対意見に罰を与えない」だけでなく、leaderが明示的に問い、不確実性を表明し、懸念への対応を閉じることで作る。

## Just culture lens

outcomeの重大さだけで個人行動を評価せず、knowledge/skill gap、at-risk workaround、reckless actionとsystem contributionを区別する。報告者を責めず、再発防止策をownerと期限のあるsystem changeへ変換する。

## Incident learning

1. patient supportとopen disclosure/local reportingを行う。
2. timelineを記憶ではなくrecord/device/dataで構成する。
3. patient/task/team/environment/equipment/organizationの寄与を調べる。
4. outcome biasを避け、当時得られた情報で判断を評価する。
5. actionはowner、期限、measure、balancing measureを持つ。
6. frontlineへ学習を返し、同種processで効果を確認する。

## References

- AHRQ. [TeamSTEPPS](https://www.ahrq.gov/teamstepps-program/index.html).
- AHRQ. [TeamSTEPPS Tools](https://www.ahrq.gov/teamstepps-program/resources/modules/index.html).
- WHO. [Patient safety fact sheet](https://www.who.int/news-room/fact-sheets/detail/patient-safety). 2023.

## Review log

- 2026-08-12: control hierarchy, closed loop, team cycle, speaking up, and incident learning expanded.
- 2026-08-11: foundational human-factors and communication page added.
