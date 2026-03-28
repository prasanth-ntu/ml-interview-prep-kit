# Interview Tracking Folder Structure Guide

> **Purpose**: Documents the structural decisions for the `interview-tracking/` folder. Reference this when adding new companies or maintaining existing ones.

---

## Design Decisions

### Decision 1: Round File Consolidation

| Decision | Single file per round |
|----------|----------------------|
| **Pattern** | `rounds/R{n}-{type}.md` |
| **Reasoning** | A round is one event. Prep, interview, and review are *phases* of that event, not separate entities. Keeping them together tells the complete story. |

**Benefits:**
- Metadata (date, interviewer, duration) written once, not repeated
- Complete context in one scroll
- Natural chronological flow: prep → interview notes → review

**File Structure:**
```markdown
# R{n} - {Type} Interview

## Metadata
| Field | Value |
|-------|-------|
| Date | YYYY-MM-DD |
| Duration | X min |
| Interviewer | Name - Title |
| Format | Video/Onsite |

---

## Pre-Interview Prep
[Interviewer research, key points, questions to ask]

---

## Interview Notes
[Live notes during interview]

---

## Post-Interview Review
### What Went Well
### Areas for Improvement
### Action Items
### Next Steps
```

---

### Decision 2: Prep Tracker Location

| Decision | `prep/tracker.md` |
|----------|------------------|
| **Pattern** | Dedicated `prep/` folder |
| **Reasoning** | Tracker is *meta-information about preparation*, not interview content. Separation of concerns keeps README clean. |

**Benefits:**
- README stays a dashboard (status + links)
- `prep/` folder can also hold study materials, quick references
- Clear separation: `rounds/` = what happened, `prep/` = how ready am I

---

### Decision 3: README as Status Dashboard

| Decision | README contains status only |
|----------|----------------------------|
| **Contains** | Status table, interview progress, next actions, links to files |
| **Does NOT contain** | Company overview, JD summary, role details, prep content |

**Why:**
- Reduces duplication (role details live in `research.md`)
- README becomes a navigation hub, not a content dump
- Quick glance shows "where am I?" not "what is this company?"

---

### Decision 4: Single Source of Truth

| Information | Canonical Location | Other files... |
|-------------|-------------------|----------------|
| Job description | `artifacts/jd.md` | Reference via link |
| Resume | `artifacts/resume.pdf` | Not duplicated |
| Transcripts | `artifacts/R{n}-transcript.txt` | Not duplicated |
| Company research | `research.md` | Reference via link |
| Interview process (intel) | `research.md` | Duration, focus, format |
| Interview progress (status) | `README.md` | Date, status, file links |
| Interview metadata | `rounds/R{n}-{type}.md` | Not duplicated |
| Prep status | `prep/tracker.md` | Not duplicated |

**DRY Principle:**
- Each piece of information lives in ONE file
- Other files link to it, never copy it
- Updates happen in one place

---

### Decision 5: Artifacts vs Dynamic Content

| Decision | Separate `artifacts/` folder for static inputs |
|----------|-----------------------------------------------|
| **Pattern** | `artifacts/` holds JD, resume, transcripts — things that don't change |
| **Reasoning** | Static inputs are *source data*. Research and prep are *derived work*. Separating them clarifies what changes vs. what's fixed. |

**What goes in `artifacts/`:**
- `jd.md` — Job description (verbatim copy)
- `resume.pdf` — Resume submitted for this application
- `official-*.pdf` — Prep guides from the company (high credibility)
- `R{n}-transcript.txt` — Interview transcripts
- `_low-credibility-*.md` — Flagged external sources (low credibility)

**What stays outside:**
- `research.md` — Your analysis and synthesis (dynamic)
- `prep/` — Your study materials (dynamic)
- `rounds/` — Your interview notes and reviews (dynamic)

---

### Decision 6: Interview Tables Separation

| Decision | README tracks progress, research.md describes process |
|----------|------------------------------------------------------|
| **Pattern** | Two tables with different columns, no overlap |
| **Reasoning** | Status is *tracking data* (changes after each interview). Format is *intel* (static research). |

**README.md — "Where am I?"**
```markdown
| Round | Type | Date | Status | File |
```

**research.md — "What should I expect?"**
```markdown
| Round | Type | Duration | Focus |
```

