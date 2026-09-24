# Module 1 Intro: Why This AI Learning Path Matters

Subtitle: Before RAG, agents, and production-looking demos, let us build the foundations that make everything else easier to debug.

Tags: AI, Generative AI, LangChain, India Tech, LLMs, LiteLLM, MLflow

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

Quick setup note: The notebooks use OpenAI-compatible clients. If you run LiteLLM, point `OPENAI_BASE_URL` at the gateway, set `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`, and keep `LITELLM_MASTER_KEY` aligned with your gateway config. The details are in [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Module 1 foundations diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module1-foundations.png)

Image: Module 1 gets prompts, tokens, context, provider setup, and evaluation clear before we move into RAG or agents.

Welcome to the first stop. If you are arriving from the series index, this is where the real learning begins. If you landed here directly, no worries: this post gives you all the context you need before the hands-on work starts.

If you work in tech in India right now, AI has probably crept into your daily conversations already. Maybe your manager wants a chatbot by next quarter. Maybe your startup wants "AI-powered" somewhere on the roadmap. Maybe your college WhatsApp group is busy debating whether LangChain, RAG, agents, or vector databases are the next big thing.

The problem is not a lack of content. It is that most AI content leaps from "what is a token" to "build a production-grade autonomous agent" before you have even figured out what broke in your first notebook.

So this series starts with foundations. Consider it a feature, not a delay.

Module 1 is the warm-up. It is not about chasing every shiny framework. It is about building the mental model you will lean on later, when you start working with retrieval, tools, agents, and MLflow traces.

Think of it like learning traffic rules before taking a car onto Outer Ring Road at 6 PM. You can technically skip it, but life will become noisy very quickly.

## What Module 1 Is Really About

Module 1 focuses on the ideas that sit underneath every LLM application:

- How LLMs process text
- Why prompts matter
- What tokens and context windows mean in practice
- How API keys and model providers fit into a notebook workflow
- Why the same question can produce different answers
- Where LangChain, RAG, and agents enter the story later

I am not trying to turn you into a researcher. I want you to feel like a practical builder who knows what the model is doing and why.

That matters a lot for Indian teams. Most of us are not working with unlimited GPU budgets. We care about cost, latency, repeatability, and whether the demo still holds up when the client asks the same question slightly differently. Good foundations help with every one of those.

## Why Not Start Directly With RAG?

You can. Many people do. They copy a RAG notebook, drop in a PDF, run a vector search, and get a decent answer. Nice.

But the moment an answer comes back wrong, you need the fundamentals to figure out why:

- Was the prompt unclear?
- Did the model ignore the retrieved context?
- Was the chunk too small?
- Did the API call fail silently?
- Is the output random because temperature is high?
- Are you evaluating the result or just vibing with it?

Without Module 1 thinking, debugging AI apps becomes guesswork. With the basics in place, you can look at a broken notebook and say, "Okay, this is probably a prompt issue" or "This looks like retrieval quality, not model quality."

That calm confidence is the whole point of this module.

## The Bigger Series

This post is the starting line. Here is the road ahead, and each stop builds on the one before it:

- Module 1: Foundations
- Module 2: OpenAI-compatible workflows, prompting, sentiment analysis, and summarization
- Module 3: Advanced RAG with PDFs, chunking, embeddings, ChromaDB, and evaluation
- Module 4: Agentic AI with tools, ReAct loops, multi-user flows, and multi-agent systems
- Sample Project: Healthcare insurance claim approval agent with human-reference comparison

The repo also tries to make the boring parts less painful: per-module setup notebooks, pinned dependencies, repository-relative paths, and optional MLflow tracing on localhost. In practice, that means fewer path errors and a clear window into what the model or chain is doing whenever you want to look.

## First Executable Notebook Preview

Module 1 is foundation material, so the first runnable Python notebook appears in `Module2/01_OpenAI_Connection.ipynb`. It starts by loading gateway-aware model settings from `.env`:

```python
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")
chat_model_name = os.getenv("CHAT_MODEL_NAME")
embedding_model_name = os.getenv("EMBEDDING_MODEL_NAME")

chat_client = openai.OpenAI(
    api_key=api_key,
    base_url=base_url,
)
```

## Who This Is For

You will feel at home here if you are a student, backend engineer, data engineer, ML engineer, solution architect, or product-minded builder who wants to move beyond AI demos into systems you can trust.

If you have written some Python, used notebooks, or called an API, you are ready. If you are new to AI, Module 1 gives you the base. And if you already know the basics, a quick read still helps us share the same vocabulary before Module 2.

## Final Thought

AI engineering is slowly becoming less about one magical prompt and more about systems: inputs, prompts, retrieval, tools, traces, evaluation, and iteration.

Module 1 is where we slow down just enough to build that system-thinking muscle. Everything later in the series leans on it.

## Next Steps

Next, we open the hood. Module 1.1 looks at tokens, prompts, context windows, and temperature, the four ideas that quietly shape every LLM application you will build.

→ **[Read: Module 1.1 – LLM Foundations Without the Hype](part-1.md)**

---

**Questions or feedback?** Let me know how the labs feel as you progress through them. AI engineering is as much about learning-by-doing as it is about reading.

## Feedback

If you are starting this path, tell me what feels obvious and what feels confusing. Foundation posts get better when readers point to the exact moment the picture became clearer, or cloudier.

## Series Navigation

- Previous: [Series index](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399)
- Next: [Module 1.1: LLM Foundations Without the Hype](https://chanderkant-sharma.medium.com/module-1-1-llm-foundations-without-the-hype-94c07a745c19)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399)
- Lab notebooks: [Module1 README](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/Module1/README.md)
