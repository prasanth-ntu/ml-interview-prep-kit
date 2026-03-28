# R1 - Technical Interview

## Metadata

| Field | Value |
|-------|-------|
| **Date** | 2025-03-18 |
| **Duration** | 60 min |
| **Interviewer** | Alex Rivera — Senior ML Engineer |
| **Format** | Virtual (Google Meet + CoderPad) |
| **LinkedIn** | [Profile](https://example.com) (fictional) |
| **Status** | ✅ Completed |

---

## Pre-Interview Prep

<!-- Keep this section focused on INTERVIEWER-SPECIFIC context.
     Generic study material (concepts, vocabulary, commands) goes in prep/quickref.md.
     Link to quickref sections here: [Relevant Topic](../prep/quickref.md#anchor) -->

### Interviewer Research
- Alex has been at Acme Tech for 1.5 years, previously at a large cloud provider working on image search
- Published a blog post about "Practical Object Detection at Scale" — values production pragmatism over research novelty
- GitHub shows contributions to open-source data augmentation libraries

### What They Likely Evaluate
- PyTorch fluency — can I write clean model code under time pressure?
- Understanding of model evaluation metrics beyond accuracy
- Practical ML intuition (trade-offs, debugging, real-world considerations)
- Code quality: readability, edge cases, testing mindset

### Key Points to Convey
- Production experience with PyTorch model training and serving
- Familiarity with object detection architectures and trade-offs
- Comfort debugging model performance issues (data quality, training dynamics)
- Study material: [ML Fundamentals](../prep/quickref.md)

### Questions to Ask
- What's the model iteration cycle like? How often do you retrain?
- How do you handle edge cases in shelf detection (occlusion, lighting)?
- What's the model serving architecture look like?

---

## Interview Notes

### Sharing by Interviewer
- Alex's team handles the core detection pipeline (training + inference)
- They recently migrated from TensorFlow to PyTorch — still cleaning up legacy code
- Model retraining happens weekly with new labeled data from stores
- Biggest pain point: false positives on partially occluded products

### Questions I Asked
- **Model serving architecture?** — ONNX Runtime behind a gRPC service, auto-scaling on GPU instances. Latency target is <200ms per frame.
- **How do you handle label noise?** — Combination of active learning and manual review. They're building a labeling quality dashboard.
- **Edge cases?** — Occlusion and lighting variation are the top two. They use synthetic data augmentation but want to improve it.

### Coding Problem

**Problem**: Implement a custom focal loss function for handling class imbalance in multi-class object detection.

**Approach**:
1. Discussed the theory: focal loss down-weights easy examples, focuses on hard negatives
2. Implemented `FocalLoss(nn.Module)` with configurable alpha (class weights) and gamma (focusing parameter)
3. Handled edge cases: numerical stability with log-sum-exp, batch dimension handling
4. Extended to support per-class alpha weights as a tensor

**Follow-up Discussion**:
- Alex asked about trade-offs between focal loss and hard negative mining — discussed when each approach works better
- Discussed how gamma parameter affects training dynamics (higher gamma = more focus on hard examples, but risk of instability)
- Talked about how to tune alpha weights from class frequency statistics

### Key Insights
- Alex seemed impressed by the numerical stability consideration — mentioned "that's exactly the kind of thing that bites you in production"
- The follow-up discussion went deep into practical trade-offs, which aligns with their "production pragmatism" culture
- They're clearly dealing with significant class imbalance (background vs product classes)

---

## Post-Interview Review

### Overall Assessment
Strong technical round. The coding problem was straightforward, but the follow-up discussion is where the real evaluation happened. Alex was testing depth of understanding and production awareness, not just ability to write code.

### What Went Well ✅
1. Nailed the focal loss implementation including numerical stability
2. Follow-up discussion flowed naturally — demonstrated genuine understanding of trade-offs
3. Asked good questions that showed interest in their real problems (label noise, occlusion)

### Areas for Improvement ⚠️
1. Took ~5 minutes to recall the exact focal loss formula — should have reviewed beforehand
2. Could have proactively written a unit test to demonstrate testing mindset
3. Missed an opportunity to connect focal loss to their specific occlusion problem

### Summary Scorecard

<!-- ⚠️ Scores are LLM-generated transcript analysis unless marked "Confirmed Feedback" -->

| Dimension | Score | Notes |
|-----------|-------|-------|
| Technical Depth | 8/10 | Strong on focal loss + training dynamics, minor hesitation on formula |
| Communication | 8/10 | Clear walkthrough of approach, good think-aloud |
| Domain Knowledge | 7/10 | Solid object detection knowledge, could go deeper on serving |
| Code Quality | 8/10 | Clean, handles edge cases, could have added tests |

**Overall: 8/10** ⚠️ LLM-Generated Assessment

---

## Next Steps

| Step | Owner | Notes |
|------|-------|-------|
| R1 feedback | Jamie (recruiter) | Expected within 3-5 days |
| Schedule R2 System Design | Jamie | Pending R1 pass |
| Prep for R2 | Me | Focus on ML system design (serving, pipelines, monitoring) |

### What to Prepare for Next Round
- End-to-end ML pipeline design (data ingestion → training → serving → monitoring)
- Model serving architecture (ONNX Runtime, gRPC, auto-scaling, latency optimization)
- Data pipeline design (streaming video processing, labeling workflows)
- Monitoring and observability for ML systems (data drift, model performance degradation)

---

## Action Items

- [x] Send thank-you email to Alex
- [ ] Review system design patterns for real-time ML inference
- [ ] Practice whiteboard ML system design problems
- [ ] Study ONNX Runtime serving architecture (mentioned by Alex)

---

## References

- [Research & JD](../research.md)
- [Prep Tracker](../prep/tracker.md)
