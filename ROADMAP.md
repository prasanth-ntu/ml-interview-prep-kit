# Roadmap

> Future improvements, feature ideas, and open questions for the ML Interview Prep Kit.
> Contributions and discussion welcome — [open an issue](https://github.com/prasanth-ntu/ml-interview-prep-kit/issues) or submit a PR.

---

## Features & Enhancements

### Progress Tracking
- [ ] Add a progress tracker (inspired by `mission.html` panel stats) — should it be part of mind map `@mindmap` metadata, a separate config file, or localStorage-based?
- [ ] Handle progress for modules outside the mind map (System Design, Coding Practice, Career Frameworks, etc.)
- [ ] Consider a unified "completion state" data model across all overview prototypes

### JD-Specific Resume Tools
- [ ] Resume generator/modifier that takes a job description and tailors content from the knowledge base
- [ ] AI prompt template for JD-to-resume alignment
- [ ] LaTeX resume generator — produce a polished, ATS-friendly PDF resume from knowledge base content and a given JD

### Research Papers Section
- [ ] Add a section for reading and summarizing research papers
- [ ] Decide: separate top-level folder (`research-papers/`) or nested under `knowledge-base/`?
- [ ] Template for paper summaries (title, key contributions, relevance to interviews, link)

### Cross-Section Navigation
- [ ] Enable hyperlinking from one folder's content to another in mind maps, Bento/Skill Tree/Mission overviews
- [ ] Make transitions seamless between mind map nodes and docs pages, and between overview prototypes
- [ ] Unified deep-link scheme (e.g., `?focus=NodeName` already works for mind map — extend to other views)

---

## Bug Fixes

### Mind Map
- [ ] When switching between Radial and Tree layout, the current depth focus (L1/L2/L3) is not retained — the view resets instead of preserving the active depth level

### MkDocs Rendering
- [ ] Fix LaTeX rendering issues with `$$ $$` delimiters in MkDocs
- [ ] Audit and fix other rendering edge cases (nested lists, complex tables, admonition nesting)

---

## Branding & Design

### Identity
- [ ] Finalize a solid repo name, title, and logo
- [ ] Create a standardized color palette, font system, and design tokens shared across all pages (mind map, docs, prototypes)
- [ ] Ensure consistent theme (light/dark) behavior across all entry points

---

## Architecture & Tooling

### Documentation Platform
- [ ] Evaluate Quartz (Obsidian-based) vs. MkDocs Material (currently used)
  - MkDocs: mature plugin ecosystem, Material theme, instant navigation, search
  - Quartz: native Obsidian vault support, graph view, backlinks, wikilinks
  - Key question: does the team use Obsidian for authoring? If so, Quartz reduces friction

### Reference Implementations
- [ ] Study [AI Engineering from Scratch](https://rohitg00.github.io/ai-engineering-from-scratch/) for inspiration on:
  - Content structure and topic organization
  - UI/UX patterns and navigation design
  - Codebase architecture and build system
  - Evaluate which patterns could improve this repo

### Overview Prototypes
- [ ] Pick a winning prototype (Bento Grid, Skill Tree, or Mission Control) or combine elements
- [ ] Integrate winner into the build system and deploy to `interview.prasanth.io/overview/`
- [ ] Add "Overview" nav link to mind map top bar

---

*Last updated: 2026-03-29*
