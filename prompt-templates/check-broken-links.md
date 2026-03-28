# Check Broken Links

> Copy this prompt into your AI assistant (Claude, ChatGPT, Gemini, Cursor, etc.)

## When to Use

After renaming, moving, or deleting files in your interview prep repository. Also useful as a periodic health check to ensure all internal markdown links still work.

## Prompt

```
Scan my markdown files for broken internal links.

## Repository Root

{your-repo}/

## Your Tasks

1. **Find all markdown files** in the repository (excluding .git/, .venv/, node_modules/, and template directories).

2. **Extract all internal links** from each file:
   - Relative file links: `[text](path/to/file.md)`
   - Anchor links: `[text](#heading-anchor)`
   - Combined: `[text](path/to/file.md#heading-anchor)`
   - Skip external URLs (http/https)
   - Skip links inside fenced code blocks

3. **Validate each link**:
   - For file references: Does the target file exist at the resolved path?
   - For anchor references: Does the target heading exist in the target file?

4. **Report results**:
   - List all broken links grouped by source file
   - For each broken link, suggest the likely fix:
     - File exists at a different path → suggest the correct path
     - Heading was renamed → suggest the closest matching heading
     - File was deleted → flag for manual review

5. **Summary**: Total files scanned, total links checked, total broken links found.

## Important Rules

- Resolve relative paths from the source file's directory, not the repo root
- Handle both `[text](path)` and `[text](path "title")` formats
- Markdown heading anchors follow GitHub conventions: lowercase, spaces→hyphens, strip special characters
- Don't flag template placeholders like `{company-name}` as broken links
```

## Example Usage

**Input**: Point the AI at your repository root directory.

**Output**: A report listing all broken internal links with suggested fixes, plus a summary of total files and links scanned. Run this after any file restructuring to catch stale references.

## Alternative: Script-Based Approach

If you prefer an automated script over an AI prompt, here's a Python approach:

```python
"""
Broken link checker for markdown repositories.
Usage: python check_links.py /path/to/repo
"""
import os
import re
import sys
from pathlib import Path

def find_markdown_files(root):
    skip = {'.git', '.venv', 'node_modules', '_templates'}
    for path in Path(root).rglob('*.md'):
        if not any(part in path.parts for part in skip):
            yield path

def extract_links(filepath):
    content = filepath.read_text(encoding='utf-8')
    # Skip fenced code blocks
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    # Find markdown links (skip external URLs)
    for match in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)', content):
        target = match.group(2).split(' ')[0]  # strip title
        if not target.startswith(('http://', 'https://', 'mailto:')):
            yield target

def heading_to_anchor(heading):
    anchor = heading.lower().strip()
    anchor = re.sub(r'[^\w\s-]', '', anchor)
    anchor = re.sub(r'\s+', '-', anchor)
    return anchor

if __name__ == '__main__':
    root = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    broken = []
    for md_file in find_markdown_files(root):
        for link in extract_links(md_file):
            file_part, _, anchor = link.partition('#')
            if file_part:
                target = (md_file.parent / file_part).resolve()
                if not target.exists():
                    broken.append((md_file, link, 'file not found'))
                    continue
            # Check anchor if present
            if anchor:
                target_file = (md_file.parent / file_part).resolve() if file_part else md_file
                if target_file.exists():
                    content = target_file.read_text(encoding='utf-8')
                    headings = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
                    anchors = [heading_to_anchor(h) for h in headings]
                    if anchor not in anchors:
                        broken.append((md_file, link, 'anchor not found'))

    for source, link, reason in broken:
        print(f"  {source.relative_to(root)}: [{link}] — {reason}")
    print(f"\nTotal broken: {len(broken)}")
```
