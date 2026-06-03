# Module 3.2: Retrieval, Re-ranking, and RAG Evaluation

Subtitle: A RAG system is only as good as the evidence it retrieves and the discipline used to evaluate it.

Tags: RAG Evaluation, Retrieval, ChromaDB, MLflow, AI Engineering, LiteLLM

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

AI Gateway note: These labs can route OpenAI-compatible calls through LiteLLM. Set `USE_LITELLM=1`, `OPENAI_BASE_URL`, `LITELLM_MASTER_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`; see the [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Retrieval and RAG evaluation diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module3-rag-pipeline.png)

Image: Retrieval, re-ranking, answer generation, and evaluation need to be inspected together, not as isolated steps.

Once documents are embedded and stored, the next question is the one every RAG project eventually has to face: are we retrieving the right stuff?

This is where many RAG demos start to wobble, even when the final answer sounds polished.

The model may produce a confident answer, but if the retrieved chunks were weak, irrelevant, or incomplete, the answer is built on shaky ground. Module 3.2 focuses on retrieval, re-ranking, and evaluation because these are the skills that turn RAG from a demo into an engineering workflow.

## Retrieval Is Not Just Search

In a RAG system, retrieval decides what context the model sees.

That means retrieval controls the model's knowledge for that request.

If the retriever misses the key paragraph, the model may:

- Give a generic answer
- Use the wrong source
- Invent missing details
- Sound correct while being wrong

So retrieval quality matters as much as model quality. Sometimes it matters more.

## Notebook Snippet: `Module3/Module2/04_ChromaDB Data Retrieval and Re-ranking in RAG.ipynb`

The ChromaDB notebook stores chunks and retrieves unique semantic matches:

```python
vectordb = Chroma.from_documents(
    documents=texts,
    embedding=embeddings,
    collection_name="healthcare_rag",
)

def semantic_retrieval(query, top_k=3):
    results = vectordb.similarity_search(query, k=top_k * 2)
    unique_results = []
    seen_contents = set()

    for doc in results:
        if doc.page_content not in seen_contents:
            unique_results.append(doc)
            seen_contents.add(doc.page_content)
        if len(unique_results) >= top_k:
            break

    return unique_results
```

## Re-ranking Helps When Top Results Are Noisy

Vector search is powerful, but it is not perfect. Sometimes the top retrieved chunks are semantically close but not actually the best evidence.

Re-ranking is a second pass that tries to order retrieved results by usefulness.

The idea is:

```text
Retrieve candidate chunks -> re-rank candidates -> pass best context to model
```

This is especially useful when:

- Documents are long
- Many chunks are similar
- The question is specific
- The domain has repeated terminology
- Multiple PDFs contain overlapping topics

For enterprise documents, re-ranking often improves answer quality because the first vector search result is not always the most useful result.

## Single-PDF Evaluation

The single-PDF evaluation notebook helps you test whether your RAG system can answer questions from one document reliably.

This is the right place to start because the problem is controlled. If the system fails on one document, adding more documents will not magically fix it.

Useful questions include:

- Was the correct section retrieved?
- Did the generated answer match the source?
- Did the answer include unsupported claims?
- Was the response too vague?
- Did changing chunk size improve retrieval?

This helps you tune the basics before scaling up.

## Notebook Snippet: RAG Evaluation Notebooks

`Module3/Module5/RAG_Evaluation_SinglePDF.ipynb` and `Module3/Module5/RAG_Evaluation_MultiplePDF.ipynb` wrap the full flow for evaluation:

```python
response = pdf_chatbot_pipeline(
    repo_path("Module3", "Module2", "Data", "HealthcaredocforRAG.pdf"),
    "How does MIoT improve hospital safety?",
    persist_directory="./Data/singlepdf_rag_eval.db",
)

print(response["AI_generated_response"])
```

## Multi-PDF Evaluation

Multi-PDF RAG is harder. Now the system must choose between multiple sources, handle overlapping concepts, and avoid mixing facts from different documents incorrectly.

This is common in real Indian business use cases:

- Multiple policy documents
- Multiple product manuals
- Multiple circulars or regulations
- Multiple SOP versions
- Multiple customer files

The evaluation challenge is not just "did it answer?" It is also "did it use the right document?"

## Metrics And Human Judgment

RAG evaluation can include metrics like hit rate, precision, recall, MRR, and answer correctness. But human review is still important, especially in domain-heavy use cases.

For learning, start with practical checks:

- Is the retrieved context relevant?
- Is the answer grounded in that context?
- Is the answer complete enough?
- Is the source easy to inspect?

Then move toward more formal evaluation.

## MLflow For Iteration

Module 3 is where MLflow tracing becomes especially useful.

You may test:

- Different chunk sizes
- Different overlap values
- Different embedding models
- Different retrieval counts
- Re-ranking on or off
- Prompt changes

Tracing helps you keep runs understandable. Without it, experiments blend together in notebook output and you end up trusting memory more than evidence.

## Module 3 Wrap-up

By the end of Module 3, you have a strong RAG foundation:

- Process PDFs
- Split documents
- Generate embeddings
- Store and query ChromaDB
- Re-rank retrieved context
- Evaluate single and multi-document RAG

This sets up Module 4 nicely. Once you can retrieve reliable knowledge, you can build agents that use tools and context more intelligently.

## Feedback

If you tune retrieval settings, note which change actually improved the answers. Chunk size, top-k, re-ranking, and prompt wording can all feel important, but the evidence usually tells a more interesting story.

## Series Navigation

- Previous: [Module 3.1](https://chanderkant-sharma.medium.com/module-3-1-pdfs-chunking-embeddings-and-chromadb)
- Next: [Module 4 Intro](https://chanderkant-sharma.medium.com/module-4-intro-from-chatbots-to-agents-that-use-tools)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-main-intro)
