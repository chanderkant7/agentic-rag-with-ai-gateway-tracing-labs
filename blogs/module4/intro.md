# Module 4 Intro: From Chatbots to Agents That Use Tools

Subtitle: Agentic AI starts when the model can reason, choose tools, and act inside a workflow.

Tags: Agentic AI, LangChain, LangGraph, ReAct, AI Agents, LiteLLM, MLflow

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

AI Gateway note: These labs can route OpenAI-compatible calls through LiteLLM. Set `USE_LITELLM=1`, `OPENAI_BASE_URL`, `LITELLM_MASTER_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`; see the [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Module 4 agent architecture diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module4-tool-use-agent-arch.png)

Image: Agentic AI becomes useful when the model can choose tools, observe results, and continue inside a controlled workflow.

At some point, a normal chatbot starts feeling limited.

You ask a question, it replies. You ask another question, it replies again. Useful, but passive.

An agent feels different. It can decide that it needs to call a tool, look something up, process intermediate results, and continue until it reaches an answer.

That shift from reply-only chat to tool-backed workflow is what Module 4 explores.

## What Makes Something An Agent?

The word "agent" gets used very casually now. Sometimes it means a chatbot with a longer prompt. Sometimes it means a workflow with tools. Sometimes it means a fully autonomous system that probably should not be fully autonomous.

For this module, keep it practical:

An agent is an LLM-powered workflow that can reason about a task, choose actions, use tools, observe results, and continue toward a final answer.

The basic loop looks like this:

```text
Thought -> Action -> Observation -> Thought -> Final Answer
```

This is the ReAct pattern: reasoning plus acting.

## Why Tools Matter

LLMs are good at language, but they are not naturally good at everything.

They should not guess the result of a database query. They should not pretend to know the latest inventory count. They should not calculate critical business logic from memory when a tool can do it correctly.

Tools let the agent interact with real functions:

- Search a dataset
- Lookup a policy
- Run a calculation
- Fetch user context
- Validate an input
- Call another system

This turns the model from "answer generator" into "workflow coordinator."

## Why Indian Teams Should Care

Many Indian tech teams work with process-heavy domains:

- Insurance
- Banking
- Healthcare
- Customer support
- Logistics
- Telecom
- Government services
- Education operations

These domains are full of rules, documents, handoffs, and exceptions. A simple chatbot can answer FAQs, but an agent can help navigate workflows.

For example, an insurance agent workflow may need to read a policy, lookup reference codes, validate conditions, compare results, and explain the decision.

That is more than chat. It is an early version of decision support.

## What Module 4 Covers

Module 4 includes notebooks on:

- Implementing tools for agentic AI
- Building ReAct agents with built-in tools
- Building ReAct agents from scratch
- Multi-user conversational agentic AI
- Multi-agent systems

The progression is intentional. First you learn tools. Then you learn the agent loop. Then you build more complex flows with users and multiple agents.

## Notebook Map

Module 4 uses these Python notebooks:

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

By the end of Module 4, the same idea becomes a graph with separate routing, retrieval, and answer-generation agents.

## LangChain, LangGraph, And MLflow

The notebooks use current LangChain and LangGraph dependencies. They also include initial setup cells for repository-relative paths and local MLflow tracing.

Tracing is especially useful for agents because agent behavior can be multi-step. You want to inspect:

- Which tool was selected
- What input was passed to the tool
- What observation came back
- Why the agent continued or stopped

Without tracing, debugging agents can become confusing quickly.

## The Big Warning

Agents are powerful, but they are not magic employees. They need boundaries.

A good agent system has:

- Clear tools
- Safe tool inputs
- Guardrails
- Logging
- Evaluation
- Human review when stakes are high

Module 4 is about learning the pattern without pretending that autonomy solves everything.

## Where This Leads

After Module 4, the sample project brings everything together in an insurance validation workflow. That is where agents, tools, data, metrics, and human comparison meet.

Module 4 is the final skill-building module before the capstone, so it is also where the series becomes more careful about boundaries and responsibility.

## Feedback

If agents have felt either magical or confusing so far, tell me which part changed that feeling: tools, ReAct loops, LangGraph, or tracing. That is the feedback that helps this module become clearer.

## Series Navigation

- Previous: [Module 3.2](https://chanderkant-sharma.medium.com/module-3-2-retrieval-re-ranking-and-rag-evaluation)
- Next: [Module 4.1](https://chanderkant-sharma.medium.com/module-4-1-tools-react-and-agent-loops)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-main-intro)
- Repo docs: [Module4 README](https://chanderkant-sharma.medium.com/module-4-intro-from-chatbots-to-agents-that-use-tools)
