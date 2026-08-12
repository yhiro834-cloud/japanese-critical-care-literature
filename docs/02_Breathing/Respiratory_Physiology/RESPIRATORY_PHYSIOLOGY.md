---
title: "呼吸生理"
status: reviewed
created: 2026-08-11
last_updated: 2026-08-12
evidence_reviewed: 2026-08-12
next_review: 2027-02-11
evidence_status: claim-mapped-with-open-items
human_review_required: true
owners: []
reviewers: [Codex source mapping; respiratory specialist pending]
tags: [breathing, physiology, oxygenation, ventilation, vq]
related: [../ABG/ABG_INTERPRETATION.md]
ssot: true
---

# 呼吸生理

> [!CAUTION]
> 教育目的の成人向け資料です。酸素投与、換気補助、人工呼吸器設定は患者の病態と施設protocolに基づき担当チームが判断してください。

## 0. Executive Summary — Quick Review

**[FACT] [CLM-RESP-001]** 呼吸によるガス交換は、空気を肺胞へ運ぶ**換気（ventilation）**、肺胞と血液の間で気体が移動する**拡散（diffusion）**、肺へ血液を運ぶ**灌流（perfusion）**を分けて考えると整理できます。[SRC-RESP-001]

**簡単に言うと：** SpO₂低下やPaCO₂上昇を見たら、「空気が届かない」「酸素が血液へ移れない」「血流との組み合わせが悪い」に分けます。

| 用語 | 意味 | 混同しやすい点 |
|---|---|---|
| 酸素化（oxygenation） | 血液へ酸素を取り込むこと | 換気と同義ではない |
| 換気（ventilation） | 肺胞へ気体を出入りさせCO₂を排出すること | SpO₂が正常でも換気不全はあり得る |
| 換気血流比（ventilation/perfusion ratio: V/Q） | 換気と灌流の相対関係 | 肺全体の平均だけでは局所不均一は分からない |
| シャント（shunt） | 換気されない肺胞へ血流がある状態 | 酸素投与への反応が乏しいことがある |
| 死腔（dead space） | 換気されても有効な灌流が乏しい状態 | 分時換気量があってもCO₂排出効率が悪い |

**新人看護師の到達点：** SpO₂、呼吸数、呼吸努力、意識、ETCO₂、酸素投与器具、吸入酸素濃度（FiO₂）、循環を同じ時刻で確認し、酸素化と換気を分けて報告すること。

**ベテラン向け深掘り：** 動脈血酸素含量（CaO₂）、酸素供給量（DO₂）、V/Q不均一、シャント、死腔、ヘモグロビン（Hb）、心拍出量（CO）、微小循環を統合し、SpO₂だけで組織酸素供給を判断しません。

## 1. 全体像 — Core

呼吸の役割は「SpO₂を上げる」ことではなく、肺胞換気、肺胞―血液間のガス交換、血液による運搬、組織への酸素供給、CO₂排泄を維持することです。

## 2. なぜ重要か

SpO₂低下、PaCO₂上昇、呼吸仕事量増加は異なる機序から起こります。酸素化障害にも換気障害にも酸素投与だけで対応すると、原因の進行や呼吸筋疲弊を見逃します。

## 3. Physiology

### 換気

- 分時換気量: `V̇E = 一回換気量 × 呼吸数`
- 肺胞換気量: `V̇A = (一回換気量 − 死腔量) × 呼吸数`
- CO₂産生が一定ならPaCO₂はalveolar ventilationに反比例する

**[FACT] [CLM-RESP-002]** 同じ分時換気量でも、浅く速い呼吸では一回換気量に占める死腔の割合が大きくなり、肺胞換気量が不足し得ます。[SRC-RESP-001]

### 酸素含量と酸素供給

`CaO₂ ≈ 1.34 × Hb × SaO₂ + 0.003 × PaO₂`

`DO₂ = cardiac output × CaO₂`

**[FACT] [CLM-RESP-003]** PaO₂が高くてもHbまたは心拍出量が低ければ酸素供給量は不足し得ます。SpO₂は組織への酸素供給量を直接測っていません。[SRC-RESP-001]

### 肺胞気式

`PAO₂ = FiO₂ × (PB − PH₂O) − PaCO₂ / R`

