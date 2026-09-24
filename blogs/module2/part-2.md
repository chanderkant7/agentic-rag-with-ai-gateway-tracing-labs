# Module 2.2: Sentiment Analysis and Summarization That Feel Useful

Subtitle: Two simple LLM workflows that map neatly to real business problems, and quietly teach you a lot.

Tags: Sentiment Analysis, Text Summarization, OpenAI, Python, LiteLLM, MLflow

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

Quick setup note: The notebooks use OpenAI-compatible clients. If you run LiteLLM, point `OPENAI_BASE_URL` at the gateway, set `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`, and keep `LITELLM_MASTER_KEY` aligned with your gateway config. The details are in [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Sentiment and summarization workflow diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module2-llm-workflow.png)

Image: Classification and summarization both reuse the same dependable path from Module 2.1: notebook config, model call, output, and trace.

In Module 2.1, we made model access boringly reliable and learned to write prompts with a clear task, context, constraints, and format. Now it is time to use that on two tasks most teams recognise immediately: sentiment analysis and summarization.

I chose them deliberately. They are two of the most common ways teams first bring LLMs into real work.

You have a pile of text: reviews, tickets, calls, chats, emails, notes, documents. You want to understand it faster. LLMs are genuinely good at that, as long as you keep the workflow controlled and read the output with a healthy dose of skepticism.

## Sentiment Analysis: More Than Positive Or Negative

The sentiment analysis notebook works with patient review data. The basic job is to sort each review into a sentiment category.

At first glance, it looks simple:

```text
Review -> model -> sentiment label
```

But real sentiment analysis needs careful prompting. Patient feedback is often mixed. Someone may praise the doctor but complain about billing. They may sound polite and still be unhappy. They may mention three departments in a single review.

So the prompt has to be clear about:

- Allowed labels
- How to handle mixed sentiment
- Whether to include reasoning
- Whether to return structured output
- Whether to avoid assumptions

This is where the Module 1 foundations and the Module 2.1 prompt structure start working together.

## Notebook Snippet: `Module2/03_Seniment_Analysis.ipynb`

The sentiment notebook reads the patient review CSV using a repository-relative path, so it works no matter where you open it from:

```python
filepath = repo_path("Module2", "Data", "SentimentAnalysis", "Patient_Reviews.csv")
reviews = pd.read_csv(filepath)
```

It also uses a Pydantic model to keep the LLM's output structured and predictable:

```python
class SentimentOutput(BaseModel):
    sentiment_label: str = Field(..., description="positive, negative, or neutral")
    confidence_score: float = Field(..., description="A value between 0 and 1")
    emotions: List[str]
```

## Why This Matters In India

India runs a lot of high-volume service environments: healthcare, fintech, telecom, edtech, ecommerce, public services, and more. Teams often receive huge amounts of feedback, and manual review simply does not scale.

Sentiment analysis can help those teams:

- Track dissatisfaction patterns
- Spot urgent negative feedback
- Summarize customer voice
- Route issues faster
- Compare feedback by location, product, or team

The notebook is a small lab, but the pattern is very real: let the model reduce the reading load, then let people focus on judgment.

## Summarization: Compress Without Losing Meaning

The summarization notebook works with conversation-style data. The goal is to turn long text into short, genuinely useful summaries.

Good summarization is not just about making text shorter. It is about keeping what matters.

A useful summary captures:

- Main issue
- Important facts
- Decisions or next steps
- Tone or urgency when relevant
- Missing information

That matters for support teams, sales calls, meeting notes, insurance claims, medical conversations, and internal operations, basically anywhere people are drowning in text.

## Notebook Snippet: `Module2/04_Text_Summarization.ipynb`

The summarization notebook turns a doctor-patient conversation into a compact summary:

```python
prompt_messages = [
    {
        "role": "developer",
        "content": "You are an assistant that summarizes conversations between Doctor and Patient",
    },
    {
        "role": "user",
        "content": f"Please summarize the following text:\n\n{conversation}\n\nSummary:",
    },
]

response = query_llm(prompt_messages)
```

## The Risk: Confident But Wrong Summaries

LLMs can summarize beautifully and still be wrong. That is the real danger.

If the transcript says the refund is pending, the summary must not say it was approved. If the patient complains about waiting time, the summary must not invent a diagnosis.

So summarization prompts need constraints like these:

```text
Only use facts present in the input.
Do not invent missing details.
If the next action is unclear, say "next action not specified."
```

This kind of guardrail is not fancy, but future-you will be very grateful for it.

## Tracing The Workflow

With MLflow running locally, each notebook logs traces to its own experiment. That lets you compare prompt versions, inspect individual model calls, and see what actually changed between runs.

This gets useful quickly once you start iterating:

- Prompt version 1 gives verbose summaries
- Prompt version 2 gives structured summaries
- Prompt version 3 adds action items

Without traces, these versions blur together in your memory. With traces, you can put them side by side and review them.

## Module 2 Wrap-up

By the end of Module 2, you have covered the first real layer of LLM application development:

- Connect to a model
- Prompt it clearly
- Classify text
- Summarize text
- Use setup notebooks and pinned dependencies
- Capture traces with MLflow

That sets you up for Module 3, where the model stops relying only on what you put in the prompt and starts working with knowledge retrieved from your own documents.

That is where RAG starts to feel real, because the model finally has a proper document workflow around it. The Module 3 Intro explains why that first RAG demo is only the beginning.

## Feedback

If you try these notebooks on your own reviews, tickets, or transcripts, I would love to hear what surprised you. Sentiment and summaries look simple until real-world text starts pushing back.

## Series Navigation

- Previous: [Module 2.1](https://chanderkant-sharma.medium.com/module-2-1-connecting-to-openai-compatible-apis-and-writing-better-prompts-dc3c8c55f4ec)
- Next: [Module 3 Intro: Why RAG Gets Serious After the First Demo](https://chanderkant-sharma.medium.com/module-3-intro-why-rag-gets-serious-after-the-first-demo-6ce1283631c3)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399)
- Lab notebooks: [Module2 README](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/Module2/README.md)
