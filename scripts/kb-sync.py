#!/usr/bin/env python3
"""Generate mind map data from embedded @mindmap metadata in fundamentals.md.

Parses HTML comment blocks (<!-- @mindmap ... -->) from the knowledge base,
builds a hierarchical tree grouped by category, and outputs a JavaScript
data file for the D3.js mind map visualization.

Also validates consistency:
- Every topic with @mindmap has a valid category
- Every related: reference points to an existing topic name
- Every topic name is unique

Usage:
    python scripts/kb-sync.py              # Generate + validate
    python scripts/kb-sync.py --check-only # Validate without writing
    make kb-sync                           # Via Makefile
"""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
KB_FILE = REPO_ROOT / "knowledge-base" / "ml-ds-llm-fundamentals.md"
OUTPUT_JS = REPO_ROOT / "ml-knowledge-map-data.js"  # Root for GitHub Pages
OUTPUT_SLUGS_JS = REPO_ROOT / "docs-assets" / "js" / "map-slug-lookup.js"

# --- Parsing ---


def parse_categories(text: str) -> dict[str, str]:
    """Extract L1 category definitions from <!-- @categories ... --> block.

    Returns dict of {category_name: description}.
    """
    match = re.search(r"<!--\s*@categories\s*\n(.*?)-->", text, re.DOTALL)
    if not match:
        return {}
    categories = {}
    for line in match.group(1).strip().splitlines():
        line = line.strip()
        if not line:
            continue
        name, _, desc = line.partition(":")
        if desc:
            categories[name.strip()] = desc.strip()
    return categories


def parse_oneliner(section_text: str) -> str:
    """Extract **One-liner**: text from a topic section.

    Handles both formats: **One-liner**: (colon outside) and **One-liner:** (colon inside).
    """
    match = re.search(r"\*\*One-liner(?:\*\*:\s*|\*\*\s*:\s*|:\*\*\s*)(.+)", section_text)
    if match:
        return match.group(1).strip()
    return ""


def parse_mindmap_block(section_text: str) -> dict | None:
    """Extract and parse <!-- @mindmap ... --> block from a topic section.

    Returns dict with keys: name, category, related, children (or None if no block).
    """
    match = re.search(r"<!--\s*@mindmap\s*\n(.*?)-->", section_text, re.DOTALL)
    if not match:
        return None

    block = match.group(1)
    result = {"name": None, "category": None, "related": [], "children": []}

    in_children = False
    child_lines = []

    for line in block.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        if stripped.startswith("children:"):
            in_children = True
            # Check if there's content after "children:" on the same line
            rest = stripped[len("children:"):].strip()
            if rest:
                child_lines.append(line)
            continue

        if in_children:
            # Lines under children: are collected raw (preserving indentation)
            child_lines.append(line)
            continue

        # Key: value parsing for non-children fields
        key, _, value = stripped.partition(":")
        key = key.strip().lower()
        value = value.strip()

        if key == "name":
            result["name"] = value
        elif key == "category":
            result["category"] = value
        elif key == "related":
            result["related"] = [r.strip() for r in value.split(",") if r.strip()]

    if child_lines:
        result["children"] = parse_children(child_lines)

    return result


def parse_children(lines: list[str]) -> list[dict]:
    """Parse indented children lines into nested structure.

    2-space indent = L3 child
    4-space indent = L4 grandchild
    ~TopicName suffix = related link on that child
    """
    children = []

    for line in lines:
        # Determine indent level from the raw line
        stripped = line.lstrip()
        indent = len(line) - len(stripped)

        # Normalize indent: find the minimum indent to handle various base indents
        # We'll use relative indentation (2-space increments)
        if not stripped:
            continue

        # Parse name: description and optional ~Related suffix
        related = []
        text = stripped

        # Extract ~Related suffixes (can be multiple, space-separated at end)
        while "  ~" in text:
            text, _, ref = text.rpartition("  ~")
            related.insert(0, ref.strip())

        name, _, desc = text.partition(":")
        name = name.strip()
        desc = desc.strip()

        node = {"name": name, "desc": desc}
        if related:
            node["related"] = related

        # Determine nesting level based on indent
        # Base indent (first child) = L3, +2 spaces = L4
        if indent <= 2:
            # L3 child
            node["_level"] = 3
            children.append(node)
        else:
            # L4 grandchild — attach to last L3 child
            node["_level"] = 4
            if children:
                parent = children[-1]
                if "children" not in parent:
                    parent["children"] = []
                parent["children"].append(node)

    # Clean up internal _level markers
    for child in children:
        child.pop("_level", None)
        for grandchild in child.get("children", []):
            grandchild.pop("_level", None)

    return children


