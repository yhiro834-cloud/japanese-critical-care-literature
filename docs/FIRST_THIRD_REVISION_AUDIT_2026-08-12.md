---
title: "Textbook V3 First-Third Revision Audit"
status: reviewed
created: 2026-08-12
last_updated: 2026-08-12
evidence_reviewed: 2026-08-12
next_review: 2027-02-12
owners: []
reviewers: [Codex terminology, visual, and structural review]
tags: [audit, first-third, terminology, visuals]
related: [FIRST_THIRD_STUDY_GUIDE.md, ../VISUAL_QUALITY_STANDARD_V2.md, ../FIGURE_INDEX.md]
ssot: false
---

# 最初の約3分の1：文章・画像改訂監査

## 対象

全20学習領域の先頭約3分の1として、基礎、気道、呼吸生理、呼吸管理、循環／ショック、神経、腎臓を対象にした。31本の実体SSOT、各カテゴリー入口、対応する症例・スライド・図を確認した。

## 文章の修正

- 31 SSOTを横断する[学習案内](FIRST_THIRD_STUDY_GUIDE.md)を作成した。
- 頻出する9略語について、正式名称、英語名、患者の何を表すか、単独判断できない理由を示した。
- 6カテゴリーの入口から学習案内へ接続し、略語を暗記ではなく病態と測定限界から学ぶ導線にした。
- 気道救助と動脈血液ガスの本文に、新しい図の読み方、正式名称、再評価点を追加した。

## 画像の修正

- 全42 SVGへ日本語表示に適した共通font stackを適用し、再発防止testを追加した。
- 先頭約3分の1の29既存図を一括レンダリングし、代表12図をcontact sheetで比較した。
- ABCDE、人工呼吸、循環、ショック、神経、尿量低下の高頻度図について、英語見出しや説明なしの略語を日本語正式名称中心へ修正した。
- 気道緊急時の救助と動脈血液ガス解釈の2図を新規作成し、本文・Slide Ready・Figure Indexへ同期した。

## 品質確認

- SVG XML、16:9、title/desc、内部リンク、Figure Indexの一意登録を自動検査した。
- 新規図と代表既存図を1600×900 PNGへレンダリングし、文字切れ、矢印、contrast、情報密度を目視確認した。
- 教育資料であり、診療protocolとしての専門家・施設承認は別途必要である。

## Review log

- 2026-08-12: first-third terminology, navigation, visual typography, two new figures, and representative render audit completed.
