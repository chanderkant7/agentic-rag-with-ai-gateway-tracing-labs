# Module 4.1: Tools, ReAct, and Agent Loops

Subtitle: The real skill in agentic AI is designing the actions an agent is allowed to take, and making them safe.

Tags: AI Agents, ReAct, LangChain, LangGraph, Tool Use, LiteLLM, MLflow

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

Quick setup note: The notebooks use OpenAI-compatible clients. If you run LiteLLM, point `OPENAI_BASE_URL` at the gateway, set `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`, and keep `LITELLM_MASTER_KEY` aligned with your gateway config. The details are in [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Tool use agent architecture diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module4-tool-use-agent-arch.png)

Image: Tool use turns an LLM from a plain answer generator into a workflow coordinator.

The Module 4 Intro described an agent as a model that can reason, choose actions, and observe results. This post makes that concrete, starting with the two building blocks everything else rests on: tools and the agent loop.

This is where you stop asking the model to answer everything from memory and start giving it controlled actions it can take.

That control matters. A useful agent is not a model doing random things. It is a model operating inside a workflow you designed on purpose.

## Tool Design Comes First

A tool is usually just a function with a clear name, a description, an input schema, and an output.

But for agents, tool design is as much a product decision as a coding one.

A good tool is:

- Focused
- Easy to describe
- Safe to call
- Predictable in output
- Useful for the agent's task

If a tool is vague, the agent will misuse it. If the input schema is loose, the agent will pass messy arguments. If the output is unclear, the next reasoning step gets weaker.

Short version: bad tools create bad agents, however impressive the model looks.

## Notebook Snippet: `Module4/01_ImplementingToolsForAgenticAI.ipynb`

The tools are ordinary Python functions, decorated for LangChain:

```python
@tool
def search_pubmed(query: str) -> list:
    """Search PubMed for scientific articles related to the query."""
    results = pubmed_db.similarity_search(query, k=5)
    return [doc.page_content for doc in results]

tools = [search_web, search_pubmed, recommend_doctor]
llm_with_tools = chat_client.bind_tools(tools=tools)
```

## The ReAct Pattern

ReAct stands for reasoning and acting. The agent alternates between thinking about what to do, taking an action, observing what happened, and deciding what comes next.

The loop runs like this:

```text
User task
Thought
Action
Observation
Thought
Action
Observation
Final answer
```

The pattern is powerful because the model does not have to solve everything in one shot. It can break the problem into steps.

Here is a small example:

```text
Question: Is this policy record valid?
Thought: I need to check the policy code.
Action: lookup_reference_code
Observation: Code A123 requires active coverage.
Thought: I need to inspect the policy status.
Action: get_policy_status
Observation: Status is inactive.
Final answer: The record is invalid because coverage is inactive.
```

That is much closer to how real operational work actually happens.

## Notebook Snippet: ReAct Notebooks

`Module4/02_BuildingToolsReactAgenticAIBuiltin.ipynb` uses LangGraph's prebuilt ReAct helper, while `Module4/03_BuildingToolsReactAgenticAIScratch.ipynb` builds the graph manually:

```python
from langgraph.prebuilt import create_react_agent

tools = [search_web, search_pubmed, recommend_doctor]
agent = create_react_agent(chat_client, tools)
```

The scratch notebook makes the routing explicit with `StateGraph`:

```python
builder = StateGraph(State)

builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_node("tools", ToolNode(tools=tools))

builder.add_edge(START, "tool_calling_llm")
builder.add_conditional_edges(
    "tool_calling_llm",
    tools_condition,
)
builder.add_edge("tools", "tool_calling_llm")

agent = builder.compile()
```

That is the useful learning move here: the prebuilt notebook teaches you the ReAct pattern, and the scratch notebook shows you exactly how the loop is wired, so nothing about it feels like magic.

## Built-in Tools vs Custom Tools

Module 4 explores both built-in tools and tools you build yourself.

Built-in tools help you learn patterns quickly. Custom tools are where your real business value shows up.

For Indian enterprise use cases, custom tools might connect to:

- Internal knowledge bases
- Policy rules
- CRM records
- Ticketing systems
- Pricing calculators
- Compliance checks
- Search indexes

An agent becomes truly useful when it can act on your domain, not just on generic web-style tasks.

## Notebook Snippet: Doctor Recommendation Tool

The first Module 4 notebook also shows a domain-specific tool that asks the LLM to reason over a list of doctors:

```python
@tool
def recommend_doctor(query: str) -> dict:
    """Recommend the most suitable doctor based on the user's symptoms."""
    doctors_list = str(doctors_db)
    prompt = f"""
    You are an assistant helping recommend a doctor based on a patient's health issues.

    Doctors:
    {doctors_list}

    Patient query:
    {query}
    """
    return chat_client.invoke(prompt).content
```

It is a nice example of tool design where retrieval, domain data, and model reasoning meet in a controlled way.

## Why Tracing Is Critical For Agents

Agent behavior happens over several steps, so debugging it is much harder than debugging a single model call.

When an answer is wrong, you need to know:

- Did the agent choose the wrong tool?
- Did the tool return unexpected data?
- Did the agent ignore the observation?
- Did the final prompt overrule the evidence?

MLflow tracing makes each of those steps visible. Start the local server before running the notebooks, and each Module 4 notebook logs into its own experiment.

## Do Not Skip Guardrails

Agents can call tools. Which also means they can call the wrong tool, call a tool too many times, or call the right tool with bad input.

Good agent design includes:

- Limited tool access
- Clear tool descriptions
- Input validation
- Error handling
- Stop conditions
- Human review for sensitive tasks

This is especially important in finance, insurance, and healthcare, the same kind of domain the sample project lives in.

## The Takeaway

Part 1 of Module 4 teaches one big lesson: agentic AI is not just prompting. It is workflow design.

The model reasons. Tools act. Observations guide the next step. Traces help you debug. Guardrails keep the whole system sane.

Once that loop makes sense, bigger systems get much easier to reason about. In Module 4.2, we add real users with their own context, and multiple agents that need to coordinate without stepping on each other.

## Feedback

If you build your own tool after reading this, watch closely how the agent calls it. Tool names, descriptions, and outputs quietly teach the model what kind of teammate that function is allowed to be.

## Series Navigation

- Previous: [Module 4 Intro](https://chanderkant-sharma.medium.com/module-4-intro-from-chatbots-to-agents-that-use-tools-848d84b62a6e)
- Next: [Module 4.2: Multi-user and Multi-agent Systems](https://chanderkant-sharma.medium.com/module-4-2-multi-user-and-multi-agent-systems-e45f19a14bb3)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399)
- Lab notebooks: [Module4 README](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/Module4/README.md)