def parse_fundamentals(text: str) -> list[dict]:
    """Parse all topics from fundamentals.md.

    Returns list of topic dicts with: heading, name, desc, category, related, children.
    """
    topics = []

    # Split by H1 headings (# Topic)
    # Find all H1 heading positions
    heading_pattern = re.compile(r"^# (.+)$", re.MULTILINE)
    matches = list(heading_pattern.finditer(text))

    for i, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        section = text[start:end]

        mindmap = parse_mindmap_block(section)
        if mindmap is None:
            continue

        oneliner = parse_oneliner(section)

        topic = {
            "heading": heading,
            "name": mindmap["name"] or heading,
            "desc": oneliner,
            "category": mindmap["category"],
            "related": mindmap["related"],
            "children": mindmap["children"],
        }
        topics.append(topic)

    return topics


# --- Tree Building ---


def build_tree(categories: dict[str, str], topics: list[dict]) -> dict:
    """Build the hierarchical tree structure for the mind map.

    Root → L1 categories → L2 topics → L3/L4 children.
    """
    # Group topics by category
    cat_topics: dict[str, list[dict]] = {}
    for topic in topics:
        cat = topic["category"]
        if cat not in cat_topics:
            cat_topics[cat] = []
        cat_topics[cat].append(topic)

    # Build tree preserving category order from @categories block
    root_children = []
    for cat_name, cat_desc in categories.items():
        cat_node = {"name": cat_name, "desc": cat_desc, "children": []}

        for topic in cat_topics.get(cat_name, []):
            topic_node = {"name": topic["name"], "desc": topic["desc"]}
            if topic["related"]:
                topic_node["related"] = topic["related"]
            if topic["children"]:
                topic_node["children"] = topic["children"]
            cat_node["children"].append(topic_node)

        root_children.append(cat_node)

    return {
        "name": "ML/AI/DS",
        "desc": "Machine Learning, AI, Data Science & LLM Knowledge Base",
        "children": root_children,
    }


# --- Validation ---


def validate(
    categories: dict[str, str], topics: list[dict]
) -> tuple[list[str], list[str]]:
    """Validate consistency of parsed data.

    Returns (errors, warnings) — errors are fatal, warnings are informational.
    """
    errors = []
    warnings = []

    # Collect L2 topic names (must be unique)
    l2_names = set()
    for topic in topics:
        name = topic["name"]
        if name in l2_names:
            errors.append(f"Duplicate topic name: '{name}'")
        l2_names.add(name)

    # Collect all names (L2 + L3 + L4) for related ref validation
    all_names = set(l2_names)
    for topic in topics:
        for child in topic.get("children", []):
            all_names.add(child["name"])
            for grandchild in child.get("children", []):
                all_names.add(grandchild["name"])

    # Validate categories
    for topic in topics:
        if topic["category"] not in categories:
            errors.append(
                f"Topic '{topic['name']}' has unknown category: '{topic['category']}'"
            )

    # Validate related references
    for topic in topics:
        for ref in topic.get("related", []):
            if ref not in all_names:
                errors.append(
                    f"Topic '{topic['name']}' has unknown related ref: '{ref}'"
                )
        # Also check children's related refs
        for child in topic.get("children", []):
            for ref in child.get("related", []):
                if ref not in all_names:
                    errors.append(
                        f"Child '{child['name']}' (in '{topic['name']}') "
                        f"has unknown related ref: '{ref}'"
                    )

    # Check for topics without one-liner (warning, not error)
    for topic in topics:
        if not topic["desc"]:
            warnings.append(f"Topic '{topic['name']}' is missing **One-liner**:")

    return errors, warnings


