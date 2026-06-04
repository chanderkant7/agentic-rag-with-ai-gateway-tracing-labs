# Module 3: Advanced RAG with ChromaDB

Module 3 builds a healthcare-focused RAG pipeline from document loading through evaluation. The notebooks move from PDF extraction and chunking to embeddings, ChromaDB retrieval, reranking, conversational retrieval, and DeepEval-based measurement.

## Recommended Structure

Use `Part1` for the active build labs and `Part2` for evaluation.

`Module3/Module2` and `Module3/Module5` contain legacy mirrors with similar curriculum content. New learners should start with `Part1` and `Part2`.

## Part 1: Build the RAG Pipeline

| Order | Notebook | What you build |
| --- | --- | --- |
| 1 | [Part1/01_Read Pdf File.ipynb](Part1/01_Read%20Pdf%20File.ipynb) | A PDF loader that extracts research-paper text with LangChain and PyMuPDF. |
| 2 | [Part1/02_DataChunking.ipynb](Part1/02_DataChunking.ipynb) | Chunking experiments using fixed-size, recursive, sentence-based, and semantic strategies. |
| 3 | [Part1/03_DocumentEmbeddings.ipynb](Part1/03_DocumentEmbeddings.ipynb) | Embedding workflows with Word2Vec and OpenAI-compatible embedding models. |
| 4 | [Part1/04_ChromaDB Data Retrieval and Re-ranking in RAG.ipynb](Part1/04_ChromaDB%20Data%20Retrieval%20and%20Re-ranking%20in%20RAG.ipynb) | Semantic retrieval, BM25 hybrid retrieval, ChromaDB storage, and LLM-based reranking. |
| 5 | [Part1/05_TalkToData.ipynb](Part1/05_TalkToData.ipynb) | A conversational RAG pipeline that retrieves, reranks, and answers questions over healthcare research content. |

The build labs work with healthcare IoT research PDFs, including:

- `Part1/Data/HealthcaredocforRAG.pdf`
- `Part1/Data/TrendsprospectschallengesandsecurityinHIOT.pdf`

## Part 2: Evaluate the RAG Pipeline

| Notebook | What it measures |
| --- | --- |
| [Part2/RAG_Evaluation_SinglePDF.ipynb](Part2/RAG_Evaluation_SinglePDF.ipynb) | Retrieval and answer quality for a focused single-PDF corpus. |
| [Part2/RAG_Evaluation_MultiplePDF.ipynb](Part2/RAG_Evaluation_MultiplePDF.ipynb) | Multi-PDF retrieval behavior, context noise, hallucination risk, and single-vs-multiple document tradeoffs. |

The evaluation notebooks use DeepEval and custom OpenAI-compatible model wrappers to measure:

- Contextual precision
- Contextual recall
- Contextual relevancy
- Answer relevancy
- Faithfulness
- Hallucination
- Custom LLM-as-judge checks with G-Eval

They also inject noisy or low-relevance chunks to show how retrieval quality affects downstream generation.

## Key Concepts

- PDF loading with `PyMuPDFLoader`
- Chunk sizing, overlap, and natural text boundaries
- Word-level and semantic embeddings
- ChromaDB vector storage and reuse
- Semantic similarity search
- BM25 plus vector hybrid retrieval
- LLM-based reranking
- Context-only prompting for grounded answers
- Evaluation with clean and noisy retrieval contexts

## Running the Notebooks

1. Activate your virtual environment from the repository root.
2. Configure `.env` with `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME`.
3. Run [`.setup/learner_setup.ipynb`](.setup/learner_setup.ipynb).
4. Run `Part1` notebooks in order, then move to `Part2`.

For a manual install from the repository root:

```bash
uv pip install -r Module3/.setup/module3/2/shim.txt -c Module3/.setup/module3/2/constraints.txt
```

Key packages include `langchain`, `langchain-community`, `langchain-openai`, `langchain-text-splitters`, `chromadb`, `sentence-transformers`, `gensim`, `pymupdf`, `deepeval`, and `mlflow`.

## Gateway, Cache, and Tracing

Module 3 notebooks read `OPENAI_API_KEY`, `OPENAI_BASE_URL`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` from `.env`. Set `OPENAI_BASE_URL` to a LiteLLM gateway URL if you want provider routing through LiteLLM.

Some notebooks set local cache and telemetry values for ChromaDB, tiktoken, and DeepEval. These settings keep repeated notebook runs faster and quieter.

Start MLflow from the repository root if you want traces. Module 3 notebooks create experiments under names like `llm-rag-agents-gateway-labs/Module3/Part1/...` and `llm-rag-agents-gateway-labs/Module3/Part2/...`.

## Learning Outcomes

By the end of Module 3, you should be able to:

- Build a document RAG pipeline from raw PDFs
- Choose chunking strategies based on retrieval behavior
- Store and query embeddings with ChromaDB
- Combine semantic and keyword retrieval
- Use reranking to reduce irrelevant context
- Evaluate RAG systems with retrieval and generation metrics
- Diagnose how noisy context can cause weaker or less faithful answers
