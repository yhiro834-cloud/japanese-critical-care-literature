---
title: "Textbook V2 Migration"
status: active
created: 2026-08-12
last_updated: 2026-08-12
evidence_reviewed: not-applicable
next_review: 2026-09-12
owners: []
reviewers: [Codex structural review]
tags: [implementation, textbook-v2]
related: [../TEXTBOOK_V2_STANDARDS.md]
ssot: false
---

# Textbook V2 Migration

Last audited: 2026-08-12

## 目的

既存の網羅性を保ちながら、全章を[Textbook V2 Standards](../TEXTBOOK_V2_STANDARDS.md)へ移行します。チェックは「ページが存在する」ではなく、用語説明、新人向け実践、ベテラン向け深掘り、Evidence、図解、症例まで品質確認したことを示します。

## 改訂順序

| Phase | 範囲 | 主な成果物 | 状態 |
|---|---|---|---|
| V2-0 | 全体設計 | 執筆基準、用語集、template、画像基準 | 進行中 |
| V2-1 | Fundamentals / ABCDE | 安全な初期評価、正常と異常、報告、再評価 | 用語基盤を実装、ABCDE本文は未着手 |
| V2-2 | Airway / Breathing | 酸素療法、人工気道、人工呼吸、ARDS、離脱 | Airway 3章とBreathing 8章のV2導線を実装 |
| V2-3 | Circulation / Shock | 血圧・flow・灌流、輸液、血管作動薬、POCUS | 主要6章のV2導線を実装 |
| V2-4 | Neuro / Renal / Infection | 意識・ICP、AKI/CRRT、感染・sepsis | 主要10章のV2導線を実装 |
| V2-5 | Trauma / Cardiac / ECMO-MCS | 高リスク急変とdevice safety | 未着手 |
| V2-6 | Endocrine / GI / Hematology | 代謝、出血、肝・膵、凝固・輸血 | 未着手 |
| V2-7 | 薬剤 / 栄養 / PADIS / Rehab | 投薬安全、comfort、回復 | 未着手 |
| V2-8 | Monitoring / Devices / Nursing | 系統的観察、alarm、handover、家族支援 | 未着手 |
| V2-9 | Special populations / Toxicology / Ethics | 対象別例外と意思決定 | 未着手 |
| V2-10 | Cases / Quiz / Slides / Figures | 全教材の本文同期と勉強会QA | 未着手 |
| V2-11 | Final audit | link、用語、Evidence、画像、専門家review台帳 | 未着手 |

## 各ページの監査項目

- [ ] 初出の略語と専門用語を説明
- [ ] 「一言でいうと」と新人看護師の到達目標
- [ ] 観察項目に理由と異常時の追加確認
- [ ] 報告例と介入後の再評価
- [ ] ベテラン向けの例外・限界・複合病態
- [ ] Red Flagsとよくある誤解
- [ ] 重要主張と一次資料の対応
- [ ] 図解または図が不要な理由
- [ ] 症例・確認問題・Slide Readyとの整合
- [ ] 医学、看護、教育、表示のreview記録

## 現在の完了内容

- [x] V2共通執筆基準
- [x] Knowledge Page Templateの二層化
- [x] 重症ケア基本用語集の初版
- [x] 人工呼吸器基本用語（PEEP、Ppeak、Pplat、driving pressure等）
- [x] Airway評価・RSI/困難気道・人工気道管理のV2化
- [x] 呼吸生理・酸素療法・HFNC・NIV・ABG・人工呼吸・ARDS・離脱のV2導線
- [x] Shock・血行動態・輸液・昇圧薬/強心薬・敗血症性shock・POCUSのV2導線
- [x] 神経5章・腎3章・感染2章のV2導線
- [x] 画像の用語説明・初学者導線・勉強会利用基準
- [ ] 既存SSOT全ページのV2変換
- [ ] 多職種専門家review
- [ ] 新人・ベテラン看護師によるユーザーテスト

## 安全上の扱い

移行中のページは原則 `review-needed` のままです。V2移行済みでも、施設protocolや専門家reviewを置き換えません。旧ページを一括削除せず、リンクと履歴を保ちながら改稿します。
