# RAG and Agentic AI using LangChain, LiteLLM AI Gateway, and MLflow

This repository is a notebook-based learning path for building LLM applications, retrieval-augmented generation (RAG) systems, tool-using agents, multi-agent workflows, and a healthcare insurance claim approval capstone. The labs use OpenAI-compatible clients, optional LiteLLM AI Gateway routing, repository-relative file paths, and optional localhost MLflow tracing.

## Quick Start

### Prerequisites

- Python 3.10+ recommended
- Jupyter Notebook, JupyterLab, or VS Code notebooks
- An API key for an OpenAI-compatible chat model
- An embedding model key for the RAG labs
- Optional: LiteLLM AI Gateway for multi-provider routing
- Optional: MLflow for local trace collection

### Create an Environment

Linux/macOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv .venv
source .venv/bin/activate
```

Windows:

```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
uv venv .venv
.venv\Scripts\activate
```

### Configure Credentials

Copy [`.env.example`](.env.example) to `.env` and update the values for your provider or gateway:

```env
OPENAI_API_KEY="sk-xxxxxxxx"
OPENAI_BASE_URL="http://127.0.0.1:4000"
CHAT_MODEL_NAME="groq/llama-3.1-8b-instant"
EMBEDDING_MODEL_NAME="openrouter/openai/text-embedding-3-small"
LITELLM_MASTER_KEY="sk-xxxxxxxx"
STORE_MODEL_IN_DB=True
```

For direct provider access, omit `OPENAI_BASE_URL` if your SDK should use its default endpoint. For LiteLLM, point `OPENAI_BASE_URL` at the running gateway.

### Install Lab Dependencies

Each executable module has a setup notebook. Run the matching setup notebook before starting that module:

| Area | Setup notebook | Manual dependency bundle |
| --- | --- | --- |
| Module 2 | `Module2/.setup/learner_setup.ipynb` | `Module2/module2/2/shim.txt` |
| Module 3 | `Module3/.setup/learner_setup.ipynb` | `Module3/.setup/module3/2/shim.txt` |
| Module 4 | `Module4/.setup/learner_setup.ipynb` | `Module4/module4/2/shim.txt` |
| Project | `Project/.setup/learner_setup.ipynb` | `Project/project/2/shim.txt` |

The setup notebooks install the pinned packages for that module and then restart the notebook kernel.

## Optional Services

### LiteLLM AI Gateway

The notebooks read `OPENAI_API_KEY`, `OPENAI_BASE_URL`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` from `.env`, so the same code can call a direct provider or a LiteLLM gateway.

A sample gateway config is provided in [config.yaml](config.yaml). Start a local gateway with:

```bash
pip install 'litellm[proxy]'
litellm --config config.yaml --port 4000
```

Export any provider keys referenced by your gateway config, such as `GROQ_API_KEY` or `GEMINI_API_KEY`.

### MLflow Tracing

The executable notebooks call `setup_mlflow_tracing(...)` from [Module1/notebook_utils.py](Module1/notebook_utils.py). Start MLflow from the repository root if you want traces:

```bash
mlflow server \
  --host 127.0.0.1 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns
```

Open the MLflow UI at `http://127.0.0.1:5000`. If the server is not running, the notebooks skip experiment selection and continue.

## Learning Path

| Step | Area | Focus |
| --- | --- | --- |
| 1 | [Module 1: Foundations](Module1/README.md) | LLM concepts, environment setup, provider configuration, and shared notebook utilities |
| 2 | [Module 2: LLM Workflow Basics](Module2/README.md) | OpenAI-compatible clients, prompt engineering, patient sentiment analysis, and clinical dialogue summarization |
| 3 | [Module 3: Advanced RAG with ChromaDB](Module3/README.md) | PDF loading, chunking, embeddings, ChromaDB retrieval, reranking, chat-over-docs, and DeepEval RAG evaluation |
| 4 | [Module 4: Agentic AI](Module4/README.md) | Tool calling, ReAct agents, HealthBuddy, multi-user conversation memory, appointment booking, and multi-agent SOP assistance |
| 5 | [Project: Healthcare Insurance Claim Approval Agent](Project/README.md) | ReAct-based claim approval, policy reasoning, validation against human references, and submission generation |

## Notebook Map

### Module 2

