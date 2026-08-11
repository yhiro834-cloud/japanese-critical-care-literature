---
title: "Mechanical Ventilation"
status: review-needed
created: 2026-08-11
last_updated: 2026-08-11
evidence_reviewed: 2026-08-11
next_review: 2027-02-11
owners: []
reviewers: [Codex evidence review]
tags: [mechanical-ventilation, waveform, peep, asynchrony]
related: [../ARDS/ARDS.md, ../Weaning/VENTILATOR_LIBERATION.md]
ssot: true
---

# Mechanical Ventilation

> [!CAUTION]
> 設定は診断、肺mechanics、循環、患者努力、施設protocolで個別化します。本頁は固定設定の処方箋ではありません。急変時は患者を先に評価し、必要ならventilatorから離してmanual ventilationし支援を要請します。

## 1. Overview

人工呼吸器はoxygenationとventilationを支え、呼吸仕事量を軽減する一方、VILI、循環抑制、横隔膜障害、鎮静関連害を生じ得ます。目標はgasを正常化することではなく、許容できるgas exchangeを最小限の害で確保し原因回復を待つことです。

## 2. Core Physiology

- **Equation of motion:** `Pvent + Pmus = (V/Crs) + (Flow × R) + PEEPtotal`
- **Pplat:** inspiratory hold中のno-flow pressure。条件が成立しているか確認
- **Driving pressure:** `Pplat − total PEEP`。静的complianceとの関係を示すが単独目標にしない
- **Compliance:** `VT / (Pplat − total PEEP)`
- **Resistance pressure:** peak–plateau差はconstant flow時の抵抗成分の手掛かり
- **Time constant:** `R × C`。呼気時間不足と高抵抗でair trapping/auto-PEEPが起きる

患者努力が強い場合、airway pressureだけではtranspulmonary stressを過小評価し得ます。

## 3. Modes and Controls

Volume-targetedとpressure-targetedは「何を保証し、何が変動するか」が異なります。mode名は機種依存なので、trigger、target/control、cycle、backup、alarmを実機で確認します。FiO₂/PEEPはoxygenation、minute ventilationは主にPaCO₂、flow/rise/cycleはcomfortとsynchronyへ影響します。

## 4. Bedside Assessment

1. 患者：胸郭、呼吸努力、意識、SpO₂、循環、ETCO₂
2. airway：tube depth、cuff、patency、secretions
3. circuit/device：接続、water、filter、valve、電源/gas
4. settings：mode、FiO₂、PEEP、VT/pressure、RR、flow、alarms
5. measured：exhaled VT/minute ventilation、Ppeak/Pplat/total PEEP、waveforms
6. cause and trend：病態、画像、gas、介入反応

## 5. Waveform Reasoning

- pressure rise/flow starvation、double triggering、ineffective effort、auto-trigger、premature/delayed cyclingを「患者要求と機械送気の不一致」として読む
- expiratory flowが次の吸気前にzeroへ戻らない所見はair trappingを示唆するが、測定条件とpatient effortを確認
- 高圧alarmは「tube obstruction/secretions/bronchospasm等のresistance」と「肺/胸壁compliance低下」をPpeak、Pplat、examで分ける
- 低圧/低volume alarmはdisconnection、leak、cuff、回路を考える

## 6. Clinical Reasoning and Treatment

```text
alarm/悪化 → 患者は換気・酸素化されているか → 不安定ならmanual ventilation
→ airway → circuit → ventilator → 病態の順に探索
→ mechanicsとwaveformから仮説 → 原因介入 → 全身状態と波形を再評価
```

肺保護はARDSだけでなくrisk患者でも意識し、PBWに基づくVT、過度なinspiratory pressure回避、適切なPEEP、過剰な自発努力とasynchronyの是正を統合します。鎮静・筋弛緩は原因探索を置き換えません。

## 7. Nursing Points

- shift/移送/処置前後にtube位置、固定、cuff、設定、measured values、alarm、backupを確認
- alarm limitsを無効化せず患者に合わせる。alarm silence後に原因を残さない
- suctionは適応、preoxygenation、循環/SpO₂反応、分泌性状を評価し、routineな過剰介入を避ける
- oral care、head positioning、mobilization、communication、sleep、delirium preventionをbundle化
- ventilator変更後は血圧も確認。PEEP/mean airway pressure上昇はvenous return/RVへ影響し得る

## 8. Red Flags / Pitfalls

- manual ventilation困難、片側呼吸音、急な低血圧：tube obstruction/displacement、tension pneumothorax等
- Pplatをpatient effort/leak下で誤読、PBWでなく実体重を使用、auto-PEEPを外因性PEEPだけで解決
- waveform異常を鎮静不足だけと決めつける、正常ABGを得るため有害なpressure/volumeを許容

## 9. Take Home Messages

1. 患者、airway、circuit、ventilator、病態を順序立てて評価する。
2. 数値は測定条件とwaveformを確認して解釈する。
3. gas正常化ではなくlung/diaphragm protectionと回復を目指す。

## 10. Related Learning

- [ARDS](../ARDS/ARDS.md)
- [Ventilator Liberation](../Weaning/VENTILATOR_LIBERATION.md)
- [Respiratory Support Case](../../23_Clinical_Cases/CASE_RESPIRATORY_SUPPORT_ESCALATION.md)

## 11. References

- Fan E, et al. ATS/ESICM/SCCM guideline: Mechanical Ventilation in Adult ARDS. Am J Respir Crit Care Med. 2017. DOI: 10.1164/rccm.201703-0548ST; PMID: 28459336.
- Acute Respiratory Distress Syndrome Network. Lower tidal volumes versus traditional tidal volumes. N Engl J Med. 2000. DOI: 10.1056/NEJM200005043421801; PMID: 10793162.

## Review Log

| Date | Reviewer | Scope | Result |
|---|---|---|---|
| 2026-08-11 | Codex | physiology / guideline / nursing | Evidence reviewed; ventilator specialist review needed |
