import re
import struct
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).parents[1]
DOCS = ROOT / "docs"


def test_internal_markdown_links_resolve():
    missing = []
    for page in ROOT.rglob("*.md"):
        for target in re.findall(r"(?<!!)\[[^]]+\]\(([^)]+)\)", page.read_text()):
            target = target.split("#", 1)[0]
            if not target or urlparse(target).scheme or target.startswith("mailto:"):
                continue
            if not (page.parent / unquote(target)).resolve().exists():
                missing.append(f"{page.relative_to(ROOT)} -> {target}")
    assert not missing, "Missing internal links:\n" + "\n".join(missing)


def test_content_pages_have_review_metadata():
    excluded_names = {"README.md", "TOPIC_MAP.md", "IMPLEMENTATION_STATUS.md"}
    required = {
        "status",
        "created",
        "last_updated",
        "evidence_reviewed",
        "next_review",
    }
    failures = []
    for page in DOCS.rglob("*.md"):
        if page.name in excluded_names or "_templates" in page.parts:
            continue
        text = page.read_text()
        if not text.startswith("---\n"):
            failures.append(f"{page.relative_to(ROOT)}: no frontmatter")
            continue
        frontmatter = text.split("---", 2)[1]
        keys = {line.split(":", 1)[0] for line in frontmatter.splitlines() if ":" in line}
        absent = sorted(required - keys)
        if absent:
            failures.append(f"{page.relative_to(ROOT)}: missing {', '.join(absent)}")
    assert not failures, "Review metadata failures:\n" + "\n".join(failures)


def test_ssot_pages_have_required_identity_and_review_log():
    failures = []
    for page in DOCS.rglob("*.md"):
        if "_templates" in page.parts:
            continue
        text = page.read_text()
        if "\nssot: true\n" not in text:
            continue
        frontmatter = text.split("---", 2)[1]
        for key in ("title:", "owners:", "reviewers:", "related:"):
            if key not in frontmatter:
                failures.append(f"{page.relative_to(ROOT)}: missing {key[:-1]}")
        if not re.search(r"^## Review [Ll]og$", text, re.MULTILINE):
            failures.append(f"{page.relative_to(ROOT)}: missing Review log")
        if len(text.splitlines()) < 45:
            failures.append(f"{page.relative_to(ROOT)}: unexpectedly short SSOT")
    assert not failures, "SSOT audit failures:\n" + "\n".join(failures)


def test_real_ssot_pages_have_v2_staged_learning_markers():
    failures = []
    for page in DOCS.rglob("*.md"):
        if "_templates" in page.parts:
            continue
        text = page.read_text()
        if "\nssot: true\n" not in text:
            continue
        required_patterns = {
            "plain-language entry": r"簡単に言うと|このページは|この章の使い方",
            "novice guidance": r"新人看護師(?:の到達点|の到達目標|が見ること|：)",
            "advanced guidance": r"ベテラン(?:向け深掘り|：)",
        }
        for label, pattern in required_patterns.items():
            if not re.search(pattern, text):
                failures.append(f"{page.relative_to(ROOT)}: missing {label}")
    assert not failures, "V2 staged-learning failures:\n" + "\n".join(failures)


def test_real_ssot_pages_have_direct_external_evidence_identity():
    failures = []
    for page in DOCS.rglob("*.md"):
        if "_templates" in page.parts:
            continue
        text = page.read_text()
        if "\nssot: true\n" not in text:
            continue
        match = re.search(
            r"^## (?:\d+\. )?References\s*$\n(.*?)(?=^## |\Z)",
            text,
            re.MULTILINE | re.DOTALL,
        )
        if not match:
            failures.append(f"{page.relative_to(ROOT)}: missing References section")
        elif not re.search(r"https?://|\bDOI\b|\bPMID\b", match.group(1), re.IGNORECASE):
            failures.append(f"{page.relative_to(ROOT)}: no direct external evidence identifier")
    assert not failures, "SSOT evidence identity failures:\n" + "\n".join(failures)


