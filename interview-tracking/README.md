# Interview Tracking System

A structured system for organizing and tracking job interviews. Each company gets its own folder with research, round-by-round notes, preparation materials, and artifacts — following a set of design decisions that keep things organized as interview complexity grows.

## How to Use

1. **Fork this repo** (or copy the `interview-tracking/` folder into your own project)
2. **Copy `_example-company/`** and rename it to your target company (e.g., `acme-tech/`)
3. **Copy templates** from `_templates/` into the appropriate subfolders as you progress through rounds
4. **Follow the structure** — see [`_structure-guide.md`](_structure-guide.md) for the 10 design decisions behind the folder layout

### Quick Start for a New Company

```bash
# Copy the example as a starting point
cp -r _example-company/ my-company/

# Or start from blank templates
mkdir -p my-company/{rounds,prep,artifacts}
cp _templates/research-template.md my-company/research.md
cp _templates/round-template.md my-company/rounds/R0-recruiter.md
cp _templates/prep-tracker-template.md my-company/prep/tracker.md
```

Then fill in the templates with your company-specific content.

## Folder Structure

```
interview-tracking/
├── README.md                  # This file
├── _structure-guide.md        # Design decisions (start here)
├── _templates/                # Blank templates for new companies
│   ├── round-template.md      # Single round: prep → notes → review
│   ├── research-template.md   # Company research + intel synthesis
│   ├── prep-tracker-template.md   # Rolling prep tracker
│   ├── quickref-template.md   # Consolidated study material
│   └── postmortem-template.md # Cross-round analysis
├── _example-company/          # Fictional example showing the system in action
│   ├── README.md              # Status dashboard
│   ├── research.md            # Company research (filled in)
│   ├── rounds/
│   │   ├── R0-recruiter.md    # Example recruiter call
│   │   └── R1-technical.md    # Example technical round
│   ├── prep/
│   │   └── tracker.md         # Example prep tracker
│   └── artifacts/             # Static inputs (JD, resume, transcripts)
└── {company}/                 # Your actual company folders go here
```

## Key Concepts

- **One file per round** — prep, interview notes, and review live together in `rounds/R{n}-{type}.md`
- **README is a dashboard** — status and links only, no content duplication
- **Single source of truth** — each piece of information lives in exactly one file
- **Artifacts vs dynamic content** — static inputs (JD, resume, transcripts) go in `artifacts/`, everything else is your analysis
- **One tracker, one quickref** — never create per-round prep files

See [`_structure-guide.md`](_structure-guide.md) for the full rationale behind these decisions.

## Templates

| Template | Purpose |
|----------|---------|
| [`round-template.md`](_templates/round-template.md) | Single round: prep, notes, and review |
| [`research-template.md`](_templates/research-template.md) | Company research and intel synthesis |
| [`prep-tracker-template.md`](_templates/prep-tracker-template.md) | Rolling preparation tracker across all rounds |
| [`quickref-template.md`](_templates/quickref-template.md) | Consolidated study material by topic |
| [`postmortem-template.md`](_templates/postmortem-template.md) | Cross-round analysis after all rounds complete |
