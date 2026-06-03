# Module 1: Foundations

## Overview

This module covers foundational Large Language Model (LLM) concepts before the hands-on RAG and Agentic AI labs in later modules. The repository currently contains documentation for Module 1; executable notebook labs begin in Module 2.

## Learning Objectives

- Understand how LLMs work
- Understand the lab environment used by later modules
- Learn provider integration concepts
- Build simple LLM applications
- Understand prompting and model behavior

## Getting Started

1. Create and activate a virtual environment from the repository root:
```bash
uv venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows
```

2. Configure API keys in a `.env` file at the repository root.

3. Continue to Module 2 for the first executable lab notebooks and run `Module2/.setup/learner_setup.ipynb` before those labs.

## Prerequisites

- Python 3.10+ recommended
- Basic Python knowledge
- API key for at least one LLM provider, with OpenAI or Azure OpenAI recommended for later notebooks

## What You'll Learn

- **LLM Fundamentals**: Transformers, tokens, context windows
- **LangChain Basics**: Prompts, model calls, retrieval, and agent concepts
- **Provider Setup**: API keys, endpoints, and environment variables
- **Simple Applications**: Chatbots, Q&A systems, text generation

## MLflow Tracing

Module 1 is documentation-only in this repository, so there are no Module 1 notebook traces to capture. The executable labs starting in Module 2 include `Initial setup` cells that call `setup_mlflow_tracing(...)` from `Module1/notebook_utils.py`.

When you move to Module 2 or later, start the local MLflow server from the repository root before running notebooks:

```bash
mlflow server \
  --host 127.0.0.1 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns
```

Open the MLflow UI at `http://127.0.0.1:5000` to inspect traces and experiments.

## LiteLLM AI Gateway

Executable labs from Module 2 onward can route OpenAI-compatible calls through a LiteLLM AI Gateway. Configure the root `.env` from `.env.example` with `USE_LITELLM=1`, `OPENAI_BASE_URL`, `LITELLM_MASTER_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` when you want the gateway path.

## Next Steps

After completing Module 1, proceed to **Module 2: RAG Basics** to learn about Retrieval-Augmented Generation.
