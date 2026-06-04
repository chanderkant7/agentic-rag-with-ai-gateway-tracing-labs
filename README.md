# RAG and Agentic AI using LangChain, LiteLLM AI Gateway, and MLflow

This repository contains notebook-based labs for LLM application development, RAG systems, agentic AI, LiteLLM AI Gateway routing, and an insurance validation project. The active lab notebooks now use per-module dependency files, repository-relative paths, and optional localhost MLflow tracing.

## Quick Setup

### Prerequisites
- Python 3.10+ recommended
- API keys for LLM providers (OpenAI, Groq, OpenRouter, etc.)
- Jupyter or a notebook environment that supports `%pip`
- Optional: a local MLflow tracking server for traces
- Optional: LiteLLM AI Gateway for multi-provider routing

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

### Quick LiteLLM AI Gateway Setup
To set up the LiteLLM AI Gateway with the Admin UI and Master Key locally without Docker, follow these exact steps.

#### Prerequisites
You must have a PostgreSQL database running locally on your machine. LiteLLM requires it to track user spend, virtual keys, and UI configurations.
------------------------------
#### Step 1: Install LiteLLM
Install the proxy server package using python pip:

pip install 'litellm[proxy]'

#### Step 2: Create config.yaml
Create a configuration file to link your upstream models and your database.

model_list:
  - model_name: gpt-4o
    litellm_params:
      model: openai/gpt-4o
      api_key: "os.environ/OPENAI_API_KEY"
general_settings:
  master_key: "sk-master-key-1234" # 🔑 Admin key to lock down the API
  database_url: "postgresql://<user>:<password>@localhost:5432/<db_name>" # Your local Postgres URI

#### Step 3: Export Environment Variables
Set your model provider keys and your UI login credentials in your terminal session:

#### Provider API Keys
export OPENAI_API_KEY="your-actual-openai-key"
#### Admin UI Login Credentials
export UI_USERNAME="admin"
export UI_PASSWORD="your-secure-password"

#### Step 4: Run the Gateway
Launch the server. LiteLLM will automatically initialize the required tables in your PostgreSQL database:

litellm --config config.yaml

------------------------------
## Step 5: Test and Access

* Admin UI Dashboard: Open your web browser and log in at http://localhost:4000/ui using your username and password.

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

## Module Overview

### Learning Progression

This repository is structured as a progressive learning path from foundational LLM concepts through advanced agentic systems:

**Module 1 → Module 2 → Module 3 → Module 4 → Project**

Each module builds on the previous, introducing new concepts and techniques incrementally.

### Module 1: Foundations
Foundation concepts including LLM fundamentals, LangChain basics, and provider setup for Module 2-4 labs. Provides utilities (`repo_path()`, `setup_mlflow_tracing()`) used across all modules.

### Module 2: RAG Basics
Introduction to OpenAI-compatible APIs, prompt engineering, sentiment analysis, and text summarization using retrieval-augmented generation patterns. First executable notebooks with basic LLM applications.

### Module 3: Advanced RAG with ChromaDB
Deep dive into document processing, embeddings, vector storage with ChromaDB, retrieval ranking, and comprehensive RAG evaluation techniques for single and multiple documents. Builds production-ready RAG systems.

### Module 4: Agentic AI
Building intelligent agents using the ReAct framework with LangGraph. Progressively construct **HealthBuddy**, a healthcare assistant that demonstrates:
- Tool-use agents with web/PubMed search and doctor recommendations
- Multi-user conversational AI with session management
- Multi-agent systems with inter-agent communication
- Advanced reasoning and decision-making patterns

### Project: Insurance Agent Validation
End-to-end implementation of an intelligent insurance validation agent with multi-agent coordination, performance comparison against human validators, and comprehensive metrics reporting.

## LiteLLM AI Gateway

The notebooks use OpenAI-compatible client settings, so they can call either a direct provider endpoint or a LiteLLM AI Gateway. When `USE_LITELLM=1`, use:

- `OPENAI_BASE_URL` for the LiteLLM gateway URL, usually `http://0.0.0.0:4000`
- `LITELLM_MASTER_KEY` for the gateway key
- `CHAT_MODEL_NAME` for chat/completion calls
- `EMBEDDING_MODEL_NAME` for embedding calls

This lets the same notebook code switch between providers such as OpenAI-compatible, Groq, OpenRouter, or similar deployments through a gateway configuration instead of rewriting notebook logic.

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

- [LangChain Docs](https://python.langchain.com/) - Agent and RAG framework
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/) - Graph-based orchestration
- [MLflow Docs](https://mlflow.org/docs/latest/) - Tracing and monitoring
- [OpenAI Python SDK](https://github.com/openai/openai-python) - LLM access
- [ChromaDB Docs](https://docs.trychroma.com/) - Vector database
- [uv Package Manager](https://github.com/astral-sh/uv) - Fast Python packaging
- [LiteLLM Docs](https://docs.litellm.ai/) - Multi-provider routing

## Overall Goals

This repository aims to provide a comprehensive learning experience for building production-quality LLM applications:

1. **Foundation**: Understand LLM concepts and basic integration
2. **Retrieval**: Master RAG systems for context-aware generation
3. **Intelligence**: Build reasoning agents that use tools effectively
4. **Scale**: Implement multi-agent systems for complex tasks
5. **Evaluation**: Benchmark agent performance against human baselines
6. **Flexibility**: Support multiple LLM providers through LiteLLM gateway

By completing this progression, learners will be equipped to:
- Design and implement LLM applications from scratch
- Build production-ready RAG systems
- Create intelligent agents with tool use
- Evaluate and optimize system performance
- Route requests through multiple providers
- Monitor and trace system behavior
