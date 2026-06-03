# Module 1.2: From Prompts to Real Applications

Subtitle: Move from isolated prompts to workflows that are easier to debug, trace, and improve.

Tags: AI Engineering, MLflow, LangChain, Generative AI, India Tech, LiteLLM

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

AI Gateway note: These labs can route OpenAI-compatible calls through LiteLLM. Set `USE_LITELLM=1`, `OPENAI_BASE_URL`, `LITELLM_MASTER_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`; see the [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![LLM application foundations diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module1-foundations.png)

Image: The practical pieces around a prompt matter: setup, context, output handling, and tracing.

Once you understand the basics of LLMs, the next question comes quickly: how do we turn this into something useful?

Not "useful" as in a flashy demo that works once during a presentation. Useful as in something an engineer, analyst, support team, or operations manager can run repeatedly without holding their breath.

That is where the real AI engineering mindset starts.

## A Prompt Is Only One Piece

Most people begin with prompts because prompts are visible. You type something, the model replies, and it feels interactive. But production-style LLM applications need more than a prompt.

They need:

- Inputs that are clean enough
- Instructions that are specific enough
- Model parameters that are stable enough
- Outputs that are structured enough
- Logs or traces that make debugging possible
- Evaluation that tells you whether things improved

That is why the later modules in this repo add setup notebooks, dependency constraints, repository-relative paths, and MLflow tracing. These are not decoration. They are the boring pieces that make labs reproducible.

And in engineering, boring is often a compliment.

## Think in Workflows

Suppose you are building a summarizer for customer support calls.

The naive workflow is:

```text
Send transcript to model -> get summary
```

The practical workflow is:

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

That difference matters. The first version is a demo. The second version is the beginning of an application.

Module 2 builds exactly this kind of muscle through OpenAI connection checks, prompt engineering, sentiment analysis, and summarization.

## Why Repository-relative Paths Matter

If you have worked with notebooks, you know the pain: a file loads on your machine, then fails for your teammate because the notebook was opened from a different folder.

The repo now uses `repo_path(...)` from `Module1/notebook_utils.py` so notebooks can find data files from the repository root consistently.

This is a small change with a big effect. It keeps the learning focused on AI concepts instead of path debugging. Nobody wants to spend Sunday evening fixing a duplicated module folder path.

## Why MLflow Tracing Is Useful Early

MLflow tracing is not only for production ML teams. It is also useful when you are learning.

With tracing, you can inspect:

- Which notebook produced the run
- Which model or chain was called
- What happened during a prompt or agent step
- Whether a failure came from setup, model access, retrieval, or tool logic

The repo uses a local MLflow server on `http://127.0.0.1:5000`. Each notebook gets its own experiment, so your Module 2 prompt work does not get mixed with Module 4 agent traces.

That makes experimentation cleaner.

## Notebook Snippet: Per-notebook Tracing

Every executable notebook has a small tracing cell. For example, `Module2/01_OpenAI_Connection.ipynb` uses:

```python
from Module1.notebook_utils import setup_mlflow_tracing

setup_mlflow_tracing(
    "llm-rag-agents-gateway-labs/Module2/01_OpenAI_Connection"
)
```

That experiment name is what keeps each notebook's traces separated in the MLflow UI.

## The Learning Path Ahead

Module 1 gives you the language of LLM engineering. Now the series moves into hands-on labs:

- Module 2: call models, write prompts, classify sentiment, summarize text
- Module 3: process PDFs, chunk documents, create embeddings, use ChromaDB, evaluate RAG
- Module 4: build tools, ReAct agents, multi-user systems, and multi-agent workflows
- Sample Project: validate insurance records and compare agent performance with human results

Each step adds one layer of system thinking.

## A Practical Mindset for Indian Builders

In India, many AI projects are built under real constraints: small teams, fast timelines, mixed data quality, budget pressure, and stakeholders who want visible results quickly.

The best way to handle that is not to memorize every framework. It is to understand the workflow and keep your system observable.

Start simple. Make it work. Trace it. Evaluate it. Improve it. That rhythm is slower than hype, but it is much kinder to real teams.

That is the rhythm of the rest of this series.

## Feedback

If you have run notebooks that broke because of paths, packages, or hidden setup assumptions, I would love to hear which fixes helped most here. Those small workflow details are worth getting right.

## Series Navigation

- Previous: [Module 1.1: LLM Foundations Without the Hype](https://chanderkant-sharma.medium.com/module-1-1-llm-foundations-without-the-hype)
- Next: [Module 2 Intro: Your First Practical LLM Workflow](https://chanderkant-sharma.medium.com/module-2-intro-your-first-practical-llm-workflow)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-main-intro)
