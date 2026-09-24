# RAG and Agentic AI Labs with LiteLLM AI Gateway & MLflow Tracing

Subtitle: A hands-on path from your first clean LLM call to a traced, measured claim approval agent, built one working notebook at a time.

Tags: Generative AI, RAG, LangChain, MLflow, AI Agents, LiteLLM

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

![RAG and Agentic AI labs learning path](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/series-learning-path.png)

Image: The full route runs from LLM foundations to practical workflows, RAG, agents, and a claim approval capstone, with LiteLLM handling model access and MLflow keeping every step visible.

Most of us have followed an AI tutorial that looked brilliant on the first run. Some are too theoretical to use on a Monday morning. Some jump straight into complex agents before explaining a single API call. And some work perfectly once, then break the moment you reopen the notebook from a different folder.

I wanted this series to feel closer to how learning actually happens: one working notebook at a time, with enough explanation to understand what you are doing and enough structure to debug calmly when something goes sideways. Because something always goes sideways.

We begin with foundations, then move through OpenAI-compatible workflows, RAG with ChromaDB, agentic AI, and finally a healthcare insurance claim approval project that pulls everything together. Each post picks up where the previous one left off, so the ideas build on each other instead of arriving as disconnected tricks. The tone stays friendly, but the work keeps its engineering backbone.

If you are an India-based developer, student, data engineer, backend engineer, ML engineer, architect, or product builder trying to make sense of LLM applications, think of this as a guided route through the noise. You do not need to be an AI researcher. Some Python, a little patience, and curiosity about why things work will take you a long way.

## What This Series Covers

The route has five stops, and each one prepares you for the next:

- Module 1: LLM foundations and application thinking, so the model stops feeling like a black box
- Module 2: OpenAI-compatible setup, prompts, sentiment analysis, and summarization, so model access becomes boringly reliable
- Module 3: Advanced RAG with PDFs, chunking, embeddings, ChromaDB, retrieval, and evaluation, so answers stay grounded in real evidence
- Module 4: Agentic AI with tools, ReAct loops, multi-user flows, and multi-agent systems, so the model can act safely inside a workflow
- Sample Project: A healthcare insurance claim approval agent measured against human decisions, where everything above gets tested on a real task

The real win is not a demo that answers once. It is understanding how LLM workflows are structured, traced, evaluated, and improved after that first exciting output appears, which is exactly where most real projects begin.

## Tech Stack

Under the hood, the labs use a practical Python stack. Nothing exotic, just tools you are likely to meet in real projects:

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

You can call models directly, or route OpenAI-compatible requests through a LiteLLM AI Gateway. I like the gateway path because it puts one notebook interface in front of multiple backend providers, and gives you one place to manage keys and model names instead of scattering them across every notebook.

The `.env.example` template uses:

```env
OPENAI_API_KEY="sk-xxxxxxxx"
OPENAI_BASE_URL="http://127.0.0.1:4000"
CHAT_MODEL_NAME="groq/llama-3.1-8b-instant"
EMBEDDING_MODEL_NAME="openrouter/openai/text-embedding-3-small"
LITELLM_MASTER_KEY="sk-xxxxxxxx"
STORE_MODEL_IN_DB=True
```

In plain English:

- `OPENAI_BASE_URL` points the OpenAI-compatible client at the LiteLLM gateway.
- `OPENAI_API_KEY` is the key the notebooks send; for a protected LiteLLM gateway, use the gateway key here.
- `CHAT_MODEL_NAME` controls the model used for chat and reasoning calls.
- `EMBEDDING_MODEL_NAME` controls the model used for embedding and RAG workflows.
- `LITELLM_MASTER_KEY` keeps your gateway configuration explicit when you manage LiteLLM locally.

So the same lab flow can run against gateway-backed providers such as Groq or OpenRouter without rewriting the notebook logic. Change the model in one place, and the notebooks follow along.