海面気圧、37℃、呼吸商（R）約0.8という仮定では、`PAO₂ ≈ FiO₂ × 713 − PaCO₂/0.8`。高度、FiO₂推定誤差、Rの変化でずれます。これは計算モデルであり、患者ごとの実測肺胞酸素分圧ではありません。

### 換気と灌流の釣り合い

- `V/Q = 0`: シャント（灌流はあるが換気なし）
- low V/Q: 換気不足の肺胞へ灌流
- high V/Q: 換気されるが灌流不足
- 死腔: 灌流が極端に少ない換気

重力、肺気量、気道閉鎖、血管障害などにより、肺内のV/Qは均一ではありません。

## Visual Series: Gas Exchange and V/Q

![肺胞ガス交換：換気・拡散・灌流](../../../assets/physiology/alveolar_gas_exchange.svg)

**Figure FIG-P-RESP-001 — 肺胞ガス交換。** 換気、肺胞膜を介する拡散、肺毛細血管の灌流を別々の過程として示す。見るべき点は、肺胞へ空気が届くだけでも、血流があるだけでも、効率的なガス交換は成立しないこと。

### Figure Interpretation

O₂は肺胞から血液へ、CO₂は血液から肺胞へ移動する。肺動脈側と肺静脈側のlabelは肺循環内の位置を表し、一般体循環の動静脈とは酸素化の関係が逆になる。

### Clinical Meaning

低酸素血症または高CO₂血症を見たら、換気、拡散、灌流のどこが障害されているかを分ける。図の矢印は方向を示す模式図で、ガス移動量を定量化していない。

![V/Qの連続体](../../../assets/physiology/vq_shunt_dead_space.svg)

**Figure FIG-P-RESP-002 — V/Q、shunt、dead space。** 換気と灌流の相対関係を5つの状態で比較する。矢印の太さは相対量の概念であり、実測値ではない。

### Figure Interpretation

shuntでは換気がなく灌流が残り、dead spaceでは換気があって灌流がほぼない。low/high V/Qはその中間にあり、実際の肺では異なるV/Q領域が同時に存在する。

### Clinical Meaning

「低酸素＝酸素不足」と一括せず、airway closure、肺胞充満、肺血管障害、過膨張などの機序へ戻る。酸素への反応だけで病態を断定せず、呼吸仕事量、PaCO₂、循環、画像を統合する。

## 4. 病態生理

### 低酸素血症の主な機序

| 機序 | 肺胞気―動脈血酸素分圧較差（A–a較差） | 酸素投与への反応の概念 | 例 |
|---|---|---|---|
| 低FiO₂ | 正常域 | 反応 | 高地、供給error |
| alveolar hypoventilation | 正常域 | 反応 | CNS抑制、neuromuscular failure |
| V/Q mismatch | 拡大 | 多くは反応 | pneumonia、COPD、asthma |
| shunt | 拡大 | 反応不良になり得る | atelectasis、alveolar flooding |
| diffusion limitation | 拡大 | 多くは反応 | interstitial disease等 |

### 高二酸化炭素血症の主な機序

- V̇A低下：drive低下、muscle fatigue、胸郭/神経筋障害
- dead space増加：PE、肺血管床減少、過膨張
- CO₂産生増加に換気が追いつかない：発熱、seizure、overfeeding等
- ventilator/circuit問題：設定、leak、rebreathing、obstruction

## 5. Causes / Etiology

Hypoxemiaとhypercapniaを別々に整理し、気道、肺実質、胸膜、肺血管、胸郭、神経筋、中枢、機器へ分けます。複数mechanismは併存します。

## 6. Assessment

### 患者を最初に見る

- 発声、意識、体位、呼吸数・pattern・深さ
- accessory muscle、paradoxical breathing、silent chest
- 胸郭左右差、呼吸音、分泌物
- SpO₂値だけでなくpleth waveformとpulse一致
- oxygen device、FiO₂、接続、流量

## 7. モニタリングと測定限界

- SpO₂ trendとsignal quality
- respiratory rate、work of breathing、意識
- ETCO₂ waveform/trend（PaCO₂と同一ではない）
- ABG/VBGを目的に応じ選択
- Hb、CO/perfusion、temperature
- ventilator pressure/flow/volume waveforms

**[FACT] [CLM-RESP-004]** 米国食品医薬品局（FDA）は、パルスオキシメータが末梢循環不良、皮膚色素、皮膚の厚さ・温度、喫煙、マニキュアなどの影響を受け得ると注意しています。[SRC-RESP-002] 臨床所見と一致しなければ測定部位と波形品質を確認し、必要に応じて動脈血液ガスやCOオキシメトリなど別手段で確かめます。