# --- Output ---


def clean_for_json(node: dict) -> dict:
    """Remove empty optional fields for cleaner output."""
    cleaned = {"name": node["name"], "desc": node["desc"]}
    if node.get("related"):
        cleaned["related"] = node["related"]
    if node.get("children"):
        cleaned["children"] = [clean_for_json(c) for c in node["children"]]
    return cleaned


def heading_to_mkdocs_slug(heading: str) -> str:
    """Convert a markdown heading text to the slug MkDocs/toc would generate.

    Replicates Python-Markdown toc extension's slugify (used by MkDocs Material):
    lowercase → strip non-alphanum except hyphens/spaces → spaces to hyphens → collapse.
    """
    slug = heading.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    slug = slug.strip("-")
    return slug


def build_mkdocs_slug_map(text: str, topics: list[dict]) -> dict[str, str]:
    """Build heading → actual MkDocs slug map, accounting for duplicate IDs.

    MkDocs/toc appends _1, _2 etc. for duplicate slugs. We replicate this by
    scanning ALL headings (H1-H6) in document order to track slug collisions.

    To handle code blocks: we use a heuristic based on the structure of this
    specific markdown file — @mindmap topics are always H1 headings outside
    code blocks, while Python comments (#) inside code blocks are not headings.
    We track all H2-H6 subheadings that appear between @mindmap H1s as
    legitimate heading-generators for slug dedup purposes.
    """
    # Strategy: walk through the file, identify all headings that MkDocs would
    # render (i.e., NOT inside code blocks), track slug counts, and map each
    # @mindmap topic heading to its actual slug.
    #
    # Since perfect code-block tracking in raw markdown is fragile (unbalanced
    # fences, indented code, etc.), we use a structural heuristic:
    # - H1 headings with @mindmap blocks are always real headings
    # - H2-H6 headings between two @mindmap H1s are real subheadings
    # - We don't need to track H1s without @mindmap (they're rare)

    # First pass: find line numbers of all @mindmap topic H1 headings
    topic_lines = set()
    heading_pattern = re.compile(r"^# (.+)$", re.MULTILINE)
    for m in heading_pattern.finditer(text):
        line_num = text[:m.start()].count("\n") + 1
        heading = m.group(1).strip()
        # Check if this heading has a corresponding @mindmap topic
        for topic in topics:
            if topic["heading"] == heading:
                topic_lines.add(line_num)
                break

    # Second pass: collect ALL headings in document order, skip code blocks
    # Use a conservative heuristic: track backtick fences, but if we detect
    # an @mindmap H1 while "in code", force-reset (the content is authoritative)
    lines = text.splitlines()
    slug_counts: dict[str, int] = {}
    heading_to_slug: dict[int, str] = {}  # line_num → slug

    in_code = False
    open_fence_len = 0

    for i, line in enumerate(lines, 1):
        stripped = line.strip()

        # Fence tracking
        m = re.match(r"^(`{3,}|~{3,})", stripped)
        if m:
            fence_len = len(m.group(1))
            if not in_code:
                # Opening fence must have >= 3 chars and may have info string
                in_code = True
                open_fence_len = fence_len
            elif fence_len >= open_fence_len and re.match(r"^(`{3,}|~{3,})\s*$", stripped):
                # Closing fence: same char type, no trailing text
                in_code = False
            continue

        # Force-reset if we hit a known @mindmap H1 while "in code"
        # This handles cases where fence tracking drifted
        if in_code and i in topic_lines:
            in_code = False

        if in_code:
            continue

        # Check for heading
        hm = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if not hm:
            continue

        heading_text = hm.group(2).strip()
        base_slug = heading_to_mkdocs_slug(heading_text)
        count = slug_counts.get(base_slug, 0)
        actual_slug = base_slug if count == 0 else f"{base_slug}_{count}"
        slug_counts[base_slug] = count + 1
        heading_to_slug[i] = actual_slug

    # Map @mindmap topics to their slugs
    result = {}
    topic_line_map = {}
    for m in heading_pattern.finditer(text):
        line_num = text[:m.start()].count("\n") + 1
        topic_line_map[m.group(1).strip()] = line_num

    for topic in topics:
        line_num = topic_line_map.get(topic["heading"])
        if line_num and line_num in heading_to_slug:
            result[topic["heading"]] = heading_to_slug[line_num]

    return result


