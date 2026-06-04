# Module 3 Intro: Why RAG Gets Serious After the First Demo

Subtitle: PDFs, embeddings, ChromaDB, and evaluation are where LLM apps become knowledge systems.

Tags: RAG, ChromaDB, LangChain, Embeddings, India Tech, LiteLLM, MLflow

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

AI Gateway note: These labs can route OpenAI-compatible calls through LiteLLM. Set `USE_LITELLM=1`, `OPENAI_BASE_URL`, `LITELLM_MASTER_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`; see the [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Module 3 RAG pipeline diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module3-rag-pipeline.png)

Image: RAG quality depends on the full pipeline: PDF extraction, chunks, embeddings, retrieval, re-ranking, answers, and evaluation.

RAG demos are easy to love.

Upload a PDF, ask a question, get an answer. It feels magical. It also feels dangerously close to something you can ship.

Then reality arrives.

The answer is wrong. The model missed the important paragraph. The PDF text extraction is messy. The chunks are too small. The vector search returns something vaguely related but not useful. Someone asks, "How do we know this is accurate?" and suddenly the demo has become an engineering problem.

That uncomfortable moment is exactly why Module 3 exists.

## What Module 3 Adds

Module 2 taught you how to call models, write prompts, classify text, and summarize content. Module 3 adds the missing piece: external knowledge.

Instead of expecting the model to know everything, you build a workflow that retrieves relevant information from your documents and passes that context to the model.

The module covers:

- Reading PDFs
- Chunking documents
- Creating embeddings
- Storing vectors in ChromaDB
- Retrieving relevant chunks
- Re-ranking results
- Evaluating RAG quality

This is the point where LLM apps start looking like real enterprise systems.

## Notebook Map

Module 3 uses these Python notebooks:

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

Most Indian companies do not need a model that knows random internet facts. They need a system that understands their documents:

- Insurance policies
- SOPs
- Product manuals
- HR policies
- Legal documents
- Support knowledge bases
- Medical or financial records
- Training content

RAG lets you connect the model to this private or domain-specific knowledge without retraining the model.

That is a practical win, especially when the valuable knowledge is sitting in PDFs and internal docs instead of public web text.

## The Hidden Work: Document Processing

People often talk about RAG as if retrieval is the hard part. Retrieval is hard, yes. But document processing is where many projects first struggle.

PDFs can be messy. Text can be split badly. Tables may not extract cleanly. Headers and footers can pollute chunks. Important context can get separated across pages.

Module 3 starts with this unglamorous but essential work. You read PDFs, extract text, and prepare content for chunking.

Good RAG starts before embeddings. If your source text is bad, your retrieval will also be bad.

## Embeddings And ChromaDB

Once documents are chunked, the next step is embeddings. An embedding converts text into a vector representation so similar pieces of text can be found through vector search.

ChromaDB stores these vectors and lets you retrieve relevant chunks for a question.

This is the basic RAG loop:

```text
Question -> embedding -> vector search -> relevant chunks -> prompt -> answer
```

The model is still important, but it is no longer working alone. The retrieval layer gives it context.

## Why Evaluation Cannot Be Optional

If Module 3 has one serious message, it is this: RAG must be evaluated.

You need to know:

- Did retrieval find the right content?
- Did the answer use the retrieved context?
- Did the model invent anything?
- Does performance improve after changing chunk size?
- Are multi-PDF answers consistent?

Without evaluation, teams often choose whatever answer "looks good." That is not enough for real use cases.

Module 3 includes RAG evaluation notebooks for single and multiple PDFs. This is where the workflow becomes more disciplined.

## MLflow Helps You Compare Runs

With local MLflow tracing enabled, each Module 3 notebook gets its own experiment. That helps you compare retrieval, prompt, and evaluation runs.

When you change chunking strategy or retrieval settings, traces give you a better way to inspect what happened.

For learning, this is useful. For teams, it is even more useful, because every retrieval change needs a trail you can inspect later.

## Where This Leads

Module 3 prepares you for Module 4. Once you can retrieve knowledge reliably, you can give agents better tools and better context.

Without RAG, an agent is often just a confident chatbot with extra steps. With RAG, an agent can work with actual domain knowledge.

That is the bridge from retrieval to agentic AI.

## Feedback

If you bring your own PDF into this module, tell me what broke first: extraction, chunking, retrieval, or evaluation. That is where the most useful RAG lessons usually hide.

## Series Navigation

- Previous: [Module 2.2](https://chanderkant-sharma.medium.com/module-2-2-sentiment-analysis-and-summarization-that-feel-useful)
- Next: [Module 3.1](https://chanderkant-sharma.medium.com/module-3-1-pdfs-chunking-embeddings-and-chromadb)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-main-intro)
- Repo docs: [Module3 README](https://chanderkant-sharma.medium.com/module-3-intro-why-rag-gets-serious-after-the-first-demo)
