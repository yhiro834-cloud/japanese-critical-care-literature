# Critical Care Master Reference — Revision Roadmap

## Governing rule

The order is **Evidence → Text → Clinical reasoning → Figure → Cross-review**. A green render, a long page, or an existing `reviewed` flag cannot advance a topic. A page becomes `Complete` only when every required score is ≥4/5 or the page is explicitly marked `NEEDS FURTHER REVIEW`.

## Phase 0 — Backup (complete)

- Baseline commit: `101ef41bf46ad5257ae0db217be5aaab2e3de9f7`
- Preserved branch: `backup/pre-master-reference-audit-2026-08-12`
- Destructive rewriting is prohibited; changes proceed by reviewable commits and PRs.

## Phase 1 — Audit (current)

Deliverables:

- `AUDIT_REPORT.md`: 170-page conservative page audit
- `CONTENT_GAP_ANALYSIS.md`: requested-domain coverage and missing master pages
- `VISUAL_AUDIT.md`: 74-asset zero-based visual audit
- `REFERENCE_AUDIT.md`: 122 unique external URLs, all re-verification status explicit
- `REVISION_ROADMAP.md`: phase sequence and gates
- `HUMAN_REVIEW_REQUIRED.md`: specialty and local-policy sign-off queue
- `REVISION_STATUS.md`: 74実体SSOT status matrix（template除外）

Exit gate: every current page, visual and external URL is inventoried; no baseline asset is implicitly approved.

## Phase 2 — Foundation

1. Create `STYLE_GUIDE.md` with preferred Japanese/English terminology, first-use abbreviation rules and prohibited mixed-language forms.
2. Add evidence-label blocks: Established Physiology / Guideline Recommendation / Evidence Suggests / Common Practice / Expert Opinion / Uncertain.
3. Define a claim citation syntax containing source ID, population, context, recommendation class/strength, access date and exceptions.
4. Update page template for Executive Summary, physiology, reasoning, nursing, physician-level depth, uncertainty and claim-level references.
5. Create threshold registry and prevent context-free numbers.
6. Define SSOT ownership and cross-link rules; run similarity/contradiction audit before merging duplicates.
7. Revise Figure Index so every asset has a structured Figure ID, related SSOT, evidence match narrative and `PowerPoint Reusable` field.

Exit gate: one pilot page and figure pass the new schema without duplicating existing SSOT content.

## Phase 3 — High-priority rewrite sequence

| Order | Workstream | Required review perspectives | Key evidence status to resolve |
|---:|---|---|---|
| 1 | ABCDE and clinical reasoning | Emergency physician, nurse educator, human factors | international emergency-care and resuscitation sources |
| 2 | Respiratory physiology | Intensivist, respiratory physiology, nursing | measurement limitations and primary physiology sources |
| 3 | Mechanical ventilation / PEEP | Intensivist, respiratory therapist, illustrator | ATS/AARC guidance; threshold vs association distinctions |
| 4 | ARDS | Intensivist, evidence reviewer | ATS 2024; Japanese ARDS guidance and update status |
| 5 | Hemodynamics | Cardiovascular intensivist, POCUS, nursing | ESICM 2025 and measurement validity |
| 6 | Shock | Intensivist, cardiovascular, evidence reviewer | ESICM 2025; phenotype-specific uncertainty |
| 7 | Sepsis | Intensivist, infectious disease, pharmacist | SSC 2026 and J-SSCG2024 claim mapping |
| 8 | Neurocritical care | Neurointensivist, pharmacist, nursing | AHA/ASA, BTF, NCS; Japanese draft/final status |
| 9 | CRRT / AKI | Nephrologist, pharmacist, nurse/engineer | KDIGO 2012 final vs 2026 public-review draft |
| 10 | ECMO / MCS | ECMO specialist, cardiac intensivist, engineer | ELSO source and device-specific limitations |
| 11 | ALS / post-arrest | Emergency, cardiac, neurointensivist | AHA 2025 and ILCOR recommendation classes |
| 12 | Emergency troubleshooting | Multidisciplinary bedside review | differential completeness and signal validity |

Each workstream follows: claim inventory → primary-source verification → rewrite → nursing/physician review → figure decision → render/visual review → contradiction scan → tests → PR.

## Phase 4 — Remaining fields

Proceed through airway, cardiac, infection, trauma, endocrine, GI/liver, hematology/transfusion, pharmacology, nutrition, PADIS, rehabilitation/PICS, infection control, procedures, monitoring/POCUS/devices, nursing, obstetric, toxicology/environmental, ethics/end-of-life/family care. Use the priorities in `CONTENT_GAP_ANALYSIS.md`.

## Phase 5 — Visual reconstruction

- Replace all seven AI raster anatomy assets unless a specialty reviewer can validate and provenance can be documented.
- Correct all 67 SVGs against the rewritten SSOT and exact evidence match.
- Use programmatic SVG for flow, pressure, circuit, waveform and quantitative relationships.
- Keep one main concept per figure.
- Write a prose statement of what each figure claims; compare it against image, text and evidence.
- Render and visually inspect every revision before adoption.

## Phase 6 — Cross-review

For each topic, record separate findings from relevant Editorial Board perspectives. A single generic “reviewed” label is insufficient. Resolve or explicitly preserve disagreements.

## Phase 7 — Final QA

- all internal links and Markdown rendering
- external citation identity and claim support
- outdated/superseded/draft source status
- duplicate and contradictory claims
- terminology and abbreviation consistency
- all visuals rendered and visually inspected
- score ≥4/5 in every Definition-of-Done dimension, or `NEEDS FURTHER REVIEW`
- human-review queue contains no hidden uncertainty

## Phase report format

At each exit: What was wrong / What was corrected / Evidence changes / Visual corrections / Remaining uncertainty / Next priority.