## MLflow Tracing

The lab notebooks include `Initial setup` cells that configure MLflow tracing through `Module1/notebook_utils.py` via `setup_mlflow_tracing(...)`.

To capture traces locally, start MLflow from the repository root before you run any notebook:

```bash
mlflow server \
  --host 127.0.0.1 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns
```

Then open `http://127.0.0.1:5000` to inspect experiments and traces.

Each notebook gets its own MLflow experiment, so your Module 2 prompt experiments never get tangled with Module 4 agent traces or the sample project runs. When something looks odd, you will know exactly where to look.

## Why The Setup Matters

The repo quietly does a few things that save a lot of pain later:

- Per-module setup notebooks
- Per-module pinned dependency bundles (`shim.txt` plus `constraints.txt`)
- Repository-relative paths through `repo_path(...)`
- Separate MLflow experiments per notebook

None of this will ever trend on social media. But these small details keep a learning day from turning into a path-debugging session. When one person runs the labs on a laptop, another on Databricks, and another on a locked-down corporate machine, that quiet reliability matters more than any clever prompt.

## Notebook Code Map

Here are the notebooks behind the articles, in case you want to jump from reading straight into runnable Python. Right after it, you will find the full reading list, module by module:

```text
Module2/01_OpenAI_Connection.ipynb
Module2/02_Prompt_Ebginnering.ipynb
Module2/03_Seniment_Analysis.ipynb
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

### Module 2: LLM Workflow Basics

- [Module 2 Intro: Your First Practical LLM Workflow](module2/intro.md)
- [Module 2.1: Connecting to OpenAI-Compatible APIs and Writing Better Prompts](module2/part-1.md)
- [Module 2.2: Sentiment Analysis and Summarization That Feel Useful](module2/part-2.md)

### Module 3: Advanced RAG with ChromaDB

- [Module 3 Intro: Why RAG Gets Serious After the First Demo](module3/intro.md)
- [Module 3.1: PDFs, Chunking, Embeddings, and ChromaDB](module3/part-1.md)
- [Module 3.2: Retrieval, Re-ranking, and RAG Evaluation](module3/part-2.md)

### Module 4: Agentic AI

- [Module 4 Intro: From Chatbots to Agents That Use Tools](module4/intro.md)
- [Module 4.1: Tools, ReAct, and Agent Loops](module4/part-1.md)
- [Module 4.2: Multi-user and Multi-agent Systems](module4/part-2.md)

### Sample Project: Healthcare Insurance Claim Approval

- [Sample Project Intro: Building a Healthcare Insurance Claim Approval Agent](project/intro.md)
- [Sample Project Part 1: Designing the Healthcare Claim Approval Workflow](project/part-1.md)
- [Sample Project Part 2: Measuring Agent Performance Against Humans](project/part-2.md)

## How To Read The Series

If you are new to LLM apps, read in order. Each post builds on the one before it:

```text
Foundations -> prompts -> RAG -> agents -> sample project
```

Already comfortable with the basics? Jump into Module 3 for RAG or Module 4 for agents. And if evaluation and business workflows are what you care about most, spend time with the sample project posts. That is where the series gets closest to day-to-day AI engineering work.

## Reading on Medium

Prefer a reading view? The whole series is published on Medium, starting with the [series overview](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399). The links above stay inside this repository so you can jump straight from an article to its notebooks.

## Feedback

If you run the labs, I would genuinely love to hear where the path felt smooth and where it slowed you down. A quick note about what broke, what clicked, or what you would like covered next will make the series better for the next learner.

Ready? Let us start where every dependable AI system starts: with the foundations. Module 1 Intro is the first stop.

## Series Navigation

- Next: [Module 1 Intro: Why This AI Learning Path Matters](https://chanderkant-sharma.medium.com/module-1-intro-why-this-ai-learning-path-matters-5c83e617be30)
- Lab notebooks: [Repository README](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs#readme)
