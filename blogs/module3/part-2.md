# Module 3.2: Retrieval, Re-ranking, and RAG Evaluation

Subtitle: A RAG system is only as good as the evidence it retrieves, and the discipline you bring to evaluating it.

Tags: RAG Evaluation, Retrieval, ChromaDB, MLflow, AI Engineering, LiteLLM

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

Quick setup note: The notebooks use OpenAI-compatible clients. If you run LiteLLM, point `OPENAI_BASE_URL` at the gateway, set `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`, and keep `LITELLM_MASTER_KEY` aligned with your gateway config. The details are in [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Retrieval and RAG evaluation diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module3-rag-pipeline.png)

Image: Retrieval, re-ranking, answer generation, and evaluation need to be inspected together, not as isolated steps.

In Module 3.1, we did the unglamorous groundwork: clean text, sensible chunks, embeddings, and a ChromaDB collection. Now comes the question every RAG project eventually has to face: are we actually retrieving the right stuff?

This is where many RAG demos start to wobble, even when the final answer sounds perfectly polished.

The model can sound confident, but if the retrieved chunks were weak, irrelevant, or incomplete, the answer is standing on shaky ground. That is why this post focuses on retrieval, re-ranking, and evaluation. These are the skills that turn RAG from a demo into an engineering workflow.

## Retrieval Is Not Just Search

In a RAG system, retrieval decides what context the model gets to see.

Which means retrieval effectively controls what the model knows for that request.

If the retriever misses the key paragraph, the model may:

- Give a generic answer
- Use the wrong source
- Invent missing details
- Sound correct while being wrong

So retrieval quality matters as much as model quality. Sometimes it matters more.

## Notebook Snippet: `Module3/Module2/04_ChromaDB Data Retrieval and Re-ranking in RAG.ipynb`

The ChromaDB notebook stores chunks and retrieves unique semantic matches, skipping duplicates:

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

Vector search is powerful, but it is not perfect. Sometimes the top chunks are semantically close without being the best evidence.

Re-ranking is a second pass that reorders those retrieved results by how useful they really are.

The idea is simple:

```text
Retrieve candidate chunks -> re-rank candidates -> pass best context to model
```

It is especially helpful when:

- Documents are long
- Many chunks are similar
- The question is specific
- The domain has repeated terminology
- Multiple PDFs contain overlapping topics

With enterprise documents, re-ranking often lifts answer quality noticeably, because the first vector search hit is not always the most useful one.

## Single-PDF Evaluation

The single-PDF evaluation notebook checks whether your RAG system can answer questions from one document reliably.

Start here, because the problem is controlled. If the system struggles with one document, adding more documents will not magically fix it.

Useful questions to ask:

- Was the correct section retrieved?
- Did the generated answer match the source?
- Did the answer include unsupported claims?
- Was the response too vague?
- Did changing chunk size improve retrieval?

This helps you tune the basics properly before you scale up.

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

Multi-PDF RAG is harder. Now the system has to choose between sources, handle overlapping concepts, and avoid mixing facts from different documents.

This shows up constantly in real Indian business use cases:

- Multiple policy documents
- Multiple product manuals
- Multiple circulars or regulations
- Multiple SOP versions
- Multiple customer files

So the evaluation question is not just "did it answer?" It is also "did it use the right document?"

## Metrics And Human Judgment

The evaluation notebooks use DeepEval-style checks for contextual precision, contextual recall, contextual relevancy, answer relevancy, faithfulness, hallucination, and custom G-Eval judging. Even so, human review still matters, especially in domain-heavy use cases.

While you are learning, start with a few practical checks:

- Is the retrieved context relevant?
- Is the answer grounded in that context?
- Is the answer complete enough?
- Is the source easy to inspect?

Then gradually move toward more formal evaluation as your confidence grows.

## MLflow For Iteration

Module 3 is where MLflow tracing really earns its place.

You might test:

- Different chunk sizes
- Different overlap values
- Different embedding models
- Different retrieval counts
- Re-ranking on or off
- Prompt changes

Tracing keeps those runs understandable. Without it, experiments blur together in notebook output, and you end up trusting your memory more than the evidence.

## Module 3 Wrap-up

By the end of Module 3, you have a solid RAG foundation:

- Process PDFs
- Split documents
- Generate embeddings
- Store and query ChromaDB
- Re-rank retrieved context
- Evaluate single and multi-document RAG

That sets up Module 4 nicely. Once you can retrieve reliable knowledge, you can build agents that use tools and context far more intelligently. The Module 4 Intro explains what changes when a model stops just answering and starts acting.

## Feedback

If you tune retrieval settings, make a note of which change genuinely improved the answers. Chunk size, top-k, re-ranking, and prompt wording can all feel important, but the evidence usually tells a more interesting story.

## Series Navigation

- Previous: [Module 3.1](https://chanderkant-sharma.medium.com/module-3-1-pdfs-chunking-embeddings-and-chromadb-e878da4be031)
- Next: [Module 4 Intro: From Chatbots to Agents That Use Tools](https://chanderkant-sharma.medium.com/module-4-intro-from-chatbots-to-agents-that-use-tools-848d84b62a6e)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399)
- Lab notebooks: [Module3 README](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/Module3/README.md)
