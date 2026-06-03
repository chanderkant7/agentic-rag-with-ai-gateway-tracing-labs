# Module 4.1: Tools, ReAct, and Agent Loops

Subtitle: The real skill in agentic AI is designing the actions an agent can safely take.

Tags: AI Agents, ReAct, LangChain, LangGraph, Tool Use, LiteLLM, MLflow

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

AI Gateway note: These labs can route OpenAI-compatible calls through LiteLLM. Set `USE_LITELLM=1`, `OPENAI_BASE_URL`, `LITELLM_MASTER_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`; see the [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Tool use agent architecture diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module4-tool-use-agent-arch.png)

Image: Tool use turns an LLM from a plain answer generator into a workflow coordinator.

The first half of Module 4 is about tools and the agent loop, which is where agentic AI becomes much more concrete.

This is where you stop asking the model to answer everything from memory and start giving it controlled actions it can take.

That control is important. A useful agent is not a model doing random things. It is a model operating inside a designed workflow.

## Tool Design Comes First

A tool is usually just a function with a clear name, description, input schema, and output.

But for agents, tool design is a product decision as much as a coding decision.

A good tool should be:

- Focused
- Easy to describe
- Safe to call
- Predictable in output
- Useful for the agent's task

If a tool is vague, the agent may misuse it. If the input schema is loose, the agent may pass messy arguments. If the output is unclear, the next reasoning step becomes weak.

In short: bad tools create bad agents, no matter how impressive the model looks.

## Notebook Snippet: `Module4/01_ImplementingToolsForAgenticAI.ipynb`

The tools are regular Python functions decorated for LangChain:

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

ReAct stands for reasoning and acting. The agent alternates between thinking about what to do, taking an action, observing the result, and deciding what comes next.

The loop is:

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

This pattern is powerful because the model does not need to solve everything in one shot. It can decompose the problem.

For example:

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

That is much closer to how real operational workflows happen.

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

That is the key learning move: the prebuilt notebook teaches the ReAct pattern, and the scratch notebook shows how the loop is wired.

## Built-in Tools vs Custom Tools

Module 4 explores both built-in tools and tools built from scratch.

Built-in tools are useful for learning patterns quickly. Custom tools are where your actual business value appears.

For Indian enterprise use cases, custom tools may connect to:

- Internal knowledge bases
- Policy rules
- CRM records
- Ticketing systems
- Pricing calculators
- Compliance checks
- Search indexes

The agent becomes useful when it can act on your domain, not just generic web-style tasks.

## Notebook Snippet: Doctor Recommendation Tool

The first Module 4 notebook also shows a domain-specific tool that asks the LLM to reason over a doctor list:

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

This is a useful example of tool design where retrieval, domain data, and model reasoning meet in a controlled way.

## Why Tracing Is Critical For Agents

Agent behavior is multi-step, so debugging is harder than debugging a single model call.

If an answer is wrong, you need to know:

- Did the agent choose the wrong tool?
- Did the tool return unexpected data?
- Did the agent ignore the observation?
- Did the final prompt overrule the evidence?

MLflow tracing helps make these steps visible. Running the local server before notebooks lets each Module 4 notebook log into its own experiment.

## Do Not Skip Guardrails

Agents can call tools. That means agents can also call the wrong tool, call a tool too many times, or use the right tool with bad input.

Good agent design includes:

- Limited tool access
- Clear tool descriptions
- Input validation
- Error handling
- Stop conditions
- Human review for sensitive tasks

This is especially important in domains like finance, insurance, and healthcare.

## The Takeaway

Part 1 of Module 4 teaches that agentic AI is not just prompting. It is workflow design.

The model reasons. Tools act. Observations guide the next step. Traces help you debug. Guardrails keep the system sane.

Once you understand that loop, multi-user and multi-agent systems become easier to reason about because you can see where each decision happens.

## Feedback

If you build your own tool after this post, pay attention to how the agent calls it. Tool names, descriptions, and outputs teach the model what kind of teammate the function is allowed to be.

## Series Navigation

- Previous: [Module 4 Intro](https://chanderkant-sharma.medium.com/module-4-intro-from-chatbots-to-agents-that-use-tools)
- Next: [Module 4.2](https://chanderkant-sharma.medium.com/module-4-2-multi-user-and-multi-agent-systems)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-main-intro)
