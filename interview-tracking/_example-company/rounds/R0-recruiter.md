# R0 - Recruiter Interview

## Metadata

| Field | Value |
|-------|-------|
| **Date** | 2025-03-10 |
| **Duration** | 30 min |
| **Interviewer** | Jamie Chen — Senior Technical Recruiter |
| **Format** | Virtual (Google Meet) |
| **LinkedIn** | [Profile](https://example.com) (fictional) |
| **Status** | ✅ Completed |

---

## Pre-Interview Prep

### Interviewer Research
- Jamie has been at Acme Tech for 2 years, previously recruited for a mid-size robotics company
- Posts on LinkedIn about "hiring for potential, not pedigree" — likely values growth mindset

### What They Likely Evaluate
- Communication clarity and enthusiasm for the role
- Salary expectations alignment
- Timeline and availability
- Basic background fit (ML experience, production systems)

### Key Points to Convey
- 4+ years of production ML experience (training, serving, monitoring)
- Hands-on with PyTorch and model optimization
- Motivated by early-stage opportunity to shape CV platform architecture
- Available to start within 4 weeks

### Questions to Ask
- What does the interview process look like end-to-end?
- What's the team composition and reporting structure?
- Is this a new role or backfill?
- What's the biggest challenge the CV team is tackling right now?

---

## Interview Notes

### Sharing by Interviewer
- Team is 4 ML engineers + 1 PM, reporting to VP of Engineering (Dr. Sarah Martinez)
- Using PyTorch for training, ONNX Runtime for inference serving
- Current flagship product: real-time shelf detection for grocery retail
- They've raised $45M Series B, aiming for profitability within 18 months
- This is a new headcount — growing the CV team to handle expanding client base

### Questions I Asked
- **Interview timeline?** — 3-4 rounds over 2-3 weeks. R1 is technical (coding + ML discussion), R2 is system design, R3 is behavioral with hiring manager
- **Team culture?** — "Engineers own their features end-to-end. We don't have separate ML research and ML engineering — everyone ships."
- **Biggest challenge?** — Scaling inference to handle real-time video feeds from 500+ stores simultaneously

### Key Insights
- "End-to-end ownership" suggests they want someone comfortable with both model development AND deployment infrastructure
- Real-time requirement at scale (500+ stores) is a strong signal that system design round will focus on serving infrastructure
- Jamie mentioned they're evaluating candidates on "how they think, not just what they know" — open-ended problem solving likely valued

---

## Post-Interview Review

### Overall Assessment
Strong recruiter screen. Good rapport with Jamie. Covered all key questions and got useful intel for upcoming rounds.

### What Went Well ✅
1. Clearly articulated motivation for the role (early-stage CV platform)
2. Asked targeted questions that revealed useful intel (team structure, tech stack, key challenges)
3. Salary expectations aligned — Jamie confirmed the range works

### Areas for Improvement ⚠️
1. Could have asked more about the on-call and work-life balance to address the Glassdoor concern
2. Spent a bit too long on background overview — should have been more concise

### Summary Scorecard

<!-- ⚠️ Scores are LLM-generated transcript analysis unless marked "Confirmed Feedback" -->

| Dimension | Score | Notes |
|-----------|-------|-------|
| Communication | 8/10 | Clear and conversational, minor verbosity |
| Enthusiasm | 9/10 | Genuine interest came through |
| Fit Signal | 8/10 | Background aligns well with role requirements |

**Overall: 8/10** ⚠️ LLM-Generated Assessment

---

## Next Steps

| Step | Owner | Notes |
|------|-------|-------|
| Schedule R1 Technical | Jamie (recruiter) | Expected within 1 week |
| Prep for R1 | Me | Focus on PyTorch coding + model evaluation |

### What to Prepare for Next Round
- PyTorch coding fluency (custom losses, training loops, data loading)
- Model evaluation beyond accuracy (precision/recall trade-offs, mAP for detection)
- Object detection fundamentals (YOLO, Faster R-CNN, anchor boxes)

---

## Action Items

- [x] Send thank-you email to Jamie
- [x] Update research.md with intel from this call
- [ ] Begin R1 prep — see [prep/tracker.md](../prep/tracker.md)

---

## References

- [Research & JD](../research.md)
- [Prep Tracker](../prep/tracker.md)
