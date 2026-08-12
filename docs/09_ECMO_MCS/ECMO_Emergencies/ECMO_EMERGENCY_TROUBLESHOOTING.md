---
title: "ECMO Emergency Troubleshooting"
status: review-needed
created: 2026-08-11
last_updated: 2026-08-12
evidence_reviewed: 2026-08-12
next_review: 2027-02-11
owners: []
reviewers: [Codex evidence review]
tags: [ecmo, emergency, low-flow, air, decannulation]
related: [../ECMO_Foundations/ECMO_FOUNDATIONS_DAILY_MANAGEMENT.md]
ssot: true
---

# ECMO Emergency Troubleshooting

## 0. まず覚える

ECMO緊急時は、alarm名だけで反射的に装置を操作しない。**患者を見て応援を呼び、ABCDEを支えながら、患者側・cannula側・回路側・機械/供給側の順に原因を切り分ける。**

**簡単に言うと：** 「患者を守る」「ECMO emergencyを宣言する」「無訓練の操作をしない」が最初の3点である。

| 用語 | 意味 | 実践上のポイント |
|---|---|---|
| low flow | 回路血流が目標または患者の基準より低い状態 | 出血、preload、胸腔内圧、cannula、回路、pumpを分けて確認 |
| chattering | 脱血側回路が周期的につぶれ振動する現象 | 過度な脱血の徴候。fluidだけでなく原因を検索する |
| oxygenator failure | 人工肺のgas交換または血液通過性能の低下 | pre/post gas、圧較差、clot、hemolysisと患者状態を統合 |
| decannulation | cannulaが抜け、重大出血や回路破綻を起こす状態 | 圧迫、蘇生、緊急応援を同時に行い、盲目的に戻さない |
| differential oxygenation | peripheral VA-ECMOで上半身と下半身の酸素化が異なる状態 | 右上肢SpO₂/ABGと脳・心臓への酸素供給を確認する |

**新人看護師の到達点：** 患者の意識・pulse・呼吸・出血を最初に確認し、ECMO emergencyを宣言する。cannula固定、回路のair/clot/kink、flow/RPM/pressure、gas・電源を見て、発生前の基準値と変化を伝えられる。clamp、cannula、RPM、回路開放は訓練と施設手順なしに行わない。

> **報告例：** 「VA-ECMOで突然low-flow alarm、血圧低下、脱血回路のchatteringがあります。大量出血は外見上なく、cannulaを保持して患者蘇生を開始しています。ECMO emergency teamと原因別algorithmをお願いします。」

**ベテラン向け深掘り：** 同じlow flowでもhypovolemia、tamponade、tension pneumothorax、腹圧上昇、cannula migration、回路閉塞では対応が異なる。pump stop、air、rupture、decannulationでは回路configurationによる逆流・air embolism riskを踏まえ、patient supportとtrained teamのisolation手順を同時進行する。

## Universal response

```text
Patient first → call ECMO emergency / help → ABCDE
→ patient side / cannula side / circuit side / machine & utilities
→ safe temporary support → definitive correction → reassess and debrief
```

> [!DANGER]
> 施設のECMO emergency cardとtrained specialist指示を優先する。無訓練でclamp、cannula操作、RPM変更、回路開放を行わない。

## Low flow / chattering

- patient: hypovolemia/bleeding、tamponade、tension pneumothorax、high intrathoracic/abdominal pressure、position
- drainage: cannula migration/kink/obstruction、suction events
- return/circuit: kink、thrombus、increased resistance、pump issue

一律fluid bolusで済ませず、原因を確認し、必要なら施設protocolで一時的RPM調整と患者蘇生を行う。recurrent chatterはcannula injury/hemolysisを生む。

## Hypoxemia / hypercapnia

gas source、blender、sweep connection、oxygenator pre/post gas、flow、recirculation、cannula、native lung/CO、Hb/temperatureを確認する。VAではright-arm oxygenationとdifferential oxygenationを評価する。

## Pump stop / power failure

即時応援、患者support、電源/connection/controller確認、施設手順のbackup power/hand crankへ。回路内逆流riskはconfigurationで異なるため、trained teamのclamp/flow restoration algorithmに従う。

## Air / circuit rupture / decannulation

air or blood lossを認識したらECMO emergencyを宣言し、出血部位圧迫、患者蘇生、施設protocolに基づく適切なclamping/isolationをtrained teamが行う。cannulaを盲目的に再挿入しない。massive hemorrhage、air embolism、CPR/OR pathwayを同時activateする。

## Oxygenator failure / clot / hemolysis

gas transfer悪化、pressure gradient、visible clot、plasma-free Hb/LDH、暗色尿、急な回路変化を統合し、elective/emergency circuit exchangeを準備する。交換中のpatient supportと役割をbriefする。

## Bedside prevention

毎shift、cannula depth/securement、回路全長、clot/air、flow/RPM/pressures、gas/power/battery、emergency supplies、distal perfusion、bleeding、handoverを二者確認する。値だけでなく基準からの変化を記録する。

## References

1. ELSO Guidelines for Adult and Pediatric ECMO Circuits. 2022. https://www.elso.org/ecmo-resources/elso-ecmo-guidelines.aspx
2. ELSO Guideline for Transport and Retrieval of Adult and Pediatric Patients with ECMO Support. 2022. https://www.elso.org/ecmo-resources/elso-ecmo-guidelines.aspx

## Review log

- 2026-08-12: V2導入、low flow/chattering等の用語、新人の初動・報告、原因別切り分けを追加。ELSO circuits/transport guidanceを再確認。
- 2026-08-11: ELSO review; local equipment-specific emergency validation required.
