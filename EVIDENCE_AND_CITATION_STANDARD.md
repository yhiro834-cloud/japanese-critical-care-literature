# Evidence・引用標準

最終更新: 2026-08-12

## 目的

章末に文献を並べるだけでなく、臨床的主張が「どの資料の、どの対象・条件・推奨」に支えられるかを追跡可能にする。

## Evidenceの優先順位

1. 現行の公式ガイドライン、診療指針、規制当局・公的機関文書
2. Systematic review / meta-analysis
3. 無作為化比較試験、前向き比較研究
4. 観察研究、診断精度研究
5. Consensus statement、専門家意見
6. 教科書・総説（二次的な理解の補助）
7. 施設手順、機器マニュアル（適用施設・機種に限定）

順位だけで採否を決めない。研究デザイン、直接性、精確性、一貫性、対象への適用可能性、利益と害を評価する。

## 主張単位の識別

- 主張ID: `CLM-章略号-連番`（例 `CLM-VENT-001`）
- 出典ID: `SRC-章略号-連番`（例 `SRC-VENT-001`）
- 一つの主張が複数資料に依存してよい。一つの出典を、支えていない主張へ流用してはならない。
- 定義、診断基準、推奨、具体的数値、禁忌、安全上の警告は原則として主張IDを必須とする。

本文例:

> **[RECOMMENDATION] [CLM-XXX-001]** 対象、介入、条件、推奨強度を含む文章。[SRC-XXX-001]

## 引用台帳の必須項目

| 項目 | 記載内容 |
|---|---|
| Source ID | `SRC-...` |
| Title | 正式タイトル |
| Authors / Group | 著者または作成グループ |
| Organization / Journal | 発行主体または雑誌 |
| Year / Version | 年、版、更新日 |
| Status | current final / draft / superseded / withdrawn / unknown |
| Evidence type | guideline / systematic review / RCT 等 |
| DOI / PMID / Official URL | 可能な限り一次資料へ直接接続 |
| Population | 成人、小児、妊婦、特定疾患など |
| Context | ICU、救急、術後、測定条件など |
| Exact claim supported | 支持する Claim ID と具体的内容 |
| Recommendation strength | 原典の表記。なければ「記載なし」 |
| Exceptions / limits | 除外、外挿、測定限界、害 |
| Verified on | 実際に本文または公式抄録を照合した日 |
| Reviewer | 医学、看護、Evidence担当 |

## 検証状態

- **VERIFIED:** 一次資料の本文または公式全文で、主張・対象・条件を照合済み。
- **IDENTITY VERIFIED:** 書誌情報と資料の存在のみ確認。主張との対応は未確認。
- **REFERENCE NOT VERIFIED:** 書誌情報または本文を未照合。根拠として断定に使わない。
- **NEEDS SOURCE REMAPPING:** 既存の引用が主張を直接支持するか不明。再割当てが必要。

## ガイドラインの扱い

- 公式ページで現行版を確認し、公開草案を最終版として扱わない。
- 原典が推奨していない閾値を、ガイドライン名を添えて推奨値に見せない。
- “we recommend” と “we suggest”、強い推奨と条件付き推奨を日本語で区別する。
- 成人データを小児、妊婦、ECMO患者などへ外挿する場合は **[UNCERTAINTY]** とする。
- 改訂により置換された資料は歴史的背景に限定し、`superseded` と明示する。

## Claim-level QA

1. 主張は一文で特定できるか。
2. 引用先が同じ患者集団・臨床状況を扱うか。
3. 数値、方向、推奨強度が原典と一致するか。
4. 例外、害、確実性の低さを省略していないか。
5. URLではなくタイトル、発行主体、年、版を記録したか。
6. 最終Evidence確認日と確認者を残したか。

未達の主張は完成扱いにせず、[HUMAN_REVIEW_REQUIRED.md](HUMAN_REVIEW_REQUIRED.md) と [REVISION_STATUS.md](REVISION_STATUS.md) に残す。
