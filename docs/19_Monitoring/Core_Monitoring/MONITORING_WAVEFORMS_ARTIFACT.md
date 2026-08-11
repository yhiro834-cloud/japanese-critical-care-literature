---
title: "Monitoring, Waveforms, and Artifact"
status: review-needed
created: 2026-08-11
last_updated: 2026-08-11
evidence_reviewed: 2026-08-11
next_review: 2027-02-11
owners: []
reviewers: [Codex evidence review]
tags: [monitoring, waveform, artifact, alarm]
related: [../../03_Circulation/Hemodynamics/HEMODYNAMIC_MONITORING.md, ../../02_Breathing/ABG/ABG_INTERPRETATION.md]
ssot: true
---

# Monitoring, Waveforms, and Artifact

## A monitor measures a signal, not the patient

```text
unexpected value/alarm → look at patient/pulse/perfusion
→ signal source/sensor/catheter → cable/transducer/device/settings
→ compare independent modality → intervene → confirm response
```

## ECG

electrode contact/placement、lead selection、motion/electrical artifactを確認し、monitor rhythmをpulse/arterial waveformと照合する。ischemia/diagnosisにはappropriate 12-leadとserial changeを用い、single-lead telemetryだけで断定しない。QT interpretationはrate/QRS/lead/drug/electrolyteを考慮する。

## SpO₂ and ETCO₂

SpO₂はpleth quality、perfusion、motion、pigmentation、dyshemoglobin、probe siteを確認し、疑わしければABG/co-oximetry等で照合する。ETCO₂はairway/ventilation、perfusion/cardiac output、dead space、sampling/circuit leakの影響を受け、PaCO₂とのgapは固定でない。

## Invasive pressure

A-line/CVP等はtransducerをappropriate referenceへlevel/zeroし、bag pressure、tubing/air/clot、flush、dynamic response、waveform dampingを確認する。数値だけを補正せず、over/underdampingとpatient perfusionを評価する。

> [!CAUTION]
> CVP、ScvO₂、lactate、CO、ICP、urine outputの単一値はdiagnosisでもtargetでもない。measurement validity、baseline、trajectory、intervention responseを統合する。

## Alarm design and handover

alarm limits/delayはpatient-specificに設定するが、危険alarmを無効化しない。baseline waveform screenshot/値、sensor/site、zero/reference、known limitation、次回校正/検査をhandoverする。alarm burdenはfalse alarmだけでなくmissed deteriorationもquality reviewする。

## References

1. AARC Clinical Practice Guideline: Blood Gas Analysis and Hemoximetry. Respir Care. 2013. DOI: `10.4187/respcare.02786`.
2. FDA. Pulse Oximeter Accuracy and Limitations. https://www.fda.gov/medical-devices/safety-communications/pulse-oximeter-accuracy-and-limitations-fda-safety-communication
3. AACN. Practice Alert: Pulmonary Artery/Central Venous Pressure Monitoring in Adults. https://www.aacn.org/clinical-resources/practice-alerts

## Review log

- 2026-08-11: Primary/professional sources reviewed; biomedical/local monitoring validation required.
