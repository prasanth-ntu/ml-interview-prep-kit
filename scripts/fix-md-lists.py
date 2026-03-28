#!/usr/bin/env python3
"""Pre-process Markdown files for Python-Markdown compatibility.

Python-Markdown requires a blank line before lists and tables that follow
a paragraph. Most editors (VS Code, GitHub) use GFM which doesn't require this.

This script inserts blank lines where needed so authors don't have to remember
the rule. Run on staged _docs/ content, not on source files.
"""

import re
import sys
from pathlib import Path

LIST_RE = re.compile(r"^(\s*[-*+]|\s*\d+[.)]) ")
TABLE_RE = re.compile(r"^\|.+\|")
SKIP_RE = re.compile(r"^(\s*[-*+]|\s*\d+[.)]) |^#{1,6} |^\s*$")


def needs_blank_line(prev: str, curr: str) -> bool:
    """Check if a blank line should be inserted before curr."""
    if not prev.strip():
        return False
    # List after non-list, non-heading, non-blank
    if LIST_RE.match(curr) and not SKIP_RE.match(prev):
        return True
    # Table after non-table, non-blank
    if TABLE_RE.match(curr) and not TABLE_RE.match(prev):
        return True
    return False


def fix_file(path: Path) -> int:
    lines = path.read_text().splitlines(keepends=True)
    out: list[str] = []
    insertions = 0

    for i, line in enumerate(lines):
        if i > 0 and needs_blank_line(lines[i - 1], line):
            out.append("\n")
            insertions += 1
        out.append(line)

    if insertions:
        path.write_text("".join(out))
    return insertions


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <dir>")
        sys.exit(1)

    root = Path(sys.argv[1])
    total = 0
    for md in sorted(root.rglob("*.md")):
        n = fix_file(md)
        if n:
            total += n

    if total:
        print(f"Inserted {total} blank lines before lists/tables in {root}")


if __name__ == "__main__":
    main()
