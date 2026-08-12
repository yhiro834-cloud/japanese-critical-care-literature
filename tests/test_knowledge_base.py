import re
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
