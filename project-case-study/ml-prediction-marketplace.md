# Case Study: ML Classification System for an E-Commerce Marketplace

## Context

A large e-commerce marketplace connects third-party sellers with buyers. When a buyer places an order, sellers are expected to fulfill it promptly. However, some sellers — rather than canceling the order themselves (which hurts their seller rating and search ranking) — deliberately provide poor service or pressure the buyer into canceling instead. Common tactics include claiming items are "out of stock" via chat, delaying fulfillment until the buyer gives up, or sending messages asking the buyer to cancel and reorder.

This seller-induced cancellation behavior degrades buyer trust and inflates return/refund costs for the platform.

The platform's existing rule-based detection system (v1) was built several years ago and relied on rigid thresholds and a simple NLP classifier for in-app chat analysis. It had significant blind spots:

- The NLP model was not retrained regularly and had degraded accuracy
- Phone call metadata was ignored entirely
- Concurrent order scenarios were mishandled (sellers overwhelmed with multiple orders)
- Conservative thresholds meant many true violations went undetected (low sensitivity)
- No natural language reasoning or explainability
- No feedback loop for continuous improvement

**Scale**: The system processes hundreds of thousands of cancellation events per day across multiple markets and languages.

## Problem Statement

Design and build an ML classification system that:

1. **Accurately classifies** whether a seller induced the buyer to cancel (binary or 3-class: induced / not-induced / inconclusive)
2. **Provides explainability** via decision factors (e.g., "chat — asked to cancel", "fulfillment — no shipping update", "phone call from seller")
3. **Operates within strict latency SLAs** (~1 second end-to-end) at scale (~100+ QPS during peak)
4. **Supports multi-market deployment** with varying languages, policies, and classification requirements
5. **Minimizes false positives** (precision >90%) since incorrect classifications result in seller penalties

## Architecture

### High-Level Pipeline

```
Buyer cancels order
    ↓
Arbitration Service collects signals
    ↓
Gateway Service (pre-processing, feature extraction)
    ↓
ML Model Service (inference on GPU)
    ↓
Return prediction + decision factors
    ↓
Downstream: penalties, metrics, feedback
```

### Model Architecture: Multi-Modal Fusion

The production model uses a **transformer + MLP fusion architecture**:

1. **Text encoder**: A multilingual DeBERTa-class model, further pre-trained on 2M+ seller-buyer chat transcripts using masked language modeling (MLM). Processes:
   - In-app chat transcripts between seller and buyer
   - Concurrent order context (seller handling multiple orders simultaneously)
   - Fulfillment timeline summaries (converted to natural language descriptions)

2. **Numerical feature module**: A multi-layer perceptron (MLP) processing ~68 engineered features:
   - **Fulfillment-based** (18): promised ship date, actual ship date, delay count, delay volatility index, percentage of deadline extensions/misses
   - **Seller activity** (7): active/idle/offline time ratios, order processing speed, average response time to buyer messages
   - **Communication** (38): message counts, response times, call metadata, unanswered buyer messages
   - **Order-specific** (5): concurrent order volume, order completion rate, recent cancellation ratio

3. **Cross-attention fusion**: Combines text and numerical representations before a classification head

4. **Multi-task heads**: Main classification head + decision factor prediction head for explainability

5. **Market embedding**: Market/region ID embedding layer to capture market-specific classification patterns

### Infrastructure

- **Gateway service**: Lightweight K8s deployment (3 pods, 2 CPU / 2 GB each) handles pre-processing and routing
- **Model serving**: GPU-accelerated PyTorch serving on T4 instances with sidecar proxy pattern
  - Proxy container: handles timeouts, logging, shadow testing
  - Serving container: runs the model with GPU support
- **Autoscaling**: HPA with CPU-based and request-count-based scaling policies
- **Logging**: Request/response shadow testing via Fluentd to object storage, parsed by daily batch pipelines

## Key Technical Decisions

### 1. Output Ordering Optimization for Latency

**Problem**: LLM-based approaches generated classification + reasoning as sequential text, resulting in 3-15 second latency depending on the technique.

**Solution**: For the fine-tuned LLM variant, we discovered that **placing the classification verdict before the reasoning** in the output format dramatically reduced time-to-first-useful-token. Instead of:

