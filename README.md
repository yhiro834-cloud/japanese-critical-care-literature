# Critical Care Knowledge Base

高度救命救急センター・ICUで必要な知識を、**基礎生理 → 病態生理 → 評価 → モニタリング → 臨床推論 → 治療 → 看護 → 症例学習 → 教育**の流れで育てるKnowledge Portalです。

> [!CAUTION]
> 本リポジトリは医療従事者の教育・学習を目的とし、個別患者への診療指示を目的としません。実際の診療では、患者個別の病態、最新の公式ガイドライン、医師を含む医療チームの判断、各施設のプロトコルを優先してください。薬剤投与量、人工呼吸器設定、ECMO、CRRTなどの高リスク介入は、適応・禁忌・監視・施設体制を含めて個別に判断してください。

## Knowledge Portal

| 探し方 | 入口 |
|---|---|
| ABCDEから探す | [ABCDE Map](docs/00_Fundamentals/ABCDE/README.md) |
| 臓器・病態から探す | [Topic Map](docs/TOPIC_MAP.md) |
| 気道・呼吸 | [Airway](docs/01_Airway/README.md) / [Breathing](docs/02_Breathing/README.md) |
| 循環・ショック | [Circulation](docs/03_Circulation/README.md) |
| 神経・腎・感染 | [Neurology](docs/04_Neurology/README.md) / [Renal](docs/05_Renal/README.md) / [Infection & Sepsis](docs/06_Infection_Sepsis/README.md) |
| デバイス・モニター | [Devices](docs/20_Devices/README.md) / [Monitoring](docs/19_Monitoring/README.md) |
| 薬剤から探す | [Pharmacology](docs/13_Pharmacology/README.md) |
| 看護から探す | [Nursing](docs/22_Nursing/README.md) |
| 症例から探す | [Clinical Cases](docs/23_Clinical_Cases/README.md) |
| Clinical Question | [Clinical Questions](docs/24_Clinical_Questions/README.md) |
| Quiz | [Quiz](docs/25_Quiz/README.md) |
| 勉強会・スライド | [Teaching Materials](docs/26_Teaching_Materials/README.md) / [Slide Ready](docs/27_Slide_Ready/README.md) |
| ガイドライン・論文 | [Guidelines Index](docs/28_Guidelines/README.md) / [References Index](docs/29_References/README.md) |
| 全体構造・執筆状況 | [docs portal](docs/README.md) |

## 基本思考：ABCDE + 再評価

1. **A — Airway:** 開通性、閉塞、気道デバイス、ETCO₂
2. **B — Breathing:** 酸素化、換気、呼吸仕事量、人工呼吸器・波形
3. **C — Circulation:** 血圧だけでなく組織灌流、CO、前負荷・収縮力・後負荷・心拍数
4. **D — Disability:** 意識、瞳孔、鎮痛・鎮静、せん妄、痙攣、頭蓋内病態
5. **E — Exposure / Everything else:** 感染、外傷、腎、代謝、栄養、皮膚、家族、環境
6. **Reassessment:** 介入の効果と有害事象を確認し、仮説を更新

詳細は[ABCDE Map](docs/00_Fundamentals/ABCDE/README.md)を参照してください。

## 情報の信頼度

ページ本文と文献収集結果は同じ扱いにしません。

- `docs/`: 執筆・レビューされたKnowledge
- `docs/28_Guidelines/`: 公式ガイドライン台帳
- `docs/29_References/`: 重要論文台帳と引用規則
- `literature/`: 自動収集された**未評価のEvidence inbox**。収載は推奨や妥当性を意味しません
- `data/`: 自動収集・重複管理用データ

各Knowledgeページには `Status`、`Evidence Reviewed`、`Next Review` を記録します。確認できない書誌情報や推奨は作らず、`要確認` と明示します。運用は[CONTRIBUTING.md](CONTRIBUTING.md)を参照してください。

## 学び方

1. Topic Mapからテーマを選ぶ
2. Physiology / Pathophysiologyで「なぜ」を確認する
3. Assessment → Interpretation → Clinical Reasoningで所見から仮説を組み立てる
4. Nursing Points / Red Flags / Troubleshootingでベッドサイド行動に接続する
5. Clinical CaseとQuizで想起練習する
6. Slide Ready Summaryで他者へ説明し、理解を確かめる

## 現在の段階

**Phase 1: Knowledge Base設計**です。分類、入口、テンプレート、Evidence管理、更新ルールを整備しています。空の領域や `planned` は未完成です。内容が存在するように見せるためのダミー本文は置きません。

## 自動文献収集（既存機能）

GitHub ActionsがCiNii ResearchとJ-STAGEから日本語文献候補を収集し、`literature/YYYY/MM/` に日次レポートを保存します。これはEvidence探索の入口であり、Knowledgeへの採用には原文確認とレビューが必要です。[Evidence上の位置づけ](docs/29_References/AUTOMATED_LITERATURE_INBOX.md)と[設定・実行ガイド](docs/29_References/LITERATURE_AUTOMATION_GUIDE.md)を参照してください。

## Contributing

新規ページは[Knowledge Page Template](docs/_templates/knowledge-page.md)から作成し、更新時は[CHANGELOG.md](CHANGELOG.md)へ臨床的変更を記録してください。詳しいレビュー手順は[CONTRIBUTING.md](CONTRIBUTING.md)にあります。
