# Prompt Templates

Reusable prompts for AI-assisted interview preparation workflows. Each template is a copy-paste-ready prompt designed to work with any AI assistant.

## What Are These?

Prompt templates are structured instructions that you paste into an AI tool to perform a specific interview prep task. They encode a workflow (e.g., "debrief after an interview") into a repeatable, consistent prompt with placeholders for your specific details.

Think of them as macros for interview preparation — instead of figuring out how to ask the AI to help you each time, you grab the template, fill in the blanks, and get structured output.

## How to Use

### With Any Chat-Based AI (Claude, ChatGPT, Gemini)

1. Open the template file
2. Copy the content inside the `## Prompt` section (the part inside the code fence)
3. Replace the `{placeholders}` with your actual details
4. Paste into your AI chat
5. Follow any interactive instructions (e.g., the drill template will ask you questions one at a time)

### With Claude Code / Gemini CLI / Aider

These templates work as prompts in any CLI-based AI tool. You can:
- Paste the prompt directly into the chat
- Reference your local files by path (replace `{your-repo}/` with your actual path)
- The AI can read and update your files directly

### With Cursor / Windsurf / VS Code + AI

1. Open your interview prep repository in the editor
2. Open the AI chat panel
3. Paste the prompt template
4. The AI can reference and edit files in your workspace directly

## Templates

| Template | File | Description |
|----------|------|-------------|
| **Interview Debrief** | [interview-debrief.md](interview-debrief.md) | Analyze your performance after an interview round using notes or a transcript |
| **Prep Drill Session** | [interview-prep-drill.md](interview-prep-drill.md) | Run an interactive mock interview tailored to your upcoming round |
| **Set Up Interview Round** | [setup-interview-round.md](setup-interview-round.md) | Create a structured prep-and-notes document for a scheduled round |
| **New Company Setup** | [new-company-setup.md](new-company-setup.md) | Bootstrap a complete interview tracking workspace for a new company |
| **Add Knowledge Topic** | [add-knowledge-topic.md](add-knowledge-topic.md) | Create a structured knowledge base entry for an ML/AI topic |
| **Check Broken Links** | [check-broken-links.md](check-broken-links.md) | Scan your markdown files for broken internal links after restructuring |

## Tips

- **Customize the prompts** for your situation. These are starting points, not rigid scripts.
- **Chain templates** for a full workflow: New Company Setup -> Set Up Interview Round -> Prep Drill -> Interview Debrief.
- **Save the output** as markdown files in your prep repository for future reference.
- **Iterate**: If the AI's first output isn't quite right, refine your inputs rather than starting over.
