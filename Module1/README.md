# Module 1: Foundations

## Overview

This module covers foundational Large Language Model (LLM) concepts, provider integration, and the lab environment setup before hands-on RAG and Agentic AI labs in Modules 2-4. The repository contains documentation and utility functions for later modules; executable notebook labs begin in Module 2.

## Learning Objectives

- Understand how LLMs work at a conceptual level
- Learn the lab environment and infrastructure used by later modules
- Understand provider integration and API authentication
- Build simple LLM applications using LangChain
- Master prompting techniques and model behavior control
- Set up development environments and dependencies
- Configure and use MLflow for tracing

## Getting Started

1. Create and activate a virtual environment from the repository root:
```bash
uv venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows
```

2. Configure API keys in a `.env` file at the repository root (copy from `.env.example`):
```env
OPENAI_API_KEY="sk-xxxxxxxx"
OPENAI_BASE_URL="https://api.openai.com/v1"
CHAT_MODEL_NAME="gpt-4o-mini"
EMBEDDING_MODEL_NAME="text-embedding-3-small"
```

3. Continue to Module 2 for the first executable lab notebooks and run `Module2/.setup/learner_setup.ipynb` before those labs.

## Prerequisites

- Python 3.10+ recommended
- Basic Python knowledge
- API key for at least one LLM provider (OpenAI recommended)
- Familiarity with terminal/command line
- Jupyter Notebook or VS Code environment

## Module Contents

This module provides foundational knowledge and utilities:

- **Concepts**: How LLMs work, tokens, context windows, model behavior
- **LangChain Basics**: Prompts, model calls, chains, retrieval basics
- **Provider Setup**: Authentication, API keys, environment variables
- **Utilities**: `notebook_utils.py` with `repo_path()` and `setup_mlflow_tracing()`
- **Simple Applications**: Basic chatbots, Q&A systems, text generation examples

## Key Concepts

- **Tokens**: Discrete units of text processed by LLMs
- **Context Window**: Maximum number of tokens an LLM can process
- **Embeddings**: Dense vector representations of text
- **Prompt Engineering**: Crafting inputs to get desired outputs
- **Chain of Thought**: Encouraging step-by-step reasoning
- **Few-Shot Learning**: Providing examples to guide behavior
- **Temperature & Sampling**: Controlling randomness in outputs

## Utilities

The `Module1/notebook_utils.py` provides helper functions used across all modules:

- `repo_path(...)`: Construct paths relative to repository root (supports any working directory)
- `setup_mlflow_tracing(...)`: Configure MLflow tracing with proper experiment naming
- Environment loading and variable management

These utilities ensure notebooks work correctly regardless of where they're opened from.

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
