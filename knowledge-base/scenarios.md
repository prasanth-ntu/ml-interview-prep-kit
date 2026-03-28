# ML System Design Scenarios

> **Purpose**: Cross-topic interview scenarios that integrate multiple KB concepts. Generalized and role-agnostic — company-specific framing belongs in your interview tracking folder.
>
> **Pattern**: Scenarios here are reusable building blocks. Company prep files add context (e.g., "Frame the chatbot scenario around the team's Sales use case").
>
> **KB Reference**: [ml-ds-llm-fundamentals.md](ml-ds-llm-fundamentals.md)

---

## Scenario Index

| # | Scenario | Key KB Topics | Difficulty |
|---|----------|--------------|------------|
| 1 | [ML Model Deployment Pipeline](#scenario-1-ml-model-deployment-pipeline) | CI/CD, Containerization, K8s, Monitoring | Medium |
| 2 | [Conversational AI Chatbot](#scenario-2-conversational-ai-chatbot) | Agentic AI, RAG, Tool Calling, Guardrails, Monitoring | Hard |
| 3 | [Real-time Anomaly Detection](#scenario-3-real-time-anomaly-detection) | Feature Engineering, Class Imbalance, Monitoring, Deployment | Medium |
| 4 | [Sales Forecasting System](#scenario-4-sales-forecasting-system) | Time Series, Feature Engineering, A/B Testing, Monitoring | Medium |
| 5 | [Recommendation System](#scenario-5-recommendation-system) | Collaborative Filtering, Embeddings, A/B Testing, Cold Start | Medium |
| 6 | [AML Transaction Monitoring](#scenario-6-aml-transaction-monitoring) | Class Imbalance, Graph ML, Explainability, Governance | Hard |

---

## Scenario 1: ML Model Deployment Pipeline

> "Walk me through how you'd deploy an ML model to production."

### Problem Statement

Design an end-to-end deployment pipeline for an ML model serving real-time predictions at scale. Cover the full lifecycle from trained model to production monitoring.

### Solution Framework

**1. Requirements**
- Latency SLA (e.g., P99 < 1s)
- Throughput target (QPS)
- Availability requirements
- Rollback strategy

**2. Pipeline Stages**

```
Orchestration (Airflow) → Model Registry (MLflow) → Containerization (Docker/ECR)
→ Deployment (K8s/HPA) → Monitoring (Datadog/Grafana) → Feedback Loop
```

> Full architecture: [ML Deployment Stack (5-Layer Model)](ml-ds-llm-fundamentals.md#ml-deployment-stack-5-layer-model)

**3. CI/CD Pipeline**

```
Pre-push: lint → type check → unit tests
CI:       all above + integration tests → Docker build → push to registry
Staging:  deploy → smoke test → load test (production QPS, P99 < SLA)
Prod:     canary (5%) → monitor 30 min → rolling to 100%
```

> Deep-dive: [CI/CD & MLOps](ml-ds-llm-fundamentals.md#cicd-mlops-pipelines) | [Testing Pyramid](ml-ds-llm-fundamentals.md#testing-pyramid-for-ml-systems)

**4. Serving Architecture**
- Proxy + serving container pattern within each pod
- HPA based on CPU utilization + request count (QPS)
- Cold-start mitigation: `initialDelaySeconds`, minimum replica floor during peak hours

> Deep-dive: [ML Serving Pod Architecture](ml-ds-llm-fundamentals.md#ml-serving-pod-architecture-proxy-serving-pattern) | [HPA](ml-ds-llm-fundamentals.md#horizontal-pod-autoscaler-hpa)

**5. Monitoring (Three-Layer)**
- Layer 1 — Real-time: QPS, P99, error rates (Datadog → Slack/PagerDuty)
- Layer 2 — D-1 ML health: feature drift (PSI), accuracy on holdout (Grafana)
- Layer 3 — D-1/D-2 business: revenue impact, conversion rates (Superset)

> Deep-dive: [Three-Layer Monitoring](ml-ds-llm-fundamentals.md#three-layer-monitoring-architecture)

**6. Incident Response**
- Alert → Assess (severity matrix) → **Mitigate first** → Resolve → Post-mortem

> Deep-dive: [Incident Response](ml-ds-llm-fundamentals.md#incident-response-on-call-for-ml-systems) | [Deployment Strategies](ml-ds-llm-fundamentals.md#deployment-strategies)

### Interview Answer Template

> *"I think of ML deployment as a 5-layer stack. Orchestration sits on top with Airflow, then model registry for versioning, containerization for packaging, Kubernetes for serving with autoscaling, and monitoring at the foundation. Each layer has different concerns, but they form a closed loop — when monitoring detects drift, it triggers retraining back at the orchestration layer."*

### Key Follow-up Questions

| Question | KB Reference |
|----------|-------------|
| "How do you handle cold-start for ML pods?" | [HPA](ml-ds-llm-fundamentals.md#horizontal-pod-autoscaler-hpa) |
| "What deployment strategy would you choose?" | [Deployment Strategies](ml-ds-llm-fundamentals.md#deployment-strategies) |
| "How do you know when to retrain?" | [Data Drift](ml-ds-llm-fundamentals.md#data-drift-bias) |
| "How do you test ML pipelines?" | [Testing Pyramid](ml-ds-llm-fundamentals.md#testing-pyramid-for-ml-systems) |

### Ready-to-Speak Scripts

Full scripted answers grounded in production experience. Use the Interview Answer Template above for the opening framing, then expand with these when probed.

#### "Walk me through how you'd deploy an ML model to production"

> *"I'll walk through the full lifecycle. First, the data pipeline runs as an Airflow DAG — extracts data, engineers features, and populates the feature store. Training produces a model registered in MLflow with code version, data hash, hyperparameters, and evaluation metrics.*
>
> *For deployment, the model gets containerized into Docker. Typically you have two deployment paths: one for services with business logic (wrapping model calls with preprocessing), and one for pure model serving. The Docker image goes to ECR, then to a staging Kubernetes cluster where we run smoke tests and load testing at production QPS levels.*
>
> *Production deployment uses canary release — 5% of traffic goes to the new version, we monitor P99 latency and error rates for 30 minutes, and if metrics hold, we roll out fully. Post-deployment, real-time monitoring via Datadog watches for latency and error spikes, while D-1 batch jobs check for feature drift via PSI in Grafana."*

**Technical details to expand on if probed:**
- **Service vs Model Serving**: Service deployment = standard deployment for apps with business logic (wraps model call with feature preprocessing). Model serving platform = handles proxy + serving separation, GPU allocation, shadow testing automatically
- **Model serving config**: `modelserving.yaml` defines pod resources, HPA targets, GPU type, timeout configs — committed to Git, CI/CD pipeline deploys
- **Latency SLA**: P99 < 1s, circuit breaker at 2s. Target performance: avg P99 of ~75ms for model inference

#### "How do you set up CI/CD for an ML pipeline?"

> *"The CI/CD pipeline has four stages. Pre-push, developers run Ruff for linting and formatting, mypy for type checking, and pytest for unit tests locally. On merge request, the CI pipeline re-runs these plus integration tests, builds the Docker image, and pushes to ECR.*
>
> *In staging, we deploy and run smoke tests — verify the health endpoint responds and the model returns valid output schemas. Then load testing at production QPS to validate P99 stays under our SLA.*
>
> *The key ML addition to standard CI/CD is Continuous Training. Beyond CI and CD, we have CT — Airflow DAGs that trigger retraining when drift is detected or on a schedule. The retrained model goes through the same promotion path: MLflow registry staging → load test → canary → production."*

**Testing pyramid details:**
```
Pre-push:   Ruff (lint) → mypy (types) → pytest (unit)
CI:         All above + integration tests → Docker build → ECR push
Staging:    Deploy → smoke test → load test (production QPS, P99 < SLA)
Production: Canary (5%) → monitor 30 min → rolling to 100%
```

#### "Tell me about a production incident you handled"

> *"Our classification model serving had a latency breach incident during peak hours. Datadog fired an alert on our Slack channel when error rates spiked — the model serving layer was returning 500 errors with P99 of nearly 3 seconds, well above our 1-second SLA.*
>
> *I acknowledged the alert, created an incident ticket, and assessed severity: it was affecting one region during peak hours — roughly 5-10% of users — so Urgent priority. For mitigation, I immediately increased the minimum GPU pods from 4 to 6, which stabilized the service within minutes.*
>
> *Root cause investigation showed it was PyTorch cold-start: when HPA scaled up new pods during the QPS spike, the first requests hit uninitialized models and timed out. The model needed about 100 seconds to warm up (configured via initialDelaySeconds). The resolution involved scheduled scaling to pre-provision pods before predicted peak hours, and we added cold-start latency as a specific Datadog metric. The post-mortem led to a discussion with the platform team about model pre-warming as a platform feature."*

#### "How do you monitor ML models in production?"

> *"I use three layers of monitoring, each at different cadences for different audiences.*
>
> *Layer 1 — real-time via Datadog: QPS, P99 latency, error rates, CPU/GPU utilization. This catches infrastructure issues immediately. Alerts go to Slack, with critical ones paging via Splunk On-Call.*
>
> *Layer 2 — D-1 batch via Grafana: ML-specific health metrics computed by Airflow jobs and pushed to a time-series DB. Feature drift using PSI, prediction distribution shifts, model accuracy on holdout sets. This catches silent model degradation that real-time infra metrics miss.*
>
> *Layer 3 — D-1/D-2 via Superset or PowerBI: business metrics like conversion rates, revenue impact, customer satisfaction. This is what stakeholders care about — even if system and ML metrics look fine, business impact is the ultimate measure.*
>
> *The key insight: system metrics and ML metrics are independent failure modes. Your model can have perfect P99 but terrible accuracy — or great accuracy but the service is down. You need both."*

#### "How would you containerize an LLM-based chatbot service?"

> *"For my POC agentic chatbot, I containerized with Docker using a multi-stage build. The first stage installs dependencies from pyproject.toml — keeping the dependency install layer cached means rebuilds are fast when only code changes. The second stage copies only the runtime artifacts.*
>
> *For an LLM-based service specifically, the key considerations are: the model itself may be too large for the container (use API calls to hosted models like Claude instead of bundling weights), the monitoring stack needs to be part of the design from day one (I included Prometheus metrics endpoint and Grafana dashboards), and you need health checks that validate not just the process but the LLM connection — a simple /health that calls the LLM with a trivial prompt.*
>
> *For Kubernetes deployment, I'd set up HPA based on request count rather than CPU, since LLM calls are I/O-bound waiting on the API — CPU won't reflect true load. And because LLM responses are slow (seconds, not milliseconds), you need longer timeouts and possibly request queuing."*

#### "Explain autoscaling for ML workloads"

> *"HPA scales pods based on metrics — typically CPU utilization and request count. For our classification model, we targeted 60% CPU and 30 QPS per pod, with a range of 4 to 10 pods.*
>
> *The ML-specific challenge is cold-start. When HPA adds a new pod, the model needs to load into memory — for a transformer model on GPU, that can take 100+ seconds. During that warm-up period, requests to the new pod time out. We mitigated this with initialDelaySeconds in the K8s config and by maintaining higher minimum replicas during known peak hours.*
>
> *There are three scaling strategies I'd consider: CPU-based for general purpose, QPS-based for request-driven workloads (what we used), and scheduled scaling for predictable traffic patterns. For LLM chatbot services, QPS-based makes the most sense because the work is I/O-bound — CPU stays low while waiting for the LLM API, so CPU-based scaling wouldn't trigger at the right time."*

### Quick-Recall Code Patterns

Condensed patterns for live coding during interviews. Full examples in KB links.

#### Python Log Parsing

If asked to parse and analyze logs:
- `with open()` for file I/O
- `json.load()` for structured logs
- `datetime.strptime()` for timestamps
- `collections.Counter` or `defaultdict` for aggregation
- `max(d, key=d.get)` for finding key of max value

#### Dockerfile for ML Model Serving

> Full example with GPU variant and Docker Compose: [KB: Containerization](ml-ds-llm-fundamentals.md#container-security-docker-kubernetes)

**Key patterns for live coding:**
- Multi-stage build: `builder` (install deps) → `runtime` (copy only what's needed)
- Poetry export to requirements.txt in builder stage
- `HEALTHCHECK` with curl to `/health` endpoint
- `EXPOSE 8080` + `CMD ["uvicorn", ...]`
- No secrets in layers, non-root user (add `RUN useradd` if asked)

#### K8s Deployment YAML with HPA

> Full YAML examples (Deployment + HPA + ServiceAccount): [KB: Kubernetes](ml-ds-llm-fundamentals.md#kubernetes-for-ml)

**Key structure for live coding:**
- `Deployment`: `spec.template.spec.containers[]` with `resources.requests/limits`, `readinessProbe` with `initialDelaySeconds` (critical for ML — model loading takes time)
- `HPA` (`autoscaling/v2`): `scaleTargetRef` → Deployment name, `minReplicas`/`maxReplicas`, `metrics[]` with CPU utilization target
- Separator: `---` between Deployment and HPA in same file
- Reference numbers: 3 min / 10 max replicas, 60% CPU target, 2 CPU / 4Gi per pod request

---

## Scenario 2: Conversational AI Chatbot

> "Design a conversational AI chatbot for internal business users."

### Problem Statement

Build an agentic chatbot that answers business questions by integrating with internal APIs and databases. Users are non-technical (executives, analysts). The system must be accurate, grounded, and auditable.

### Solution Framework

**1. Requirements Gathering**
- Who are the users? (expertise level, query patterns)
- What data sources exist? (APIs, databases, documents)
- Accuracy vs. speed tradeoff
- Security/privacy constraints (internal data, PII)

**2. Architecture (Layered)**

```
L6: User Interface (chat, voice, API)
L5: Orchestration (LangGraph/CrewAI — routing, state, memory)
L4: Agent Logic (tool selection, reasoning, planning)
L3: Tool Layer (API integrations, SQL generation, doc retrieval)
L2: Foundation Models (LLM provider — Claude, GPT, local models)
L1: Infrastructure (monitoring, logging, guardrails, security)
```

> Deep-dive: [Agentic Pipeline Architecture](ml-ds-llm-fundamentals.md#agentic-pipeline-architecture) | [LangGraph](ml-ds-llm-fundamentals.md#langgraph)

**3. Grounding & Accuracy**
- **Tool-first prompting**: Force model to use tools before answering from internal knowledge
- **RAG for static knowledge**: Embed documents, retrieve relevant context
- **LLM-as-Judge**: Cross-validate answers for high-stakes queries

> Deep-dive: [RAG Pipeline](ml-ds-llm-fundamentals.md#rag-pipeline-architecture) | [Tool Calling](ml-ds-llm-fundamentals.md#tool-calling-function-calling)

**4. Guardrails**
- Input validation (prompt injection defense)
- Output validation (factuality checks, PII filtering)
- Fallback to human escalation on low-confidence answers

> Deep-dive: [Guardrails Frameworks](ml-ds-llm-fundamentals.md#guardrails-frameworks) | [API Security](ml-ds-llm-fundamentals.md#api-security)

**5. Evaluation**
- Golden test sets for regression detection
- LLM-as-Judge for automated quality scoring
- User feedback (thumbs up/down) as real-world signal
- Task completion rate as business metric

> Deep-dive: [LLM Evaluation Metrics](ml-ds-llm-fundamentals.md#llm-evaluation-metrics) | [Agent Evaluation](ml-ds-llm-fundamentals.md#agent-evaluation)

### Interview Answer Template

> *"I'd design this as a layered agentic system. The orchestration layer handles routing and state management — I'd use LangGraph for its state machine approach. The agent layer selects tools: API integrations for live data, RAG for document knowledge, and SQL generation for database queries. Guardrails are critical — input validation to prevent prompt injection, output validation to ensure grounded answers, and a fallback path to human support when confidence is low."*

### Key Follow-up Questions

| Question | KB Reference |
|----------|-------------|
| "How do you prevent hallucination?" | [LLM Hallucination](ml-ds-llm-fundamentals.md#llm-hallucination) |
| "How would you evaluate this system?" | [Agent Evaluation](ml-ds-llm-fundamentals.md#agent-evaluation) |
| "How do you handle prompt injection?" | [Guardrails](ml-ds-llm-fundamentals.md#guardrails-frameworks) |
| "LangGraph vs CrewAI — why?" | [LangGraph](ml-ds-llm-fundamentals.md#langgraph) vs [CrewAI](ml-ds-llm-fundamentals.md#crewai) |

---

## Scenario 3: Real-time Anomaly Detection

> "Design a system to detect fraudulent transactions in real-time."

### Problem Statement

Build a real-time anomaly detection pipeline for financial transactions. Must handle high throughput, extreme class imbalance, and provide explainable decisions for regulatory compliance.

### Solution Framework

**1. Requirements**
- Latency: sub-second decision for each transaction
- False positive tolerance: low (blocks legitimate transactions)
- Explainability: regulatory requirement (why was this flagged?)
- Volume: millions of transactions per day

**2. Feature Engineering**
- **Real-time features**: Transaction amount, merchant category, time since last transaction, geographic distance from last transaction
- **Aggregated features**: Rolling window aggregates (avg spend last 7d, transaction count last 24h)
- **Graph features**: Merchant-customer network patterns

> Deep-dive: [Feature Engineering](ml-ds-llm-fundamentals.md#feature-engineering) | [Feature Stores](ml-ds-llm-fundamentals.md#feature-stores)

**3. Model Architecture**
- Two-stage: fast rule-based filter → ML model for borderline cases
- Handle class imbalance: focal loss, SMOTE on training data, threshold tuning
- Ensemble: XGBoost for tabular features + autoencoder for anomaly scoring

> Deep-dive: [Class Imbalance](ml-ds-llm-fundamentals.md#class-imbalance) | [XGBoost](ml-ds-llm-fundamentals.md#xgboost) | [Anomaly Detection](ml-ds-llm-fundamentals.md#anomaly-detection)

**4. Explainability**
- SHAP values for each prediction — "this was flagged because transaction amount was 10x normal"
- Feature importance dashboard for analysts
- Audit trail for regulatory review

> Deep-dive: [SHAP](ml-ds-llm-fundamentals.md#shap-shapley-additive-explanations) | [Model Interpretability](ml-ds-llm-fundamentals.md#model-interpretability-explainability)

**5. Deployment & Monitoring**
- Feature store with online (real-time lookup) + offline (training) stores
- Circuit breaker: if model is slow, fall back to rule-based filter
- Monitor: prediction distribution shifts, false positive rates, feature drift

> Deep-dive: [Circuit Breaker](ml-ds-llm-fundamentals.md#circuit-breaker-pattern) | [Data Drift](ml-ds-llm-fundamentals.md#data-drift-bias)

### Interview Answer Template

> *"I'd use a two-stage approach. A fast rule-based filter catches obvious fraud, then an ML model handles borderline cases. For the ML model, I'd use XGBoost on tabular features combined with an autoencoder for anomaly scoring. Class imbalance is the key challenge — I'd use focal loss during training and tune the decision threshold on precision-recall curves rather than accuracy. Every prediction includes SHAP explanations for regulatory compliance."*

---

## Scenario 4: Sales Forecasting System

> "Design a forecasting system for regional sales predictions."

### Problem Statement

Build a forecasting system that predicts sales at multiple geographic levels (global, regional, per-partner) with varying data availability and seasonality patterns.

### Solution Framework

**1. Requirements**
- Forecast horizon (weekly, monthly, quarterly)
- Granularity levels (global → region → partner)
- Accuracy metric: MAPE (industry standard for sales)
- Stakeholders: finance team, regional managers, executives

**2. Data Pipeline**
- Multiple data sources: CRM, POS systems, market indices, calendar events
- Feature engineering: lag features, rolling aggregates, Fourier features for seasonality
- Data quality: handle missing values, detect outliers, reconcile across sources

> Deep-dive: [Time Series Forecasting](ml-ds-llm-fundamentals.md#time-series-forecasting)

**3. Model Selection**

| Level | Data Volume | Model | Why |
|-------|------------|-------|-----|
| Global | High | Prophet / LightGBM | Stable trends, rich features |
| Regional | Medium | Prophet | Handles holidays, interpretable |
| Per-partner | Low | Hierarchical reconciliation | Borrow strength from higher levels |

> Deep-dive: [Time Series Forecasting](ml-ds-llm-fundamentals.md#time-series-forecasting) — Prophet, Hierarchical Forecasting

**4. Hierarchical Reconciliation**
- Forecasts at each level must be coherent (partner forecasts sum to regional)
- Top-down vs bottom-up vs optimal reconciliation
- Trade-off: top-down loses partner detail, bottom-up amplifies partner noise

**5. Evaluation & Monitoring**
- Backtest: walk-forward validation (train on past, test on future)
- Production: track MAPE by level, detect forecast degradation
- A/B test: compare model versions on recent data before rollout

> Deep-dive: [A/B Testing](ml-ds-llm-fundamentals.md#ab-testing) | [Cross-Validation (Time Series)](ml-ds-llm-fundamentals.md#cross-validation)

### Interview Answer Template

> *"I'd build a hierarchical forecasting system. At the global level, Prophet handles trend and seasonality well. At the partner level where data is sparse, I'd use hierarchical reconciliation to borrow strength from regional aggregates. The key metric is MAPE — it's scale-invariant across geographies. I'd use walk-forward backtesting to validate, and monitor forecast accuracy in production with alerts when MAPE exceeds historical baselines."*

---

## Scenario 5: Recommendation System

> "Design a recommendation engine for an e-commerce platform."

### Problem Statement

Build a recommendation system that surfaces relevant products to users, handling cold-start for new users/items and scaling to millions of user-item interactions.

### Solution Framework

**1. Requirements**
- Real-time vs batch recommendations
- Cold-start handling (new users, new items)
- Diversity vs relevance trade-off
- Business constraints (inventory, margin, fairness)

**2. Architecture**

```
Candidate Generation (1M → 1K) → Ranking (1K → 100) → Re-ranking (100 → 10, business rules)
```

**3. Model Approach**

| Stage | Method | KB Reference |
|-------|--------|-------------|
| Candidate gen | Collaborative filtering + content-based | [Recommendation Systems](ml-ds-llm-fundamentals.md#recommendation-systems) |
| Ranking | Two-tower model (user embedding, item embedding) | [Embeddings](ml-ds-llm-fundamentals.md#nlp-feature-extraction-traditional) |
| Re-ranking | Business rules (diversity, inventory, freshness) | — |

> Deep-dive: [Recommendation Systems](ml-ds-llm-fundamentals.md#recommendation-systems)

**4. Cold-Start Solutions**
- New users: content-based (use demographics, browsing behavior)
- New items: item features (category, description embeddings)
- Hybrid: blend collaborative + content-based, weight shifts as data accumulates

**5. Evaluation**
- Offline: precision@K, recall@K, NDCG, catalog coverage
- Online: A/B test click-through rate, conversion rate, revenue per session
- Watch for popularity bias (recommending only popular items)

> Deep-dive: [A/B Testing](ml-ds-llm-fundamentals.md#ab-testing)

### Interview Answer Template

> *"I'd use a three-stage pipeline: candidate generation narrows millions of items to thousands using collaborative filtering, a ranking model scores those candidates using a two-tower architecture with user and item embeddings, and a re-ranking layer applies business rules for diversity and inventory constraints. Cold-start is handled by blending collaborative filtering with content-based features — as user interaction data accumulates, the collaborative signal gets more weight."*

---

## Scenario 6: AML Transaction Monitoring

> "Design an ML system to detect money laundering in a bank's transaction monitoring platform."

### Problem Statement

Build an ML-based transaction monitoring system to replace/augment legacy rule-based detection. Must achieve very high recall (99%+), provide explainable decisions for investigators and auditors, deploy across 40+ markets with varying regulations, and reduce false positive rates that burden investigation teams.

### Solution Framework

**1. Requirements**
- Recall: 99%+ (missing a crime = regulatory failure, fines)
- Investigator capacity: limited — need high precision at top K alerts
- Explainability: regulatory requirement (FEAT, FATF) — every alert must have a "why"
- Multi-market: different regulations, typologies, risk profiles per jurisdiction
- Governance: audit trails, model documentation, validation gates

> Deep-dive: [Class Imbalance](ml-ds-llm-fundamentals.md#class-imbalance) | [Model Interpretability](ml-ds-llm-fundamentals.md#model-interpretability-explainability)

**2. Architecture (Rule → ML Transformation)**

```
Legacy:     Rules (FATF typologies) → Alerts → Investigators → SAR
Hybrid:     Rules + ML scoring → Ranked alerts → Investigators → SAR
Target:     ML-native (graph + temporal) → Ranked + Explained → Investigators → SAR
```

Key distinction: AML detection works at **pattern/customer level**, not individual transactions. A single $5K transfer isn't suspicious — a customer receiving 20 small deposits from different sources then wiring overseas is a mule pattern.

> Key reference: See AML/Financial Crime literature for typology details (structuring, layering, mule networks).

**3. Feature Engineering**

| Feature Type | Examples | Why |
|-------------|----------|-----|
| **Transaction-level** | Amount, time, payment type | Baseline signals |
| **Aggregated** | Rolling avg spend, transaction count in windows | Behavioral patterns |
| **Graph-based** | Community ID, in/out degree, network centrality | Mule networks, layering |
| **CDD baseline** | Expected volume vs actual, risk score | Anomaly detection |
| **Temporal** | Weekend activity, velocity of transfers | Timing-based typologies |

Graph features consistently outperform transaction-level features for AML — they capture the relational structure criminals use.

> Deep-dive: [Feature Engineering](ml-ds-llm-fundamentals.md#feature-engineering)

**4. Model Architecture**

| Approach | Use Case | Explainability |
|----------|----------|---------------|
| XGBoost + graph features | Primary detection — tabular features enriched with network signals | High (SHAP) |
| Rule-based ensemble | Known typologies (structuring) — catch obvious patterns | Very high |
| Graph Neural Networks | Mule network detection, layering | Medium (requires narrative generation) |
| LLM-assisted | Automated feature discovery, rule generation, SAR narrative drafting | Variable |

Hybrid ensemble: combine rule-based + ML + graph signals with post-processing logic to merge predictions. Banking requires explainability — pure black-box won't pass audit.

> Deep-dive: [Class Imbalance](ml-ds-llm-fundamentals.md#class-imbalance) | [SHAP](ml-ds-llm-fundamentals.md#shap-shapley-additive-explanations) | [XGBoost](ml-ds-llm-fundamentals.md#xgboost)

**5. Governance-Gated Deployment**

```
Model Development → Validation (backtest, bias check)
→ Governance Forum (audit review, documentation)
→ Pilot (1 market, shadow mode) → Monitor (PSI, CSI, recall)
→ Phased rollout (market by market) → Production monitoring
→ Feedback loop (investigator dispositions → retraining)
```

Key banking constraint: models must pass governance forums before deployment. Auditors review model documentation, validation results, and explainability. On-premises hosting often required (no external APIs).

> Deep-dive: [Deployment Strategies](ml-ds-llm-fundamentals.md#deployment-strategies)

**6. Metrics**

| Metric | Purpose | Target |
|--------|---------|--------|
| Recall | Catch all crimes | >95% (ideally 99%) |
| Precision @ top K | Investigator efficiency | 10-20% |
| Lift @ K | Value over random sampling | 5-10x |
| PR-AUC | Overall model quality (imbalanced) | 0.3-0.5 |
| PSI/CSI | Drift detection | <0.1 stable |

Avoid ROC-AUC (misleading for extreme imbalance) and overall accuracy (99.9% by predicting "legitimate" for everything).

> Deep-dive: [Class Imbalance](ml-ds-llm-fundamentals.md#class-imbalance)

### Interview Answer Template

> *"I'd design this as a hybrid ML system replacing legacy rules. The key insight is that AML detection works at pattern level, not individual transactions — graph-based features consistently outperform transaction-level features because they capture the relational structure criminals use, like mule networks and layering.*
>
> *My model architecture would be an ensemble: XGBoost with graph-enriched features for primary detection, with SHAP for explainability. Graph neural networks handle network-level typologies like mule detection. I'd keep rule-based detection for well-known patterns like structuring — it's highly explainable and catches obvious cases.*
>
> *Deployment follows governance gates — model validation, bias testing, audit review, then phased rollout starting with one market in shadow mode. Metrics prioritize recall (99%+, since missing a crime is regulatory failure) and precision at top K alerts (since investigators can only review a fixed number). I'd monitor PSI/CSI for drift and maintain feedback loops where investigator dispositions feed back into model retraining."*

### Key Follow-up Questions

| Question | KB Reference |
|----------|-------------|
| "How do you handle extreme class imbalance (0.1% positive)?" | [Class Imbalance](ml-ds-llm-fundamentals.md#class-imbalance) |
| "How do you explain a GNN's decision to an auditor?" | [Model Interpretability](ml-ds-llm-fundamentals.md#model-interpretability-explainability) |
| "How would you approach a typology with no historical labels?" | [Anomaly Detection](ml-ds-llm-fundamentals.md#anomaly-detection) |
| "How do you reduce false positives without hurting recall?" | [Class Imbalance](ml-ds-llm-fundamentals.md#class-imbalance) |
| "How would you use GenAI in AML?" | Cautious: investigator copilot (SAR narratives, rule generation) ✓, primary detection ✗ |

---

## How to Use Scenarios in Company Prep

Scenarios here are **generalized**. In company prep files, add framing:

```markdown
### Company-Specific Framing

**Scenario 2 (Chatbot)** — Frame for {Company} {Team}:
- End users: {who — executives, analysts, customers}
- Data sources: {their specific APIs/databases}
- Constraints: {security, compliance, scale}
- Link: [Scenario 2](../../../../knowledge-base/scenarios.md#scenario-2-conversational-ai-chatbot)
```

This keeps scenarios DRY while allowing company-specific adaptation.

---

*Created: 2026-02-14*
