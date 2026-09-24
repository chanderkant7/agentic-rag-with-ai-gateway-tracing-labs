# Module 3.1: PDFs, Chunking, Embeddings, and ChromaDB

Subtitle: The less glamorous RAG steps are usually the ones that decide whether your answers can be trusted.

Tags: RAG, ChromaDB, Embeddings, PDFs, LangChain, LiteLLM, MLflow

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

Quick setup note: The notebooks use OpenAI-compatible clients. If you run LiteLLM, point `OPENAI_BASE_URL` at the gateway, set `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`, and keep `LITELLM_MASTER_KEY` aligned with your gateway config. The details are in [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![PDF to ChromaDB RAG pipeline diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module3-rag-pipeline.png)

Image: The first half of RAG is making documents searchable: extraction, chunking, embeddings, and vector storage.

The Module 3 Intro made a promise: good RAG starts long before the model writes a single word. This post keeps that promise. It covers the retrieval foundation, the part of RAG people tend to underestimate until their answers start drifting.

Before you can ask smart questions of your documents, you have to make those documents searchable. That sounds simple, right up until you open a PDF and realise the text is far messier than it looked on screen.

So we work through it in four steps: reading PDFs, chunking text, generating embeddings, and storing vectors in ChromaDB.

This is where practical RAG really begins. Not with a dramatic answer, but with source text that is clean enough to trust.

## Step 1: Reading PDFs

PDFs are everywhere in Indian enterprise workflows: policies, reports, contracts, manuals, circulars, forms, SOPs, and training material.

But PDFs are not always friendly to machines. A PDF is designed to look right on screen, not to give up clean text.

Some common headaches:

- Broken line order
- Repeated headers and footers
- Tables that flatten badly
- Page numbers mixed with content
- Scanned pages with no text layer
- Multi-column layouts

The PDF notebook encourages you to inspect the extracted text before you trust it. That one habit saves a lot of pain later, because if the extracted text is poor, your embeddings will faithfully preserve every bit of that poor quality.

## Notebook Snippet: `Module3/Module2/01_Read Pdf File.ipynb`

PDF loading uses the current LangChain Community loader:

```python
from langchain_community.document_loaders import PyMuPDFLoader

def load_pdf_with_langchain(pdf_path):
    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()
    print(f"Successfully loaded {len(documents)} document chunks from the PDF.")
    return documents

pdf_path = repo_path("Module3", "Module2", "Data", "HealthcaredocforRAG.pdf")
docs = load_pdf_with_langchain(pdf_path)
```

## Step 2: Chunking Text

Once you have text, you need to split it into chunks.

Chunking is one of the most important decisions in any RAG system. Make chunks too small and they lose context. Make them too large and retrieval gets noisy and expensive.

Module 3 explores several chunking strategies:

- Fixed-size chunks
- Recursive character splitting
- Overlap between chunks
- Context-preserving splits

There is no universal perfect chunk size. A legal contract, a medical policy, and a product FAQ may each need a different approach.

The question worth asking again and again is simple: when a user asks something, can the retriever find a chunk that actually contains enough information to answer it?

## Notebook Snippet: `Module3/Module2/02_DataChunking.ipynb`

The recursive splitter keeps related text together far better than naive splits do:

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

def recursive_chunking(docs, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return splitter.split_documents(docs)

recursive_chunks = recursive_chunking(docs)
```

## Step 3: Embeddings

Embeddings turn text chunks into vectors that capture meaning, so similar text can be found even when the wording is completely different.

For example, a user might ask:

```text
What is covered under emergency hospitalization?
```

While the document says:

```text
Emergency inpatient treatment is eligible under the policy...
```

A keyword search could easily miss that. Embedding search has a much better chance, because it matches meaning rather than exact words.

That is why embeddings sit at the heart of RAG.

## Notebook Snippet: `Module3/Module2/03_DocumentEmbeddings.ipynb`

The embedding notebook uses the gateway-aware embedding model from `.env`:

```python
embeddings_client = openai.OpenAI(api_key=api_key, base_url=base_url)

@retry(wait=wait_random_exponential(min=45, max=120), stop=stop_after_attempt(6))
def get_embeddings(texts_chunk):
    return embeddings_client.embeddings.create(
        input=texts_chunk,
        model=embedding_model_name,
    ).data
```

## Step 4: ChromaDB

ChromaDB stores embeddings along with their metadata, so you can run vector search over them.

In the RAG workflow, ChromaDB becomes the searchable memory for your documents:

```text
Document chunks -> embeddings -> ChromaDB collection -> retrieval
```

The notebook walks you through creating a collection, adding documents, and querying for the most relevant chunks.

The important part is not just storing vectors. It is keeping enough metadata to trace every answer back to its source. In real systems, being able to say "this came from page 12 of the policy" matters a lot.

## Why LangChain Package Split Matters

The notebooks use the updated LangChain import structure:

- `langchain_community.document_loaders`
- `langchain_community.vectorstores`
- `langchain_text_splitters`
- `langchain_core`

This matters because LangChain has evolved quickly. Using current imports keeps the notebooks in line with modern package expectations and steers clear of older, deprecated patterns.

## Use MLflow While Experimenting

Whenever you change chunk size, overlap, embedding model, or retrieval settings, keep MLflow running locally.

It shows which notebook produced which run and keeps Module 3 traces separate from everything else, which really helps when you are comparing retrieval experiments.

## The Takeaway

RAG quality is not decided by the final prompt alone. It is built step by step:

- Extract text cleanly
- Chunk it thoughtfully
- Embed it consistently
- Store it with useful metadata
- Retrieve the right context

Get these pieces right, and your final answer has a much better chance of being useful instead of merely confident. In Module 3.2, we put that to the test with retrieval, re-ranking, and proper RAG evaluation.

## Feedback

If you try this with a messy PDF, share what the extracted text looked like. Those ugly first outputs are often the best teachers in any RAG project.

## Series Navigation

- Previous: [Module 3 Intro](https://chanderkant-sharma.medium.com/module-3-intro-why-rag-gets-serious-after-the-first-demo-6ce1283631c3)
- Next: [Module 3.2: Retrieval, Re-ranking, and RAG Evaluation](https://chanderkant-sharma.medium.com/module-3-2-retrieval-re-ranking-and-rag-evaluation-1001b93b1c41)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399)
- Lab notebooks: [Module3 README](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/Module3/README.md)