## 8. Interpretation

### SpO₂, SaO₂, PaO₂

- SpO₂: pulse oximeterによる推定
- SaO₂: arterial saturation。co-oximetry実測かblood gas計算値か確認
- PaO₂: plasmaに溶けたoxygen tension

Oxyhemoglobin dissociation curveはpH、temperature、PaCO₂、2,3-DPG等でshiftします。同じPaO₂でもSaO₂は一定ではありません。

![酸素ヘモグロビン解離曲線](../../../assets/physiology/oxyhemoglobin_curve.svg)

**Figure FIG-P-RESP-003 — 酸素ヘモグロビン解離曲線。** PaO₂とHb酸素飽和度のS字関係、急峻部・平坦部、右方/左方移動を定性的に示す。患者固有の目標値を示す図ではない。

### Figure Interpretation

急峻部ではPaO₂の変化に伴い飽和度が大きく変わりやすく、平坦部では飽和度変化が小さい。pH、PaCO₂、体温などで曲線の位置が変わるため、同じPaO₂でも飽和度は一定ではない。

### Clinical Meaning

SpO₂が保たれていてもHb低下や心拍出量低下があれば酸素運搬は不足し得る。SpO₂、SaO₂、PaO₂、CaO₂、DO₂を同義語として扱わない。

### P/F ratio

`PaO₂ / FiO₂`はoxygenation impairmentの簡便指標ですが、PEEP、FiO₂、hemodynamics、sampling時点の影響を受けます。原因診断そのものではありません。

### A–a gradient

`A–a = PAO₂ − PaO₂`。hypoventilation/低FiO₂と肺内gas-exchange障害を考える補助ですが、年齢・FiO₂・気圧・計算仮定の影響があります。

### ETCO₂–PaCO₂ gap

ETCO₂は通常PaCO₂より低いことが多いものの、gapはdead space、CO、V/Q、samplingで変化します。固定換算しません。

## 9. Diagnosis

Gas valueだけで診断せず、患者、time course、device、imaging、hemodynamicsを統合します。ABGはoxygenation、ventilation、acid–baseのsnapshotです。

## 10. Clinical Reasoning

```text
SpO₂低下 / 呼吸状態悪化
→ 患者を見る・応援要請
→ Airwayは開通しているか
→ oxygen device / sensor / circuitは正しいか
→ ventilation failureか、oxygenation failureか、両方か
→ 胸郭・呼吸音・分泌物・waveform・ETCO₂
→ ABGと画像/POCUSを目的に応じ追加
→ low FiO₂ / hypoventilation / VQ / shunt / diffusion / dead space
→ 原因への介入
→ work of breathing・意識・gas・害を再評価
```

## 11. 初期対応とチーム連携

Mechanismと原因に対応します。酸素化だけでなくairway patency、alveolar ventilation、recruitmentの可否、肺循環、Hb、COを評価します。oxygen targetやdevice選択の詳細は今後のSSOTへ分離します。

## 12. 看護実践

- SpO₂ alarm時は患者→sensor→oxygen/device→呼吸評価
- oxygen変更前後のdevice、flow/FiO₂、SpO₂、RR、意識を記録
- cyanosisがないことやSpO₂が正常なことだけで換気不全を否定しない
- opioid/sedative後はRRだけでなく深さ、意識、ETCO₂を確認
- 採血時のFiO₂/PEEP/体位を記録し、比較可能にする

## 13. ICU Nursing Pearls

- 正常SpO₂でもhypercapniaは起こる
- 貧血ではSpO₂正常でもCaO₂が低い
- shock/低灌流ではpulse oximeter signal自体が不安定になり得る
- 数値と患者が合わないときは患者を信じ、測定系を疑い、別手段で確認する

## 14. Red Flags

- 意識低下、発声不能、silent chest
- exhaustion、paradoxical breathing、呼吸数低下への転換
- 酸素増量でも進行する低酸素
- ETCO₂ waveform消失/急変
- 片側呼吸音消失、急な気道内圧上昇
- severe acidemiaまたは急速なPaCO₂上昇

## 15. Troubleshooting

**Patient → Airway → oxygen source/device → Breathing → circuit/ventilator → measurement → ABG → cause → reassessment**。

## 16. Common Pitfalls

