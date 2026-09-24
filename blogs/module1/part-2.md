# Module 1.2: From Prompts to Real Applications

Subtitle: Take the ideas from Module 1.1 out of single prompts and into small workflows you can debug, trace, and improve.

Tags: AI Engineering, MLflow, LangChain, Generative AI, India Tech, LiteLLM

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

Quick setup note: The notebooks use OpenAI-compatible clients. If you run LiteLLM, point `OPENAI_BASE_URL` at the gateway, set `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`, and keep `LITELLM_MASTER_KEY` aligned with your gateway config. The details are in [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![LLM application foundations diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module1-foundations.png)

Image: A prompt is just one piece. Setup, context, output handling, and tracing turn it into an application.

In Module 1.1, we looked at what the model actually sees: tokens, prompts, context, and temperature. Once those click, the next question arrives quickly: how do we turn this into something useful?

Not "useful" as in a flashy demo that works once during a presentation. Useful as in something an engineer, analyst, support team, or operations manager can run again and again without holding their breath.

That is where the real AI engineering mindset starts to show up.

## A Prompt Is Only One Piece

Most of us begin with prompts because prompts are visible. You type something, the model replies, and it feels interactive and alive. But production-style LLM applications need a lot more than a good prompt.

They need:

- Inputs that are clean enough
- Instructions that are specific enough
- Model parameters that are stable enough
- Outputs that are structured enough
- Logs or traces that make debugging possible
- Evaluation that tells you whether things improved

That is why this repo adds setup notebooks, dependency constraints, repository-relative paths, and MLflow tracing to the later modules. None of this is decoration. These are the boring pieces that make labs reproducible for everyone, not just the person who wrote them.

And in engineering, boring is often the highest compliment.

## Think in Workflows

Let us make this concrete. Suppose you are building a summarizer for customer support calls.

The naive workflow looks like this:

```text
Send transcript to model -> get summary
```

The practical workflow looks more like this:

```text
Load transcript
Clean text
Choose prompt template
Call model
Validate summary shape
Log trace
Review output
Iterate
```

That difference matters. The first version is a demo. The second is the beginning of an application, because every step can be checked when something goes wrong.

Module 2 builds exactly this muscle, through OpenAI-compatible connection checks, prompt engineering, sentiment analysis, and summarization.

## Why Repository-relative Paths Matter

If you have spent time with notebooks, you know this pain well: a file loads perfectly on your machine, then fails for your teammate because they opened the notebook from a different folder.

The repo now uses `repo_path(...)` from `Module1/notebook_utils.py` so notebooks can find data files from the repository root consistently.

It is a small change with a big effect. It keeps your attention on AI concepts instead of path debugging. Nobody wants to spend a Sunday evening fixing a duplicated module folder path.

## Why MLflow Tracing Is Useful Early

MLflow tracing is not just for production ML teams. It is genuinely useful while you are still learning.

With tracing, you can see:

- Which notebook produced the run
- Which model or chain was called
- What happened during a prompt or agent step
- Whether a failure came from setup, model access, retrieval, or tool logic

The repo uses a local MLflow server on `http://127.0.0.1:5000`. Each notebook gets its own experiment, so your Module 2 prompt work does not get mixed with Module 4 agent traces.

So your experiments never turn into one big mixed pile.

## Notebook Snippet: Per-notebook Tracing

Every executable notebook has a small tracing cell. For example, `Module2/01_OpenAI_Connection.ipynb` uses:

```python
from Module1.notebook_utils import setup_mlflow_tracing

setup_mlflow_tracing(
    "llm-rag-agents-gateway-labs/Module2/01_OpenAI_Connection"
)
```

That experiment name is what keeps each notebook's traces neatly separated in the MLflow UI.

## The Learning Path Ahead

Module 1 gives you the language of LLM engineering. From here, the series moves into hands-on labs:

- Module 2: call models, write prompts, classify sentiment, summarize text
- Module 3: process PDFs, chunk documents, create embeddings, use ChromaDB, evaluate RAG
- Module 4: build tools, ReAct agents, multi-user systems, and multi-agent workflows
- Sample Project: approve or route healthcare insurance claims and compare agent performance with human reference results

Each step adds one more layer of system thinking, and each one leans on the last.

## A Practical Mindset for Indian Builders

In India, many AI projects are built under very real constraints: small teams, tight timelines, mixed data quality, budget pressure, and stakeholders who want visible results quickly.

The best way to handle that is not to memorize every framework. It is to understand the workflow and keep your system observable.

Start simple. Make it work. Trace it. Evaluate it. Improve it. That rhythm is slower than the hype, but it is much kinder to real teams.

That rhythm is what the rest of this series is built on. Module 2 puts it into practice with your first hands-on LLM workflow: a clean model call, a better prompt, and two small tasks that map neatly to real business problems.

## Feedback

If you have run notebooks that broke because of paths, packages, or hidden setup assumptions, I would love to hear which fixes helped you most here. Those tiny workflow details are worth getting right.

## Series Navigation

- Previous: [Module 1.1](https://chanderkant-sharma.medium.com/module-1-1-llm-foundations-without-the-hype-94c07a745c19)
- Next: [Module 2 Intro: Your First Practical LLM Workflow](https://chanderkant-sharma.medium.com/module-2-intro-your-first-practical-llm-workflow-b767002d5fd2)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399)
- Lab notebooks: [Module1 README](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/Module1/README.md)
