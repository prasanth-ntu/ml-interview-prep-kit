# Acme Tech - Preparation Tracker

> **Status**: Active
> **Interview Cycle**: March - April 2025
> **Last Updated**: 2025-03-19

---

## R0 Prep (Mar 8-10)

> **Interview Date**: Monday, 10 March 2025, 2:00 PM PST
> **Interviewer**: Jamie Chen — Senior Technical Recruiter
> **Prep Start**: 2025-03-08

### Interviewer Context

- Technical recruiter with 2 years at Acme Tech
- Previously recruited for robotics companies — understands ML roles well
- LinkedIn posts emphasize "hiring for potential" — likely values growth mindset over pedigree

### Study Schedule

| Day | Date | Focus Areas | Time Budget | Status |
|-----|------|-------------|-------------|--------|
| Day 1 | 08 Mar | Company research, role analysis | 2 hrs | ✅ Done |
| Day 2 | 09 Mar | Prepare talking points, questions | 1 hr | ✅ Done |
| Interview Day | 10 Mar | Review notes, relax | 30 min | ✅ Done |

### Topic Progress

**Confidence Scale**: ⬜ Not reviewed | 🟡 Partial | 🟢 Confident

| Topic | Confidence | Status | Source | Progress Notes |
|-------|------------|--------|--------|----------------|
| **Company background** | 🟢 | ✅ | Crunchbase, blog | Series B, $45M raised, retail CV |
| **Role requirements** | 🟢 | ✅ | JD | Production ML, PyTorch, CV |
| **Salary expectations** | 🟢 | ✅ | Levels.fyi | $180-220K base, equity on top |
| **Questions to ask** | 🟢 | ✅ | Prep | 4 targeted questions ready |

### R0 Retrospective

| Aspect | Expected | Actual |
|--------|----------|--------|
| Format | Video call, 30 min | Google Meet, 30 min — as expected |
| Topics | Background, salary, timeline | All covered + bonus intel on team structure |
| Difficulty | Low | Low — conversational and friendly |

**Lessons for next round**: Jamie confirmed R1 is technical with coding. Focus on PyTorch and model evaluation.

---

## R1 Prep (Mar 11-18)

> **Interview Date**: Tuesday, 18 March 2025, 10:00 AM PST
> **Interviewer**: Alex Rivera — Senior ML Engineer
> **Prep Start**: 2025-03-11

### Interviewer Context

- Senior ML Engineer, 1.5 years at Acme Tech, previously at a large cloud provider (image search)
- Blog post on "Practical Object Detection at Scale" — values production pragmatism
- Open-source contributions to data augmentation libraries

### Study Schedule

| Day | Date | Focus Areas | Time Budget | Status |
|-----|------|-------------|-------------|--------|
| Day 1 | 11 Mar | PyTorch fundamentals review | 3 hrs | ✅ Done |
| Day 2 | 12 Mar | Custom loss functions, training loops | 3 hrs | ✅ Done |
| Day 3 | 13 Mar | Object detection architectures | 3 hrs | ✅ Done |
| Day 4 | 14 Mar | Model evaluation metrics (mAP, PR curves) | 2 hrs | ✅ Done |
| Day 5 | 15 Mar | Practice coding problems | 4 hrs | ✅ Done |
| Day 6 | 16 Mar | Mock interview with friend | 2 hrs | ✅ Done |
| Day 7 | 17 Mar | Light review, rest | 1 hr | ✅ Done |
| Interview Day | 18 Mar | Final refresh | 30 min | ✅ Done |

### Topic Progress

**Confidence Scale**: ⬜ Not reviewed | 🟡 Partial | 🟢 Confident

| Topic | Confidence | Status | Source | Progress Notes |
|-------|------------|--------|--------|----------------|
| **PyTorch custom modules** | 🟢 | ✅ | JD + R0 intel | Practiced nn.Module subclassing, custom losses |
| **Object detection (YOLO, FRCNN)** | 🟢 | ✅ | JD + blog | Reviewed architectures, trade-offs, anchor boxes |
| **Model evaluation metrics** | 🟢 | ✅ | JD | mAP, PR curves, IoU thresholds |
| **Training dynamics** | 🟡 | ✅ | General prep | Good on LR schedules, less sure on distributed training |
| **Data augmentation** | 🟡 | ✅ | Alex's GitHub | Reviewed albumentations, mixup, mosaic augmentation |
| **Class imbalance handling** | 🟢 | ✅ | Glassdoor + R0 | Focal loss, OHEM, class weights — strong topic |

### R1 Retrospective

| Aspect | Expected | Actual |
|--------|----------|--------|
| Format | CoderPad coding, 60 min | CoderPad + discussion — as expected |
| Topics | PyTorch coding + ML discussion | Focal loss implementation + deep trade-off discussion |
| Difficulty | Medium-Hard | Medium coding, Hard discussion (went very deep) |

**Lessons for next round**: Discussion depth matters more than coding speed here. R2 system design will likely focus on their real serving architecture. Study ONNX Runtime and real-time inference patterns.

---

## R2 Prep (Mar 19 - TBD)

> **Interview Date**: TBD (waiting for R1 feedback)
> **Interviewer**: TBD
> **Prep Start**: 2025-03-19

### Interviewer Context

- TBD — update once R2 is scheduled

### Study Schedule

| Day | Date | Focus Areas | Time Budget | Status |
|-----|------|-------------|-------------|--------|
| Day 1 | 19 Mar | ML system design patterns | 3 hrs | ✅ Done |
| Day 2 | 20 Mar | Model serving (ONNX Runtime, gRPC) | 3 hrs | ⏳ In progress |
| Day 3 | TBD | Data pipeline design | 3 hrs | ⏳ Not started |
| Day 4 | TBD | Monitoring and observability for ML | 2 hrs | ⏳ Not started |
| Day 5 | TBD | Practice system design problems | 4 hrs | ⏳ Not started |

### Topic Progress

**Confidence Scale**: ⬜ Not reviewed | 🟡 Partial | 🟢 Confident

| Topic | Confidence | Status | Source | Progress Notes |
|-------|------------|--------|--------|----------------|
| **ML pipeline design** | 🟡 | ⏳ | R0/R1 intel | Reviewing end-to-end patterns |
| **Model serving architecture** | ⬜ | ⏳ | Alex (R1) | ONNX Runtime + gRPC — need to study |
| **Real-time inference** | ⬜ | ⏳ | R0 intel | <200ms target, GPU auto-scaling |
| **Data pipeline (streaming)** | ⬜ | ⏳ | JD | Video feed processing at scale |
| **ML monitoring** | ⬜ | ⏳ | General | Data drift, model degradation |

---

<!-- Copy the R{n} Prep section above for each new round -->
<!-- IMPORTANT: One file for ALL rounds — never create per-round tracker files -->