```xml
<reasoning>The seller asked the buyer to cancel because...</reasoning>
<verdict>induced</verdict>
```

We used:

```xml
<verdict>induced</verdict>
<decision_factors>['Chat - asked to cancel', 'Fulfillment - no shipping update']</decision_factors>
<reasoning>The seller asked the buyer to cancel because...</reasoning>
```

Combined with streaming, this reduced effective latency from ~10s to ~0.8s for the fine-tuned LLM, because the downstream system only needs the verdict — it can process the request before the full reasoning is generated.

**Interview insight**: This is a general principle for any LLM-in-the-loop system — structure outputs so the most critical field comes first, then stream.

### 2. Self-Reflection Chain: When It Helps vs. When It Doesn't

We tested a self-reflection pattern where the model re-evaluates its initial classification:

| Technique | Accuracy | Precision | F1 |
|-----------|----------|-----------|-----|
| Few-shot RAG (10 examples) | 0.908 | 0.934 | 0.928 |
| Few-shot RAG (10) + Self-reflection | 0.845 | 0.963 | 0.867 |

**Key finding**: Self-reflection **increased precision but decreased accuracy and sensitivity**. The model became more conservative — it was more confident when it said "induced" but missed more true cases.

**When self-reflection helps**: When false positives are extremely costly and you can tolerate lower recall. When the task involves ambiguous reasoning that benefits from a second pass.

**When it hurts**: When sensitivity matters (catching as many true cases as possible). The additional inference pass adds latency and cost, and the conservative bias may not be worth the precision gain.

**Interview insight**: Don't assume chain-of-thought / self-reflection always improves performance. Benchmark it on your specific metrics — it often trades recall for precision.

### 3. Fine-Tuning ROI: Small Fine-Tuned Model vs. LLM API

We evaluated a progression of approaches:

| Approach | Accuracy | Latency (p99) | Cost/day |
|----------|----------|---------------|----------|
| Rule-based (v1) | 72.4% | ~100ms | ~$0 |
| Claude 3.5 Sonnet (zero-shot) | 73.6% | ~8s | ~$700 |
| Claude 3.5 Sonnet (few-shot RAG) | 90.8% | ~15s | ~$3,000 |
| GPT-4o-mini (few-shot RAG) | 76.3% | ~3s | ~$90 |
| Llama 3.1 8B fine-tuned | 89.0% | ~1s | ~$60 |
| Custom transformer + MLP fusion | 91.9% | ~75ms | ~$180 |

**Key findings**:
- Enterprise LLMs validated the approach quickly (POC in weeks) but were cost-prohibitive at scale ($3K+/day)
- Fine-tuned open-source LLMs achieved comparable accuracy at 50x lower cost
- The custom fusion model **outperformed all LLM approaches** while being 200x faster, because it could natively process numerical features that LLMs struggle with
- The LLM's main remaining value: generating training labels and providing explainability during development

**Interview insight**: LLMs are excellent for rapid POC and label generation, but production systems often benefit from distilling into a smaller, task-specific model. The key question is whether the task requires genuine language understanding or if it can be decomposed into text + structured features.

### 4. Consistency Evaluation Methodology

LLMs are non-deterministic. We evaluated output consistency by running 50 inference attempts per sample and measuring:

- **Verdict consistency**: % of times the same classification was produced
- **Self-BLEU**: Measures lexical similarity across generated reasoning texts (0.97+ = very consistent)
- **Self-ROUGE / Self-Cosine / Self-Jaccard**: Cross-validate reasoning consistency

**Finding**: The fine-tuned model produced consistent verdicts (100% agreement across 50 runs for tested samples) but with some variation in reasoning text. This is acceptable — the verdict is the production-critical output.

**Interview insight**: When using LLMs in production, you need a consistency evaluation framework beyond just accuracy. Temperature=0 doesn't guarantee determinism. Measure what matters: is the action-critical output stable?

### 5. Data Labeling Strategy and Conflict Resolution

**Initial labeling**: Established a Standard Operating Procedure (SOP) with structured labels (category, decision factors 1-3, free-text reasoning). Labeled ~5,000 samples per market with a mix of random sampling (60%) and positive-class enriched sampling (40%).

