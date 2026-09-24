# Module 2.1: Connecting to OpenAI-Compatible APIs and Writing Better Prompts

Subtitle: Before you build RAG or agents, make model access and prompts boringly reliable. Everything later depends on it.

Tags: OpenAI, Prompt Engineering, Python, MLflow, Generative AI, LiteLLM

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

Quick setup note: The notebooks use OpenAI-compatible clients. If you run LiteLLM, point `OPENAI_BASE_URL` at the gateway, set `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`, and keep `LITELLM_MASTER_KEY` aligned with your gateway config. The details are in [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![OpenAI connection workflow diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module2-llm-workflow.png)

Image: The first useful workflow: clean setup, one model call, a response you understand, and a trace you can see.

In the Module 2 Intro, we said the plumbing comes first. So here is the honest truth: the first serious step in any LLM project is not building an agent. It is making one clean model call and understanding the response without guessing.

That may sound too basic, but this is exactly where many projects quietly go wrong. Teams reach for a fancy architecture before confirming that their API key, endpoint, model name, environment variables, and prompt format work consistently.

That is why Module 2 starts with OpenAI-compatible connection setup, and why this post takes it seriously.

## The Boring Setup Is The Real Setup

In the notebook flow, you first run the `Initial setup` cell. That cell handles repo-level utilities and MLflow tracing. Then the Module 2 setup notebook installs the pinned packages for this section:

- `openai==2.40.0`
- `httpx==0.28.1`
- `pandas==2.3.3`
- `pydantic==2.13.4`
- `python-dotenv==1.2.2`
- `tenacity==9.1.4`
- `mlflow==3.13.0`

The point is repeatability. Everyone running the lab should share the same package baseline, which stops the classic "works on my machine" problem before it turns into a group debugging session.

For Indian teams, where one person runs things locally, another on Databricks, another on a college lab system, and another on a locked-down corporate laptop, pinned dependencies are not overkill. They are a kindness.

## The First Model Call

Once your credentials are loaded, the first model call checks whether the basic loop works end to end:

```text
Input prompt -> model request -> response object -> extracted answer
```

At this stage, the goal is not creativity. It is clarity:

- Did the request go through?
- Did the model return a usable response?
- Do you understand where the answer lives in the response object?
- Can you repeat the call?

Once this works, the rest of Module 2 gets much easier, because you are no longer wondering whether the plumbing is the problem.

## Notebook Snippet: `Module2/01_OpenAI_Connection.ipynb`

The connection notebook wraps chat calls in retry logic, because real APIs occasionally hiccup:

```python
@retry(wait=wait_random_exponential(min=45, max=120), stop=stop_after_attempt(6))
def query_llm(prompt_messages, max_tokens=4096, temperature=1.0, top_p=1.0):
    response = chat_client.chat.completions.create(
        messages=prompt_messages,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        model=chat_model_name,
    )
    return {"text": response.choices[0].message.content}
```

`Module2/02_Prompt_Ebginnering.ipynb` then reuses the same function for prompt experiments:

```python
query = "My invoice for order #1234 seems incorrect. Can you clarify the charges?"
prompt_messages = [
    {
        "role": "developer",
        "content": "Classify this customer query into one of: Billing, Technical, Sales. Respond ONLY with the category name.",
    },
    {"role": "user", "content": query},
]

response = query_llm(prompt_messages, temperature=0)
```

## Prompt Engineering: Practical Version

Prompt engineering is often taught like a bag of tricks. "Use this magic phrase." "Tell it to act as an expert." "Add a little emotional pressure." Most of that does not survive contact with serious work.

A practical prompt has four parts:

1. Task: what should the model do?
2. Context: what information should it use?
3. Constraints: what should it avoid or follow?
4. Format: how should the answer be returned?

For example, instead of this:

```text
Analyze this review.
```

Try this:

```text
Classify this patient review as Positive, Negative, or Neutral.
Return only the label and a one-sentence reason.
Do not mention information that is not present in the review.
```

Now the model has far less room to wander, and you have far less to clean up afterwards.

## Why Output Format Matters

If you are building a toy chatbot, free-form output is fine. The moment you are building a workflow, output format matters a lot.

Imagine you need to store model results in a CSV, feed them to a dashboard, or compare them with human labels. A random paragraph is painful to work with. A consistent label, score, or JSON object is easy.

Module 2 gently nudges you toward structured thinking. Even when the notebooks are simple, the habit is a professional one, and it pays off in the sample project later.

## Use MLflow While Learning

Start MLflow with:

```bash
mlflow server \
  --host 127.0.0.1 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns
```

you can inspect traces at `http://127.0.0.1:5000`.

This matters because early LLM debugging is often invisible. MLflow gives you a place to actually see experiments and traces, instead of relying on notebook output and your memory of what you ran an hour ago.

## The Takeaway

Part 1 of Module 2 comes down to reliability:

- Set up credentials
- Make clean model calls
- Write clear prompts
- Control output shape
- Trace what happened

With that foundation in place, Module 2.2 puts it to work on two very practical tasks, sentiment analysis and summarization, without dragging setup doubts into every notebook that follows.

## Feedback

If this helped you get a clean model call running, tell me what your setup looked like: a direct provider, the LiteLLM gateway, local MLflow, or something else. Those details help future readers avoid the same setup traps.

## Series Navigation

- Previous: [Module 2 Intro](https://chanderkant-sharma.medium.com/module-2-intro-your-first-practical-llm-workflow-b767002d5fd2)
- Next: [Module 2.2: Sentiment Analysis and Summarization That Feel Useful](https://chanderkant-sharma.medium.com/module-2-2-sentiment-analysis-and-summarization-that-feel-useful-95f1b11e4af9)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399)
- Lab notebooks: [Module2 README](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/Module2/README.md)
