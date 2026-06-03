# Medium Blog Series: RAG and Agentic AI Labs

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

- Suggested tags: `AI`, `LangChain`, `RAG`, `MLflow`, `Generative AI`
- Mention the LiteLLM AI Gateway setup when publishing technical intros: `USE_LITELLM=1`, `OPENAI_BASE_URL`, `LITELLM_MASTER_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME`.
- Publish in the order below so the "Previous" and "Next" links can be replaced with live Medium URLs as each post goes up.
- Medium supports Markdown paste reasonably well, but review code blocks and headings after pasting.
- Keep each post's first paragraph punchy; Medium previews usually pull from the opening text.
- Use the `Subtitle:` line as Medium's subtitle and remove that label after pasting if you prefer a cleaner post.
- Use the `Tags:` line as the tag source and remove that line from the final Medium body.
- Relative links work inside the repo only. Replace them with published Medium links from [chanderkant-sharma.medium.com](https://chanderkant-sharma.medium.com) after each post goes live.
