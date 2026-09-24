# Module 1.1: LLM Foundations Without the Hype

Subtitle: Tokens, prompts, context windows, and temperature, explained for people who actually build things.

Tags: LLMs, Prompt Engineering, Generative AI, India Tech, AI Engineering, LiteLLM, MLflow

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

Quick setup note: The notebooks use OpenAI-compatible clients. If you run LiteLLM, point `OPENAI_BASE_URL` at the gateway, set `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`, and keep `LITELLM_MASTER_KEY` aligned with your gateway config. The details are in [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Prompt and LLM foundations diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module1-foundations.png)

Image: A simple mental model for prompts, tokens, context, model settings, and output evaluation.

In the Module 1 Intro, we agreed to slow down and build the mental model first. This is where that begins: four ideas that quietly shape every LLM app you will ever build.

Every AI learning path eventually reaches a slightly awkward question: what is an LLM actually doing under the hood?

The popular answer is "it predicts the next token." Correct, but not very satisfying. It is like saying Swiggy is "a logistics system." True, but it does not explain why your dosa arrives hot on some days and takes 50 minutes on others.

For builders, here is a more useful answer: an LLM turns text into a probability-driven response, shaped by patterns it learned during training and by whatever context you hand it at runtime.

Which means your application quality really depends on three things:

- What the model already knows
- What you give it in the prompt
- How you control and evaluate the output

This post slows down on those three ideas before the frameworks start competing for your attention. Grab a chai; most of this needs no code at all.

## Tokens Are the Real Currency

When you send text to an LLM, it does not see words quite the way we do. It sees tokens. A token might be a whole word, part of a word, punctuation, or even whitespace, depending on the tokenizer.

Why should a builder care?

Because tokens quietly decide:

- Cost
- Latency
- Context length
- How much data you can pass into the model

If you are building for Indian users, tokens get interesting. English is usually efficient. Hinglish, names, addresses, policy numbers, and domain-specific abbreviations can behave very differently. A long customer support transcript or an insurance policy can burn through your context budget surprisingly fast.

That is exactly why later modules lean on chunking, retrieval, and summarization. You cannot paste your entire document universe into one prompt and hope for the best. Many of us have tried. The model politely disagrees.

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

The second prompt gives the model a job, a structure, constraints, and a quality bar. In real teams, that is the difference between "AI gave some output" and "we can plug this into an operations workflow."

That move from casual prompting to deliberate prompting is the habit Module 1 is trying to build. Module 2 will put it to work.

## Context Windows Are Not Infinite Memory

A common misunderstanding is that LLMs "remember everything." They do not, at least not in a normal API workflow.

The model only sees what you send in the current context window. If something is not in the prompt, the system message, the conversation history, the retrieved context, or a tool output, the model cannot reliably use it. It is not being forgetful. It simply never saw it.

This matters as soon as you build:

- Chatbots
- RAG systems
- Agents
- Multi-user workflows
- Evaluation notebooks

In Module 3, you will see exactly how retrieved chunks get inserted into this context. Understand context windows now, and RAG will feel far less mysterious later.

## Temperature Is Not Creativity Juice

Temperature controls randomness. Turn it up and outputs get more varied. Turn it down and they get more stable.

For brainstorming, a higher temperature can help. For policy validation, sentiment classification, or structured extraction, you almost always want less randomness.

It is one of those small engineering knobs that saves an awkward meeting later. If your manager asks why the same input got two different answers, temperature is one of the first things to check.

## Providers and API Keys

Modern LLM apps usually talk to OpenAI-compatible providers or gateway-backed endpoints over an API. So your notebook or app needs credentials, an endpoint, a model name, and sometimes a bit of model-specific configuration.

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

Once tokens, prompts, context, temperature, and provider setup click, the rest of the series gets noticeably easier:

- Module 2 prompting feels natural
- Module 3 chunking makes sense
- Module 4 agent loops become debuggable
- The sample project evaluation becomes measurable

You stop treating the model like a black box and start treating it like one component in a larger system.

That is the quiet shift from AI user to AI builder.

Next up is Module 1.2, where we take these ideas out of isolated prompts and into small workflows you can trace, debug, and improve. That is where things start to feel like real applications.

## Feedback

If any concept here still feels fuzzy, that is genuinely useful feedback. Tell me which one tripped you up: tokens, prompts, context, temperature, or provider setup. That kind of detail makes the next version sharper.

## Series Navigation

- Previous: [Module 1 Intro](https://chanderkant-sharma.medium.com/module-1-intro-why-this-ai-learning-path-matters-5c83e617be30)
- Next: [Module 1.2: From Prompts to Real Applications](https://chanderkant-sharma.medium.com/module-1-2-from-prompts-to-real-applications-4acdc6ba9338)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399)
- Lab notebooks: [Module1 README](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/Module1/README.md)
