---
title: "Case: Conflicting Signals and Diagnostic Timeout"
status: review-needed
created: 2026-08-12
last_updated: 2026-08-12
evidence_reviewed: 2026-08-12
next_review: 2027-02-12
owners: []
reviewers: [Codex evidence review]
tags: [case, fundamentals, clinical-reasoning, human-factors]
related: [../00_Fundamentals/Clinical_Reasoning/CLINICAL_REASONING.md, ../00_Fundamentals/ICU_Assessment/ICU_SYSTEMATIC_ASSESSMENT.md]
ssot: false
---

# Case: Conflicting Signals and Diagnostic Timeout

## Presentation

肺炎で人工呼吸中の患者。体位変換後にSpO₂ 82%、A-line MAP 48 mmHg、頻脈alarmが同時に出た。患者は発汗し、plethとA-line波形は不良。担当者は「体動artifact」と考えたが、vasopressor syringeは残量がありpumpも作動表示だった。

## Pause 1 — Rescue and verify in parallel

- A/B/Cを直接評価し、pulse、skin、意識、airway/circuit、胸郭運動を確認する。
- 別担当者がsensor/electrode、A-line transducer、infusion lineを患者からpumpまでtraceする。
- monitorを直す間もoxygenation、ventilation、perfusionの救命介入を遅らせない。

## New information

vasopressor lineは三方活栓部で閉塞し、SpO₂ probeは外れかけていた。低血圧は真、SpO₂値はartifactを含んでいた。

## Pause 2 — Diagnostic timeout

1. working diagnosis：vasopressor delivery interruptionによる真の低灌流。
2. supporting/refuting data：poor pulse/CRTは支持、SpO₂単独値は信頼性が低い。
3. alternatives：tension pneumothorax、airway/circuit problem、arrhythmia、bleeding、sepsis progression。
4. response：line復旧後のMAPだけでなくpulse/CRT、dose、再閉塞、organ perfusionを確認。

## Team debrief

「artifactか真の急変か」の二者択一が誤りだった。複数signalに異なる真偽があり得る。patient-first assessment、independent modality、line trace、closed-loop assignmentがpremature closureを防ぐ。

## References

- [Clinical Reasoning](../00_Fundamentals/Clinical_Reasoning/CLINICAL_REASONING.md)
- [Human Factors and Communication](../00_Fundamentals/Human_Factors/HUMAN_FACTORS_COMMUNICATION.md)
- [Monitoring and Artifact](../19_Monitoring/Core_Monitoring/MONITORING_WAVEFORMS_ARTIFACT.md)
