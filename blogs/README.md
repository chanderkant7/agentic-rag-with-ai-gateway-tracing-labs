# RAG and Agentic AI Labs: Blog Series

This folder holds the Markdown source for the blog series that walks through these labs. Every post is published on Medium, and the drafts here are kept in sync with the published versions, so you can read on whichever side you prefer.

The series is written for India-based developers, data engineers, ML engineers, architects, and students who want a guided route from their first clean LLM call to a traced, measured claim approval agent. Each post picks up where the previous one left off.

## Reading Order


### Series overview

| Post | Read on Medium | Markdown draft |
| --- | --- | --- |
| RAG and Agentic AI Labs with LiteLLM AI Gateway & MLflow Tracing | [Medium](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399) | [Intro.md](Intro.md) |

### Module 1: Foundations

| Post | Read on Medium | Markdown draft |
| --- | --- | --- |
| Module 1 Intro: Why This AI Learning Path Matters | [Medium](https://chanderkant-sharma.medium.com/module-1-intro-why-this-ai-learning-path-matters-5c83e617be30) | [module1/intro.md](module1/intro.md) |
| Module 1.1: LLM Foundations Without the Hype | [Medium](https://chanderkant-sharma.medium.com/module-1-1-llm-foundations-without-the-hype-94c07a745c19) | [module1/part-1.md](module1/part-1.md) |
| Module 1.2: From Prompts to Real Applications | [Medium](https://chanderkant-sharma.medium.com/module-1-2-from-prompts-to-real-applications-4acdc6ba9338) | [module1/part-2.md](module1/part-2.md) |

### Module 2: LLM Workflow Basics

| Post | Read on Medium | Markdown draft |
| --- | --- | --- |
| Module 2 Intro: Your First Practical LLM Workflow | [Medium](https://chanderkant-sharma.medium.com/module-2-intro-your-first-practical-llm-workflow-b767002d5fd2) | [module2/intro.md](module2/intro.md) |
| Module 2.1: Connecting to OpenAI-Compatible APIs and Writing Better Prompts | [Medium](https://chanderkant-sharma.medium.com/module-2-1-connecting-to-openai-compatible-apis-and-writing-better-prompts-dc3c8c55f4ec) | [module2/part-1.md](module2/part-1.md) |
| Module 2.2: Sentiment Analysis and Summarization That Feel Useful | [Medium](https://chanderkant-sharma.medium.com/module-2-2-sentiment-analysis-and-summarization-that-feel-useful-95f1b11e4af9) | [module2/part-2.md](module2/part-2.md) |

### Module 3: Advanced RAG with ChromaDB

| Post | Read on Medium | Markdown draft |
| --- | --- | --- |
| Module 3 Intro: Why RAG Gets Serious After the First Demo | [Medium](https://chanderkant-sharma.medium.com/module-3-intro-why-rag-gets-serious-after-the-first-demo-6ce1283631c3) | [module3/intro.md](module3/intro.md) |
| Module 3.1: PDFs, Chunking, Embeddings, and ChromaDB | [Medium](https://chanderkant-sharma.medium.com/module-3-1-pdfs-chunking-embeddings-and-chromadb-e878da4be031) | [module3/part-1.md](module3/part-1.md) |
| Module 3.2: Retrieval, Re-ranking, and RAG Evaluation | [Medium](https://chanderkant-sharma.medium.com/module-3-2-retrieval-re-ranking-and-rag-evaluation-1001b93b1c41) | [module3/part-2.md](module3/part-2.md) |

### Module 4: Agentic AI

| Post | Read on Medium | Markdown draft |
| --- | --- | --- |
| Module 4 Intro: From Chatbots to Agents That Use Tools | [Medium](https://chanderkant-sharma.medium.com/module-4-intro-from-chatbots-to-agents-that-use-tools-848d84b62a6e) | [module4/intro.md](module4/intro.md) |
| Module 4.1: Tools, ReAct, and Agent Loops | [Medium](https://chanderkant-sharma.medium.com/module-4-1-tools-react-and-agent-loops-1fc5334d5b14) | [module4/part-1.md](module4/part-1.md) |
| Module 4.2: Multi-user and Multi-agent Systems | [Medium](https://chanderkant-sharma.medium.com/module-4-2-multi-user-and-multi-agent-systems-e45f19a14bb3) | [module4/part-2.md](module4/part-2.md) |

### Sample Project: Healthcare Insurance Claim Approval

| Post | Read on Medium | Markdown draft |
| --- | --- | --- |
| Sample Project Intro: Building a Healthcare Insurance Claim Approval Agent | [Medium](https://chanderkant-sharma.medium.com/sample-project-intro-building-a-healthcare-insurance-claim-approval-agent-a1e3915b712a) | [project/intro.md](project/intro.md) |
| Sample Project Part 1: Designing the Healthcare Claim Approval Workflow | [Medium](https://chanderkant-sharma.medium.com/sample-project-part-1-designing-the-healthcare-claim-approval-workflow-1b6dbf3a5cc4) | [project/part-1.md](project/part-1.md) |
| Sample Project Part 2: Measuring Agent Performance Against Humans | [Medium](https://chanderkant-sharma.medium.com/sample-project-part-2-measuring-agent-performance-against-humans-2f4c03798b72) | [project/part-2.md](project/part-2.md) |

## What Each Post Includes

- A title and subtitle that match the published Medium post
- Suggested tags for Medium
- A link to this repository and a short LiteLLM setup note
- Notebook snippets taken from the matching lab, with the notebook path named above each snippet
- A short feedback prompt specific to that post
- Series navigation to the previous and next posts, the series overview, and the module README

## Visual Assets

Diagrams live in [`assets/`](assets/) and are referenced through GitHub raw URLs, so they render both on GitHub and on Medium.

## Voice Notes

These are the writing principles the series follows. They are worth keeping if you add a new post:

- Write like a senior teammate walking someone through the lab, not like a manual announcing features.
- Keep technical claims precise, and use lived examples where they help: broken notebooks, client demos, messy PDFs, support tickets, and evaluation surprises.
- Open each post by connecting it to the one before, and close by pointing to the one after.
- Prefer short, direct transitions over phrases like "this article explores" or "in conclusion."
- Make every feedback request specific to the post, so the ending feels personal rather than repeated.

## Keeping Drafts and Medium in Sync

When you edit a post, update both the Markdown draft and the Medium post. Inside the drafts, keep series navigation pointing at the full Medium URLs, including the post ID at the end, because Medium does not resolve the shorter slug-only links.
