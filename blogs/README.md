# RAG and Agentic AI Labs

This folder contains Medium.com-ready blog drafts for the lab series. The tone is practical, warm, and conversational, aimed at India-based tech learners, engineers, and builders who want to move from LLM basics to RAG, agents, and a capstone validation project without feeling lost in jargon.

Each post includes:

- A Medium-style title
- Subtitle text near the top
- Suggested tags
- Internal series navigation links
- Repository documentation links where useful

## Publishing Order

### Series Landing Post
- [Main Intro: RAG and Agentic AI Labs](Intro.md)

### Module 1: Foundations
- [Intro: Why This AI Learning Path Matters](module1/intro.md)
- [Module 1.1: LLM Foundations Without the Hype](module1/part-1.md)
- [Module 1.2: From Prompts to Real Applications](module1/part-2.md)

### Module 2: RAG Basics
- [Intro: Your First Practical LLM Workflow](module2/intro.md)
- [Module 2.1: Connecting to OpenAI and Writing Better Prompts](module2/part-1.md)
- [Module 2.2: Sentiment Analysis and Summarization That Feel Useful](module2/part-2.md)

### Module 3: Advanced RAG with ChromaDB
- [Intro: Why RAG Gets Serious After the First Demo](module3/intro.md)
- [Module 3.1: PDFs, Chunking, Embeddings, and ChromaDB](module3/part-1.md)
- [Module 3.2: Retrieval, Re-ranking, and RAG Evaluation](module3/part-2.md)

### Module 4: Agentic AI
- [Intro: From Chatbots to Agents That Use Tools](module4/intro.md)
- [Module 4.1: Tools, ReAct, and Agent Loops](module4/part-1.md)
- [Module 4.2: Multi-user and Multi-agent Systems](module4/part-2.md)

### Sample Project: Insurance Agent Validation
- [Sample Project Intro: Building an Insurance Validation Agent](project/intro.md)
- [Sample Project Part 1: Designing the Validation Workflow](project/part-1.md)
- [Sample Project Part 2: Measuring Agent Performance Against Humans](project/part-2.md)

## Visual Assets

The blog drafts use diagrams and architecture images from `blogs/assets/`. When publishing on Medium, keep the image markdown as-is after the GitHub repository is public, or upload the same assets manually if Medium does not fetch an external image.

## Voice Notes

- Write like a senior teammate is walking the reader through the lab, not like a manual is announcing features.
- Keep the technical claims precise, but use lived examples where they help: broken notebooks, client demos, messy PDFs, support tickets, and evaluation surprises.
- Prefer short, direct transitions over generic phrases such as "this article explores" or "in conclusion."
- Make feedback requests specific to each article so the ending feels personal instead of repeated.

## Medium.com Publishing Notes

### Pre-Publishing Checklist
- **Tags**: Use the tags from each post's YAML header. Primary tags: `Generative AI`, `RAG`, `LangChain`, `MLflow`, `AI Agents`, `LiteLLM`
- **Subtitle**: Each post has a `Subtitle:` line—use it and remove the label
- **Images**: Verify all images load from GitHub raw URLs or replace with Medium-hosted versions
- **Code Blocks**: Review formatting after pasting into Medium
- **Links**: All relative repo links will need to be replaced with live Medium URLs after publication

### Publishing Order
Follow this sequence so "Previous" and "Next" navigation stays correct:

1. [Main Intro: RAG and Agentic AI Labs](Intro.md)
2. [Module 1 Intro](module1/intro.md) → [Part 1](module1/part-1.md) → [Part 2](module1/part-2.md)
3. [Module 2 Intro](module2/intro.md) → [Part 1](module2/part-1.md) → [Part 2](module2/part-2.md)
4. [Module 3 Intro](module3/intro.md) → [Part 1](module3/part-1.md) → [Part 2](module3/part-2.md)
5. [Module 4 Intro](module4/intro.md) → [Part 1](module4/part-1.md) → [Part 2](module4/part-2.md)
6. [Project Intro](project/intro.md) → [Part 1](project/part-1.md) → [Part 2](project/part-2.md)

### Formatting Guidelines
- **First paragraph**: Keep punchy—Medium shows this in previews
- **Code examples**: Include context about which notebook the code comes from
- **AI Gateway note**: Include in all technical posts (already embedded)
- **Call-to-action**: End with a question or reflection specific to each topic
- **Links back**: Consider linking to the full repository at the end

### After Publication
- Replace all Medium.com author links with live post URLs: [chanderkant-sharma.medium.com](https://chanderkant-sharma.medium.com)
- Update navigation links between posts with live Medium URLs
- Update repo's [.env.example](.env.example) with any new configuration examples