def test_learning_asset_topic_sets_remain_aligned():
    expected = {
        "AIRWAY", "BEDSIDE_SYSTEMS_NURSING", "CARDIAC_CRITICAL_CARE",
        "CRITICAL_CARE_FUNDAMENTALS", "ECMO_MCS", "ENDOCRINE_METABOLIC",
        "GI_LIVER_PANCREAS", "HEMATOLOGY", "HEMODYNAMICS",
        "INFECTION_CONTROL_PROCEDURES", "INFECTION_SEPSIS", "NEUROCRITICAL",
        "PADIS_REHAB_PICS", "PHARMACOLOGY_NUTRITION", "RENAL",
        "RESPIRATORY_PHYSIOLOGY_ABG", "RESPIRATORY_SUPPORT",
        "SHOCK_SEPTIC_SHOCK", "SPECIAL_TOXICOLOGY_SYSTEMS", "TRAUMA_BURNS",
    }
    questions = {p.stem.removesuffix("_QUESTIONS") for p in (DOCS / "24_Clinical_Questions").glob("*_QUESTIONS.md")}
    quizzes = {p.stem.removeprefix("QUIZ_") for p in (DOCS / "25_Quiz").glob("QUIZ_*.md")}
    slides = {re.sub(r"_(20|30)MIN$", "", p.stem) for p in (DOCS / "27_Slide_Ready").glob("*MIN.md")}
    questions = {"CRITICAL_CARE_FUNDAMENTALS" if name == "FUNDAMENTALS" else name for name in questions}
    assert questions == expected
    assert quizzes == expected
    assert slides == expected


def test_svg_visual_assets_are_parseable_accessible_and_widescreen():
    failures = []
    for asset in (ROOT / "assets").rglob("*.svg"):
        try:
            root = ET.parse(asset).getroot()
        except ET.ParseError as exc:
            failures.append(f"{asset.relative_to(ROOT)}: invalid XML ({exc})")
            continue
        view_box = root.attrib.get("viewBox", "").split()
        if view_box != ["0", "0", "1600", "900"]:
            failures.append(f"{asset.relative_to(ROOT)}: expected 1600x900 viewBox")
        if root.attrib.get("role") != "img" or "aria-labelledby" not in root.attrib:
            failures.append(f"{asset.relative_to(ROOT)}: missing accessible image role/labels")
        namespace = {"svg": "http://www.w3.org/2000/svg"}
        if root.find("svg:title", namespace) is None or root.find("svg:desc", namespace) is None:
            failures.append(f"{asset.relative_to(ROOT)}: missing title/desc")
    assert not failures, "SVG asset failures:\n" + "\n".join(failures)


def test_svg_visual_assets_use_japanese_readable_font_stack():
    failures = []
    expected = "Hiragino Sans, Yu Gothic, Arial, sans-serif"
    for asset in (ROOT / "assets").rglob("*.svg"):
        text = asset.read_text()
        font_stacks = re.findall(r'font-family="([^"]+)"', text)
        if not font_stacks:
            failures.append(f"{asset.relative_to(ROOT)}: no explicit font stack")
        elif any(stack != expected for stack in font_stacks):
            failures.append(f"{asset.relative_to(ROOT)}: inconsistent Japanese font stack")
    assert not failures, "SVG font failures:\n" + "\n".join(failures)


def test_first_third_study_guide_covers_core_abbreviations_and_domains():
    guide = (DOCS / "FIRST_THIRD_STUDY_GUIDE.md").read_text()
    for abbreviation in ("SpO₂", "ETCO₂", "ABG", "MAP", "CRT", "GCS", "ICP", "AKI", "CRRT"):
        assert f"| {abbreviation} |" in guide
    for domain in ("00_Fundamentals", "01_Airway", "02_Breathing", "03_Circulation", "04_Neurology", "05_Renal"):
        assert domain in guide


def test_completed_figure_index_files_exist():
    index = (ROOT / "FIGURE_INDEX.md").read_text()
    missing = []
    for target in re.findall(r"`(assets/[^`]+\.(?:svg|png))`", index):
        if not (ROOT / target).exists():
            missing.append(target)
    assert not missing, "Indexed figures missing:\n" + "\n".join(missing)


def test_figure_index_related_knowledge_pages_exist():
    index = (ROOT / "FIGURE_INDEX.md").read_text()
    missing = []
    for target in re.findall(r"`(docs/[^`]+\.md)`", index):
        if not (ROOT / target).exists():
            missing.append(target)
    assert not missing, "Indexed knowledge pages missing:\n" + "\n".join(missing)


def test_every_svg_is_registered_once_in_figure_index():
    index = (ROOT / "FIGURE_INDEX.md").read_text()
    indexed = re.findall(r"`(assets/[^`]+\.svg)`", index)
    actual = {str(path.relative_to(ROOT)) for path in (ROOT / "assets").rglob("*.svg")}
    assert len(indexed) == len(set(indexed)), "Figure Index contains duplicate SVG registrations"
    assert set(indexed) == actual, (
        "Figure Index / asset mismatch:\n"
        f"unindexed={sorted(actual - set(indexed))}\n"
        f"missing={sorted(set(indexed) - actual)}"
    )


