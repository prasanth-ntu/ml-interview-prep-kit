# Add Knowledge Base Topic

> Copy this prompt into your AI assistant (Claude, ChatGPT, Gemini, Cursor, etc.)

## When to Use

When you encounter a topic during interview prep that you need to learn or review, and want to add it to your personal knowledge base in a structured format optimized for quick review and interview recall.

## Prompt

```
Help me create a structured knowledge base entry for an ML/AI/Data Science topic.

## Topic

{topic-name}

## Context

Why I need this: {e.g., "Came up in a system design interview", "Gap identified in prep tracker", "Prerequisite for understanding X"}

## What I Already Know

{Brief description of your current understanding — helps the AI calibrate depth}

## Your Tasks

Create a knowledge base entry with this two-layer structure:

### Layer 1: Quick Reference (for interview recall)

- **One-liner**: A crisp, 1-sentence definition I can use to open an interview answer
- **Key comparison table**: Compare this topic with related alternatives (e.g., "Batch vs Stream processing", "L1 vs L2 regularization")
- **When to use / When not to use**: Decision criteria in bullet points
- **Common interview question + model answer**: The most likely question about this topic and a strong 2-3 sentence answer
- **Gotchas**: Common misconceptions or traps interviewers test for

### Layer 2: Deep Understanding (for follow-up questions)

- **How it works**: Detailed explanation with math/pseudocode if relevant
- **Trade-offs**: Detailed pros/cons with specific scenarios
- **Real-world examples**: Where this is used in production systems
- **Related topics**: Cross-references to other concepts I should review alongside this
- **Q&A pairs**: 3-5 progressively harder questions with answers

## Format Rules

- Use markdown with clear headers
- Tables for comparisons (not prose)
- Code blocks for any formulas, pseudocode, or examples
- Keep Layer 1 scannable in under 2 minutes
- Layer 2 can be as detailed as needed
- Include "See also:" links to related topics
```

## Example Usage

**Input**: "Topic: Attention Mechanisms. Context: Came up in a transformer architecture discussion. I know the basic idea of Q/K/V but couldn't explain multi-head attention clearly."

**Output**: A structured knowledge base entry with a quick-reference section for interview recall and a detailed section for deep understanding, tailored to your current knowledge level.