- SpO₂をoxygen deliveryと同一視
- oxygenationとventilationを混同
- ETCO₂からPaCO₂を固定換算
- P/F ratioだけで病名を決める
- normal SpO₂で呼吸疲弊を否定

## 17. Clinical Case

- [SpO₂突然低下とPaCO₂上昇](../../23_Clinical_Cases/CASE_DESATURATION_HYPERCAPNIA.md)

## 18. Clinical Questions

- [Respiratory Physiology / ABG Questions](../../24_Clinical_Questions/RESPIRATORY_PHYSIOLOGY_ABG_QUESTIONS.md)

## 19. Quiz

- [Respiratory Physiology / ABG Quiz](../../25_Quiz/QUIZ_RESPIRATORY_PHYSIOLOGY_ABG.md)

## 20. Take Home Messages

1. Oxygenation、ventilation、oxygen deliveryを分ける。
2. PaCO₂は主にalveolar ventilationを反映する。
3. Hypoxemia mechanismはA–a gradientと臨床像で整理する。
4. SpO₂にはmeasurement limitationがある。
5. 数値ではなく患者から始め、介入後に同じ指標で再評価する。

## 21. Slide Ready Summary

[20分教材](../../27_Slide_Ready/RESPIRATORY_PHYSIOLOGY_ABG_20MIN.md)

## 22. Claim-level References

| Source ID | Title | Authors / Group | Organization / Journal | Year / Version | Status | Evidence type | DOI / PMID / Official URL | Population | Context | Exact claim supported | Recommendation strength | Exceptions / limits | Verified on |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SRC-RESP-001 | ATS/ACCP Statement on Cardiopulmonary Exercise Testing | ATS / ACCP writing group | American Thoracic Society / American College of Chest Physicians | 2003; official ATS-hosted statement | current for cited physiology concepts; newer topic-specific standards may apply | Professional statement | https://www.thoracic.org/statements/resources/pfet/cardioexercise.pdf | 主に成人 | 呼吸生理・運動生理 | CLM-RESP-001〜003: 換気、V/Q、死腔、酸素運搬の基礎概念 | Formal recommendation grade not used for these facts | ICU患者の治療目標を定める文書ではない。式の定数は条件依存 | 2026-08-12 |
| SRC-RESP-002 | Pulse Oximeters | U.S. Food and Drug Administration | FDA | 2025 draft-guidance information and prior safety communications summarized on current page | current official safety information; 2025 device guidance remains draft until finalized | Regulatory safety information | https://www.fda.gov/medical-devices/products-and-medical-procedures/pulse-oximeters | 成人・小児を含む機器利用者 | パルスオキシメータの性能と限界 | CLM-RESP-004: 測定値へ影響する因子と単独依存の危険 | Not a graded clinical recommendation | 装置ごとの性能差があり、家庭用一般ウェルネス製品は医療判断用と同一でない | 2026-08-12 |
| SRC-RESP-003 | AARC Clinical Practice Guideline: Patient-Ventilator Assessment | Goodfellow LT, et al. | Respiratory Care / AARC | 2024 | current final | GRADE clinical practice guideline | DOI: https://doi.org/10.4187/respcare.12007; PMID: https://pubmed.ncbi.nlm.nih.gov/39048148/; official PDF: https://www.aarc.org/wp-content/uploads/2024/10/patient-ventilator-assessment-aarc-cpg.pdf | 非侵襲的・侵襲的人工呼吸患者 | 患者―人工呼吸器評価 | ベッドサイド評価、酸素化・換気・血行動態・気道・設定・波形・加温加湿・記録を統合する枠組み | 項目によりstrong / conditional。人工呼吸章で個別対応 | 呼吸生理全般や酸素目標を規定する資料ではない | 2026-08-12 |

追加の採血・酸塩基平衡の根拠は[動脈血液ガスの章](../ABG/ABG_INTERPRETATION.md#22-references)で管理します。

## Review Log

| Date | Reviewer | Scope | Result |
|---|---|---|---|
| 2026-08-12 | Codex | claim mapping / terminology / source status / visual-text consistency | Major revision; respiratory specialist review still needed |
| 2026-08-12 | Codex | visual physiology / labels / directional accuracy | Three original SVGs added; respiratory expert review still needed |
| 2026-08-11 | Codex | evidence identity / nursing safety | Source identity checked; claim-level review was incomplete |