def generate_js(tree: dict) -> str:
    """Generate JavaScript file content from tree."""
    cleaned = clean_for_json(tree)
    json_str = json.dumps(cleaned, indent=2, ensure_ascii=False)

    return (
        "// AUTO-GENERATED by scripts/kb-sync.py from ml-ds-llm-fundamentals.md\n"
        "// Do not edit manually. Run: make kb-sync\n"
        f"const knowledgeMapData = {json_str};\n"
    )


def generate_slug_lookup_js(topics: list[dict], heading_slugs: dict[str, str]) -> str:
    """Generate slug ↔ node name lookup tables for docs ↔ mind map navigation.

    Two tables:
      mapSlugLookup:  heading-slug → node name (used by docs 🧠 links)
      mapNodeToSlug:  node name → heading-slug (used by mind map "Open in Docs")
    """
    slug_to_name = {}
    name_to_slug = {}
    for topic in topics:
        slug = heading_slugs.get(topic["heading"])
        if not slug:
            continue
        slug_to_name[slug] = topic["name"]
        name_to_slug[topic["name"]] = slug

    slug_json = json.dumps(slug_to_name, indent=2, ensure_ascii=False)
    node_json = json.dumps(name_to_slug, indent=2, ensure_ascii=False)
    return (
        "// AUTO-GENERATED by scripts/kb-sync.py — bidirectional slug ↔ node name lookup\n"
        "// Do not edit manually. Run: make kb-sync\n"
        f"const mapSlugLookup = {slug_json};\n"
        f"const mapNodeToSlug = {node_json};\n"
    )


# --- Main ---


def main():
    check_only = "--check-only" in sys.argv

    if not KB_FILE.exists():
        print(f"ERROR: {KB_FILE} not found")
        return 1

    text = KB_FILE.read_text(encoding="utf-8")

    # Parse
    categories = parse_categories(text)
    if not categories:
        print("ERROR: No <!-- @categories ... --> block found in fundamentals.md")
        return 1

    topics = parse_fundamentals(text)
    print(f"Parsed {len(topics)} topics across {len(categories)} categories")

    # Validate
    errors, warnings = validate(categories, topics)
    if warnings:
        print(f"\n{len(warnings)} warning(s):")
        for warn in warnings:
            print(f"  ⚠ {warn}")
    if errors:
        print(f"\n{len(errors)} validation error(s):")
        for err in errors:
            print(f"  ✗ {err}")
        return 1

    print("Validation passed")

    if check_only:
        return 0

    # Build tree and generate JS
    tree = build_tree(categories, topics)
    js_content = generate_js(tree)

    # Count nodes
    def count_nodes(node):
        total = 1
        for child in node.get("children", []):
            total += count_nodes(child)
        return total

    node_count = count_nodes(tree)

    OUTPUT_JS.write_text(js_content, encoding="utf-8")
    print(f"Generated {OUTPUT_JS.relative_to(REPO_ROOT)} ({node_count} nodes)")

    # Generate slug ↔ node name lookup for docs ↔ mind map navigation
    heading_slugs = build_mkdocs_slug_map(text, topics)
    slug_js = generate_slug_lookup_js(topics, heading_slugs)
    OUTPUT_SLUGS_JS.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_SLUGS_JS.write_text(slug_js, encoding="utf-8")
    print(f"Generated {OUTPUT_SLUGS_JS.relative_to(REPO_ROOT)} ({len(topics)} slugs)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
