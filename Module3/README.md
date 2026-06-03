# Module 3: Advanced RAG with ChromaDB

## Overview

This advanced module covers RAG systems using ChromaDB for vector storage and retrieval. Learn document chunking, embeddings, retrieval ranking, and RAG evaluation. The notebooks now use current LangChain package imports, repository-relative paths, and localhost MLflow tracing.

## Module Structure

### Module 2: Document Processing & Embeddings

#### **DataChunking.ipynb**
- Chunking strategies (fixed-size, recursive, semantic)
- Handling overlapping chunks
- Optimizing chunk size for retrieval
- Preserving context in chunks

#### **DocumentEmbeddings.ipynb**
- Generating embeddings with various models
- Embedding quality and dimensionality
- Storing embeddings in ChromaDB
- Vector similarity search

#### **Read Pdf File.ipynb**
- PDF parsing and extraction
- Handling different PDF formats
- Text extraction and cleaning
- Metadata preservation

#### **TalkToData.ipynb**
- Interactive chat with document data
- Real-time retrieval and generation
- Conversation history management
- Context-aware responses

#### **ChromaDB Data Retrieval and Re-ranking in RAG.ipynb**
- ChromaDB setup and configuration
- Advanced retrieval techniques
- Re-ranking retrieved documents
- Filtering and hybrid search
- Performance optimization

### Module 5: RAG Evaluation

#### **RAG_Evaluation_SinglePDF.ipynb**
- Evaluating RAG with single document
- Retrieval precision and recall
- Generation quality metrics
- Consistency checks

#### **RAG_Evaluation_MultiplePDF.ipynb**
- Handling multiple document sources
- Cross-document retrieval accuracy
- Handling conflicting information
- Scalability testing

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

- Implement production-ready RAG systems
- Master vector database operations
- Optimize retrieval performance
- Evaluate RAG system quality
- Handle multi-document scenarios
- Scale RAG to large datasets

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

## Data

- `Data/` - Contains sample PDFs and documents for processing
- NLTK data for text processing

## Evaluation Metrics

- **Retrieval Metrics**: MRR, NDCG, Hit Rate
- **Generation Metrics**: BLEU, ROUGE, Exact Match
- **Latency**: Response time and throughput
- **Cost**: Token usage and API calls

## Next Steps

Complete Module 4 to learn how to build intelligent agents using tools and RAG systems together.
