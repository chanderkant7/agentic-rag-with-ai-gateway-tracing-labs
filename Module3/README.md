# Module 3: Advanced RAG with ChromaDB

## Overview

This advanced module covers RAG systems using ChromaDB for vector storage and retrieval. Learn document chunking, embeddings, retrieval ranking, and RAG evaluation. The notebooks now use current LangChain package imports, repository-relative paths, and localhost MLflow tracing.

## Module Structure

### Part 1: Document Processing & Embeddings

#### **01_Read Pdf File.ipynb**
- PDF parsing and extraction techniques
- Handling different PDF formats and encodings
- Text extraction and preprocessing
- Metadata preservation and handling

#### **02_DataChunking.ipynb**
- Chunking strategies: fixed-size, recursive, and semantic
- Handling overlapping chunks for context preservation
- Optimizing chunk size for retrieval effectiveness
- Balancing context window and retrieval precision

#### **03_DocumentEmbeddings.ipynb**
- Generating embeddings with various models (OpenAI, HuggingFace, etc.)
- Understanding embedding quality and dimensionality
- Storing embeddings in ChromaDB vector database
- Vector similarity search and retrieval

#### **04_ChromaDB Data Retrieval and Re-ranking in RAG.ipynb**
- ChromaDB setup, configuration, and client operations
- Advanced retrieval techniques (similarity, MMR, filtering)
- Re-ranking retrieved documents for relevance
- Hybrid search combining multiple retrieval strategies
- Performance optimization and collection management

#### **05_TalkToData.ipynb**
- Interactive chat interface with document data
- Real-time retrieval and response generation
- Conversation history management and context
- Context-aware multi-turn interactions

### Part 2: RAG Evaluation

#### **RAG_Evaluation_SinglePDF.ipynb**
- Evaluating RAG performance with single document
- Computing retrieval metrics (precision, recall, MRR)
- Assessing generation quality (BLEU, ROUGE, exact match)
- Consistency and hallucination detection

#### **RAG_Evaluation_MultiplePDF.ipynb**
- Handling and evaluating multiple document sources
- Cross-document retrieval accuracy
- Managing conflicting or complementary information
- Scalability testing and performance benchmarking

#### **LLMTestcases.py**
- Automated test frameworks
- Performance benchmarking
- Regression testing
- Quality assurance

## Key Technologies

- **ChromaDB**: Vector database for embeddings
- **LangChain**: RAG orchestration
- **Various Embedding Models**: OpenAI, HuggingFace, etc.
- **PDF Processing**: PyMuPDF

## Learning Objectives

- Parse and process various document formats (PDF, text)
- Implement effective document chunking strategies
- Generate and manage embeddings at scale
- Master ChromaDB operations and vector search
- Implement production-ready RAG systems
- Evaluate RAG system quality comprehensively
- Optimize retrieval and ranking performance
- Handle multi-document RAG scenarios
- Debug and improve retrieval accuracy
- Scale RAG to large document collections

## Running the Notebooks

1. Activate your virtual environment from the repository root.
2. Run the Module 3 setup notebook once:
```bash
jupyter notebook Module3/.setup/learner_setup.ipynb
```
3. Open Jupyter and follow Module 2 before Module 5.

The setup notebook installs:

```bash
uv pip install -r Module3/module3/2/requirements.txt -c Module3/module3/2/constraints.txt
```

Current key package pins include `langchain==1.3.4`, `langchain-community==0.4.2`, `langchain-openai==1.2.2`, `langchain-text-splitters==1.1.2`, `chromadb==1.5.9`, `sentence-transformers==5.5.1`, `deepeval==4.0.5`, `pymupdf==1.27.2.3`, and `mlflow==3.13.0`.

## LiteLLM AI Gateway

Module 3 RAG notebooks can use LiteLLM as an AI Gateway for both chat and embedding calls. Configure `OPENAI_BASE_URL` for the gateway URL, `CHAT_MODEL_NAME` for answer generation, and `EMBEDDING_MODEL_NAME` for embedding workflows. The root `.env.example` includes a ready template with `USE_LITELLM=1`.

## Updated LangChain Imports

The notebooks use the newer package split:

- Document loaders from `langchain_community.document_loaders`
- Vector stores from `langchain_community.vectorstores`
- Text splitters from `langchain_text_splitters`
- Documents and tools from `langchain_core`

## MLflow and Paths

Each lab notebook has an `Initial setup` cell that enables tracing through `Module1/notebook_utils.py` via `setup_mlflow_tracing(...)`. Data paths use `repo_path(...)`, so notebooks can be opened from different working directories.

Start MLflow from the repository root before running notebooks if you want traces captured:

```bash
mlflow server \
  --host 127.0.0.1 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns
```

Open the MLflow UI at `http://127.0.0.1:5000`. Module 3 notebooks create separate experiments under names like `llm-rag-agents-gateway-labs/Module3/<module>/<notebook-name>`.

If the server is not running, the setup helper skips experiment selection and the notebook continues. You can also override the tracking URI by setting `MLFLOW_TRACKING_URI` before running a notebook.

## Key Concepts

- **Document Chunking**: Breaking documents into manageable pieces while preserving context
- **Embeddings**: Dense vector representations capturing semantic meaning
- **Vector Search**: Finding similar documents using embedding similarity
- **ChromaDB**: Persistent and in-memory vector database for embeddings
- **Re-ranking**: Sorting retrieved documents by relevance
- **Hybrid Search**: Combining multiple retrieval strategies (BM25 + semantic)
- **Retrieval Metrics**: Measuring retrieval quality (precision, recall, MRR, NDCG)
- **Generation Quality**: Evaluating LLM outputs (BLEU, ROUGE, exact match)
- **Hallucination Detection**: Identifying false or unsupported claims

## Data

- `Data/` - Contains sample PDFs and documents for processing
- NLTK data for text processing

## Evaluation Metrics

- **Retrieval Metrics**: MRR, NDCG, Hit Rate
- **Generation Metrics**: BLEU, ROUGE, Exact Match
- **Latency**: Response time and throughput
- **Cost**: Token usage and API calls

## Next Steps

Complete **Module 4: Agentic AI** to learn how to build intelligent agents using tools and RAG systems together.
