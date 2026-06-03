# Module 2: RAG Basics

## Overview

This module introduces core LLM workflows and early RAG-adjacent patterns using OpenAI-compatible APIs. The notebooks now include initial setup cells for repository-relative paths and localhost MLflow tracing.

## Module Contents

### 1. **01_OpenAI_Connection.ipynb**
- Setting up OpenAI API access
- Authentication and configuration
- Testing basic completion requests
- Understanding API response structures

### 2. **02_Prompt_Ebginnering.ipynb**
- Crafting effective prompts
- Few-shot learning techniques
- Temperature and parameter tuning
- Prompt optimization strategies

### 3. **03_Seniment_Analysis.ipynb**
- Building sentiment classifiers with LLMs
- Using Patient_Reviews.csv dataset
- Multi-class sentiment classification
- Real-world NLP application

### 4. **04_Text_Summarization.ipynb**
- Abstractive and extractive summarization
- Using conversation datasets
- Implementing RAG for context-aware summaries
- Quality metrics for summarization

## Data Files

- `Data/SentimentAnalysis/Patient_Reviews.csv` - Patient review dataset
- `Data/TextSummarization/conversation_*.txt` - Conversation samples for summarization

## Learning Objectives

- Understand RAG fundamentals and use cases
- Retrieve and rank relevant documents
- Integrate retrieval with LLM generation
- Handle different data formats (text, CSV)
- Evaluate RAG system performance

## Prerequisites

- Completion of Module 1
- Basic prompt design knowledge
- OpenAI API key or compatible endpoint credentials

## Running the Notebooks

1. Activate your virtual environment from the repository root.
2. Ensure `.env` has the API keys used by the notebooks.
3. Run `Module2/.setup/learner_setup.ipynb` once for the environment.
4. Open Jupyter:
```bash
jupyter notebook
```
5. Follow notebooks in order.

The setup notebook installs:

```bash
uv pip install -r Module2/module2/2/requirements.txt -c Module2/module2/2/constraints.txt
```

Current key package pins include `openai==2.40.0`, `httpx==0.28.1`, `pandas==2.3.3`, `pydantic==2.13.4`, `python-dotenv==1.2.2`, `tenacity==9.1.4`, and `mlflow==3.13.0`.

## LiteLLM AI Gateway

Module 2 notebooks read `OPENAI_BASE_URL`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` from `.env`, so the same OpenAI-compatible code can call a direct provider or a LiteLLM AI Gateway.

Use the gateway settings from the root `.env.example`:

```env
LITELLM_MASTER_KEY="sk-xxxxxxxx"
OPENAI_BASE_URL="http://0.0.0.0:4000"
CHAT_MODEL_NAME="groq/openai/gpt-oss-20b"
EMBEDDING_MODEL_NAME="openrouter/openai/text-embedding-3-small"
USE_LITELLM=1
```

## MLflow and Paths

Each lab notebook has an `Initial setup` cell that imports `Module1/notebook_utils.py`, enables MLflow tracing, and uses `repo_path(...)` for data paths.

Start MLflow from the repository root before running notebooks if you want traces captured:

```bash
mlflow server \
  --host 127.0.0.1 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns
```

Open the MLflow UI at `http://127.0.0.1:5000`. Module 2 notebooks create separate experiments under names like `llm-rag-agents-gateway-labs/Module2/<notebook-name>`.

If the server is not running, the setup helper skips experiment selection and the notebook continues. You can also override the tracking URI by setting `MLFLOW_TRACKING_URI` before running a notebook.

## Key Concepts

- **Retrieval**: Finding relevant documents from a corpus
- **Context Window**: Using retrieved documents as context
- **Ranking**: Scoring document relevance
- **Generation**: Creating response using retrieved context

## Next Steps

Progress to **Module 3: Advanced RAG with ChromaDB** for production-ready vector databases and advanced retrieval techniques.
