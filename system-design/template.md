# AI System Design — Interview Framework

Use this step-by-step for any "Design a ..." question.

---

## Step 1: Clarify Requirements (2 min)

Ask questions before designing:
- **Users:** Who uses it? How many concurrent users?
- **Data:** What data sources? How much? How often updated?
- **Quality:** What's acceptable accuracy/latency?
- **Scale:** MVP vs production? Single-tenant vs multi-tenant?
- **Constraints:** Budget? Existing infrastructure? Compliance?

Example: "Design a RAG system for customer support"
→ "How many documents? What format? What's acceptable response time? Do we need citations? Multi-language?"

---

## Step 2: High-Level Architecture (3 min)

Draw the major components and data flow:

```
User → API Gateway → Application Server → [LLM / Vector DB / Tools] → Response
```

Name the components, don't detail them yet.

---

## Step 3: Deep Dive Each Component (10 min)

For each major component, explain:
1. **What** it does
2. **Why** this choice (trade-offs)
3. **How** it works technically

### Typical AI System Components:
- **Ingestion pipeline** — document processing, chunking, embedding
- **Vector store** — which DB, indexing strategy
- **Retrieval** — search method, reranking, filtering
- **LLM layer** — model choice, prompt design, guardrails
- **API layer** — endpoints, auth, rate limiting
- **Monitoring** — latency, quality, cost tracking

---

## Step 4: Handle Edge Cases (2 min)

- What if the knowledge base doesn't have the answer?
- What if the LLM hallucinates?
- What if latency spikes?
- How do you handle toxic/adversarial queries?
- What if documents are updated frequently?

---

## Step 5: Scale & Improve (2 min)

- Caching frequent queries
- Async processing for heavy operations
- A/B testing different models/prompts
- Feedback loop (user ratings → improve retrieval)
- Cost optimization (smaller models for simple queries)

---

## Common Mistakes to Avoid

1. **Jumping into details without clarifying** — always ask requirements first
2. **Over-engineering** — start simple, add complexity when justified
3. **Ignoring trade-offs** — every choice has a cost, acknowledge it
4. **Forgetting monitoring** — "how do you know it's working?"
5. **Not mentioning evaluation** — "how do you measure quality?"
