# Module 1: Foundations

Module 1 is the orientation layer for the notebook labs. It introduces the environment, provider configuration, shared utilities, and the LLM concepts learners need before running the hands-on notebooks in Modules 2-4 and the capstone project.

There are no executable lab notebooks in this module. The first runnable labs begin in [Module 2](../Module2/README.md).

## What This Module Covers

- How LLMs process prompts, tokens, context windows, and generated outputs
- Why embeddings matter for retrieval and semantic search
- How OpenAI-compatible chat and embedding clients are configured
- How LiteLLM can route the same notebook code to different providers
- How MLflow tracing is wired into later notebooks
- How repository-relative paths keep notebooks portable

## Shared Utilities

[notebook_utils.py](notebook_utils.py) provides two helpers used throughout the repository:

- `repo_path(...)`: builds absolute paths from the repository root, so notebooks can load data reliably from any working directory.
- `setup_mlflow_tracing(...)`: sets the MLflow tracking URI, selects a per-notebook experiment, and enables OpenAI and LangChain autologging when those packages are available.

## Setup

Create and activate an environment from the repository root:

```bash
uv venv .venv
source .venv/bin/activate
```

On Windows:

```bash
uv venv .venv
.venv\Scripts\activate
```

Copy the root [`.env.example`](../.env.example) to `.env` and provide the values your notebooks should use:

```env
OPENAI_API_KEY="sk-xxxxxxxx"
OPENAI_BASE_URL="http://127.0.0.1:4000"
CHAT_MODEL_NAME="groq/llama-3.1-8b-instant"
EMBEDDING_MODEL_NAME="openrouter/openai/text-embedding-3-small"
```

For direct OpenAI-compatible provider calls, leave `OPENAI_BASE_URL` unset if you want the SDK default. For LiteLLM, set it to the gateway URL.

## Optional MLflow Tracing

Start MLflow from the repository root before running later notebooks if you want traces:

```bash
mlflow server \
  --host 127.0.0.1 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns
```

Executable notebooks in later modules use `http://127.0.0.1:5000` by default. If MLflow is unavailable, the helper logs a skip message and lets the notebook continue.

## Next Step

Continue with [Module 2: LLM Workflow Basics](../Module2/README.md) to run the first notebooks: API connection, prompt engineering, patient sentiment analysis, and clinical conversation summarization.
