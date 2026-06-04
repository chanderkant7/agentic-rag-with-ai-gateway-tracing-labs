# RAG and Agentic AI Labs with Litellm AI Gateway & MLflow Tracing

Subtitle: A practical Medium.com series for learning LLM apps, RAG, agents, MLflow tracing, and an insurance validation sample project.

Tags: Generative AI, RAG, LangChain, MLflow, AI Agents, LiteLLM

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

![RAG and Agentic AI labs learning path](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/series-learning-path.png)

Image: The full series moves from LLM foundations to practical apps, RAG, agents, and a sample insurance validation project, with LiteLLM and MLflow supporting the workflow.

There are many AI tutorials online. Some are too theoretical. Some jump straight into complex agents. Some look great for one run and then break the moment you reopen the notebook from another folder.

I wanted this series to feel closer to the way real learning happens: one working notebook at a time, with enough explanation to understand what you are doing and enough structure to debug when something goes sideways.

The path starts with foundations, then moves through OpenAI workflows, RAG with ChromaDB, agentic AI, and a sample insurance validation project. The tone is casual, but the work is engineering-first.

If you are an India-based developer, student, data engineer, backend engineer, ML engineer, architect, or product builder trying to make sense of LLM applications, treat this as a guided route through the noise.

## What This Series Covers

The series moves in five stages:

- Module 1: LLM foundations and application thinking
- Module 2: OpenAI connection, prompts, sentiment analysis, and summarization
- Module 3: Advanced RAG with PDFs, chunking, embeddings, ChromaDB, retrieval, and evaluation
- Module 4: Agentic AI with tools, ReAct loops, multi-user flows, and multi-agent systems
- Sample Project: Insurance validation agent with human-versus-agent comparison

The goal is not only to build demos. The goal is to understand how LLM workflows are structured, traced, evaluated, and improved after the first exciting output appears.

## Tech Stack

The repo and blog series use a modern Python-based AI stack:

- **Python 3.10+** for notebooks and utilities
- **Jupyter notebooks** for hands-on labs
- **OpenAI Python SDK** for model calls
- **LiteLLM AI Gateway** for routing OpenAI-compatible calls across providers
- - **OpenAI-compatible APIs** for enterprise and gateway routing scenarios
- **LangChain** for LLM and RAG orchestration
- **LangChain Community** for document loaders and vector store integrations
- **LangChain Text Splitters** for document chunking
- **LangGraph** for agent and graph-style workflows
- **ChromaDB** for vector storage and retrieval
- **rank-bm25** for retrieval support
- **PyMuPDF** for PDF processing
- **Pandas** for tabular analysis and result comparison
- **MLflow 3.x** for local tracing and experiment inspection
- **uv** for Python environment setup
- **python-dotenv** for local environment variables

## LiteLLM AI Gateway

![LiteLLM gateway and MLflow tracing setup](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/gateway-tracing.png)

Image: The notebooks can route model calls through LiteLLM while MLflow records separate traces for each notebook experiment.

The notebooks can call models directly or route OpenAI-compatible requests through a LiteLLM AI Gateway. The gateway path is useful when you want one notebook interface but multiple backend providers.

The `.env.example` template uses:

```env
LITELLM_MASTER_KEY="sk-xxxxxxxx"
OPENAI_API_KEY="sk-xxxxxxxx"
OPENAI_ADMIN_KEY="sk-xxxxxxxx"
OPENAI_BASE_URL="http://0.0.0.0:4000"
CHAT_MODEL_NAME="groq/openai/gpt-oss-20b"
EMBEDDING_MODEL_NAME="openrouter/openai/text-embedding-3-small"
USE_LITELLM=1
```

In simple terms:

- `OPENAI_BASE_URL` points the OpenAI-compatible client at the LiteLLM gateway.
- `LITELLM_MASTER_KEY` is the gateway access key.
- `CHAT_MODEL_NAME` controls the model used for chat and reasoning calls.
- `EMBEDDING_MODEL_NAME` controls the model used for embedding and RAG workflows.
- `USE_LITELLM=1` tells the labs to prefer the gateway route where supported.

That means the same lab flow can work with gateway-backed providers such as Groq or OpenRouter without rewriting the notebook logic.

## MLflow Tracing

The lab notebooks include `Initial setup` cells that configure MLflow tracing through `Module1/notebook_utils.py` via `setup_mlflow_tracing(...)`.

