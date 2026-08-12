# Phase 2 Report — 再構築基盤

実施日: 2026-08-12  
対象: 用語、文章、Evidence、引用、臨床数値、章テンプレート、図版登録

## 何が問題だったか

- 日本語と英語の混在規則が弱く、略語が初学者の理解を妨げる箇所があった。
- 章末文献は存在しても、どの主張を直接支えるか追跡できなかった。
- 目標値、診断基準、介入目安、危険所見が同じ「閾値」として独り歩きする危険があった。
- 章テンプレートに対象集団、推奨強度、例外、介入後再評価の必須欄が不足していた。
- 13点のSVGがFigure Indexの箇条書きに留まり、Figure IDとEvidence状態を持たなかった。

## 何を修正したか

- `STYLE_GUIDE.md` を新設し、自然な日本語、初出用語、略語、主張ラベル、看護実践記述を標準化した。
- `EVIDENCE_AND_CITATION_STANDARD.md` を新設し、Claim ID、Source ID、引用必須項目、検証状態を定義した。
- `THRESHOLD_REGISTRY.md` を新設し、高リスク数値を対象・条件・例外・根拠と一体で管理する構造にした。
- Knowledge PageテンプレートをQuick Review / Core / Advancedの三層へ更新し、ICU Nursing PearlsとClaim-level Referencesを追加した。
- `FIGURE_STANDARD.md` を新設し、Figure Claim、医学的整合、表示、再利用、専門家査読の合格条件を定めた。
- 未構造化だった13図を固有Figure ID付きで `FIGURE_INDEX.md` の表へ移行した。
- `TEXTBOOK_V2_STANDARDS.md` に新しい正本を明示し、過去の `reviewed` 表記を医学的完成と見なさないことを明記した。

## Evidence確認

Phase 2はEvidenceの内容を一括確定する段階ではなく、検証方法を固定する段階である。未照合の主張や数値は `REFERENCE NOT VERIFIED` または `NEEDS SOURCE REMAPPING` と明示し、確定値を新規に作成していない。

## 図版確認

全74点をFigure Indexの構造化行として登録した。ただし、既存図の医学的正確性をPhase 2で保証したものではない。追加した13行は `NEEDS FURTHER REVIEW`、AI生成PNG 7点はPhase 1判定どおり再描画・専門家確認が必要である。

## 残る不確実性

- 74章の個別主張と一次資料の対応は未完了。
- 数値レジストリの値は各専門領域Phaseで確定する。
- 図の解剖、波形、回路、定量表現には専門家査読が必要。
- 施設手順、機種、法制度に依存する内容は一般化できない。

## 次のPhase

Phase 3ではABCDE、呼吸生理、人工呼吸・PEEP、ARDSを優先し、上記基準を実際の章に適用する。主張単位の出典照合、用語説明、看護観察・報告・再評価、図版の医学的照合を同時に進める。
