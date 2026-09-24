# Module 4 Intro: From Chatbots to Agents That Use Tools

Subtitle: Agentic AI begins when the model can reason, pick a tool, and act inside a workflow you designed.

Tags: Agentic AI, LangChain, LangGraph, ReAct, AI Agents, LiteLLM, MLflow

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

Quick setup note: The notebooks use OpenAI-compatible clients. If you run LiteLLM, point `OPENAI_BASE_URL` at the gateway, set `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`, and keep `LITELLM_MASTER_KEY` aligned with your gateway config. The details are in [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Module 4 agent architecture diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module4-tool-use-agent-arch.png)

Image: Agentic AI gets useful when the model can choose tools, observe the results, and keep going inside a controlled workflow.

By the end of Module 3, our model could answer from real documents instead of memory. That is a big step. But at some point, even a well-grounded chatbot starts to feel limited.

You ask a question, it replies. You ask another, it replies again. Useful, but passive.

An agent feels different. It can decide it needs to call a tool, look something up, work with the intermediate result, and keep going until it reaches an answer.

That shift, from reply-only chat to a tool-backed workflow, is what Module 4 is all about.

## What Makes Something An Agent?

The word "agent" gets thrown around very casually these days. Sometimes it means a chatbot with a longer prompt. Sometimes it means a workflow with tools. And sometimes it means a fully autonomous system that probably should not be fully autonomous.

For this module, let us keep it practical:

An agent is an LLM-powered workflow that can reason about a task, choose actions, use tools, observe results, and continue toward a final answer.

The basic loop looks like this:

```text
Thought -> Action -> Observation -> Thought -> Final Answer
```

This is the ReAct pattern: reasoning plus acting, one step at a time.

## Why Tools Matter

LLMs are great with language, but they are not naturally good at everything.

They should not guess the result of a database query. They should not pretend to know today's inventory count. And they should not work out critical business logic from memory when a tool can do it correctly.

Tools let an agent work with real functions:

- Search a dataset
- Lookup a policy
- Run a calculation
- Fetch user context
- Validate an input
- Call another system

Now the model is less of an "answer generator" and more of a workflow coordinator.

## Why Indian Teams Should Care

Many Indian tech teams work in process-heavy domains:

- Insurance
- Banking
- Healthcare
- Customer support
- Logistics
- Telecom
- Government services
- Education operations

These domains are full of rules, documents, handoffs, and exceptions. A simple chatbot can answer FAQs, but an agent can help people navigate the actual workflow.

An insurance workflow, for example, might need to read a policy, look up reference codes, validate conditions, compare results, and explain the decision. You will build exactly that in the sample project.

That is more than chat. It is an early form of decision support.

## What Module 4 Covers

Module 4 includes notebooks on:

- Implementing tools for agentic AI
- Building ReAct agents with built-in tools
- Building ReAct agents from scratch
- Multi-user conversational agentic AI
- Multi-agent systems

The order is intentional. First you learn tools. Then you learn the agent loop. Then you build richer flows with multiple users and multiple agents.

## Notebook Map

These are the Python notebooks behind Module 4:

```text
Module4/01_ImplementingToolsForAgenticAI.ipynb
Module4/02_BuildingToolsReactAgenticAIBuiltin.ipynb
Module4/03_BuildingToolsReactAgenticAIScratch.ipynb
Module4/04_BuildingMultiUserConversationalAgenticAI.ipynb
Module4/05_BuildingMultiAgentSystem.ipynb
```

The first notebook introduces tools with LangChain's `@tool` decorator:

```python
@tool
def search_web(query: str) -> list:
    """Search the web for general or up-to-date healthcare information."""
    results = web_search_db.similarity_search(query, k=5)
    return [doc.page_content for doc in results]
```

The later notebooks build on the same pattern:

```python
healthbuddy_agent = create_react_agent(
    model=chat_client,
    tools=tools,
    prompt=AGENT_SYS_PROMPT,
)
```

By the end of Module 4, the same idea grows into a graph with separate agents for routing, retrieval, and answer generation.

## LangChain, LangGraph, And MLflow

The notebooks use current LangChain and LangGraph packages, plus the same initial setup cells for repository-relative paths and local MLflow tracing you have used since Module 2.

Tracing is especially valuable for agents, because agent behavior unfolds over several steps. You want to see:

- Which tool was selected
- What input was passed to the tool
- What observation came back
- Why the agent continued or stopped

Without tracing, agents can get confusing very quickly.

## The Big Warning

Agents are powerful, but they are not magic employees. They need boundaries.

A good agent system has:

- Clear tools
- Safe tool inputs
- Guardrails
- Logging
- Evaluation
- Human review when stakes are high

Module 4 is about learning the pattern without pretending autonomy solves everything.

## Where This Leads

After Module 4, the sample project brings everything together in a healthcare insurance claim approval workflow. That is where agents, tools, data, metrics, and human comparison finally meet.

Module 4 is the last skill-building stop before that capstone, so it is also where the series gets more careful about boundaries and responsibility. We start in Module 4.1 with the building blocks: tools, ReAct, and the agent loop.

## Feedback

If agents have felt either magical or confusing so far, tell me which part changed that feeling for you: tools, ReAct loops, LangGraph, or tracing. That is the feedback that helps this module get clearer.

## Series Navigation

- Previous: [Module 3.2](https://chanderkant-sharma.medium.com/module-3-2-retrieval-re-ranking-and-rag-evaluation-1001b93b1c41)
- Next: [Module 4.1: Tools, ReAct, and Agent Loops](https://chanderkant-sharma.medium.com/module-4-1-tools-react-and-agent-loops-1fc5334d5b14)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399)
- Lab notebooks: [Module4 README](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/Module4/README.md)