**Why no Status column in research.md:**
- Avoids duplicate updates after each interview
- research.md stays focused on intel for prep
- README is the single source for progress tracking

---

### Decision 7: Prep File Consolidation

| Decision | ONE tracker + ONE quickref per company |
|----------|----------------------------------------|
| **Pattern** | `prep/tracker.md` = single rolling file, `prep/quickref.md` = single merged study material |
| **Reasoning** | Per-round tracker files cause file bloat. One file per purpose, with `## R{n} Prep` sections per round. |

**Rules:**
- `prep/tracker.md` — ALL rounds tracked in ONE file. Never create per-round trackers
- `prep/quickref.md` — ALL study material in ONE file, organized by topic area (not by round)
- Additional domain-specific references (e.g., `system-architecture.md`) may be separate files
- Templates: [`_templates/prep-tracker-template.md`](_templates/prep-tracker-template.md), [`_templates/quickref-template.md`](_templates/quickref-template.md)

---

### Decision 8: Cross-Round Postmortem

| Decision | After all rounds complete → `rounds/postmortem.md` |
|----------|-----------------------------------------------------|
| **Pattern** | Separate synthesis document for cross-round analysis |
| **Reasoning** | README must stay a dashboard (Decision 3). Post-interview analysis is derived content that grows over time and deserves its own file. |

**What goes in postmortem:**
- Round-by-round summary scores (labeled as LLM estimates)
- Format predictability analysis (expected vs actual)
- Consolidated pass likelihood (labeled as LLM estimate)
- Cross-round patterns and lessons
- Transferable action items

**Template**: [`_templates/postmortem-template.md`](_templates/postmortem-template.md)

---

### Decision 9: Transcript Sources

| Decision | Keep all sources in `artifacts/` with `-{source}` suffix |
|----------|----------------------------------------------------------|
| **Pattern** | `R{n}-transcript-{source}.txt` (e.g., `R2-transcript-whisper.txt`) |
| **Reasoning** | Different transcription sources excel at different things. No need to choose a canonical source. |

**Rules:**
- Round file metadata should note which transcript source was used for analysis
- Raw transcripts are static artifacts — never modify them
- Analysis goes in the round file, not alongside the transcript

> **Legal note:** Recording consent laws vary by jurisdiction (one-party vs. all-party consent). Many companies also prohibit interview recording regardless of local law. Always verify both before recording. When in doubt, ask the interviewer for permission or rely on post-interview notes.

---

### Decision 10: Link Management

| Decision | Relative links with on-demand validation |
|----------|------------------------------------------|
| **Reasoning** | Relative links keep the repo portable. Validate after renames or restructures. |

**Link conventions:**

| Link Type | Convention | Example |
|-----------|-----------|---------|
| Within company folder | Relative from current file | `[research](../research.md)` |
| Cross-company | Relative path | `../{other-company}/research.md` |

**On rename protocol:**
1. Before renaming, search for references to the old filename
2. Rename file + update all references in the same commit
3. Verify no broken links

---

## Standard Folder Structure

```
interview-tracking/{company}/
├── README.md              # Status dashboard only (Decision 3)
├── research.md            # Company + role research + intel synthesis
├── rounds/
│   ├── R0-{type}.md       # Combined: prep → notes → review
│   ├── R1-{type}.md
│   ├── ...
│   └── postmortem.md      # Cross-round synthesis (after all rounds, Decision 8)
├── prep/
│   ├── tracker.md         # Single rolling tracker — all rounds (Decision 7)
│   ├── quickref.md        # Merged study materials — all topics (Decision 7)
│   └── {domain}-reference.md  # Optional domain-specific docs
└── artifacts/             # Static inputs only (Decision 5)
    ├── jd.md              # Job description (verbatim)
    ├── resume.pdf         # Resume submitted
    ├── R{n}-transcript-{source}.txt  # Transcripts with source suffix (Decision 9)
    └── _low-credibility-{source}.md  # Flagged external sources
```

---

## Naming Conventions

### Round Types

