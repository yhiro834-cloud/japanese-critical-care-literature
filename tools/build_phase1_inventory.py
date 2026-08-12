#!/usr/bin/env python3
"""Build conservative Phase-1 inventories; this does not medically validate claims."""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def fm(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    return {m.group(1): m.group(2).strip() for m in re.finditer(r"^([a-z_]+):\s*(.*)$", text.split("---", 2)[1], re.M)}


def topic(path: Path, text: str) -> str:
    meta = fm(text)
    if meta.get("title"):
        return meta["title"].strip('"')
    heading = re.search(r"^#\s+(.+)$", text, re.M)
    return heading.group(1) if heading else path.stem.replace("_", " ").title()


def audit_pages() -> None:
    pages = []
    for path in sorted(DOCS.rglob("*.md")):
        if "_templates" in path.parts or path.name == "README.md":
            continue
        text = path.read_text()
        if not text.startswith("---\n"):
            continue
        meta = fm(text)
        ssot = meta.get("ssot") == "true"
        lines = len(text.splitlines())
        refs = bool(re.search(r"^## (?:\d+\. )?References", text, re.M))
        links = len(re.findall(r"https?://[^\s)>]+", text))
        nursing = bool(re.search(r"新人看護師|Nursing|看護", text, re.I))
        advanced = bool(re.search(r"ベテラン|Advanced|深掘り", text, re.I))
        reasoning = bool(re.search(r"Clinical Reasoning|臨床推論|仮説|鑑別|再評価", text, re.I))
        visuals = len(re.findall(r"assets/[^)\s]+\.(?:svg|png)", text))
        accuracy = 2 if ssot else 1
        evidence = 2 if refs and links else 1
        completeness = 3 if lines >= 100 else 2 if lines >= 55 else 1
        clinical = 3 if reasoning and lines >= 80 else 2 if reasoning else 1
        reasoning_score = 3 if reasoning and "再評価" in text else 2 if reasoning else 1
        nursing_score = 3 if nursing and "再評価" in text else 2 if nursing else 1
        physician = 3 if advanced and lines >= 100 else 2 if advanced else 1
        visual = 3 if visuals else 1
        education = 3 if nursing and advanced else 2
        integrity = 2 if refs and links else 1
        action = "REWRITE" if ssot else "MAJOR REVISION"
        missing = "claim-level citation mapping; fact/recommendation/practice labels"
        contradiction = "not yet cross-compared against sibling SSOTs"
        duplication = "not yet sentence-level deduplicated"
        urgency = "Critical" if ssot and any(x in str(path) for x in ("Mechanical_Ventilation", "Shock", "ECMO", "CRRT", "Cardiac_Arrest", "Stroke", "ICP")) else "High" if ssot else "Medium"
        pages.append((path, topic(path, text), lines, accuracy, evidence, completeness, clinical, reasoning_score, nursing_score, physician, visual, education, integrity, duplication, missing, contradiction, urgency, action))

    out = [
        "# Repository-wide Knowledge Page Audit — Phase 1 Baseline",
        "",
        "> This is a conservative zero-based audit. `status: reviewed`, document length, and the presence of references are not accepted as proof of medical correctness. Until claim-level source verification and cross-review are complete, no page receives Medical Accuracy, Evidence Quality, or Reference Integrity ≥4.",
        "",
        f"Pages audited: **{len(pages)}**. Scores are 0–5 and intentionally provisional.",
        "",
        "## Scoring interpretation",
        "",
        "- 0–1: absent or unusable evidence",
        "- 2: plausible structure, but medical/evidence verification incomplete",
        "- 3: useful baseline with major verification or depth gaps",
        "- 4: target reached after claim-level evidence and cross-review",
        "- 5: exemplary; reserved for unusually complete and independently checked work",
        "",
        "## Page-by-page audit",
        "",
        "| File | Topic | Current Quality | Medical Accuracy | Evidence Quality | Completeness | Clinical Utility | Clinical Reasoning | Nursing Utility | Physician Utility | Visual Accuracy | Educational Value | Reference Integrity | Duplication | Missing Content | Contradictions | Urgency | Recommended Action |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|---|",
    ]
    for row in pages:
        path, name, lines, *rest = row
        scores = rest[:10]
        duplication, missing, contradiction, urgency, action = rest[10:]
        current = f"Structured baseline ({lines} lines); not claim-verified"
        cells = [f"`{path.relative_to(ROOT)}`", name.replace("|", "/"), current, *map(str, scores), duplication, missing, contradiction, urgency, action]
        out.append("| " + " | ".join(cells) + " |")
    (ROOT / "AUDIT_REPORT.md").write_text("\n".join(out) + "\n")


def visual_audit() -> None:
    index = (ROOT / "FIGURE_INDEX.md").read_text()
    files = sorted(list((ROOT / "assets").rglob("*.svg")) + list((ROOT / "assets").rglob("*.png")))
    out = [
        "# Visual Asset Audit — Phase 1 Baseline",
        "",
        "> Every asset is treated as unverified until its anatomy/physiology, arrows, labels, and evidence match are independently checked against the rewritten master text. Successful rendering is not medical validation.",
        "",
        f"Assets audited: **{len(files)}** (SVG {sum(p.suffix == '.svg' for p in files)}, PNG {sum(p.suffix == '.png' for p in files)}).",
        "",
        "| Figure ID | File | Topic | Anatomical Accuracy | Physiological Accuracy | Direction / Arrow Accuracy | Label Accuracy | Scale / Proportion | Clinical Accuracy | Educational Value | Readability | PowerPoint Utility | Evidence Match | Final Decision |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|",
    ]
    high_risk = ("ecmo", "crrt", "ventilation", "waveform", "pressure", "circuit", "neurology", "hemodynamic", "pocus")
    for n, path in enumerate(files, 1):
        rel = str(path.relative_to(ROOT))
        match = re.search(rf"^\| ([^|]+) \|[^\n]*`{re.escape(rel)}`", index, re.M)
        fig_id = match.group(1).strip() if match else f"UNSTRUCTURED-{n:03d}"
        name = path.stem.replace("_", " ")
        is_raster = path.suffix == ".png"
        risky = any(k in rel.lower() for k in high_risk)
        anatomy = 2 if is_raster else 3
        physiology = 2 if risky or is_raster else 3
        arrows = 2 if risky else 3
        labels = 3
        scale = 2 if is_raster else 3
        clinical = 2
        education = 3
        readability_score = 4
        ppt = "Yes (SVG)" if path.suffix == ".svg" else "Yes (raster; limited editing)"
        evidence = 2
        decision = "REDRAW" if is_raster else "CORRECT"
        out.append(f"| {fig_id} | `{rel}` | {name} | {anatomy} | {physiology} | {arrows} | {labels} | {scale} | {clinical} | {education} | {readability_score} | {ppt} | {evidence} | {decision} |")
    (ROOT / "VISUAL_AUDIT.md").write_text("\n".join(out) + "\n")


def reference_audit() -> None:
    refs: dict[str, set[str]] = {}
    for path in sorted(DOCS.rglob("*.md")):
        for url in re.findall(r"https?://[^\s)>]+", path.read_text()):
            url = url.rstrip(".,;]")
            refs.setdefault(url, set()).add(str(path.relative_to(ROOT)))
    out = [
        "# Reference Audit — Phase 1 Baseline",
        "",
        "> URL presence is not citation integrity. Every record below requires title/author/organization/journal/year/DOI/PMID verification and claim-level support checking. No uncertain record is silently repaired.",
        "",
        f"Unique external references discovered: **{len(refs)}**.",
        "",
        "## High-priority official-source identity checks (2026-08-12)",
        "",
        "| Domain | Official source | Publication / status finding | Phase-1 implication |",
        "|---|---|---|---|",
        "| Sepsis | https://www.sccm.org/survivingsepsiscampaign/guidelines-and-resources/surviving-sepsis-campaign-adult-guidelines | SSC adult guideline 2026; official SCCM page states it updates 2021 and contains 129 statements | Remap every sepsis recommendation; do not carry 2021 strength forward |",
        "| Japanese sepsis | https://www.jsicm.org/news/news241225-J-SSCG2024.html | J-SSCG2024 final version announced 2024-12-25 | Compare population, question and strength with SSC 2026 |",
        "| Resuscitation / PCAS | https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines | AHA CPR/ECC 2025 is the current official guideline set | Replace inherited 2020/2023 wording where superseded; retain COR/LOE |",
        "| Hemodynamics | https://www.esicm.org/wp-content/uploads/2025/10/Visual-abstract-final.pdf | ESICM circulatory shock and hemodynamic monitoring 2025 official visual abstract | Verify against full guideline before citing exact recommendations |",
        "| AKI / AKD | https://kdigo.org/guidelines/acute-kidney-injury/ | KDIGO 2026 document is explicitly a public-review draft; 2012 remains current final until publication | Never present draft statements as adopted clinical guidance |",
        "| ECMO | https://www.elso.org/ecmo-resources/elso-ecmo-guidelines.aspx | Official ELSO list confirms adult VV 2021, adult VA 2021 and circuit 2022 guidance | Verify each ECMO claim and circuit figure against the relevant document |",
        "| Ventilator assessment | https://www.aarc.org/resource/clinical-practice-guidelines/ | Official AARC list confirms Patient–Ventilator Assessment 2024 and SBT 2024 | Use exact recommendation text; not a source for all ventilator thresholds |",
        "| Neurocritical care | https://www.neurocriticalcare.org/Resources-Publications/Neurocritical-Care-Guidelines | Official NCS index confirms current topic-specific guidelines; years vary | Verify each neuro topic separately; do not infer one guideline covers all disorders |",
        "| Japanese critical care | https://www.jsicm.org/publication/guideline.html | Official JSICM index lists J-SSCG2024, Japanese nutrition 2024 (published 2025), J-ReCIP 2023 and other guidance | Add Japanese guidance where scope matches; distinguish title year from publication date |",
        "",
        "## Full URL inventory",
        "",
        "| Title | Author / Group | Organization / Journal | Year | DOI | PMID | URL | Used by | Identity status | Claim-support status | Action |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for url, pages in sorted(refs.items()):
        host = urlparse(url).netloc
        doi = urlparse(url).path.lstrip("/") if host == "doi.org" else "NOT RE-VERIFIED"
        used = ", ".join(f"`{p}`" for p in sorted(pages)[:3]) + (f" (+{len(pages)-3})" if len(pages) > 3 else "")
        out.append(f"| REFERENCE NOT RE-VERIFIED | REFERENCE NOT RE-VERIFIED | {host} | REFERENCE NOT RE-VERIFIED | {doi} | REFERENCE NOT RE-VERIFIED | {url} | {used} | REFERENCE NOT RE-VERIFIED | NOT MAPPED TO CLAIM | verify primary source; remove or flag if unresolved |")
    (ROOT / "REFERENCE_AUDIT.md").write_text("\n".join(out) + "\n")


def revision_status() -> None:
    rows = []
    for path in sorted(DOCS.rglob("*.md")):
        text = path.read_text()
        if "_templates" in path.parts or "\nssot: true\n" not in text:
            continue
        rows.append((path, topic(path, text)))
    out = [
        "# Revision Status",
        "",
        "> Phase 1 starts from zero-based audit. Existing `reviewed` metadata does not equal completion under the Master Reference criteria.",
        "",
        "| Topic | File | Audit | Evidence reviewed | Text rewritten | Figures reviewed | Figures rebuilt | Cross-reviewed | Complete | Human review required |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for path, name in rows:
        out.append(f"| {name.replace('|','/')} | `{path.relative_to(ROOT)}` | Audited | Not started | Not started | Not started | Not started | Not started | No | Yes |")
    (ROOT / "REVISION_STATUS.md").write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    audit_pages()
    visual_audit()
    reference_audit()
    revision_status()
