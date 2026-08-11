---
title: "Device Lifecycle and Backup Safety"
status: review-needed
created: 2026-08-11
last_updated: 2026-08-12
evidence_reviewed: 2026-08-12
next_review: 2027-02-11
owners: []
reviewers: [Codex evidence review]
tags: [device, backup, line-safety, human-factors]
related: [../../18_Procedures/Safety_Framework/PROCEDURAL_SAFETY_FRAMEWORK.md, ../../17_Infection_Control/Device_Infection_Prevention/DEVICE_INFECTION_PREVENTION.md]
ssot: true
---

# Device Lifecycle and Backup Safety

## Lifecycle

適応/goal → correct device/configuration → insertion/connection confirmation → secure/label → function/infection/skin daily checks → emergency backup → prompt removal。各deviceにowner、settings、dependencies、alarm response、removal/exit criteriaを持たせる。

## Dependency map

各deviceについて「停止すると何分で危険か」「何に依存するか」「manual代替は何か」を明示する。

| Device function | Dependencies | Backup question |
|---|---|---|
| Airway/ventilation | tube/trach、circuit、gas、power、humidification | bag-mask/manual ventilation、spare airway、trained help |
| Infusion | drug/product、line/lumen、pump、power、carrier | spare syringe/pump、manual emergency plan |
| Drainage | patient position、catheter、tubing、collection/suction | safe temporary management、specialist contact |
| KRT/ECMO/MCS | access/cannula、circuit、power/gas、anticoagulation、team | emergency card、manual/device-specific backup |

## Line and connector map

airway、vascular、enteral、neuraxial、drainを両端までtraceし、route-compatible connector、lumen purpose、concentration、direction of flowを表示する。接続変更、transport、handoff後にretraceする。unknown lineへ注入しない。

line mapはpatient側のinsertion site、external length/depth、connector、lumen purpose、downstream device、infusate/outputを対応させる。bedsideに余剰connector/注射器を放置せず、neuraxial/enteral/IV routeを物理的・運用的に分離する。

## Daily device round

- indicationはまだあるか、より低侵襲へ移行可能か
- insertion/depth/securement/dressing/skin/limb perfusion
- connections、kinks、clamps、filters、battery/gas/power、consumables
- expected value/outputとpatient response
- contamination/break、alarm/event、maintenance due
- manual alternative、spare device、trained responder、emergency contact

## Device change control

setting、software/profile、circuit component、filter、concentration、connection、patient positionを変える前にexpected effectとhazardをbriefし、変更後にpatient response、setting、connection、alarmを確認する。複数変更を同時に行う場合は時刻を記録する。

## Failure response

```text
recognize patient dependence → independent support
→ patient/interface → connection/circuit → device/settings
→ utilities/consumables → replace/escalate
→ preserve logs/device → report/debrief
```

故障機器は問題を具体的にtagし、再使用を防いでclinical engineering/manufacturer/local reportingへ渡す。patient careを確保した後、event log、settings、consumables、写真等を施設policyに従い保全する。

> [!DANGER]
> alarmを消すことは原因修正ではない。device failure時は患者supportを独立した方法で確保してから、patient side / connection / circuit / machine / utilitiesを確認する。

## Transport and downtime

必要薬/oxygen/battery残量をplanned duration以上で確認し、spare、route、elevator、receiving hookup、return/abort planをbriefする。EHR/network/power downtimeでもdevice settingsとoutputをpaper/independent recordへ保持する。

## References

1. FDA. Medical Device Safety and recalls resources. https://www.fda.gov/medical-devices/medical-device-safety
2. WHO. Medical equipment maintenance programme overview. https://www.who.int/publications/i/item/9789241501538

## Review log

- 2026-08-12: dependency map, line map, change control, failure/log preservation expanded.
- 2026-08-11: Device safety framework review; biomedical engineering/manufacturer/local inventory review required.
