# Module 2.2: Sentiment Analysis and Summarization That Feel Useful

Subtitle: Two simple LLM workflows that map nicely to real business problems.

Tags: Sentiment Analysis, Text Summarization, OpenAI, Python, LiteLLM, MLflow

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

AI Gateway note: These labs can route OpenAI-compatible calls through LiteLLM. Set `USE_LITELLM=1`, `OPENAI_BASE_URL`, `LITELLM_MASTER_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`; see the [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Sentiment and summarization workflow diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module2-llm-workflow.png)

Image: Classification and summarization reuse the same dependable path: notebook config, model call, output, and trace.

After connection setup and prompt engineering, Module 2 moves into two practical tasks that many teams understand immediately: sentiment analysis and summarization.

These are not random examples. They are two of the most common ways teams first bring LLMs into real workflows.

You have a pile of text. Reviews, tickets, calls, chats, emails, notes, documents. You want to understand it faster. LLMs are good at that, provided you keep the workflow controlled and check the output with a little skepticism.

## Sentiment Analysis: More Than Positive Or Negative

The sentiment analysis notebook uses patient review data. The basic task is to classify text into sentiment categories.

At first glance, this looks simple:

```text
Review -> model -> sentiment label
```

But real sentiment analysis needs careful prompting. Patient feedback can be mixed. A person may praise the doctor but complain about billing. They may sound polite but still be dissatisfied. They may mention multiple departments in one review.

So the prompt needs to be clear about:

- Allowed labels
- How to handle mixed sentiment
- Whether to include reasoning
- Whether to return structured output
- Whether to avoid assumptions

This is where Module 1 foundations and Module 2 prompt engineering come together.

## Notebook Snippet: `Module2/03_Seniment_Analysis.ipynb`

The sentiment notebook reads the patient review CSV with a repository-relative path:

```python
filepath = repo_path("Module2", "Data", "SentimentAnalysis", "Patient_Reviews.csv")
reviews = pd.read_csv(filepath)
```

It also uses a Pydantic model to keep LLM output structured:

```python
class SentimentOutput(BaseModel):
    sentiment_label: str = Field(..., description="positive, negative, or neutral")
    confidence_score: float = Field(..., description="A value between 0 and 1")
    emotions: List[str]
```

## Why This Matters In India

India has high-volume service environments: healthcare, fintech, telecom, edtech, ecommerce, public services, and more. Teams often receive huge amounts of feedback, and manual review does not scale well.

Sentiment analysis can help teams:

- Track dissatisfaction patterns
- Spot urgent negative feedback
- Summarize customer voice
- Route issues faster
- Compare feedback by location, product, or team

The notebook is a small lab, but the pattern is very real: use the model to reduce reading load, then let people focus on judgment.

## Summarization: Compress Without Losing Meaning

The summarization notebook works with conversation-style data. The goal is to turn long text into concise, useful summaries.

Good summarization is not just making text shorter. It is preserving what matters.

A useful summary should capture:

- Main issue
- Important facts
- Decisions or next steps
- Tone or urgency when relevant
- Missing information

This matters for support teams, sales calls, meeting notes, insurance claims, medical conversations, and internal operations.

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

LLMs can summarize beautifully and still be wrong. That is the danger.

If the transcript says the refund is pending, the summary should not say the refund is approved. If the patient complains about wait time, the summary should not invent a diagnosis.

So summarization prompts should include constraints like:

```text
Only use facts present in the input.
Do not invent missing details.
If the next action is unclear, say "next action not specified."
```

This kind of guardrail is not fancy, but it is useful.

## Tracing The Workflow

With MLflow running locally, each notebook can log traces to its own experiment. This helps you compare prompt versions, inspect model calls, and understand what changed between runs.

That becomes especially useful when you iterate:

- Prompt version 1 gives verbose summaries
- Prompt version 2 gives structured summaries
- Prompt version 3 adds action items

Without traces, these changes blur together. With traces, you can review them.

## Module 2 Wrap-up

By the end of Module 2, you have learned the first layer of LLM application development:

- Connect to a model
- Prompt it clearly
- Classify text
- Summarize text
- Use setup notebooks and pinned dependencies
- Capture traces with MLflow

This prepares you for Module 3, where the model stops relying only on prompt input and starts working with retrieved knowledge from documents.

That is where RAG becomes real, because the model finally has a document workflow around it.

## Feedback

If you test these notebooks with your own reviews, tickets, or transcripts, I would like to hear what surprised you. Sentiment and summaries look simple until real-world text starts pushing back.

## Series Navigation

- Previous: [Module 2.1](https://chanderkant-sharma.medium.com/module-2-1-connecting-to-openai-and-writing-better-prompts)
- Next: [Module 3 Intro](https://chanderkant-sharma.medium.com/module-3-intro-why-rag-gets-serious-after-the-first-demo)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-main-intro)
