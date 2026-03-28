# Design: RAG System for Customer Support

> This is the #1 AI system design question. A must-know for any LLM/AI role.

---

## The Question
"Design a RAG-based customer support chatbot that answers questions from a company's knowledge base."

---

## Step 1: Clarify

- Knowledge base: ~500-5000 articles (help docs, FAQs, product guides)
- Users: Customer-facing, ~1000 concurrent users at peak
- Latency: < 3 seconds for response
- Accuracy: Must be grounded — no hallucination on policy/pricing questions
- Features: Citations, "I don't know" for gaps, multi-turn conversation
- Updates: Knowledge base updated weekly

---

## Step 2: High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     INGESTION (Offline)                       │
│  Documents → Chunking → Embedding → Vector Store (FAISS)     │
│  (Scheduled pipeline, runs on KB updates)                    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                     SERVING (Online)                          │
│  User Query                                                  │
│    → Embedding                                               │
│    → Vector Search (top 10)                                  │
│    → Cross-encoder Reranking (top 3)                         │
│    → Relevance Filter (threshold)                            │
│    → LLM (system prompt + context + query)                   │
│    → Response + Citations                                    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                     API LAYER                                │
│  FastAPI → Auth → Rate Limiting → Chat Endpoint              │
│  WebSocket for streaming responses                           │
└─────────────────────────────────────────────────────────────┘
```

---

## Step 3: Deep Dive

### Ingestion Pipeline
- **Document loading:** Parse HTML/MD/PDF → plain text
- **Chunking:** Semantic chunking (group by meaning, not fixed size)
  - Why: "In my project, semantic chunking reduced 322 noisy chunks to 82 high-quality ones"
- **Embedding:** Sentence Transformers (all-MiniLM-L6-v2) for cost-efficiency, or OpenAI ada-002 for quality
- **Storage:** FAISS for < 100K chunks. Pinecone/Qdrant for scale + filtering
- **Schedule:** Re-run ingestion on KB updates (cron or event-triggered)

### Retrieval
- **Two-stage pipeline:**
  1. FAISS bi-encoder search → top 10 candidates (fast, ~50ms)
  2. Cross-encoder reranking → top 3 (accurate, ~200ms)
- **Relevance threshold:** If best score < threshold, return "I don't have information about that" instead of hallucinating
- **Why two stages:** "Cross-encoder is too slow for full corpus, bi-encoder too imprecise for final ranking. Two stages give you speed + accuracy."

### LLM Layer
- **Model:** GPT-4 / Claude for quality, Llama 3 via Groq for cost/speed
- **System prompt:** Persona + rules (only use provided context, cite sources, say "I don't know")
- **Context window management:** Only inject top 3 chunks to avoid noise
- **Streaming:** Token-by-token via SSE/WebSocket for perceived speed

### API Layer
- **FastAPI** with async endpoints
- **JWT authentication** for user sessions
- **Rate limiting** (10 req/min per user)
- **Conversation history** stored in Redis (TTL: 30 min)

---

## Step 4: Edge Cases

| Scenario | Handling |
|----------|---------|
| KB doesn't have the answer | Relevance threshold → "I don't know" + suggest contacting support |
| Hallucination risk | System prompt grounding + only use retrieved context + citations |
| Adversarial queries | Content filter on input + output, refuse policy-violating queries |
| Stale KB | Scheduled re-ingestion + cache invalidation |
| High latency | Cache frequent queries, pre-compute common embeddings |
| Multi-language | Multilingual embedding model, or translate → retrieve → translate back |

---

## Step 5: Scale & Monitor

### Scaling
- **Vector DB:** Move from FAISS to Pinecone (serverless, auto-scales)
- **API:** Horizontal scaling behind load balancer
- **Caching:** Redis cache for frequent queries (cache key = embedding hash)
- **Async:** Background ingestion with Celery/Airflow

### Monitoring
- **Latency:** P50, P95, P99 per component (retrieval, reranking, LLM)
- **Quality:** User feedback (thumbs up/down), automated eval (RAGAS)
- **Cost:** Token usage per query, cost per conversation
- **Alerts:** Latency > 5s, error rate > 1%, low user satisfaction

### Improvement Loop
```
User Feedback → Identify Bad Responses → Improve Chunks/Prompts → A/B Test → Deploy
```

---

## How This Maps to Bubble

| Design Component | Your Bubble Implementation |
|-----------------|---------------------------|
| Chunking | Semantic chunking (322 → 82 chunks) |
| Embedding | Sentence Transformers (HuggingFace) |
| Vector Store | FAISS |
| Two-stage retrieval | Bi-encoder + Cross-encoder reranking |
| Relevance filtering | Configurable threshold |
| LLM | Groq (Llama 3) |
| Agent orchestration | LangGraph |
| Config-driven | Pydantic + YAML (swap models without code changes) |

**Interview tip:** "I've actually built this. Let me walk you through my implementation and the decisions I made..."
