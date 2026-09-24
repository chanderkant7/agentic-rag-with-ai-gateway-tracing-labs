# RAG and Agentic AI using LangChain, LiteLLM AI Gateway, and MLflow

A hands-on, notebook-based path from your first clean LLM call to a traced, measured healthcare insurance claim approval agent. Along the way you build prompt workflows, retrieval-augmented generation (RAG) with ChromaDB, tool-using agents, and multi-agent systems, one working notebook at a time.

The labs are built to be forgiving on a normal laptop: OpenAI-compatible clients, optional LiteLLM AI Gateway routing, repository-relative file paths that work wherever you launch Jupyter, and optional local MLflow tracing so you can see what every model call and agent step actually did.

📖 **Prefer to read first?** Every module has a companion article. Start with the [series overview on Medium](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399), or browse the Markdown versions in [`blogs/`](blogs/README.md).

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

For direct provider access, omit `OPENAI_BASE_URL` if your SDK should use its default endpoint. For LiteLLM, point `OPENAI_BASE_URL` at the running gateway. Never commit your real `.env`; it is already listed in `.gitignore`.

### Install Lab Dependencies

Each executable module has a setup notebook. Run the matching setup notebook before starting that module:

| Area | Setup notebook | Manual dependency bundle |
| --- | --- | --- |
| Module 2 | `Module2/.setup/learner_setup.ipynb` | `Module2/module2/2/shim.txt` |
| Module 3 | `Module3/.setup/learner_setup.ipynb` | `Module3/.setup/module3/2/shim.txt` |
| Module 4 | `Module4/.setup/learner_setup.ipynb` | `Module4/module4/2/shim.txt` |
| Project | `Project/.setup/learner_setup.ipynb` | `Project/project/2/shim.txt` |

The setup notebooks install the pinned packages for that module and then restart the notebook kernel. Pinning matters more than it sounds: when one person runs the labs locally, another on Databricks, and another on a locked-down corporate laptop, a shared package baseline saves a lot of "works on my machine" debugging.

## Local Services

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

Open the MLflow UI at `http://127.0.0.1:5000`. If the server is not running, the notebooks skip experiment selection and carry on, so tracing is always optional.

## Learning Path

Each step builds on the one before it. If you are new to LLM apps, go in order; if you already know the basics, jump straight to Module 3 for RAG or Module 4 for agents.

| Step | Area | Focus | Read the articles |
| --- | --- | --- | --- |
| 1 | [Module 1: Foundations](Module1/README.md) | LLM concepts, environment setup, provider configuration, and shared notebook utilities | [Intro](https://chanderkant-sharma.medium.com/module-1-intro-why-this-ai-learning-path-matters-5c83e617be30) · [1.1](https://chanderkant-sharma.medium.com/module-1-1-llm-foundations-without-the-hype-94c07a745c19) · [1.2](https://chanderkant-sharma.medium.com/module-1-2-from-prompts-to-real-applications-4acdc6ba9338) |
| 2 | [Module 2: LLM Workflow Basics](Module2/README.md) | OpenAI-compatible clients, prompt engineering, patient sentiment analysis, and clinical dialogue summarization | [Intro](https://chanderkant-sharma.medium.com/module-2-intro-your-first-practical-llm-workflow-b767002d5fd2) · [2.1](https://chanderkant-sharma.medium.com/module-2-1-connecting-to-openai-compatible-apis-and-writing-better-prompts-dc3c8c55f4ec) · [2.2](https://chanderkant-sharma.medium.com/module-2-2-sentiment-analysis-and-summarization-that-feel-useful-95f1b11e4af9) |
| 3 | [Module 3: Advanced RAG with ChromaDB](Module3/README.md) | PDF loading, chunking, embeddings, ChromaDB retrieval, reranking, chat-over-docs, and DeepEval RAG evaluation | [Intro](https://chanderkant-sharma.medium.com/module-3-intro-why-rag-gets-serious-after-the-first-demo-6ce1283631c3) · [3.1](https://chanderkant-sharma.medium.com/module-3-1-pdfs-chunking-embeddings-and-chromadb-e878da4be031) · [3.2](https://chanderkant-sharma.medium.com/module-3-2-retrieval-re-ranking-and-rag-evaluation-1001b93b1c41) |
| 4 | [Module 4: Agentic AI](Module4/README.md) | Tool calling, ReAct agents, HealthBuddy, multi-user conversation memory, appointment booking, and multi-agent SOP assistance | [Intro](https://chanderkant-sharma.medium.com/module-4-intro-from-chatbots-to-agents-that-use-tools-848d84b62a6e) · [4.1](https://chanderkant-sharma.medium.com/module-4-1-tools-react-and-agent-loops-1fc5334d5b14) · [4.2](https://chanderkant-sharma.medium.com/module-4-2-multi-user-and-multi-agent-systems-e45f19a14bb3) |
| 5 | [Project: Healthcare Insurance Claim Approval Agent](Project/README.md) | ReAct-based claim approval, policy reasoning, validation against human references, and submission generation | [Intro](https://chanderkant-sharma.medium.com/sample-project-intro-building-a-healthcare-insurance-claim-approval-agent-a1e3915b712a) · [Part 1](https://chanderkant-sharma.medium.com/sample-project-part-1-designing-the-healthcare-claim-approval-workflow-1b6dbf3a5cc4) · [Part 2](https://chanderkant-sharma.medium.com/sample-project-part-2-measuring-agent-performance-against-humans-2f4c03798b72) |

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
- `setup_mlflow_tracing(...)` creates per-notebook MLflow experiments under `llm-rag-agents-gateway-labs/...`, so prompt experiments, RAG runs, and agent traces never get mixed together.
- ChromaDB vector stores (`*.db/` folders) are built locally the first time you run the RAG notebooks and are ignored by git. The first run creates embeddings through your configured model, so expect a few embedding calls.
- DeepEval and tokenizer cache files are local development artifacts used by the RAG labs.
- Module 2 contains two historical filename typos: `02_Prompt_Ebginnering.ipynb` and `03_Seniment_Analysis.ipynb`. The links use the actual filenames.

## Resources

- [LangChain Docs](https://python.langchain.com/) - RAG and agent framework
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/) - graph-based orchestration
- [MLflow Docs](https://mlflow.org/docs/latest/) - tracing and monitoring
- [OpenAI Python SDK](https://github.com/openai/openai-python) - OpenAI-compatible client usage
- [ChromaDB Docs](https://docs.trychroma.com/) - vector database
- [DeepEval Docs](https://docs.confident-ai.com/) - RAG and LLM evaluation
- [LiteLLM Docs](https://docs.litellm.ai/) - multi-provider routing

## Feedback

If you run the labs, I would genuinely like to hear where the path felt smooth and where it slowed you down. Open an issue with what broke, what clicked, or what you would like covered next; it makes the series better for the next learner.
