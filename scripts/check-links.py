#!/usr/bin/env python3
"""Check for broken internal markdown links across the repository.

Finds all .md files, extracts relative markdown links, resolves them,
and reports any that point to non-existent files or missing headings.

Usage:
    python scripts/check-links.py [--fix]
    make check-links
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_DIRS = {".git", ".venv", "node_modules", "__pycache__", ".github", "_docs", "_site"}
EXCLUDE_PATTERNS = {"_templates", "_example-company"}  # Templates have placeholder links

# Matches markdown links like [text](path) but NOT external URLs
LINK_PATTERN = re.compile(r"\[([^\]]*)\]\((?!https?://|mailto:)([^)]+)\)")


def find_md_files() -> list[Path]:
    """Find all markdown files in the repo, excluding certain directories."""
    md_files = []
    all_excludes = EXCLUDE_DIRS | EXCLUDE_PATTERNS
    for path in REPO_ROOT.rglob("*.md"):
        if not any(part in all_excludes for part in path.parts):
            md_files.append(path)
    return sorted(md_files)


def extract_links(file_path: Path) -> list[tuple[int, str, str]]:
    """Extract all internal markdown links from a file.

    Skips links inside fenced code blocks and template placeholders.
    Returns list of (line_number, display_text, link_target).
    """
    links = []
    text = file_path.read_text(encoding="utf-8", errors="replace")
    in_code_block = False

    for i, line in enumerate(text.splitlines(), start=1):
        # Track fenced code blocks
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        # Strip inline code spans before matching links
        # This prevents matching links inside backtick-wrapped examples like `[text](path)`
        line_no_inline_code = re.sub(r"`[^`]+`", "", line)

        for match in LINK_PATTERN.finditer(line_no_inline_code):
            display_text, target = match.group(1), match.group(2)

            # Skip template placeholders containing { or }
            if "{" in target or "}" in target:
                continue
            # Skip obvious placeholder targets
            if target in ("url", "URL", "link", "path"):
                continue
            # Skip Google Docs bookmark anchors (imported documents)
            if "bookmark=" in target:
                continue

            links.append((i, display_text, target))
    return links


def extract_headings(file_path: Path) -> set[str]:
    """Extract all markdown heading anchors from a file.

    Converts headings to GitHub-style anchors:
    '## My Heading (with stuff)' -> 'my-heading-with-stuff'
    """
    headings = set()
    text = file_path.read_text(encoding="utf-8", errors="replace")
    for line in text.splitlines():
        match = re.match(r"^#{1,6}\s+(.+)$", line)
        if match:
            heading = match.group(1).strip()
            # GitHub-style anchor conversion
            # 1. Lowercase
            anchor = heading.lower()
            # 2. Remove everything except alphanumeric, spaces, hyphens
            anchor = re.sub(r"[^\w\s-]", "", anchor)
            # 3. Replace each space with a hyphen individually (do NOT collapse —
            #    GitHub preserves double hyphens, e.g., "CI/CD & MLOps" → "cicd--mlops")
            anchor = anchor.replace(" ", "-")
            anchor = anchor.strip("-")
            headings.add(anchor)
    return headings


def validate_link(
    source_file: Path, target: str
) -> tuple[bool, str]:
    """Validate a single link target relative to its source file.

    Args:
        source_file: The .md file containing the link
        target: The raw link target (e.g., "../prep/tracker.md#section")

    Returns:
        (is_valid, error_message) — (True, "") if valid, (False, reason) if broken
    """
    # Split target into file path and optional anchor
    if "#" in target:
        file_part, anchor = target.split("#", 1)
    else:
        file_part, anchor = target, None

    # Pure anchor links (same file)
    if not file_part:
        if anchor:
            headings = extract_headings(source_file)
            if anchor not in headings:
                return False, f"anchor #{anchor} not found in same file"
        return True, ""

    # Resolve relative path from source file's directory
    resolved = (source_file.parent / file_part).resolve()

    # Check file/directory existence
    if not resolved.exists():
        return False, f"file not found: {file_part}"

    # If anchor specified and target is a file, check heading exists
    if anchor and resolved.is_file() and resolved.suffix == ".md":
        headings = extract_headings(resolved)
        if anchor not in headings:
            return False, f"anchor #{anchor} not found in {file_part}"

    return True, ""


def main():
    fix_mode = "--fix" in sys.argv

    md_files = find_md_files()
    broken_links: list[tuple[Path, int, str, str, str]] = []

    for file_path in md_files:
        links = extract_links(file_path)
        for line_num, display_text, target in links:
            is_valid, error = validate_link(file_path, target)
            if not is_valid:
                rel_path = file_path.relative_to(REPO_ROOT)
                broken_links.append((rel_path, line_num, display_text, target, error))

    if not broken_links:
        print(f"All links valid across {len(md_files)} markdown files.")
        return 0

    # Report
    print(f"\nBroken links found ({len(broken_links)}):\n")
    print(f"{'File':<55} {'Line':>5}  {'Error'}")
    print("-" * 100)
    for rel_path, line_num, display_text, target, error in broken_links:
        print(f"{str(rel_path):<55} {line_num:>5}  {error}")
        if display_text:
            print(f"{'':>55} {'':>5}  [{display_text}]({target})")

    print(f"\n{len(broken_links)} broken link(s) in {len(md_files)} files.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
