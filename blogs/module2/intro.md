# Module 2 Intro: Your First Practical LLM Workflow

Subtitle: Move from "LLM theory" to notebooks that connect, prompt, classify, and summarize.

Tags: AI, OpenAI, Prompt Engineering, MLflow, India Tech, LiteLLM

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

AI Gateway note: These labs can route OpenAI-compatible calls through LiteLLM. Set `USE_LITELLM=1`, `OPENAI_BASE_URL`, `LITELLM_MASTER_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`; see the [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Module 2 LLM workflow diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module2-llm-workflow.png)

Image: Module 2 turns model access into a repeatable notebook workflow with gateway-aware configuration and MLflow tracing.

If Module 1 was about building the mental model, Module 2 is where the work starts feeling real.

This is the point where you stop only talking about tokens, prompts, and context windows, and start running notebooks that actually call models, process text, and produce useful outputs. Not world-changing yet, but useful enough that you can imagine putting the same workflow inside a support tool, hospital dashboard, internal ops assistant, or analytics pipeline.

For many Indian tech teams, this is the sweet spot. You may not need a complicated multi-agent system on day one. You first need a stable way to call an LLM, write a sensible prompt, classify text, and summarize long conversations without turning every run into a debugging session.

That is exactly what Module 2 covers.

## What You Build In Module 2

Module 2 has four notebooks:

- OpenAI connection setup
- Prompt engineering
- Sentiment analysis
- Text summarization

On paper, these sound simple. In practice, they teach the patterns that show up again and again in real LLM apps:

- How to configure API access
- How to make model calls repeatable
- How to design prompts with clear instructions
- How to turn messy text into structured outputs
- How to evaluate whether the result is useful

This is also where the repo's newer setup improvements start helping. Each notebook has an `Initial setup` cell, uses repository-relative paths through `repo_path(...)`, and can send traces to a local MLflow server.

## Notebook Map

Module 2 uses these Python notebooks:

```text
Module2/01_OpenAI_Connection.ipynb
Module2/02_Prompt_Ebginnering.ipynb
Module2/03_Seniment_Analysis.ipynb
Module2/04_Text_Summarization.ipynb
```

The first notebook proves the model and embedding clients work through either a direct provider or LiteLLM gateway:

```python
chat_client = openai.OpenAI(api_key=api_key, base_url=base_url)
embedding_client = openai.OpenAI(api_key=api_key, base_url=base_url)

response = embedding_client.embeddings.create(
    input=["hello from litellm"],
    model=embedding_model_name,
)
```

## Why Start With Connection Setup?

Because API setup breaks more often than people admit.

Wrong key. Wrong endpoint. Wrong model name. Expired credential. Environment variable not loaded. Notebook opened from the wrong folder. Everyone who has built LLM apps has lost time to these issues.

The first notebook makes sure the plumbing works before you build logic on top of it. It is not glamorous, but it saves real time.

Think of it like checking your laptop charger before a client demo. Basic, but life-saving.

## Why Prompt Engineering Still Matters

There is a lot of debate around prompt engineering. Some people overhype it. Some people dismiss it. The practical truth is in the middle.

Prompting is not a replacement for good software design, but it is still the interface between your app and the model. A vague prompt gives vague output. A clear prompt gives you a fighting chance.

Module 2 treats prompting as an engineering skill:

- Give the model a role only when it helps
- Specify the output format
- Add examples when the task is ambiguous
- Control tone and length
- Reduce randomness for classification-style tasks

This is the kind of prompt engineering that survives beyond demo day.

## Why Sentiment Analysis And Summarization?

Because these are practical, common, and easy to understand.

Sentiment analysis shows how LLMs can classify text into business-friendly categories. In the healthcare review dataset, the model is not just generating text; it is helping you understand customer or patient feedback at scale.

Summarization shows another important pattern: compressing long text into something actionable. This is useful for call transcripts, support tickets, meeting notes, claims documents, and internal reports.

In Indian companies, where teams often handle high volumes with lean operations, these workflows can create immediate value.

## MLflow Makes The Learning Visible

Module 2 also introduces local MLflow tracing. If you start the MLflow server before running notebooks, the setup cell can log traces under a separate experiment for each notebook.

That means you can inspect what happened instead of guessing. Which model call ran? Which experiment did it belong to? Did the notebook skip tracing because the server was offline? These details matter when you are learning and when you are debugging.

## Where This Leads

Module 2 is not the final destination. It is the bridge.

Once you can connect to a model, write prompts, classify text, and summarize content, you are ready for Module 3: retrieval, PDFs, embeddings, ChromaDB, and evaluation.

That is where LLM apps start answering with knowledge from your documents, not only with what fits in the prompt.

## Feedback

If you try Module 2, tell me where the first successful model call happened and where it got stuck. Setup stories are not glamorous, but they are exactly what make these labs better.

## Series Navigation

- Previous: [Module 1.2](https://chanderkant-sharma.medium.com/module-1-2-from-prompts-to-real-applications)
- Next: [Module 2.1](https://chanderkant-sharma.medium.com/module-2-1-connecting-to-openai-and-writing-better-prompts)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-main-intro)
- Repo docs: [Module2 README](https://chanderkant-sharma.medium.com/module-2-intro-your-first-practical-llm-workflow)
