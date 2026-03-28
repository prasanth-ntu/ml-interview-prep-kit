# Career Strategy Template

A structured framework for career planning during job transitions. Includes the Domain-First Prep process for interview preparation, T-Shape Audit for identifying knowledge gaps, and productivity systems for maintaining momentum.

**How to use:**
1. Fill in the "Current Direction" section to clarify your path
2. Use the Domain-First Prep process before each interview cycle
3. Run the T-Shape Audit to identify and close knowledge gaps
4. Adopt the MVD (Minimum Viable Discipline) system to maintain consistency

---

## Current Career Direction

### Decided Path

**[Your target role type]** -- Use first year to [primary goal] -- Reassess at 12 months

### Critical Timeline

| Deadline | What | Status |
|----------|------|--------|
| [Date] | [Milestone] | [Status] |
| [Date] | [Milestone] | [Status] |
| [Date] | [Must-have outcome] | [Status] |

### Compensation Targets

- **Minimum base**: [Amount]/month ([Amount]/year)
- **Target total comp**: [Amount]+ (base + bonus + equity)
- **Must have**: [Critical benefits -- insurance, WFH, etc.]

### Current Pipeline

| Priority | Company | Why This Role |
|----------|---------|---------------|
| 1 | [Company A] | [What moat/capital it builds] |
| 2 | [Company B] | [What moat/capital it builds] |
| 3 | [Company C] | [What moat/capital it builds] |

### Three Career Moats (Each Role Type Offers One)

| Role Type | Moat Type | What You Become |
|-----------|-----------|-----------------|
| Big Tech / High Brand | Technical depth + brand | "[Domain] builder at [Company] scale" |
| Consulting / Varied | Technical breadth | "Advisor who's seen N+ architectures" |
| Domain Specialist | Deep expertise | "[Domain] expert" (transferable within vertical) |

> **All types are valid.** No wrong choice -- each compounds differently over time.

---

## Domain-First Prep Process

This is the core interview preparation framework. The key insight: **prep should start from the team's business function, not from generic ML study guides.**

### The Process (Run for Every Interview Pipeline)

#### Step 1: Map the Org's Core Function

What does this team/org actually *do*? Not the JD buzzwords, but the business function.

| Org Type | Business Function | Core Problems |
|----------|------------------|---------------|
| Sales org | Revenue generation | Forecasting, demand planning, revenue analytics |
| Risk/Compliance | Loss prevention | Anomaly detection, regulatory reporting, explainability |
| Product org | User engagement | A/B testing, recommendation, engagement metrics |
| Ops org | Efficiency | Optimization, logistics, real-time systems |
| Infrastructure | Platform reliability | Scalability, monitoring, deployment |
| Research | Innovation | Novel methods, benchmarks, publications |

#### Step 2: Derive the Likely Technical Domains

What ML/DS techniques serve that function?

| Business Function | Key Technical Domains |
|-------------------|----------------------|
| Revenue/Sales | Time series forecasting, causal inference, MAPE, Prophet, hierarchical models |
| Risk/Compliance | Rare-event classification, explainability, recall-focused metrics, graph ML |
| Product | Experimentation platforms, bandits, ranking models, recommendation |
| Ops | Optimization, routing, real-time inference, constraint satisfaction |

#### Step 3: Audit Your T-Shape Against Those Domains

Can you name the standard tools, metrics, and approaches for each relevant domain? (See T-Shape Audit below.)

#### Step 4: Close Fundamentals Gaps Before the Interview

Even 2-3 hours of focused study converts "can't name it" into "haven't built it but understand the landscape." That's the difference between a concerning gap and an acceptable one.

> **The meta-lesson:** Domain analysis should happen *when you start prepping for the company*, not the night before. If the JD says "Sales org" -- forecasting prep should start immediately.

---

## T-Shape Audit

### The T-Shape Concept

Senior-level interviewers expect **T-shaped knowledge**: deep in your specialization, broad enough to speak intelligently about adjacent areas.

| What's Acceptable | What's Concerning |
|-------------------|-------------------|
| "I haven't built forecasting systems, but here's how I'd approach it..." | "I don't have experience with that" + can't name tools/metrics |
| Proactively acknowledges gap + asks good clarifying questions | Gap in both experience AND fundamentals |
| Limited hands-on but understands the landscape and tradeoffs | Can't demonstrate short ramp-up distance |

