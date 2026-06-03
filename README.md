# RAG and Agentic AI using LangChain, LiteLLM AI Gateway, and MLflow

This repository contains notebook-based labs for LLM application development, RAG systems, agentic AI, LiteLLM AI Gateway routing, and an insurance validation project. The active lab notebooks now use per-module dependency files, repository-relative paths, and optional localhost MLflow tracing.

## Quick Setup

### Prerequisites
- Python 3.10+ recommended
- API keys for the providers used in each lab, usually OpenAI, Azure OpenAI, or models routed through LiteLLM
- Jupyter or a notebook environment that supports `%pip`
- Optional: a local MLflow tracking server for traces

### Create an Environment

**Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
uv venv .venv
.venv\Scripts\activate
```

Each module has its own setup notebook and pinned dependency set. Start a module by running its setup notebook:

- `Module2/.setup/learner_setup.ipynb`
- `Module3/.setup/learner_setup.ipynb`
- `Module4/.setup/learner_setup.ipynb`
- `Project/.setup/learner_setup.ipynb`

Those setup notebooks install from the matching `requirements.txt` and `constraints.txt` files under each module or project package directory.

### Quick MLflow Setup

MLflow is installed by the Module2, Module3, Module4, and Project setup notebooks. Start a local tracking server before running lab notebooks if you want traces:

```bash
mlflow server \
  --host 127.0.0.1 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns
```

Open the MLflow UI at `http://127.0.0.1:5000`. The notebooks use this URL by default and create separate experiments per notebook.

### Configure API Keys and AI Gateway

Create a `.env` file in the project root. For direct OpenAI-compatible access, define your provider key. For LiteLLM AI Gateway access, route calls through `OPENAI_BASE_URL` and set model names through environment variables:

```env
LITELLM_MASTER_KEY="sk-xxxxxxxx"
OPENAI_API_KEY="sk-xxxxxxxx"
OPENAI_ADMIN_KEY="sk-xxxxxxxx"
OPENAI_BASE_URL="http://0.0.0.0:4000"
CHAT_MODEL_NAME="groq/openai/gpt-oss-20b"
EMBEDDING_MODEL_NAME="openrouter/openai/text-embedding-3-small"
USE_LITELLM=1
```

See [`.env.example`](.env.example) for the current template.

## LiteLLM AI Gateway

The notebooks use OpenAI-compatible client settings, so they can call either a direct provider endpoint or a LiteLLM AI Gateway. When `USE_LITELLM=1`, use:

- `OPENAI_BASE_URL` for the LiteLLM gateway URL, usually `http://0.0.0.0:4000`
- `LITELLM_MASTER_KEY` for the gateway key
- `CHAT_MODEL_NAME` for chat/completion calls
- `EMBEDDING_MODEL_NAME` for embedding calls

This lets the same notebook code switch between providers such as OpenAI-compatible, Groq, OpenRouter, or Azure-style deployments through a gateway configuration instead of rewriting notebook logic.

## MLflow Tracing

The Module2, Module3, Module4, and Project lab notebooks include an initial setup cell that enables MLflow tracing through `Module1/notebook_utils.py` via `setup_mlflow_tracing(...)`. Use the quick setup command above to start the local MLflow server before running notebooks.

By default, notebooks use `http://127.0.0.1:5000`. Each notebook writes to a separate MLflow experiment named after its module or project path. If MLflow is not running, the helper skips experiment selection and the notebook can continue.

## Path Handling

Notebook file paths now use `repo_path(...)` from `Module1/notebook_utils.py` instead of shell working-directory assumptions. This keeps data, setup, and cache paths stable when notebooks are opened from different locations.

## Current Dependency Baseline

The dependency files were refreshed to near-latest compatible versions. Important pins include:

- `openai==2.40.0`
- `mlflow==3.13.0`
- `langchain==1.3.4`
- `langchain-community==0.4.2`
- `langchain-openai==1.2.2`
- `langgraph==1.2.4`
- `chromadb==1.5.9`
- `pandas==2.3.3`

`pandas` remains on the latest compatible 2.x release because MLflow 3.13 requires `pandas<3`.

## Modules & Content

### **Module 1: Foundations**
Introductory examples covering basic LLM concepts and LangChain fundamentals.

### **Module 2: RAG Basics**
Retrieve documents and generate answers with:
- OpenAI Connection setup
- Prompt Engineering
- Sentiment Analysis on Patient Reviews
- Text Summarization on conversation datasets

### **Module 3: Advanced RAG with ChromaDB**
- Document embedding and chunking strategies
- ChromaDB data retrieval and re-ranking
- PDF processing and RAG evaluation
- Single and multi-PDF RAG systems

### **Module 4: Agentic AI**
Building intelligent agents with tools:
- React Agents (with/without built-in tools)
- Multi-user Conversational AI
- Multi-Agent Systems
- Tool implementation for agents

## Project: Insurance Agent Validation

End-to-end project implementing an intelligent insurance validation agent:
- **Data**: Insurance policies, reference codes, test records
- **Features**:
  - Multi-agent validation workflow
  - Human vs Agent performance comparison
  - Comprehensive test result analysis
  - Validation accuracy metrics

**Key Files**:
- `code.ipynb` - Complete implementation
- `validation_records.json` - Test dataset
- `agent_validation_records_results.csv` - Agent results
- `human_vs_agent_comparison.csv` - Performance comparison

## Resources

- [LangChain Docs](https://python.langchain.com/)
- [MLflow Docs](https://mlflow.org/docs/latest/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [uv Package Manager](https://github.com/astral-sh/uv)

## License

Educational purposes
