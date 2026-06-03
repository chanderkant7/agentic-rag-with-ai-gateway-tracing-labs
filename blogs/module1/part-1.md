# Module 1.1: LLM Foundations Without the Hype

Subtitle: Tokens, prompts, context windows, and temperature explained for practical builders.

Tags: LLMs, Prompt Engineering, Generative AI, India Tech, AI Engineering, LiteLLM, MLflow

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

AI Gateway note: These labs can route OpenAI-compatible calls through LiteLLM. Set `USE_LITELLM=1`, `OPENAI_BASE_URL`, `LITELLM_MASTER_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`; see the [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Prompt and LLM foundations diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module1-foundations.png)

Image: A simple mental model for prompts, tokens, context, model settings, and output evaluation.

Every AI journey eventually reaches a slightly awkward question: what is an LLM actually doing?

The popular answer is "it predicts the next token." Correct, but not very satisfying. It is like saying Swiggy is "a logistics system." True, but it does not explain why your dosa arrives hot on some days and takes 50 minutes on others.

For builders, the useful answer is this: an LLM turns text into a probability-driven response based on patterns it learned during training and the context you provide at runtime.

That means your application quality depends on three things:

- What the model already knows
- What you give it in the prompt
- How you control and evaluate the output

This post is about getting comfortable with these three before the frameworks start competing for your attention.

## Tokens Are the Real Currency

When you send text to an LLM, the model does not see words exactly the way we do. It sees tokens. A token can be a word, part of a word, punctuation, or even whitespace depending on the tokenizer.

Why should you care as a builder?

Because tokens affect:

- Cost
- Latency
- Context length
- How much data you can pass into the model

If you are building for Indian use cases, token behavior can get interesting. English is usually efficient. Hinglish, names, addresses, policy numbers, and domain-specific abbreviations can behave differently. A long customer support transcript or insurance policy can burn through context quickly.

This is why later modules use chunking, retrieval, and summarization. You cannot just paste your whole document universe into one prompt and hope for the best.

## Prompts Are Instructions, Not Wishes

A prompt is not a magic spell. It is an instruction packet.

Weak prompt:

```text
Summarize this.
```

Better prompt:

```text
Summarize this customer conversation in 5 bullet points.
Include the issue, customer sentiment, promised action, pending owner, and urgency.
Keep it under 120 words.
```

The second prompt gives the model a job, structure, constraints, and quality expectations. In real teams, this is the difference between "AI gave some output" and "this can go into an operations workflow."

Module 1 thinking helps you move from casual prompting to deliberate prompting.

## Context Windows Are Not Infinite Memory

One common misunderstanding is that LLMs "remember everything." They do not, at least not in the normal API workflow.

The model sees what you send in the current context window. If something is not in the prompt, system message, conversation history, retrieved context, or tool output, the model cannot reliably use it.

This matters when you build:

- Chatbots
- RAG systems
- Agents
- Multi-user workflows
- Evaluation notebooks

Later in the series, you will see how retrieved chunks are inserted into context. But if you understand context windows first, RAG becomes much less mysterious.

## Temperature Is Not Creativity Juice

Temperature controls randomness. Higher temperature can make outputs more varied. Lower temperature makes outputs more stable.

For brainstorming, higher temperature may be useful. For policy validation, sentiment classification, or structured extraction, you usually want lower randomness.

This is a practical engineering tradeoff. If your manager asks why the same input got two different answers, temperature is one of the first things to check.

## Providers and API Keys

Modern LLM apps often use OpenAI, Azure OpenAI, or other providers through APIs. That means your notebook or app needs credentials, endpoints, deployment names, and sometimes model-specific configuration.

The repo keeps credentials in `.env` and expects each module setup to install the right dependencies. That separation matters. Code should not hard-code secrets, and notebooks should not depend on whoever ran them last from whichever folder.

## Notebook Snippet: Provider Setup

The provider setup pattern first appears in `Module2/01_OpenAI_Connection.ipynb`:

```python
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")
chat_model_name = os.getenv("CHAT_MODEL_NAME")

chat_client = openai.OpenAI(
    api_key=api_key,
    base_url=base_url,
)
```

That one `base_url` is what lets the same notebook call a direct provider or a LiteLLM AI Gateway.

## Why This Foundation Pays Off

Once you understand tokens, prompts, context, temperature, and provider setup, the rest of the series becomes easier:

- Module 2 prompting feels natural
- Module 3 chunking makes sense
- Module 4 agent loops become debuggable
- The sample project evaluation becomes measurable

You stop treating the model like a black box and start treating it like a component in a system.

That is the quiet shift from AI user to AI builder.

## Feedback

If any concept here still feels fuzzy, that is useful feedback. Tell me which one: tokens, prompts, context, temperature, or provider setup. I can make the next version sharper.

## Series Navigation

- Previous: [Module 1 Intro](https://chanderkant-sharma.medium.com/module-1-intro-why-this-ai-learning-path-matters)
- Next: [Module 1.2: From Prompts to Real Applications](https://chanderkant-sharma.medium.com/module-1-2-from-prompts-to-real-applications)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-main-intro)