**The key distinction:** There's a difference between "I haven't built X" (experience gap -- fine) and "I can't name the standard tools/metrics for X" (fundamentals gap -- concerning). The first shows specialization. The second signals narrow learning habits.

### Breadth Audit Template

Customize this for your field. Three separate columns track the real state -- having notes does not equal having learned it:

- **Coverage**: Do you have reference material on this topic?
- **Readiness**: Can you answer conceptual + technical questions under interview pressure?
- **Experience**: Hands-on project work (strengthens answers but not required for the T-shape bar)

| Domain | Fundamentals Bar | Coverage | Readiness | Experience | Notes |
|--------|-----------------|----------|-----------|------------|-------|
| [Your core specialty] | [Key tools/metrics] | | | | |
| [Adjacent domain 1] | [Key tools/metrics] | | | | |
| [Adjacent domain 2] | [Key tools/metrics] | | | | |
| [Adjacent domain 3] | [Key tools/metrics] | | | | |
| [Adjacent domain 4] | [Key tools/metrics] | | | | |

**Example for ML/DS roles:**

| Domain | Fundamentals Bar | Coverage | Readiness | Experience |
|--------|-----------------|----------|-----------|------------|
| Classification & rare events | Precision/recall, class imbalance, SMOTE | | | |
| NLP / LLMs / GenAI | Transformers, RAG, evaluation, agents | | | |
| Time series forecasting | ARIMA, Prophet, MAPE, hierarchical models | | | |
| Recommendation systems | Collaborative filtering, embeddings, ranking | | | |
| Causal inference | A/B testing, DiD, uplift modeling | | | |
| MLOps / production | CI/CD, drift, monitoring, deployment | | | |
| Experimentation | Statistical significance, power analysis, sequential testing | | | |

### Readiness Pipeline

The honest path from gap to battle-tested:

```
No material --> Content added --> Read through --> Q&A drill --> Interview-ready --> Project-proven
```

| Level | What It Means | Can You... |
|-------|--------------|------------|
| No material | No reference material exists | -- |
| Content added | Material captured, not yet studied | Look it up if asked |
| Read through | Studied the material once | Recognize terms, explain at high level |
| Q&A drill | Practiced with mock questions | Answer conceptual + technical questions under pressure |
| Interview-ready | Can discuss fluently without notes | Name tools, articulate tradeoffs, connect to experience |
| Project-proven | Built something end-to-end | Share war stories, debug edge cases, explain implementation decisions |

Each step is distinct. Don't skip steps or mark something ready just because notes exist. Project-proven is the gold standard -- it separates "I've read about X" from "I've used X in production and here's what surprised me."

### Using the Audit

**Before a new interview pipeline:** Run Domain-First Prep (above) to identify which domains matter, then check readiness for those domains.

**Between interviews:** Pick one gap per week to move through the readiness pipeline.

**Goal:** All domains at minimum -- material exists + reviewed + can articulate standard tools and tradeoffs under pressure.

---

## Interview Lessons Framework

### LLM Self-Assessment Calibration

If you use LLMs to analyze interview transcripts or mock interviews, be aware of systematic biases:

| LLM Bias | What Happens | Correction |
|----------|-------------|------------|
| Social signal over-weighting | Positive comments and engagement read as pass signals | These are politeness norms, not evaluation signals |
| Domain-agnostic scoring | Scores breadth equally regardless of role focus | Weight gaps in the role's core domain 2-3x higher |
| Compensatory assumption | Assumes strength in area A compensates for gap in area B | Interviewers evaluate each competency against a bar, not on average |
| Candidate perspective blindness | Dismisses candidate's gut feeling as "underestimation" | You were in the room -- your read on interviewer reactions has signal |

**Rule of thumb:** When LLM estimate diverges significantly from your self-assessment, your self-assessment is probably more calibrated -- you were in the room, the LLM only read a transcript.

---

## Productivity Systems

### Minimum Viable Discipline (MVD)

The core insight: **consistency beats intensity**. A system that survives bad days is better than one that only works on good days.

#### Bad Day Baseline (10-20 min) -- "Keep the chain alive"

