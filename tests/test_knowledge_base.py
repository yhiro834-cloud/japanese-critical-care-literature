import re
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
