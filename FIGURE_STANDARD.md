# 図版・医療イラスト標準

最終更新: 2026-08-12

## 原則

- 1図1概念とし、図だけで診療手順を完結させない。
- 図が伝える **Figure Claim** を一文で固定し、本文の Claim ID と対応させる。
- 解剖、左右、流れ、圧、時間、因果、機器接続をそれぞれ監査する。
- 数値グラフ、回路、波形、アルゴリズムは検証可能なSVG等で作成し、生成AIの見た目を根拠にしない。
- 生成AIによる解剖イラストは教育補助とし、専門家の目視監査前は完成扱いにしない。

## Figure Index 必須項目

Figure ID、Topic、Learning Objective、File、Related Knowledge Page、Figure Type、PowerPoint Reusable、Suggested Slide Use、Evidence Source、Last Reviewedを登録する。さらに各図の査読記録で次を管理する。

| 項目 | 合格条件 |
|---|---|
| Figure Claim | 一文で、本文の主張と一致 |
| Anatomy | 部位、左右、位置関係が正確または非該当 |
| Physiology / pathophysiology | 矢印と因果が本文・Evidenceと一致 |
| Labels | 自然な日本語。略語は説明あり |
| Quantitative fidelity | 軸、単位、波形、比率が原典と一致または「模式図」と明示 |
| Clinical boundary | 図だけで診断・投薬・機器設定を決めない旨が明確 |
| Accessibility | 1600×900、色以外の区別、title/desc、可読フォント |
| Reuse | PowerPointで切れず、出典とFigure IDを保持 |
| Review status | correct / revise / redraw / needs expert review |

## 本文直下の説明

1. Caption: 何を示す図か。
2. 最初に見る場所: 読み始める位置。
3. 読み方: 矢印、色、配置の意味。
4. Clinical Meaning: ベッドサイド観察との接続。
5. 判断限界: 図から決められないこと。
6. Mini Case: 所見を使う短い問い。

## 完了判定

医学、看護、Evidence、教育、表示の各確認を記録し、いずれか未確認なら [HUMAN_REVIEW_REQUIRED.md](HUMAN_REVIEW_REQUIRED.md) に残す。高解像度であることは医学的正確性の代わりにならない。