- [01_OpenAI_Connection.ipynb](Module2/01_OpenAI_Connection.ipynb) - configure and test OpenAI-compatible chat and embedding clients.
- [02_Prompt_Ebginnering.ipynb](Module2/02_Prompt_Ebginnering.ipynb) - practice zero-shot, few-shot, chain-of-thought, tree-of-thought, and stateful prompting.
- [03_Seniment_Analysis.ipynb](Module2/03_Seniment_Analysis.ipynb) - classify patient/caregiver review sentiment and extract emotional signals.
- [04_Text_Summarization.ipynb](Module2/04_Text_Summarization.ipynb) - summarize doctor-patient conversations into structured clinical notes.

### Module 3

Use `Module3/Part1` for the active RAG build labs:

- [01_Read Pdf File.ipynb](Module3/Part1/01_Read%20Pdf%20File.ipynb) - load and extract research PDF text with LangChain.
- [02_DataChunking.ipynb](Module3/Part1/02_DataChunking.ipynb) - compare fixed, recursive, sentence-based, and semantic chunking.
- [03_DocumentEmbeddings.ipynb](Module3/Part1/03_DocumentEmbeddings.ipynb) - generate Word2Vec and OpenAI-compatible embeddings.
- [04_ChromaDB Data Retrieval and Re-ranking in RAG.ipynb](Module3/Part1/04_ChromaDB%20Data%20Retrieval%20and%20Re-ranking%20in%20RAG.ipynb) - build semantic and hybrid retrieval with ChromaDB, BM25, and LLM reranking.
- [05_TalkToData.ipynb](Module3/Part1/05_TalkToData.ipynb) - assemble a conversational RAG pipeline over healthcare research content.

Use `Module3/Part2` for RAG evaluation:

- [RAG_Evaluation_SinglePDF.ipynb](Module3/Part2/RAG_Evaluation_SinglePDF.ipynb) - evaluate retrieval and generation quality on one focused PDF.
- [RAG_Evaluation_MultiplePDF.ipynb](Module3/Part2/RAG_Evaluation_MultiplePDF.ipynb) - compare multi-PDF retrieval, noise, faithfulness, hallucination, and G-Eval behavior.

`Module3/Module2` and `Module3/Module5` contain legacy mirrors of the same curriculum.

### Module 4

- [01_ImplementingToolsForAgenticAI.ipynb](Module4/01_ImplementingToolsForAgenticAI.ipynb) - define tools, inspect tool-call requests, and manually execute tool responses.
- [02_BuildingToolsReactAgenticAIBuiltin.ipynb](Module4/02_BuildingToolsReactAgenticAIBuiltin.ipynb) - build HealthBuddy with LangGraph's `create_react_agent`.
- [03_BuildingToolsReactAgenticAIScratch.ipynb](Module4/03_BuildingToolsReactAgenticAIScratch.ipynb) - recreate the ReAct loop with explicit LangGraph state, nodes, and edges.
- [04_BuildingMultiUserConversationalAgenticAI.ipynb](Module4/04_BuildingMultiUserConversationalAgenticAI.ipynb) - add multi-turn memory, multi-user sessions, appointment slots, and booking tools.
- [05_BuildingMultiAgentSystem.ipynb](Module4/05_BuildingMultiAgentSystem.ipynb) - coordinate specialist agents for HR, Finance, and IT SOP questions.

### Project

- [code.ipynb](Project/code.ipynb) - build a healthcare insurance claim approval agent with patient summarization, policy guideline interpretation, coverage evaluation, validation benchmarking, and final submission export.

## Shared Conventions

- `repo_path(...)` keeps notebook data paths stable regardless of where Jupyter is launched.
- `setup_mlflow_tracing(...)` creates per-notebook MLflow experiments under `llm-rag-agents-gateway-labs/...`.
- ChromaDB and DeepEval cache files are local development artifacts used by the RAG labs.
- Module 2 contains two historical filename typos: `02_Prompt_Ebginnering.ipynb` and `03_Seniment_Analysis.ipynb`. The links use the actual filenames.

## Resources

- [LangChain Docs](https://python.langchain.com/) - RAG and agent framework
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/) - graph-based orchestration
- [MLflow Docs](https://mlflow.org/docs/latest/) - tracing and monitoring
- [OpenAI Python SDK](https://github.com/openai/openai-python) - OpenAI-compatible client usage
- [ChromaDB Docs](https://docs.trychroma.com/) - vector database
- [DeepEval Docs](https://docs.confident-ai.com/) - RAG and LLM evaluation
- [LiteLLM Docs](https://docs.litellm.ai/) - multi-provider routing
