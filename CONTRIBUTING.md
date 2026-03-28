# Contributing to ML Interview Prep Kit

Thanks for your interest in contributing! This project aims to be a comprehensive, community-driven resource for ML/AI/DS interview preparation.

## How to Contribute

### Knowledge Base Topics

The knowledge base ([ml-ds-llm-fundamentals.md](knowledge-base/ml-ds-llm-fundamentals.md)) is the core of this project. To add a new topic:

1. Add a `# Topic Name` heading with `<!-- @mindmap -->` metadata block
2. Include a `**One-liner**:` summary
3. Follow the two-layer structure: quick reference tables + detailed explanation
4. Run `make kb-sync` to validate and regenerate the mind map

Example structure:
```markdown
# Your Topic Name
<!-- @mindmap
name: Short Name
category: ML Foundations
related: Related Topic 1, Related Topic 2
children:
  Subtopic 1: Brief description
  Subtopic 2: Brief description
-->

**One-liner**: A concise definition of the topic.

| Concept | Description |
|---------|-------------|
| ...     | ...         |

## Detailed Explanation
...
```

### Coding Practice

Add solutions to `coding-practice/by-platform/leetcode/{difficulty}/`. Use the template at `coding-practice/templates/problem-template.py`.

### System Design Walkthroughs

Add new system design scenarios to `system-design/`. Follow the template at `system-design/template.md`.

## Guidelines

- **No personal information**: Don't include real company names, salary figures, or identifying details
- **Run validation**: Always run `make validate` before submitting
- **Keep it practical**: Focus on interview-relevant content with ready-to-speak phrasing
- **One topic per PR**: Makes review easier

## Development Setup

```bash
# Clone the repo
gh repo fork prasanth-ntu/ml-interview-prep-kit --clone
cd ml-interview-prep-kit

# Run validation
make validate

# View mind map locally
make mindmap
```

## Contributors

- [Prasanth](https://github.com/prasanth-ntu) — Knowledge base, mind map, templates, tooling
