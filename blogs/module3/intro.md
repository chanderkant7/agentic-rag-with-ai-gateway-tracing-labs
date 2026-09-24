# Module 3 Intro: Why RAG Gets Serious After the First Demo

Subtitle: PDFs, embeddings, ChromaDB, and evaluation are where LLM apps grow into real knowledge systems.

Tags: RAG, ChromaDB, LangChain, Embeddings, India Tech, LiteLLM, MLflow

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

Quick setup note: The notebooks use OpenAI-compatible clients. If you run LiteLLM, point `OPENAI_BASE_URL` at the gateway, set `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`, and keep `LITELLM_MASTER_KEY` aligned with your gateway config. The details are in [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Module 3 RAG pipeline diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module3-rag-pipeline.png)

Image: RAG quality depends on the whole pipeline: PDF extraction, chunks, embeddings, retrieval, re-ranking, answers, and evaluation.

Module 2 ended with a model that could classify and summarize whatever you put in the prompt. Module 3 asks a bigger question: what if the knowledge lives in your documents instead? That is where RAG comes in, and RAG demos are very easy to love.

Upload a PDF, ask a question, get an answer. It feels magical. It also feels dangerously close to something you could ship on Friday.

Then reality shows up.

The answer is wrong. The model missed the one paragraph that mattered. The PDF text extraction is a mess. The chunks are too small. The vector search returns something vaguely related but not actually useful. Then someone asks, "How do we know this is accurate?" and suddenly the demo has become an engineering problem.

That slightly uncomfortable moment is exactly why Module 3 exists.

## What Module 3 Adds

Module 2 taught you how to call models, write prompts, classify text, and summarize content. Module 3 adds the missing piece: external knowledge.

Instead of expecting the model to know everything, you build a workflow that fetches the relevant information from your documents and hands that context to the model along with the question.

Across the module, you will work through:

- Reading PDFs
- Chunking documents
- Creating embeddings
- Storing vectors in ChromaDB
- Retrieving relevant chunks
- Re-ranking results
- Evaluating RAG quality

This is where LLM apps stop being simple prompt wrappers and start looking like real enterprise systems.

## Notebook Map

These are the Python notebooks behind Module 3:

```text
Module3/Part1/01_Read Pdf File.ipynb
Module3/Part1/02_DataChunking.ipynb
Module3/Part1/03_DocumentEmbeddings.ipynb
Module3/Part1/04_ChromaDB Data Retrieval and Re-ranking in RAG.ipynb
Module3/Part1/05_TalkToData.ipynb
Module3/Part2/RAG_Evaluation_SinglePDF.ipynb
Module3/Part2/RAG_Evaluation_MultiplePDF.ipynb
```

The shape of the RAG workflow is visible in `Module3/Module2/05_TalkToData.ipynb`:

```python
def pdf_chatbot_pipeline(file_path, user_query):
    raw_docs = load_pdf_with_langchain(file_path)
    chunks = chunk_documents(raw_docs)
    vectorstore = store_embeddings(chunks, persist_directory="chroma_healthcare.db")
    retrieved = retrieve_chunks(user_query, vectorstore)
    answer = generate_answer(user_query, retrieved)
    return answer
```

## Why RAG Matters So Much

Most Indian companies do not need a model that knows random internet trivia. They need a system that understands their own documents:

- Insurance policies
- SOPs
- Product manuals
- HR policies
- Legal documents
- Support knowledge bases
- Medical or financial records
- Training content

RAG lets you connect a model to this private or domain-specific knowledge without retraining it.

That is a genuine win, especially when your most valuable knowledge is buried in PDFs and internal docs rather than public web pages.

## The Hidden Work: Document Processing

People often talk about RAG as if retrieval is the hard part. Retrieval is hard, yes. But document processing is where many projects stumble first.

PDFs can be messy. Text gets split in odd places. Tables do not always extract cleanly. Headers and footers sneak into chunks. Important context gets separated across pages.

So Module 3 starts with this messy but essential work: reading PDFs, extracting text, and preparing content for chunking.

Good RAG starts long before embeddings. If your source text is bad, your retrieval will be bad too, no matter how clever the rest of the pipeline is.

## Embeddings And ChromaDB

Once documents are chunked, the next step is embeddings. An embedding turns text into a vector, so similar pieces of text can be found through vector search.

ChromaDB stores those vectors and hands back the most relevant chunks for any question.

Put together, the basic RAG loop looks like this:

```text
Question -> embedding -> vector search -> relevant chunks -> prompt -> answer
```

The model still matters, but it is no longer working alone. The retrieval layer gives it the context it needs.

## Why Evaluation Cannot Be Optional

If Module 3 has one serious message, it is this: RAG must be evaluated.

You need honest answers to questions like:

- Did retrieval find the right content?
- Did the answer use the retrieved context?
- Did the model invent anything?
- Does performance improve after changing chunk size?
- Are multi-PDF answers consistent?

Without evaluation, teams often pick whichever answer "looks good." That is not enough for real use cases, especially in domains like insurance or healthcare.

That is why Module 3 includes RAG evaluation notebooks for both single and multiple PDFs. This is where the workflow becomes properly disciplined.

## MLflow Helps You Compare Runs

With local MLflow tracing turned on, each Module 3 notebook gets its own experiment, so you can compare retrieval, prompt, and evaluation runs side by side.

When you change a chunking strategy or a retrieval setting, traces give you a clear way to see what actually happened.

For learning, that is useful. For teams, it is even more useful, because every retrieval change deserves a trail someone can inspect later.

## Where This Leads

Module 3 also prepares you for Module 4. Once you can retrieve knowledge reliably, you can give agents better tools and better context.

Without RAG, an agent is often just a confident chatbot with extra steps. With RAG, an agent can work with real domain knowledge.

That is the bridge from retrieval to agentic AI. But first, Module 3.1 rolls up its sleeves on the less glamorous work: PDFs, chunking, embeddings, and ChromaDB.

## Feedback

If you bring your own PDF into this module, tell me what broke first: extraction, chunking, retrieval, or evaluation. That is usually where the most useful RAG lessons are hiding.

## Series Navigation

- Previous: [Module 2.2](https://chanderkant-sharma.medium.com/module-2-2-sentiment-analysis-and-summarization-that-feel-useful-95f1b11e4af9)
- Next: [Module 3.1: PDFs, Chunking, Embeddings, and ChromaDB](https://chanderkant-sharma.medium.com/module-3-1-pdfs-chunking-embeddings-and-chromadb-e878da4be031)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399)
- Lab notebooks: [Module3 README](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/Module3/README.md)