| Type | When to Use | Example |
|------|-------------|---------|
| `recruiter` | HR/recruiter screen | `R0-recruiter.md` |
| `hiring-manager` | HM interview | `R1-hiring-manager.md` |
| `technical` | Technical/coding round | `R2-technical.md` |
| `system-design` | System design round | `R3-system-design.md` |
| `behavioral` | Behavioral/culture fit | `R4-behavioral.md` |
| `panel` | Multiple interviewers | `R5-panel.md` |
| `offer` | Offer discussion | `R6-offer.md` |

### File Naming

| File Type | Pattern | Example |
|-----------|---------|---------|
| Company research | `research.md` | `research.md` |
| Round file | `R{n}-{type}.md` | `R1-hiring-manager.md` |
| Prep tracker | `prep/tracker.md` | `prep/tracker.md` |
| Quick reference | `prep/quickref.md` | `prep/quickref.md` |
| Domain reference | `prep/{domain}-reference.md` | `prep/cv-pipeline-reference.md` |
| Postmortem | `rounds/postmortem.md` | `rounds/postmortem.md` |

---

## Templates

### README.md Template

```markdown
# {Company} {Year}

| Field | Value |
|-------|-------|
| Status | 🟡 In Progress / 🟢 Offer / 🔴 Rejected |
| Current Round | R{n} {Status} |
| Next Action | {What to do next} |

## Interview Progress

| Round | Type | Date | Status | File |
|-------|------|------|--------|------|
| R0 | Recruiter | YYYY-MM-DD | ✅ | [R0-recruiter.md](rounds/R0-recruiter.md) |
| R1 | {Type} | YYYY-MM-DD | 🟡 | [R1-{type}.md](rounds/R1-{type}.md) |

## Quick Links

- [Company & Role Research](research.md)
- [Prep Tracker](prep/tracker.md)
```

### File Templates

| Template | Purpose |
|----------|---------|
| [`round-template.md`](_templates/round-template.md) | Single round: prep → notes → review |
| [`research-template.md`](_templates/research-template.md) | Company research + intel synthesis |
| [`prep-tracker-template.md`](_templates/prep-tracker-template.md) | Rolling prep tracker (all rounds) |
| [`quickref-template.md`](_templates/quickref-template.md) | Consolidated study material |
| [`postmortem-template.md`](_templates/postmortem-template.md) | Cross-round analysis (after all rounds) |

---

## Artifacts & Prep Conventions

### Folder Purposes

| Folder | Purpose | Contents |
|--------|---------|----------|
| `artifacts/` | Static inputs | JD, resume, transcripts, flagged external sources |
| `prep/` | Study materials | Quick references, cheat sheets, topic summaries |

### Artifacts Naming Convention

**Pattern:** `{type}.{ext}` or `R{n}-{descriptor}.{ext}`

| File Type | Pattern | Example |
|-----------|---------|---------|
| Job description | `jd.md` | `jd.md` |
| Resume | `resume.pdf` | `resume.pdf` |
| Official guide (general) | `official-{topic}.pdf` | `official-candidate-guide.pdf` |
| Official guide (round) | `R{n}-official-{topic}.pdf` | `R2-official-pair-programming.pdf` |
| Transcript | `R{n}-transcript.txt` | `R0-transcript.txt` |
| Transcript (alt source) | `R{n}-transcript-{source}.txt` | `R1-transcript-otter.txt` |
| Low-credibility source | `_low-credibility-{source}.md` | `_low-credibility-random-blog.md` |

**Rules:**
1. **Round number prefix** for interview-specific files (transcripts)
2. **Use lowercase kebab-case** for all filenames
3. **Prefix with underscore** for low-credibility sources
4. **No company name in filename** (folder already provides context)

**Example:**
```
artifacts/
├── jd.md                            # Job description (verbatim)
├── resume.pdf                       # Resume submitted
├── official-candidate-guide.pdf     # General prep guide from company
├── R0-transcript.txt                # Clean, round-prefixed
├── R1-transcript-otter.txt          # Source as suffix
├── R2-official-pair-programming.pdf # Round-specific guide from company
└── _low-credibility-random-blog.md  # Flagged source
```

### Artifacts vs Prep

| Question | Answer |
|----------|--------|
| Is it static input that doesn't change? | → `artifacts/` |
| Is it study material you'll review/update? | → `prep/` |
| Is it low-quality/unverified external content? | → `artifacts/` with `_low-credibility-` prefix |