def test_review_audit_has_no_pending_content_pages():
    pending = []
    for page in DOCS.rglob("*.md"):
        if "_templates" in page.parts or page.name == "README.md":
            continue
        text = page.read_text()
        if text.startswith("---\n") and not re.search(r"^status: reviewed$", text, re.MULTILINE):
            pending.append(str(page.relative_to(ROOT)))
    assert not pending, "Content pages not marked reviewed:\n" + "\n".join(pending)


def test_illustration_plan_covers_all_33_categories_without_residual_work():
    plan = (DOCS / "ILLUSTRATION_COVERAGE_PLAN.md").read_text()
    registered = {int(n) for n in re.findall(r"^\| (\d{2}) ", plan, re.MULTILINE)}
    assert registered == set(range(33))
    for marker in ("残課題", "拡充中", "順次同期", "監査対象", "更新監査"):
        assert marker not in plan


def test_raster_medical_illustrations_are_indexed_and_high_resolution():
    index = (ROOT / "FIGURE_INDEX.md").read_text()
    actual = {str(path.relative_to(ROOT)) for path in (ROOT / "assets").rglob("*.png")}
    indexed = set(re.findall(r"`(assets/[^`]+\.png)`", index))
    assert indexed == actual
    failures = []
    for target in sorted(actual):
        data = (ROOT / target).read_bytes()[:24]
        if data[:8] != b"\x89PNG\r\n\x1a\n":
            failures.append(f"{target}: invalid PNG signature")
            continue
        width, height = struct.unpack(">II", data[16:24])
        if width < 1200 or height < 800:
            failures.append(f"{target}: only {width}x{height}")
    assert not failures, "Raster illustration failures:\n" + "\n".join(failures)


def test_master_reference_phase1_audit_is_exhaustive():
    required = {
        "AUDIT_REPORT.md", "CONTENT_GAP_ANALYSIS.md", "VISUAL_AUDIT.md",
        "REFERENCE_AUDIT.md", "REVISION_ROADMAP.md",
        "HUMAN_REVIEW_REQUIRED.md", "REVISION_STATUS.md", "PHASE1_REPORT.md",
    }
    assert all((ROOT / name).exists() for name in required)
    audit = (ROOT / "AUDIT_REPORT.md").read_text()
    audited_files = set(re.findall(r"\| `(docs/[^`]+\.md)` \|", audit))
    expected_pages = {
        str(path.relative_to(ROOT))
        for path in DOCS.rglob("*.md")
        if "_templates" not in path.parts and path.name != "README.md" and path.read_text().startswith("---\n")
    }
    assert audited_files == expected_pages
    visual = (ROOT / "VISUAL_AUDIT.md").read_text()
    audited_assets = set(re.findall(r"`(assets/[^`]+\.(?:svg|png))`", visual))
    expected_assets = {str(path.relative_to(ROOT)) for path in (ROOT / "assets").rglob("*") if path.suffix in {".svg", ".png"}}
    assert audited_assets == expected_assets
    revision = (ROOT / "REVISION_STATUS.md").read_text()
    real_ssot = {
        str(path.relative_to(ROOT))
        for path in DOCS.rglob("*.md")
        if "_templates" not in path.parts and "\nssot: true\n" in path.read_text()
    }
    audited_ssot = set(re.findall(r"\| `(docs/[^`]+\.md)` \| Audited \|", revision))
    assert audited_ssot == real_ssot


def test_learning_asset_coverage_registers_all_twenty_domains():
    coverage = (DOCS / "LEARNING_ASSET_COVERAGE.md").read_text()
    registered = set(re.findall(r"^\| ([A-Z][A-Z0-9_]+) \|", coverage, re.MULTILINE))
    expected = {
        "AIRWAY", "BEDSIDE_SYSTEMS_NURSING", "CARDIAC_CRITICAL_CARE",
        "CRITICAL_CARE_FUNDAMENTALS", "ECMO_MCS", "ENDOCRINE_METABOLIC",
        "GI_LIVER_PANCREAS", "HEMATOLOGY", "HEMODYNAMICS",
        "INFECTION_CONTROL_PROCEDURES", "INFECTION_SEPSIS", "NEUROCRITICAL",
        "PADIS_REHAB_PICS", "PHARMACOLOGY_NUTRITION", "RENAL",
        "RESPIRATORY_PHYSIOLOGY_ABG", "RESPIRATORY_SUPPORT",
        "SHOCK_SEPTIC_SHOCK", "SPECIAL_TOXICOLOGY_SYSTEMS", "TRAUMA_BURNS",
    }
    assert registered == expected