- Add 3 lines to documentation
- Send one outreach message
- Practice one interview story out loud

#### Normal Day (60-120 min)

- 10 min: choose 1 outcome
- 45-70 min: build/write
- 10 min: document/commit

#### High-Energy Day (deep work)

- 2 x 45-50 min focused blocks
- No "catch up" -- high-energy is bonus, not debt repayment

### Traffic Light Tracking (Not Streaks)

Streaks create shame spirals when broken. Use traffic light tracking instead:

- **Green**: Full session (60-120 min)
- **Amber**: Bad-day baseline (10-20 min) -- **counts as a win**
- **Red**: Nothing

**Goal: Reduce red runs, not maximize greens.**

### Relapse Plan (After Missing 2-3 Days)

1. Say: "I'm restarting, not catching up."
2. Do the smallest task (10 minutes)
3. Log a win ("Returned")
4. Pre-load tomorrow: open the repo + leave a note for next step

**Success metric: Restart speed, not streak length.**

### The Core Loop to Break

> Rigid/unrealistic targets --> miss --> shame --> avoidance --> inconsistency

This pattern resurfaces whenever:
- "Learn everything" becomes the new rigid target
- Rejections trigger shame spirals
- New job pressure exceeds capacity

Recognition is the first step to breaking the loop.

---

## High-Leverage Habits

1. **Sleep protection** -- Fixed caffeine cutoff, phone out of reach, wind-down routine
2. **Anti-shame tracking** -- Traffic light system (amber counts as a win)
3. **Environment design** -- Keep a "NEXT" file with the next 3 micro-steps. Reduce friction to start.
4. **Health-first days** -- On bad health days, do bad-day baseline only. No planning, no guilt.
5. **Weekly closure ritual (20 min)** -- Choose next week's 3 outcomes, delete the rest

---

## Useful Scripts

### 30-Second Pitch

> "I'm a [role] who's strongest at [core strength -- what makes you different]. Over the past [timeframe] I've [1-2 key accomplishments]. I'm looking for [what you want next] at a company where [what matters to you]."

### "Why Are You Leaving?" Answer

> "After [X years] at [company], I've grown from [starting point] to [current level/scope]. I'm looking for [what's next -- depth, breadth, domain, scale] at a company where [specific draw]."

### Boundary Script (Protecting Productive Time)

> "Given current constraints, I'm focusing on one deliverable at a time. If priorities change, I can swap -- but I can't stack."

---

## Decision Frameworks

### The "Impact vs. Cutting-Edge" Tension

Many people feel pulled between (a) state-of-the-art technology and (b) impact-driven work. This is often a false dichotomy.

**What actually sustains motivation (look at your own evidence):**

| Experience | Sustained? | Why? |
|-----------|-----------|------|
| [Past role 1] | Yes/No | [What about the daily work energized or drained you] |
| [Past role 2] | Yes/No | [What about the daily work energized or drained you] |
| [Current situation] | Yes/No | [What about the daily work energizes or drains you] |

**Bottom line:** Motivation that depends on a *narrative* ("I'm saving the world" / "I'm doing cutting-edge AI") fades. Motivation from *the actual daily work* -- shipping, iterating, seeing results -- sustains. Pick the role where the daily work energizes you, and let the narrative follow.

### Regret Asymmetry Analysis

When choosing between options, ask: which choice is easier to recover from if it turns out wrong?

| Scenario | Regret Level | Recovery Path |
|----------|-------------|---------------|
| Take Option A, miss Option B's niche? | [High/Low] | [Can you get back to B later?] |
| Take Option B, miss Option A's advantages? | [High/Low] | [Can you get back to A later?] |

**One option's value is usually more guaranteed** (e.g., brand + comp are structural). **The other's value is more conditional** (e.g., depends on team, manager, scope). Factor this asymmetry into your decision.

---

## Key Quotes

> *"Outperforming in a weak org buys you internal power, not long-term freedom."*

> *"It's not 10 years of any work. It's 10 years of compounding the right capital."*

> *"Career capital doesn't compound from being the best at one thing. It compounds from sitting at a rare intersection."*

> *"Most people overestimate what they can do in one year and underestimate what they can do in ten years."*

---

*Review this template at the start of each job search cycle. Update with lessons learned after each interview round.*
