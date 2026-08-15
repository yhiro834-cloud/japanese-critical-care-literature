# Critical Care Knowledge Base

高度救命救急センター・ICUで必要な知識を、**基礎生理 → 病態生理 → 評価 → モニタリング → 臨床推論 → 治療 → 看護 → 症例学習 → 教育**の流れで育てるKnowledge Portalです。

> [!CAUTION]
> 本リポジトリは医療従事者の教育・学習を目的とし、個別患者への診療指示を目的としません。実際の診療では、患者個別の病態、最新の公式ガイドライン、医師を含む医療チームの判断、各施設のプロトコルを優先してください。薬剤投与量、人工呼吸器設定、ECMO、CRRTなどの高リスク介入は、適応・禁忌・監視・施設体制を含めて個別に判断してください。

## Knowledge Portal

| 探し方 | 入口 |
|---|---|
| ABCDEから探す | [ABCDE Map](docs/00_Fundamentals/ABCDE/README.md) |
| 初めて学ぶ・用語から探す | [重症ケア基本用語集](docs/00_Fundamentals/Glossary/CRITICAL_CARE_GLOSSARY.md) / [人工呼吸器の基本用語](docs/02_Breathing/Mechanical_Ventilation/VENTILATOR_TERMS.md) |
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
| 視覚教材 | [Figure Index](FIGURE_INDEX.md) / [Visual Asset Plan](VISUAL_ASSET_PLAN.md) / [Design System](assets/README.md) |
| ガイドライン・論文 | [Guidelines Index](docs/28_Guidelines/README.md) / [References Index](docs/29_References/README.md) |
| 全体構造・執筆状況 | [docs portal](docs/README.md) |
| V2の執筆・画像基準 | [Textbook V2 Standards](TEXTBOOK_V2_STANDARDS.md) |
| V2全面改訂の進捗 | [Textbook V2 Migration](docs/TEXTBOOK_V2_MIGRATION.md) |
| 完成監査 | [Completion Audit 2026-08-12](docs/COMPLETION_AUDIT_2026-08-12.md) / [Implementation Status](docs/IMPLEMENTATION_STATUS.md) |

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

1. 新人看護師は用語集と各章の「まず覚える」から始める
2. 観察 → 報告 → 再評価を確認し、患者の変化へ結びつける
3. Physiology / Pathophysiologyで「なぜ」を確認する
4. 中堅・ベテランは測定限界、複合病態、Evidenceの不確実性まで読む
5. Clinical CaseとQuizで所見から仮説を組み立てる
6. 図解とSlide Ready Summaryを使って他者へ説明し、理解を確かめる

## 現在の段階

00〜32の全カテゴリーについて、SSOT本文、Cases/CQ/Quiz/Slide Readyへの導線、図解、根拠台帳の編集・根拠・表示監査を完了し、本文を`reviewed`へ統一しました。これは外部専門学会による認証や、施設固有protocolとの整合保証を意味しません。Evidence surveillanceと領域専門家による追加レビューは継続します。完了範囲と検証結果は[Completion Audit 2026-08-12](docs/COMPLETION_AUDIT_2026-08-12.md)を参照してください。

## 自動文献収集（既存機能）

GitHub ActionsがCiNii ResearchとJ-STAGEから日本語文献候補を収集し、`literature/YYYY/MM/` に日次レポートを保存します。これはEvidence探索の入口であり、Knowledgeへの採用には原文確認とレビューが必要です。[Evidence上の位置づけ](docs/29_References/AUTOMATED_LITERATURE_INBOX.md)と[設定・実行ガイド](docs/29_References/LITERATURE_AUTOMATION_GUIDE.md)を参照してください。

## Contributing

新規ページは[Knowledge Page Template](docs/_templates/knowledge-page.md)から作成し、更新時は[CHANGELOG.md](CHANGELOG.md)へ臨床的変更を記録してください。詳しいレビュー手順は[CONTRIBUTING.md](CONTRIBUTING.md)にあります。

## 文献が見つかった後に行われること

1. J-STAGEとCiNii Researchの公式APIで文献を検索します。
2. DOIやデータベースIDで重複を除外します。
3. APIから取得できた抄録を確認し、本文未確認と明確に区別します。
4. 原文中の語句だけを使って研究デザインを判定します。
5. 明記された範囲だけでPICO／PECO、対象者、症例数、施設数を整理します。
6. 抄録に明示された主要結果と統計値を抽出します。
7. 目的・方法・結果・結論の原文文を選ぶ「抽出的要約」を作ります。
8. 文献ごとのEvidence Cardを `evidence/YYYY/MM/` に生成します。
9. 研究利用可能性と領域関連性をルールで一次評価します。
10. 研究・臨床利用前に、人間が原著論文を最終確認します。

### AI要約を使用しない理由

有料のOpenAI、Anthropic、Gemini等の生成AI APIは使用しません。原文にない情報が生成されるリスクを避け、どの原文情報から抽出したか追跡できることを優先します。PDF URLがあってもPDF本文を確認した扱いにはせず、PDFを大量ダウンロードしません。

このシステムは「論文を読んだ人間の代わり」ではありません。自動分類・重要度・研究デザイン・PICO・抽出的要約は、読むべき文献を見つけるための一次整理です。研究や臨床で引用・利用する前に、特に数値、統計解析、結論、因果関係、ガイドラインの推奨、推奨度、エビデンスレベルを必ず原文で確認してください。
