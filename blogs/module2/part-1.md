# Module 2.1: Connecting to OpenAI and Writing Better Prompts

Subtitle: Before you build RAG or agents, make model access and prompts boringly reliable.

Tags: OpenAI, Prompt Engineering, Python, MLflow, Generative AI, LiteLLM

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

AI Gateway note: These labs can route OpenAI-compatible calls through LiteLLM. Set `USE_LITELLM=1`, `OPENAI_BASE_URL`, `LITELLM_MASTER_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`; see the [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![OpenAI connection workflow diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module2-llm-workflow.png)

Image: The first useful workflow is clean setup, a model call, an understandable response, and a visible trace.

The first serious step in any LLM project is not building an agent. It is making one clean model call and understanding the response without guessing.

That may sound too basic, but this is where many projects quietly go wrong. Teams jump into a fancy architecture before they know whether their API key, endpoint, model name, environment variables, and prompt format are working consistently.

Module 2 starts with OpenAI connection setup for exactly this reason.

## The Boring Setup Is The Real Setup

In the notebook flow, you first run the `Initial setup` cell. That cell handles repo-level utilities and MLflow tracing. Then the Module 2 setup notebook installs the pinned packages for this section:

- `openai==2.40.0`
- `httpx==0.28.1`
- `pandas==2.3.3`
- `pydantic==2.13.4`
- `python-dotenv==1.2.2`
- `tenacity==9.1.4`
- `mlflow==3.13.0`

The key point is repeatability. Everyone running the lab should be using the same package baseline. That reduces the classic "works on my machine" problem before it becomes a group debugging session.

For Indian teams where one person may run locally, another in Databricks, another in a college lab system, and another in a corporate laptop with restrictions, pinned dependencies are not overkill. They are kindness.

## The First Model Call

Once credentials are loaded, the first model call tests whether the basic loop works:

```text
Input prompt -> model request -> response object -> extracted answer
```

At this stage, the goal is not creativity. The goal is clarity:

- Did the request go through?
- Did the model return a usable response?
- Do you understand where the answer lives in the response object?
- Can you repeat the call?

Once this works, the rest of Module 2 becomes much easier.

## Notebook Snippet: `Module2/01_OpenAI_Connection.ipynb`

The connection notebook wraps chat calls with retry logic:

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

Prompt engineering is often taught like a bag of tricks. "Use this magic phrase." "Say act as an expert." "Add emotional pressure." Most of that is not how serious teams should work.

A practical prompt has four things:

1. Task: what should the model do?
2. Context: what information should it use?
3. Constraints: what should it avoid or follow?
4. Format: how should the answer be returned?

For example, instead of:

```text
Analyze this review.
```

Use:

```text
Classify this patient review as Positive, Negative, or Neutral.
Return only the label and a one-sentence reason.
Do not mention information that is not present in the review.
```

This gives the model less room to wander.

## Why Output Format Matters

If you are building a toy chatbot, free-form output is fine. If you are building a workflow, output format matters.

Imagine you need to store model results in a CSV, send them to a dashboard, or compare them with human labels. A random paragraph is painful. A consistent label, score, or JSON object is much easier.

Module 2 gently pushes you toward structured thinking. Even when the notebooks are simple, the habit is professional.

## Use MLflow While Learning

If you start MLflow with:

```bash
mlflow server \
  --host 127.0.0.1 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns
```

you can inspect traces at `http://127.0.0.1:5000`.

This is useful because early LLM debugging is often invisible. MLflow gives you a place to see experiments and traces instead of relying only on notebook output and memory.

## The Takeaway

Part 1 of Module 2 is about reliability:

- Set up credentials
- Make clean model calls
- Write clear prompts
- Control output shape
- Trace what happened

Once that is in place, you can move to sentiment analysis and summarization without dragging setup uncertainty into every later notebook.

## Feedback

If this helped you get a clean model call running, share what your setup looked like: direct provider, LiteLLM gateway, local MLflow, or something else. Those details help future readers avoid the same setup traps.

## Series Navigation

- Previous: [Module 2 Intro](https://chanderkant-sharma.medium.com/module-2-intro-your-first-practical-llm-workflow)
- Next: [Module 2.2](https://chanderkant-sharma.medium.com/module-2-2-sentiment-analysis-and-summarization-that-feel-useful)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-main-intro)
