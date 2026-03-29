# ML Interview Prep Kit

> A comprehensive, open-source toolkit for ML/AI/Data Science interview preparation — interactive mind map, 100+ topic knowledge base, interview tracking system, career frameworks, and AI-powered workflows.

[![Live Mind Map](https://img.shields.io/badge/Live-Mind_Map-blue?style=for-the-badge)](https://interview.prasanth.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**[Explore the Interactive Mind Map →](https://interview.prasanth.io)**

---

## What You Get

| Section | What's Inside |
|---------|---------------|
| **[Knowledge Base](knowledge-base/)** | 100+ ML/AI/DS/LLM topics with two-layer structure: quick reference tables + detailed explanations with interview phrasing |
| **[Interactive Mind Map](https://interview.prasanth.io)** | D3.js visualization of all topics with search, dark mode, zoom, export, and related-topic navigation |
| **[System Design Scenarios](system-design/)** | 6 end-to-end ML system design walkthroughs with ready-to-speak scripts |
| **[Coding Practice](coding-practice/)** | LeetCode solutions + 6 topic guides (arrays, DP, trees, linked lists, sorting, math) |
| **[Interview Tracking](interview-tracking/)** | 5 templates + structure guide (10 design decisions) for tracking multiple company pipelines |
| **[Career Frameworks](career-frameworks/)** | Offer decision matrix, negotiation tactics, STAR story methodology, career strategy templates |
| **[Project Case Study](project-case-study/)** | Generic ML classification system walkthrough for system design interviews |
| **[AI Prompt Templates](prompt-templates/)** | Platform-agnostic prompts for interview prep workflows (works with Claude, Gemini, ChatGPT) |

## Quick Start

```bash
# 1. Fork & clone
gh repo fork prasanth-ntu/ml-interview-prep-kit --clone

# 2. Explore the knowledge base
open knowledge-base/ml-ds-llm-fundamentals.md

# 3. View the interactive mind map locally
make mindmap

# 4. Start tracking your interviews
cp -r interview-tracking/_example-company interview-tracking/your-company
```

## Repository Structure

```
ml-interview-prep-kit/
├── index.html                         # Interactive mind map v2 (interview.prasanth.io)
├── index-v1.html                      # Archived v1 mind map
├── knowledge-base/
│   ├── ml-ds-llm-fundamentals.md      # 100+ topics — the core reference
│   ├── scenarios.md                   # 6 ML system design scenarios
│   └── sql-fundamentals.md            # SQL quick reference
├── coding-practice/                   # LeetCode solutions + topic guides
├── system-design/                     # System design templates + walkthroughs
├── interview-tracking/                # Templates + example company
│   ├── _structure-guide.md            # 10 design decisions for tracking
│   ├── _templates/                    # 5 reusable templates
│   └── _example-company/             # Worked example (fictional)
├── career-frameworks/                 # Decision matrices + STAR methodology
├── project-case-study/                # Generic ML case study for interviews
├── prompt-templates/                  # AI workflow prompts (Claude/Gemini/ChatGPT)
├── scripts/                           # Build tooling
│   ├── kb-sync.py                     # Mind map data generator
│   ├── check-links.py                 # Internal link validator
│   └── pii-scan.py                    # Confidential term scanner
└── Makefile                           # Build commands
```

## Knowledge Base Topics

The knowledge base covers 14 categories across ML, AI, Data Science, and LLM engineering:

**ML Foundations** · Linear/Logistic Regression · Gradient Descent · Bias-Variance · Cross-Validation · Feature Engineering · Class Imbalance

**Classical Algorithms** · Decision Trees · SVM · KNN · Naive Bayes · K-Means

**Ensemble Methods** · Random Forest · AdaBoost · Gradient Boosting · XGBoost

**Deep Learning** · MLP · CNN · RNN · Activation Functions · Batch Norm · Attention

**NLP & LLMs** · Transformers · Tokenization · Context Engineering · Prompt Engineering · Fine-tuning · LoRA · RLHF · Hallucination

**Agentic AI** · LangChain · LangGraph · RAG · Tool Calling · Guardrails · MCP · A2A

**MLOps** · CI/CD · Containerization · K8s · Monitoring · Deployment Strategies · Feature Stores

...and more. [See the full mind map →](https://interview.prasanth.io)

## Build Commands

```bash
make kb-sync       # Regenerate mind map data from KB metadata
make mindmap       # Open interactive mind map locally
make check-links   # Validate all internal markdown links
make validate      # Run all checks (kb-sync + links + PII scan)
make pii-scan      # Scan for confidential terms (requires config)
```

### PII Scanner

The repo includes a configurable PII scanner to prevent accidental leaks when you add your own content:

```bash
# Set up your scan terms
cp scripts/.pii-terms.example.json scripts/.pii-terms.json
# Edit .pii-terms.json with your confidential terms
make pii-scan
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Contributions welcome:
- New knowledge base topics (with `@mindmap` metadata)
- Coding practice solutions
- System design walkthroughs
- Bug fixes and improvements

## Contributors

- [Prasanth](https://github.com/prasanth-ntu) — Knowledge base, mind map, templates, tooling

## License

MIT — see [LICENSE](LICENSE) for details.