To capture traces locally, start MLflow from the repository root:

```bash
mlflow server \
  --host 127.0.0.1 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns
```

Then open `http://127.0.0.1:5000` to inspect experiments and traces.

Each notebook writes to its own MLflow experiment, which keeps Module 2 prompt experiments separate from Module 4 agent traces and the sample project workflow.

## Why The Setup Matters

The repo uses:

- Per-module setup notebooks
- Pinned `requirements.txt` and `constraints.txt`
- Repository-relative paths through `repo_path(...)`
- Separate MLflow experiments per notebook

These details may sound boring, but they remove the small frustrations that steal attention from learning. When multiple learners or teammates run the same notebooks on different machines, that quiet reliability matters a lot.

## Full Series Links

## Notebook Code Map

Use these notebook names when you want to jump from a Medium article into runnable Python:

```text
Module2/01_OpenAI_Connection.ipynb
Module2/02_Prompt_Engineering.ipynb
Module2/03_Sentiment_Analysis.ipynb
Module2/04_Text_Summarization.ipynb
Module3/Part1/01_Read Pdf File.ipynb
Module3/Part1/02_DataChunking.ipynb
Module3/Part1/03_DocumentEmbeddings.ipynb
Module3/Part1/04_ChromaDB Data Retrieval and Re-ranking in RAG.ipynb
Module3/Part1/05_TalkToData.ipynb
Module3/Part2/RAG_Evaluation_SinglePDF.ipynb
Module3/Part2/RAG_Evaluation_MultiplePDF.ipynb
Module4/01_ImplementingToolsForAgenticAI.ipynb
Module4/02_BuildingToolsReactAgenticAIBuiltin.ipynb
Module4/03_BuildingToolsReactAgenticAIScratch.ipynb
Module4/04_BuildingMultiUserConversationalAgenticAI.ipynb
Module4/05_BuildingMultiAgentSystem.ipynb
Project/code.ipynb
```

### Module 1: Foundations

- [Module 1 Intro: Why This AI Learning Path Matters](module1/intro.md)
- [Module 1.1: LLM Foundations Without the Hype](module1/part-1.md)
- [Module 1.2: From Prompts to Real Applications](module1/part-2.md)

### Module 2: RAG Basics

- [Module 2 Intro: Your First Practical LLM Workflow](module2/intro.md)
- [Module 2.1: Connecting to OpenAI and Writing Better Prompts](module2/part-1.md)
- [Module 2.2: Sentiment Analysis and Summarization That Feel Useful](module2/part-2.md)

### Module 3: Advanced RAG with ChromaDB

- [Module 3 Intro: Why RAG Gets Serious After the First Demo](module3/intro.md)
- [Module 3.1: PDFs, Chunking, Embeddings, and ChromaDB](module3/part-1.md)
- [Module 3.2: Retrieval, Re-ranking, and RAG Evaluation](module3/part-2.md)

### Module 4: Agentic AI

- [Module 4 Intro: From Chatbots to Agents That Use Tools](module4/intro.md)
- [Module 4.1: Tools, ReAct, and Agent Loops](module4/part-1.md)
- [Module 4.2: Multi-user and Multi-agent Systems](module4/part-2.md)

### Sample Project: Insurance Agent Validation

- [Sample Project Intro: Building an Insurance Validation Agent](project/intro.md)
- [Sample Project Part 1: Designing the Validation Workflow](project/part-1.md)
- [Sample Project Part 2: Measuring Agent Performance Against Humans](project/part-2.md)

## How To Read The Series

If you are new to LLM apps, read in order. The concepts build naturally:

```text
Foundations -> prompts -> RAG -> agents -> sample project
```

If you already know the basics, jump into Module 3 for RAG or Module 4 for agents. If you care about evaluation and business workflows, spend time with the sample project posts; that is where the series becomes closest to day-to-day AI engineering work.

## Medium.com Publishing Note

When publishing on Medium.com, use this `Intro.md` as the series landing post. After each article is published, replace the relative links above with the live Medium URLs.

## Feedback

If you run the labs, I would genuinely like to hear where the path felt smooth and where it slowed you down. A small note about what broke, what clicked, or what you want covered next will help make the series better for the next learner.

## Series Navigation

- Next: [Module 1 Intro](https://chanderkant-sharma.medium.com/module-1-intro-why-this-ai-learning-path-matters)
- Index: [Blog README](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-main-intro)
