---
title: "Clinical Reasoning in Critical Care"
status: reviewed
created: 2026-08-11
last_updated: 2026-08-12
evidence_reviewed: 2026-08-12
next_review: 2027-02-11
owners: []
reviewers: [Codex evidence review]
tags: [clinical-reasoning, cognitive-bias, differential, reassessment]
related: [../ABCDE/README.md, ../../21_Emergency_Troubleshooting/Bedside_Emergencies/BEDSIDE_EMERGENCY_ALARM_RESPONSE.md]
ssot: true
---

# Clinical Reasoning in Critical Care

## 0. まず覚える

**臨床推論（clinical reasoning）**は、患者の情報から問題を表現し、危険な仮説を比較し、行動と再評価で仮説を更新する過程です。

**簡単に言うと：** 最初の診断名へ当てはめるのではなく、「何が今危険か」「別の説明は何か」「介入後にどう変わったか」を繰り返します。

**新人看護師の到達点：** baselineとの差、変化時刻、ABCDE、測定の信頼性、直前の薬剤/処置、実施事項と反応を一つの短い報告へまとめること。

**ベテラン向け深掘り：** pretest probability、反証所見、混合病態、認知bias、iatrogenic/device causeを明示し、治療反応を証明と誤認せずdiagnostic timeoutで再構成します。

### 報告例

> 「○時からbaselineと比べて○○が悪化し、主な生理異常は○○です。最も危険な仮説は○○、反証所見は○○です。介入○○後も○○が残るため、再評価と代替原因の確認をお願いします。」

## From data to action

1. one-line problem representation：誰が、どのbaselineから、どの速度で、何が悪化したか。
2. syndrome/physiology：oxygenation、ventilation、perfusion、brain、metabolic/deviceのどこか。
3. differential：common、dangerous、reversible、iatrogenicを並列化。
4. discriminating data：仮説間で結果が変わる所見/検査を選ぶ。
5. action threshold：確定前に治療すべき脅威と、待てる検査を分ける。
6. reassessment：介入反応と新情報でproblem representationを更新する。

## Problem representation

年齢/背景を列挙するだけでなく、diagnostically meaningfulな特徴へ圧縮する。

```text
baseline + tempo + dominant physiology + severity
+ key positive/negative + treatment response
```

例：「自立していた免疫抑制中の成人が数時間で発熱・低酸素・vasopressor依存となり、fluid後もCRT延長が残る」。表現は新情報で書き換える。

## Parallel lanes under time pressure

| Lane | Question | Output |
|---|---|---|
| Rescue | 今すぐ死に至る可逆的脅威は？ | ABCDE介入、招集、再評価時刻 |
| Diagnose | どの仮説が所見を最も説明するか？ | ranked differential、反証所見 |
| Verify | signal/sample/deviceは正しいか？ | 独立した照合、再測定 |
| Prevent harm | 介入で何を悪化させ得るか？ | stop rule、dose/setting check |
| Communicate | 誰が何をいつ確認するか？ | owner、closed loop、contingency |

## Debiasing pause

- anchoring：最初の診断以外に説明できるか。
- premature closure：反証所見とworst-case alternativeは何か。
- search satisfaction：一つの異常で探索を止めていないか。
- attribution：年齢、精神疾患、非協力等のlabelで生理的異常を見逃していないか。
- automation bias：monitor/AI/device outputを患者所見と照合したか。

### Diagnostic timeout

状態が説明どおりに改善しない、診断とデータが一致しない、handoff/転棟前、新しい侵襲的介入の前に短く止まる。

1. working diagnosisを一文で言う。
2. それを支持する所見と反証する所見を一つずつ言う。
3. dangerous alternative、iatrogenic/device cause、複数病態を確認する。
4. pending resultと「誰がいつ見るか」を決める。
5. 仮説を変えるtriggerを記録する。

> [!NOTE]
> debiasing checklistの効果は状況により限定的で、使用自体が安全を保証しない。認知負荷、workflow、team、EHR、feedbackを含むsystemとして扱う。

## Bayesian discipline without false precision

検査前確率、検査特性、結果後確率を意識するが、曖昧な数字を捏造しない。陰性結果は感度・timing・sample quality・spectrumが適切な場合にだけ除外力を持つ。複数検査を独立と仮定して確信を過大化しない。

## Treatment response is data—but not proof

介入後改善は仮説を支持し得るが、自然経過、同時介入、非特異的効果がある。改善しない場合もdose/timing/measurement/irreversibilityを検討し、単純に診断を否定しない。

## Escalation language

`Concern → Evidence → Risk → Request → Reassessment time`で具体化する。例：「新規低血圧とCRT延長が進行しshockを懸念。今すぐbedside reviewと原因別評価、5分後再評価を依頼します」。

> [!CAUTION]
> checklistは認知を支えるが、病態を確定しない。時間圧下では治療と診断を並行し、結果待ちで救命介入を遅らせない。

## References

- AHRQ. [Diagnostic Safety Issue Briefs](https://www.ahrq.gov/diagnostic-safety/resources/issue-briefs.html).
- AHRQ. [Current State of Diagnostic Safety](https://www.ahrq.gov/diagnostic-safety/resources/issue-briefs/dxsafety-current-state3.html).
- AHRQ. [Evidence on Clinical Reasoning Checklists](https://www.ahrq.gov/diagnostic-safety/resources/issue-briefs/dxchecklists-3.html).

## Review log

- 2026-08-12: problem representation, parallel lanes, timeout, probability, and response interpretation expanded.
- 2026-08-11: reasoning and debiasing framework added.
