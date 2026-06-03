# Sample Project Intro: Building an Insurance Validation Agent

Subtitle: The capstone sample project brings prompts, retrieval, tools, agents, metrics, and MLflow together.

Tags: Agentic AI, Insurance Tech, LangChain, MLflow, AI Evaluation, LiteLLM

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

AI Gateway note: These labs can route OpenAI-compatible calls through LiteLLM. Set `USE_LITELLM=1`, `OPENAI_BASE_URL`, `LITELLM_MASTER_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`; see the [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Insurance validation agent flow diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/project-claim-approver-flow.png)

Image: The sample project connects policy context, reference checks, agent validation, and human comparison into one workflow.

After four modules, the natural question is: can we build something that feels like a real application?

The sample project answers that with an insurance validation agent.

This is not just another chatbot. The goal is to validate insurance records against reference codes, compare agent results with human validation, and measure performance using practical metrics.

For an India tech audience, this is a useful capstone because insurance, fintech, compliance, and operations workflows are everywhere. These domains do not only need fluent answers. They need traceable decisions that someone can review.

## What The Sample Project Tries To Do

The sample project builds an agentic workflow around insurance validation.

At a high level:

```text
Insurance record -> policy/reference lookup -> validation agent -> verdict -> comparison with human results
```

The workflow uses structured data, reference codes, agent reasoning, and evaluation outputs.

The sample project includes:

- Insurance policy data
- Reference validation codes
- Test records
- Agent-generated validation results
- Human versus agent comparison
- Summary metrics

That makes it a good bridge between learning notebooks and real-world AI engineering.

## Notebook Map

The sample project has one main notebook:

```text
Project/code.ipynb
```

It combines tool definitions, claim validation, agent execution, and performance comparison in one workflow.

The notebook centers on a three-tool claim workflow:

```text
summarize_patient_record
-> summarize_policy_guideline
-> check_claim_coverage
```

The agent is instructed to execute that sequence before returning a decision.

## Why Insurance Validation?

Insurance workflows are full of rules, exceptions, documents, and judgement calls. That makes them a useful testbed for agentic AI.

An agent may need to:

- Parse a record
- Lookup a rule
- Compare details
- Decide whether conditions are met
- Explain the reason
- Produce a structured verdict

This is not the same as answering "What is RAG?" It is a decision-support workflow.

## The Human Comparison Is Important

A lot of AI demos stop after showing a model answer. This sample project goes further by comparing agent outputs with human validation.

That matters because AI systems need measurement.

You want to know:

- How often was the agent correct?
- Where did it disagree with humans?
- What types of records caused errors?
- Did the agent produce explainable results?
- Is the workflow good enough to assist, or only good enough to prototype?

This moves the conversation from "AI is cool" to "AI is performing at this level on this task, with these limitations."

## How The Earlier Modules Connect

The sample project uses ideas from the full series:

- Module 1: LLM fundamentals and prompt thinking
- Module 2: model calls, prompting, classification, summarization
- Module 3: retrieval and grounding
- Module 4: tools, agents, multi-step workflows

It also uses the repo-wide improvements:

- Per-project setup notebook
- Pinned dependencies
- `repo_path(...)` for stable file paths
- Local MLflow tracing
- Separate sample project experiment

This gives you a cleaner environment for testing the full workflow.

## What To Watch For

The interesting part is not whether the agent can produce a polished explanation. Most LLMs can do that.

The interesting part is whether the explanation matches the data and whether the final verdict is measurable.

That is the core lesson of the sample project: in business workflows, fluency is not enough. Correctness, traceability, and evaluation matter.

## Feedback

If you run the sample project, I would love to hear whether the workflow felt realistic. Insurance validation is only one example, but the design pattern should feel familiar to anyone building AI around rules and review.

## Series Navigation

- Previous: [Module 4.2](https://chanderkant-sharma.medium.com/module-4-2-multi-user-and-multi-agent-systems)
- Next: [Sample Project Part 1](https://chanderkant-sharma.medium.com/sample-project-part-1-designing-the-insurance-validation-workflow)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-main-intro)
- Repo docs: [Sample Project README](https://chanderkant-sharma.medium.com/sample-project-intro-building-an-insurance-validation-agent)
