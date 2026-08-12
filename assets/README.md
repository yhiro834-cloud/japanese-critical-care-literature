# Visual Asset Design System

このDirectoryは、Knowledge Base本文を補助するオリジナル教育用Visual Assetを管理します。第三者の図は保存しません。

## Visual grammar

| Meaning | Color | Shape / line |
|---|---|---|
| Normal / confirmed | `#1976A3` blue | solid line / rounded rectangle |
| Assessment / observation | `#31546D` slate | outlined card |
| Intervention | `#16856B` green | solid header / action arrow |
| Warning / red flag | `#C74440` red | diamond / double border |
| Pathology / abnormal | `#D97706` amber | amber fill / dashed line |
| Flow / reassessment | `#5B5BD6` indigo | directional arrow / loop |

色だけに依存せず、label、形状、線種を併用します。背景は`#FFFFFF`、本文は`#172B3A`、補助線は`#CBD8E1`を基本とします。

## Production rules

- Canvasは原則1600 × 900（16:9）。viewBoxを維持し、PowerPointで拡大可能なSVGを優先する。
- One Figure = One Main Concept。短いlabelと凡例で単独使用可能にする。
- font stackは`Arial, Helvetica, sans-serif`。本文24 px以上、見出し32 px以上。
- arrow markerは血流・因果・手順の方向を明確にし、両方向を不用意に使わない。
- Figure ID、教育用である旨、Evidence/SSOT参照をfooterへ記載する。
- 図内は日本語約8割を基本とし、SpO₂、ETCO₂、ABG、MAP、GCS、ECGなど臨床で共通する略語と初出の英語だけを残す。
- 専門用語・略語は、図内で意味が推測できない場合に日本語名または短い定義を添える。
- 勉強会投影用の本図とは別に、必要に応じて「一言でいうと」「最初に見る場所」「ミニ症例」「判断限界」を本文へ置き、初学者とスマートフォン閲覧者の入口を作る。
- 数値、dose、推奨強度は、確認済みSSOTに存在する場合だけ掲載する。

## Quality checklist

1. Medical Accuracy: 左右、方向、因果、labelをSSOTと照合したか。
2. Educational Value: 文章だけより理解が速くなるか。
3. Simplicity: 独立概念を詰め込んでいないか。
4. Readability: GitHub幅と16:9 slideの双方で読めるか。
5. Accessibility: 色以外の区別、十分なcontrast、意味のあるalt textがあるか。
6. Evidence: Figure IndexからSSOT/Evidenceへ追跡できるか。
7. Copyright: オリジナル構成で第三者図を模写していないか。
8. Terminology: 新人が略語と図の目的を説明できるか。
9. Teaching Use: ベテランが例外・限界を補足しながら勉強会で使用できるか。
