#!/usr/bin/env python3
"""Pre-process Markdown files for Python-Markdown (MkDocs) compatibility.

Fixes two GFM-vs-Python-Markdown incompatibilities so authors can write
naturally (as they would for GitHub/VS Code) without worrying about
MkDocs rendering quirks:

1. Blank lines before lists/tables — Python-Markdown requires them;
   GFM doesn't. Applies to both top-level and blockquote-nested content.

2. GFM callouts → MkDocs admonitions — converts `> [!WARNING] text`
   to `!!! warning` blocks that MkDocs Material renders as styled boxes.

Run on staged _docs/ content, not on source files.
"""

import re
import sys
from pathlib import Path

# --- Blank-line-before-list/table fix ---

LIST_RE = re.compile(r"^(\s*[-*+]|\s*\d+[.)]) ")
TABLE_RE = re.compile(r"^\|.+\|")
SKIP_RE = re.compile(r"^(\s*[-*+]|\s*\d+[.)]) |^#{1,6} |^\s*$")

# Same patterns but inside blockquotes ("> " prefix)
BQ_LIST_RE = re.compile(r"^>\s+([-*+]|\d+[.)]) ")
BQ_TABLE_RE = re.compile(r"^>\s*\|.+\|")
BQ_SKIP_RE = re.compile(r"^>\s+([-*+]|\d+[.)]) |^>\s*$")


def needs_blank_line(prev: str, curr: str) -> bool:
    """Check if a blank line should be inserted before curr."""
    if not prev.strip():
        return False
    # Top-level: list after non-list, non-heading, non-blank
    if LIST_RE.match(curr) and not SKIP_RE.match(prev):
        return True
    # Top-level: table after non-table, non-blank
    if TABLE_RE.match(curr) and not TABLE_RE.match(prev):
        return True
    # Blockquote: list after non-list blockquote line
    if BQ_LIST_RE.match(curr) and prev.startswith(">") and not BQ_SKIP_RE.match(prev) and not BQ_LIST_RE.match(prev):
        return True
    # Blockquote: table after non-table blockquote line
    if BQ_TABLE_RE.match(curr) and prev.startswith(">") and not BQ_TABLE_RE.match(prev) and not prev.strip() == ">":
        return True
    return False


def make_blank_line(curr: str) -> str:
    """Return the right blank line — preserving blockquote prefix if needed."""
    if curr.startswith(">"):
        return ">\n"
    return "\n"


# --- GFM callout → MkDocs admonition conversion ---

# Mapping from GFM callout types to MkDocs admonition types
CALLOUT_MAP = {
    "NOTE": "note",
    "TIP": "tip",
    "IMPORTANT": "important",
    "WARNING": "warning",
    "CAUTION": "danger",
    "TODO": "tip",
    "SUMMARY": "abstract",
}

CALLOUT_RE = re.compile(r"^>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION|TODO|SUMMARY)\]\s*(.*)")


def convert_callouts(lines: list[str]) -> tuple[list[str], int]:
    """Convert GFM callout blocks to MkDocs admonition syntax."""
    out: list[str] = []
    conversions = 0
    i = 0

    while i < len(lines):
        m = CALLOUT_RE.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue

        callout_type = m.group(1)
        title_text = m.group(2).strip()
        adm_type = CALLOUT_MAP.get(callout_type, "note")
        conversions += 1

        # Build admonition header
        if title_text:
            # Clean up <br> at end of title
            title_text = re.sub(r"<br\s*/?>$", "", title_text).strip()
            out.append(f'!!! {adm_type} "{title_text}"\n')
        else:
            out.append(f"!!! {adm_type}\n")

        out.append("\n")  # Required blank line after admonition header

        # Collect continuation lines (start with "> ")
        i += 1
        while i < len(lines) and lines[i].startswith(">"):
            content = lines[i][1:]  # Strip leading ">"
            # Strip one leading space if present ("> content" → "content")
            if content.startswith(" "):
                content = content[1:]
            # Indent with 4 spaces for admonition body
            if content.strip():
                out.append("    " + content)
            else:
                out.append("\n")
            i += 1

        # Ensure blank line after admonition block
        if out and out[-1].strip():
            out.append("\n")

    return out, conversions


def fix_file(path: Path) -> tuple[int, int]:
    """Fix a single markdown file. Returns (blank_line_insertions, callout_conversions)."""
    lines = path.read_text().splitlines(keepends=True)

    # Step 1: Convert GFM callouts to MkDocs admonitions
    lines, callout_count = convert_callouts(lines)

    # Step 2: Insert blank lines before lists/tables
    out: list[str] = []
    insertions = 0

    for i, line in enumerate(lines):
        if i > 0 and needs_blank_line(lines[i - 1], line):
            out.append(make_blank_line(line))
            insertions += 1
        out.append(line)

    if insertions or callout_count:
        path.write_text("".join(out))
    return insertions, callout_count


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <dir>")
        sys.exit(1)

    root = Path(sys.argv[1])
    total_blanks = 0
    total_callouts = 0
    for md in sorted(root.rglob("*.md")):
        blanks, callouts = fix_file(md)
        total_blanks += blanks
        total_callouts += callouts

    parts = []
    if total_blanks:
        parts.append(f"{total_blanks} blank lines before lists/tables")
    if total_callouts:
        parts.append(f"{total_callouts} GFM callouts → MkDocs admonitions")
    if parts:
        print(f"Fixed: {', '.join(parts)} in {root}")


if __name__ == "__main__":
    main()
