# Acme Tech - Research

> **Last Updated**: 2025-03-15

---

## Quick Reference

| Field | Value |
|-------|-------|
| **Company** | Acme Tech |
| **Role** | Senior ML Engineer |
| **Team** | Computer Vision Platform |
| **Level** | Senior (IC3) |
| **Location** | San Francisco, CA (Hybrid) |
| **Posted** | 2025-02-20 |
| **JD** | [artifacts/jd.md](artifacts/jd.md) |

### Key Intel (TL;DR)

- **Culture**: Fast-moving Series B startup, strong engineering culture, "build it right" mentality
- **Comp**: $180K-$220K base + 0.1-0.3% equity
- **Red flags**: High pace may mean on-call burden; product-market fit still evolving
- **Why this role**: Ground-floor CV platform work, chance to shape architecture decisions

---

## Interview Process

| Round | Type | Duration | Focus |
|-------|------|----------|-------|
| R0 | Recruiter | 30 min | Background, salary expectations, timeline |
| R1 | Technical | 60 min | ML coding + model evaluation discussion |
| R2 | System Design | 60 min | End-to-end ML system design |
| R3 | Behavioral | 45 min | Culture fit, leadership, conflict resolution |

> **Current status**: See [README.md](README.md) for progress tracking.

---

## Interview Intel

### What to Expect by Round

| Round Type | Format | Common Topics |
|------------|--------|---------------|
| Technical | CoderPad + discussion | Image classification, object detection, PyTorch, model evaluation metrics |
| System Design | Whiteboard | ML pipeline design, model serving, data pipelines, monitoring |
| Behavioral | STAR format | Ownership, cross-team collaboration, handling ambiguity |

### Common Questions

**Coding:**
- Implement a custom loss function for imbalanced classes
- Write a data augmentation pipeline
- Debug a model training loop with vanishing gradients

**ML/Technical:**
- How would you handle class imbalance in object detection?
- Walk through your approach to model evaluation beyond accuracy
- Compare YOLO vs Faster R-CNN trade-offs

**Behavioral:**
- Tell me about a time you shipped an ML model that underperformed in production
- How do you prioritize between model accuracy and inference latency?
- Describe a situation where you disagreed with a technical decision

---

## Compensation

| Level | TC Range | Notes |
|-------|----------|-------|
| Senior (IC3) | $250K-$320K | Base $180-220K + equity at Series B valuation |

> **Source**: Levels.fyi, Glassdoor, recruiter confirmation during R0

---

## Why This Company?

- Early-stage CV platform — opportunity to define architecture from scratch
- Strong founding team (ex-research lab engineers)
- Retail computer vision is a growing market with clear ROI

## Why This Role?

- Directly aligned with production ML experience (model serving, pipeline design)
- Leadership opportunity on a small team (4 engineers)
- Hands-on technical work, not just management

---

## Red Flags & Mitigations

| Concern | Source | Mitigation |
|---------|--------|------------|
| High pace / burnout risk | Glassdoor reviews mention "startup hours" | Ask about on-call expectations in R3 |
| Product-market fit unclear | Series B, still iterating on core product | Ask about customer traction and retention in R3 |
| Small team = wearing many hats | Recruiter mentioned "full-stack ML" | Clarify role scope: research vs engineering vs infra |

---

## Questions to Ask

### To Recruiter
- What does the interview timeline look like?
- What's the team size and reporting structure?
- Is the role backfill or new headcount?

### To Hiring Manager
- What's the biggest technical challenge the CV team faces right now?
- How do you balance research exploration vs shipping to production?
- What does success look like in the first 6 months?

---

## Resources

### Official
- [Acme Tech Engineering Blog](https://example.com/blog) (fictional)
- [Acme Tech Careers Page](https://example.com/careers) (fictional)

### Interview Prep
- LeetCode ML tag problems
- "Designing Machine Learning Systems" by Chip Huyen — Chapters 7-9

### Community
- Glassdoor reviews for "Acme Tech ML Engineer"
- Blind posts about Series B startup interviews

---

## Intel Sources

### Recruiter Call (R0)

**Source**: Direct conversation during recruiter screen
**Credibility**: High — first-party information

**Key Intel:**
- Team is 4 engineers + 1 PM, reporting to VP of Engineering
- They use PyTorch for training, ONNX Runtime for serving
- Current focus: real-time shelf detection for grocery retail clients
- Timeline: want to fill role within 4 weeks

**Impact on Prep:**
- **Confirms**: Focus on production ML (serving, monitoring) not just research
- **Challenges**: "Real-time" requirement means latency will be important in system design

### Glassdoor Reviews

**Source**: 12 reviews from current/former employees
**Credibility**: Medium — reviews may be biased, mix of roles

**Key Intel:**
- Engineers praise technical culture and autonomy
- 2 reviews mention long hours during product launches
- Interview process described as "fair but thorough"

**Impact on Prep:**
- **Confirms**: Technical depth matters more than leetcode grinding
- **Challenges**: May need to demonstrate comfort with ambiguity and fast iteration

---

### Source Reliability

| Source | Rating | Type | Notes |
|--------|--------|------|-------|
| Recruiter Call | ⭐⭐⭐⭐⭐ | Primary | Most reliable |
| Glassdoor | ⭐⭐⭐⭐ | Secondary | Real reviews, may be outdated |
| Engineering Blog | ⭐⭐⭐ | Secondary | Useful for tech stack context |
| Blind Posts | ⭐⭐ | Tertiary | Unverified, different team/year |
