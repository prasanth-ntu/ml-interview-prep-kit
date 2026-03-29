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

### Reference Implementations & Competitive Research
- [ ] Study [AI Engineering from Scratch](https://rohitg00.github.io/ai-engineering-from-scratch/) for inspiration on:
  - Content structure and topic organization
  - UI/UX patterns and navigation design
  - Codebase architecture and build system
  - Evaluate which patterns could improve this repo
- [ ] Survey similar repos, platforms, websites, and tools in the ML/DS interview prep space
  - Catalog what they do well (content depth, UX, interactivity, community, AI features)
  - Identify gaps and opportunities we can differentiate on
  - Draw inspiration across all aspects: content, design, architecture, engagement model

### Architecture & Modularity Review
- [ ] Audit the current repo architecture for modularity, scalability, extensibility, and collaboration-readiness
  - Is the folder structure, build pipeline, and content model set up for easy contribution by others?
  - Do we need formal data models (e.g., structured schemas for topics, progress, user state)?
  - Should we adopt specific architectural principles or frameworks (e.g., component-based design, plugin architecture, monorepo tooling)?
- [ ] Define a target architecture that is future-proof
  - Separation of content, presentation, and logic layers
  - Standardized data formats (JSON/YAML schemas for topics, metadata, progress)
  - Clear extension points for new sections, tools, and integrations

### AI Integration Strategy
- [ ] Decide the core AI delivery model — this is a fundamental design question:
  - **Local/agent mode**: Users clone the repo and use it with their own AI agents (Claude Code, Copilot, etc.) locally. Simpler to build, no hosting costs, full user control.
  - **Web-hosted mode**: AI features embedded in the deployed website (chat, JD analysis, resume gen, adaptive quizzing). Requires hosting, backend infra, database, auth, and cost management.
  - **Hybrid**: Static site for content + optional local AI workflows (prompt templates, agent configs) that users run on their own machines. Avoids hosting complexity while still being AI-native.
- [ ] Evaluate trade-offs for each model:
  - Web: editing, persistence, scalability, hosting costs, database needs, user auth
  - Local: onboarding friction, dependency on user's local setup, harder to provide seamless UX
  - Hybrid: best of both? Or worst of both?
- [ ] If web-hosted AI features are pursued, scope the infra requirements:
  - Backend (serverless functions vs. dedicated server)
  - Database (user state, progress, generated content)
  - API key management and cost controls
  - Scalability and rate limiting

### Overview Prototypes
- [ ] Pick a winning prototype (Bento Grid, Skill Tree, or Mission Control) or combine elements
- [ ] Integrate winner into the build system and deploy to `interview.prasanth.io/overview/`
- [ ] Add "Overview" nav link to mind map top bar

---

*Last updated: 2026-03-29*
