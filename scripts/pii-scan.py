#!/usr/bin/env python3
"""
PII & Confidential Term Scanner.

Scans all text files in the repository for confidential terms defined in
an external config file (scripts/.pii-terms.json). The config is gitignored —
copy from .pii-terms.example.json and fill in your own terms.

Usage:
    python scripts/pii-scan.py [--path <dir>]  # defaults to repo root
    python scripts/pii-scan.py --strict        # exit code 1 on ANY hit (critical or warning)
    python scripts/pii-scan.py --config <file> # custom config file

Exit codes:
    0 — no critical hits (warnings may exist)
    1 — critical hits found (must fix before publishing)
    2 — config file not found
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ─── Defaults ─────────────────────────────────────────────────────────────────

DEFAULT_CONFIG = Path(__file__).parent / ".pii-terms.json"

SCAN_EXTENSIONS = {".md", ".py", ".js", ".html", ".txt", ".yaml", ".yml", ".json", ".toml"}

EXCLUDE_DIRS = {
    ".git", ".venv", "__pycache__", "node_modules", "_docs", "_site", "_serve",
    ".ipynb_checkpoints", ".DS_Store",
}


# ─── Config Loading ──────────────────────────────────────────────────────────

def load_config(config_path: Path) -> dict:
    """Load scan terms from JSON config file."""
    if not config_path.exists():
        print(f"\n\033[31mError: Config file not found: {config_path}\033[0m")
        print(f"Copy from .pii-terms.example.json and customize:\n")
        print(f"  cp scripts/.pii-terms.example.json scripts/.pii-terms.json\n")
        sys.exit(2)

    with open(config_path) as f:
        return json.load(f)


# ─── Scanner ─────────────────────────────────────────────────────────────────

def should_skip_file(filepath: Path, skip_files: set) -> bool:
    """Check if file should be entirely skipped."""
    return filepath.name in skip_files


def is_allowlisted(filepath: Path, term: str, allowlist: dict) -> bool:
    """Check if a specific term is expected in this file."""
    fname = filepath.name
    if fname in allowlist:
        allowed = allowlist[fname]
        return term.lower() in {t.lower() for t in allowed}
    return False


def scan_file(filepath: Path, config: dict) -> list[dict]:
    """Scan a single file for PII/confidential terms."""
    hits = []
    skip_files = set(config.get("skip_files", []))
    allowlist = config.get("allowlist", {})

    if should_skip_file(filepath, skip_files):
        return hits

    try:
        content = filepath.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        return hits

    lines = content.splitlines()
    critical_terms = set(config.get("critical_terms", []))
    case_sensitive_terms = set(config.get("case_sensitive_critical", []))
    warning_terms = set(config.get("warning_terms", []))
    regex_patterns = config.get("critical_regex", [])

    for line_num, line in enumerate(lines, start=1):
        line_lower = line.lower()

        # Case-insensitive critical terms
        for term in critical_terms:
            if term.lower() in line_lower:
                if not is_allowlisted(filepath, term, allowlist):
                    hits.append({
                        "file": str(filepath),
                        "line": line_num,
                        "term": term,
                        "severity": "CRITICAL",
                        "context": line.strip()[:120],
                    })

        # Case-sensitive critical terms
        for term in case_sensitive_terms:
            if term in line:
                if not is_allowlisted(filepath, term, allowlist):
                    hits.append({
                        "file": str(filepath),
                        "line": line_num,
                        "term": term,
                        "severity": "CRITICAL",
                        "context": line.strip()[:120],
                    })

        # Regex patterns
        for entry in regex_patterns:
            pattern = entry["pattern"]
            description = entry["description"]
            if re.search(pattern, line, re.IGNORECASE):
                if not is_allowlisted(filepath, description, allowlist):
                    hits.append({
                        "file": str(filepath),
                        "line": line_num,
                        "term": f"[regex] {description}",
                        "severity": "CRITICAL",
                        "context": line.strip()[:120],
                    })

        # Warning terms
        for term in warning_terms:
            if term.lower() in line_lower:
                hits.append({
                    "file": str(filepath),
                    "line": line_num,
                    "term": term,
                    "severity": "WARNING",
                    "context": line.strip()[:120],
                })

    return hits


def scan_directory(root: Path, config: dict) -> list[dict]:
    """Scan all text files in directory recursively."""
    all_hits = []

    for filepath in sorted(root.rglob("*")):
        if any(part in EXCLUDE_DIRS for part in filepath.parts):
            continue
        if not filepath.is_file():
            continue
        if filepath.suffix not in SCAN_EXTENSIONS:
            continue

        all_hits.extend(scan_file(filepath, config))

    return all_hits


# ─── Output ──────────────────────────────────────────────────────────────────

def print_results(hits: list[dict], root: Path) -> tuple[int, int]:
    """Print scan results grouped by severity. Returns (critical_count, warning_count)."""
    critical = [h for h in hits if h["severity"] == "CRITICAL"]
    warnings = [h for h in hits if h["severity"] == "WARNING"]

    if not hits:
        print("\n\033[32m✅ CLEAN — No PII or confidential terms detected.\033[0m\n")
        return 0, 0

    if critical:
        print(f"\n\033[31m{'='*70}")
        print(f"  CRITICAL HITS: {len(critical)}")
        print(f"{'='*70}\033[0m\n")

        current_file = None
        for h in sorted(critical, key=lambda x: (x["file"], x["line"])):
            rel_path = str(Path(h["file"]).relative_to(root))
            if rel_path != current_file:
                current_file = rel_path
                print(f"\033[1m  {rel_path}\033[0m")
            print(f"    L{h['line']:>5}  [{h['term']}]")
            print(f"           {h['context']}")
            print()

    if warnings:
        print(f"\n\033[33m{'='*70}")
        print(f"  WARNINGS: {len(warnings)}")
        print(f"{'='*70}\033[0m\n")

        current_file = None
        for h in sorted(warnings, key=lambda x: (x["file"], x["line"])):
            rel_path = str(Path(h["file"]).relative_to(root))
            if rel_path != current_file:
                current_file = rel_path
                print(f"\033[1m  {rel_path}\033[0m")
            print(f"    L{h['line']:>5}  [{h['term']}]")
            print(f"           {h['context']}")
            print()

    print(f"\n{'─'*70}")
    print(f"  Summary: \033[31m{len(critical)} critical\033[0m | \033[33m{len(warnings)} warnings\033[0m")
    print(f"{'─'*70}\n")

    return len(critical), len(warnings)


def main():
    parser = argparse.ArgumentParser(description="Scan for PII and confidential terms")
    parser.add_argument("--path", type=Path, default=Path(__file__).parent.parent,
                        help="Directory to scan (default: repo root)")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG,
                        help="Path to JSON config file (default: scripts/.pii-terms.json)")
    parser.add_argument("--strict", action="store_true",
                        help="Exit code 1 on any hit (critical or warning)")
    args = parser.parse_args()

    config = load_config(args.config)
    root = args.path.resolve()
    print(f"\n🔍 Scanning {root} for PII/confidential terms...\n")

    hits = scan_directory(root, config)
    critical_count, warning_count = print_results(hits, root)

    if critical_count > 0:
        sys.exit(1)
    if args.strict and warning_count > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
