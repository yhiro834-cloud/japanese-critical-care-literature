# Documentation Portal

## Core architecture and operations

- [Topic Map](TOPIC_MAP.md): 集中治療領域全体とSingle Source of Truthの配置
- [Knowledge Page Template](_templates/knowledge-page.md)
- [Clinical Case Template](_templates/clinical-case.md)
- [Quiz Template](_templates/quiz.md)
- [Slide Ready Template](_templates/slide-ready.md)
- [Guidelines Index](28_Guidelines/README.md)
- [References Index](29_References/README.md)
- [Evidence review workflow](29_References/EVIDENCE_WORKFLOW.md)
- [更新ルール](../CONTRIBUTING.md)
- [変更履歴](../CHANGELOG.md)
- [完成監査](COMPLETION_AUDIT_2026-08-12.md) / [実装状況](IMPLEMENTATION_STATUS.md)

## Status legend

| Status | 意味 |
|---|---|
| `planned` | Topicのみ定義。本文は未作成 |
| `draft` | 執筆中。臨床利用前にレビューが必要 |
| `reviewed` | 編集・根拠・構造の内部監査済み。外部専門家レビューや施設承認とは別 |
| `reviewed` | 指定日までEvidence・臨床レビュー済み |
| `update-needed` | 新Evidence、期限超過、または重要な修正が必要 |

`reviewed` は恒久的な保証ではありません。各ページの `Evidence Reviewed` と `Next Review` を確認してください。

## Single Source of Truth

詳細説明は最も適切な1ページだけに置き、他ページから相対リンクします。例えばDriving Pressureの定義・測定・限界はMechanical Ventilation配下を本体とし、ARDSページはARDSにおける意味と適用だけを説明します。

## ファイル命名

- ディレクトリ: 既存の番号付き分類を維持
- Topicページ: `UPPER_SNAKE_CASE.md` または領域内で合意した英語名
- 症例: `CASE_<problem>.md`
- Quiz: `QUIZ_<topic>.md`
- URLを壊す改名は避け、必要なら移行リンクを残す