**Conflict resolution loop**:
1. Train two models (fine-tuned LLM + custom model) on labeled data
2. Extract samples where model predictions conflict with human labels (~24% of test set)
3. Send conflicting samples back to operations team for re-labeling
4. ~36% of conflicting labels were updated after re-evaluation
5. Both models improved by 3-6 percentage points after relabeling

**Interview insight**: Your model is only as good as your labels. Systematic conflict resolution between model predictions and human labels uncovers labeling errors and ambiguous cases. Budget for at least one relabeling cycle.

### 6. Continued Pre-Training for Domain Adaptation

Rather than fine-tuning a base multilingual model directly, we added a **continued pre-training** phase:

1. **Continued pre-training**: MLM objective on 2M+ unlabeled seller-buyer chat messages (no labels needed)
2. **Fine-tuning**: Supervised training on 5K labeled samples with label smoothing (0.1)

The continued pre-training step improved accuracy by 3 percentage points and F1 by 1 point. This is because the base model had no exposure to the platform's multilingual chat patterns, slang, abbreviations, and domain vocabulary.

**Interview insight**: Continued pre-training is underutilized. When you have large amounts of unlabeled domain text, MLM pre-training before supervised fine-tuning is often the highest-ROI step.

## Rollout Strategy

### Phased Approach

1. **Data backfill**: Run model predictions on 1 month of historical data to calibrate thresholds
2. **Threshold selection**: Different thresholds for different downstream actions:
   - High confidence (score > 0.95): Direct penalty on seller metrics
   - Medium confidence (score > 0.45): Flag for investigation
   - Below threshold: Default to non-induced
3. **Market-by-market rollout**: Start with highest-volume market, validate metrics, expand
4. **Shadow mode**: Run v2 alongside v1, compare outputs before switching traffic

### Monitoring

- Real-time: QPS, latency, error rates, prediction distribution by market
- Offline: Daily batch pipeline computes decision factor breakdowns, compares with historical trends
- Business metrics: Buyer cancellation rate, seller compliance rate

## Interview Walkthrough

### How to Present This (15-20 minutes)

**Opening (2 min)**: Frame the problem — "E-commerce marketplace, seller-induced order cancellations hurt buyer trust, existing rule-based system had degraded to ~72% accuracy."

**Requirements gathering (3 min)**:
- What are the input signals available?
- What is the latency budget?
- What is more costly: false positive (penalizing innocent seller) or false negative (missing a violation)?
- Multi-market and multi-language requirements?

**Architecture (5 min)**: Walk through the pipeline. Emphasize the multi-modal fusion approach — why text alone isn't enough, why numerical features complement language understanding.

**Key decisions (5 min)**: Pick 2-3 of the decisions above based on the interviewer's interest. The fine-tuning ROI comparison and self-reflection analysis are usually the most interesting.

**Production concerns (3 min)**: Latency optimization, autoscaling, monitoring, rollout strategy.

### Common Follow-Up Questions

**Q: Why not just use an LLM for everything?**
A: We did start there for POC. Three problems: (1) Cost at scale ($3K+/day), (2) Latency (8-15s vs 75ms SLA), (3) LLMs struggle with numerical features — 68 engineered features from fulfillment timelines, seller activity patterns, and call metadata are better processed by an MLP. The LLM was invaluable for label generation and POC validation.

**Q: How do you handle class imbalance?**
A: ~25% of cancellations are seller-induced. We used enriched sampling during labeling (40% positive-class enriched), label smoothing (0.1) during training, and threshold tuning during rollout to balance precision/recall per market.

**Q: How would you add a new market?**
A: The model uses a market embedding layer, so adding a market requires: (1) Collect ~5K labeled samples, (2) Run continued pre-training on that market's chat data, (3) Fine-tune the model with the new market ID, (4) Calibrate thresholds via backfill.

**Q: How do you ensure the model stays accurate over time?**
A: Monitor prediction distributions in dashboards. Retrain triggers: (1) observed data/feature drift, (2) new input signals added, (3) accumulation of ~1K confirmed wrong predictions from operations feedback. The daily pipeline logs all predictions for retrospective analysis.
