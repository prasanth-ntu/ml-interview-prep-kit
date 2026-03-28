# New Company Interview Setup

> Copy this prompt into your AI assistant (Claude, ChatGPT, Gemini, Cursor, etc.)

## When to Use

When you start interviewing with a new company and want to set up a structured folder with research, tracking, and preparation templates.

## Prompt

```
Help me set up a structured interview preparation workspace for a new company.

## Company Details

- Company: {company-name}
- Role: {role-title}
- Year: {year}
- Job Description: (paste below or summarize key points)

{Paste job description here}

## Your Tasks

Generate the following markdown files that I can save to organize my interview prep:

### 1. README.md — Company Overview & Progress Tracker

Include:
- Company name, role, year
- Interview progress table (empty, with columns: Round | Type | Date | Status | Notes)
- Key dates and deadlines
- Current status and next action

### 2. research.md — Company Research & Intelligence

Include sections for:
- **Company Overview**: What they do, market position, recent news
- **Team/Org context**: What's known about the team, hiring manager, org structure
- **Tech stack**: Known technologies, platforms, tools
- **Culture signals**: Glassdoor themes, interview style, what they value
- **Role alignment**: How my experience maps to their requirements
- **Questions to ask**: Smart questions for each round type
- **Intel sources**: Where information came from (JD, LinkedIn, articles, etc.)

Pre-fill what you can from the job description. Mark unknowns with {TODO}.

### 3. tracker.md — Prep Tracker

Include:
- **T-shape audit**: Map my strengths to their requirements, identify gaps
- **Study plan**: Topics to cover, prioritized by likelihood and my confidence level
- **Topic progress table**: Topic | Confidence (1-5) | Last reviewed | Notes
- Leave space for per-round prep sections to be added later

### 4. Recommended Folder Structure

Suggest a clean folder layout:
```
{company-name}/{year}/
├── README.md
├── research.md
├── rounds/          (one file per interview round)
├── prep/
│   └── tracker.md
└── artifacts/       (JD, transcripts, etc.)
```

## Important Rules

- Use kebab-case for folder names
- Don't duplicate information across files — each file has one job
- Keep the README as a dashboard (quick status), research for deep context, tracker for study planning
- Pre-fill from the JD where possible, use {TODO} for unknowns
- Focus on actionable prep, not generic advice
```

## Example Usage

**Input**: Paste the prompt with the company name, role, and job description.

**Output**: Three ready-to-save markdown files that form your interview preparation workspace, plus a recommended folder structure to organize everything.
