# Module 2 Intro: Your First Practical LLM Workflow

Subtitle: Leave "LLM theory" behind and start running notebooks that connect, prompt, classify, and summarize.

Tags: AI, OpenAI, Prompt Engineering, MLflow, India Tech, LiteLLM

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

Quick setup note: The notebooks use OpenAI-compatible clients. If you run LiteLLM, point `OPENAI_BASE_URL` at the gateway, set `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`, and keep `LITELLM_MASTER_KEY` aligned with your gateway config. The details are in [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Module 2 LLM workflow diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module2-llm-workflow.png)

Image: Module 2 turns model access into a repeatable notebook workflow, with gateway-aware configuration and MLflow tracing built in.

Module 1 gave us the mental model: tokens, prompts, context, and the idea that a prompt is only one piece of a workflow. Module 2 is where that thinking finally meets running code.

Here you stop only talking about tokens, prompts, and context windows, and start running notebooks that actually call models, process text, and produce useful output. Not world-changing yet, but useful enough that you can picture the same workflow inside a support tool, a hospital dashboard, an internal ops assistant, or an analytics pipeline.

For many Indian tech teams, this is the sweet spot. You probably do not need a complicated multi-agent system on day one. What you need first is a stable way to call an LLM, write a sensible prompt, classify text, and summarize long conversations, without every run turning into a debugging session.

That is Module 2 in a nutshell.

## What You Build In Module 2

Module 2 has four notebooks, and each one builds on the last:

- OpenAI-compatible connection setup
- Prompt engineering
- Sentiment analysis
- Text summarization

On paper, these sound simple. In practice, they teach patterns you will see again and again in real LLM apps:

- How to configure API access
- How to make model calls repeatable
- How to design prompts with clear instructions
- How to turn messy text into structured outputs
- How to evaluate whether the result is useful

This is also where the repo's newer setup improvements start helping. Each notebook has an `Initial setup` cell, uses repository-relative paths through `repo_path(...)`, and can send traces to a local MLflow server.

## Notebook Map

These are the Python notebooks behind Module 2:

```text
Module2/01_OpenAI_Connection.ipynb
Module2/02_Prompt_Ebginnering.ipynb
Module2/03_Seniment_Analysis.ipynb
Module2/04_Text_Summarization.ipynb
```

The first notebook simply proves that the chat and embedding clients work, through either a direct provider or the LiteLLM gateway:

```python
chat_client = openai.OpenAI(api_key=api_key, base_url=base_url)
embedding_client = openai.OpenAI(api_key=api_key, base_url=base_url)

response = embedding_client.embeddings.create(
    input=["hello from litellm"],
    model=embedding_model_name,
)
```

## Why Start With Connection Setup?

Because API setup breaks far more often than anyone admits.

Wrong key. Wrong endpoint. Wrong model name. An expired credential. An environment variable that never loaded. A notebook opened from the wrong folder. Everyone who has built an LLM app has lost an afternoon to at least one of these.

So the first notebook makes sure the plumbing works before you build any logic on top of it. It is not glamorous, but it saves real time. The whole-afternoon kind of real time.

Think of it like checking your laptop charger before a client demo. Basic, but life-saving.

## Why Prompt Engineering Still Matters

Prompt engineering attracts plenty of debate. Some people overhype it. Others dismiss it entirely. The practical truth sits somewhere in the middle.

Prompting is not a replacement for good software design, but it is still the interface between your app and the model. A vague prompt gives vague output. A clear prompt gives you a fighting chance.

Module 2 treats prompting as an engineering skill, not a bag of magic phrases:

- Give the model a role only when it helps
- Specify the output format
- Add examples when the task is ambiguous
- Control tone and length
- Reduce randomness for classification-style tasks

This is the kind of prompt engineering that survives well beyond demo day.

## Why Sentiment Analysis And Summarization?

Because almost every team is sitting on piles of text, and these two patterns turn that text into something useful.

Sentiment analysis shows how an LLM can sort text into business-friendly categories. With the healthcare review dataset, the model is not just generating text. It is helping you understand customer or patient feedback at scale.

Summarization shows another essential pattern: compressing long text into something actionable. Think call transcripts, support tickets, meeting notes, claims documents, and internal reports.

In Indian companies, where teams often handle high volumes with lean operations, these two workflows can deliver value almost immediately.

## MLflow Makes The Learning Visible

Module 2 is also where local MLflow tracing enters the picture. Start the MLflow server before running the notebooks, and each notebook's setup cell logs traces under its own experiment.

Now you can inspect what happened instead of guessing. Which model call ran? Which experiment did it belong to? Did the notebook skip tracing because the server was offline? Those details matter while you are learning, and even more when you are debugging.

## Where This Leads

Module 2 is not the destination. It is the bridge.

Once you can connect to a model, write good prompts, classify text, and summarize content, you are ready for Module 3: PDFs, embeddings, ChromaDB, retrieval, and evaluation.

That is where LLM apps start answering from the knowledge in your documents, not just what fits in a prompt. But first, Module 2.1 makes that very first model call boringly reliable.

## Feedback

If you try Module 2, tell me where your first successful model call happened, and where things got stuck. Setup stories are not glamorous, but they are exactly what make these labs better.

## Series Navigation

- Previous: [Module 1.2](https://chanderkant-sharma.medium.com/module-1-2-from-prompts-to-real-applications-4acdc6ba9338)
- Next: [Module 2.1: Connecting to OpenAI-Compatible APIs and Writing Better Prompts](https://chanderkant-sharma.medium.com/module-2-1-connecting-to-openai-compatible-apis-and-writing-better-prompts-dc3c8c55f4ec)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399)
- Lab notebooks: [Module2 README](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/Module2/README.md)
