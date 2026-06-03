# Module 4.2: Multi-user and Multi-agent Systems

Subtitle: Real agentic apps need user context, coordination, and clear responsibility boundaries.

Tags: Multi-agent Systems, LangGraph, AI Agents, Conversational AI, MLflow, LiteLLM

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

AI Gateway note: These labs can route OpenAI-compatible calls through LiteLLM. Set `USE_LITELLM=1`, `OPENAI_BASE_URL`, `LITELLM_MASTER_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`; see the [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Multi-agent architecture diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module4-multi-agent-arch.png)

Image: Multi-user and multi-agent systems need routing, state, specialist agents, and observability.

Once a single agent can use tools, the next challenge is scale.

Not scale as in millions of users on day one. Scale as in realistic complexity:

- More than one user
- More than one conversation
- More than one agent role
- More than one tool
- More than one step before the final answer

Module 4.2 explores multi-user conversational agents and multi-agent systems, the point where clean demos start needing real boundaries.

## Multi-user Agents Need Context

A single-user notebook demo can keep things simple. But real applications usually serve many users.

That means the system needs to know:

- Who is asking?
- What conversation are they in?
- What context belongs to them?
- Which tools are they allowed to use?
- What should not leak between users?

This matters in any serious domain. A customer support assistant should not mix two customers' histories. An insurance workflow should not leak one policyholder's data into another conversation.

Multi-user design is not just a feature. It is a safety requirement, and users should never have to hope the system remembers who is who.

## Notebook Snippet: `Module4/04_BuildingMultiUserConversationalAgenticAI.ipynb`

The multi-user notebook keeps conversation state separate with a session/thread ID:

```python
def call_conversational_agent(agent, prompt, user_session_id, verbose=False):
    events = agent.stream(
        {"messages": [{"role": "user", "content": prompt}]},
        {"configurable": {"thread_id": user_session_id}},
        stream_mode="values",
    )

    for event in events:
        if verbose:
            event["messages"][-1].pretty_print()
```

The same notebook also trims long message history before calling the model:

```python
trimmed_state = trim_messages(
    state["messages"],
    max_tokens=127000,
    strategy="last",
    token_counter=count_tokens_approximately,
    include_system=True,
    allow_partial=True,
)

state_with_instructions = [AGENT_SYS_PROMPT] + trimmed_state
response = [llm_with_tools.invoke(state_with_instructions)]
```

This keeps the agent practical for longer conversations instead of blindly sending the full history forever.

## Conversation Persistence

Agents also need memory, but memory must be handled carefully.

There is a difference between:

- Short-term conversation history
- User profile context
- Retrieved document context
- Tool outputs
- Long-term stored memory

Mixing all of these casually can create confusing behavior. Module 4 helps you think through conversation state and context management more deliberately.

## Multi-agent Systems

Multi-agent systems split responsibilities across agents.

Instead of one agent doing everything, you might have:

- A retrieval agent
- A validation agent
- A summarization agent
- A planner agent
- A reviewer agent

This can make complex workflows easier to manage, but it also adds coordination overhead.

More agents do not automatically mean better results. Sometimes one well-designed agent with good tools is better than five agents passing vague messages to each other.

The trick is to use multiple agents only when roles are genuinely distinct.

## Notebook Snippet: `Module4/05_BuildingMultiAgentSystem.ipynb`

The multi-agent notebook starts by classifying the user's request into the right department workflow:

```python
@tool
def classify_department(query: str) -> str:
    """
    Classify a policy-related question into HR, Finance, or IT.
    """
    prompt = f"""
    You are a policy assistant responsible for determining which internal
    department should handle a given employee query.

    Query: {query}
    """
    return chat_client.invoke(prompt).content
```

The supervisor then decides which agent should act next:

```python
members = ["intent_classifier_agent", "sop_retriever_agent", "answer_generator_agent"]

def supervisor_node(state: State) -> Command[
    Literal["intent_classifier_agent", "sop_retriever_agent", "answer_generator_agent", "__end__"]
]:
    messages = [{"role": "system", "content": SUPERVISOR_PROMPT}] + state["messages"]
    response = chat_client.invoke(messages)
    goto = response.content
    if goto == "FINISH":
        goto = "__end__"
    return Command(goto=goto)
```

And each worker node returns control to the supervisor:

```python
def sop_retriever_node(state: State) -> Command[Literal["supervisor"]]:
    result = sop_retriever_agent.invoke(state)
    return Command(
        update={
            "messages": [
                HumanMessage(
                    content=result["messages"][-1].content,
                    name="sop_retriever_agent",
                )
            ]
        },
        goto="supervisor",
    )
```

## Where LangGraph Helps

LangGraph is useful because agent workflows often look like graphs, not straight lines.

A workflow may branch:

```text
Input -> classify request -> choose path -> call tool -> review -> answer
```

Some paths may loop. Some may stop early. Some may require escalation.

Graph-based orchestration helps represent these flows clearly.

## Observability Becomes Even More Important

In a multi-agent workflow, a wrong final answer may come from many places:

- Wrong routing
- Weak retrieved context
- Bad tool output
- Bad agent handoff
- Missing user context
- Poor final synthesis

This is why MLflow tracing is valuable. You need visibility into the steps, not just the final output.

For learning, tracing helps you understand the notebook. For production, tracing helps you debug incidents and improve workflows.

## A Practical India Tech Example

Imagine a bank support assistant:

- One agent understands the customer query
- One retrieves policy or FAQ content
- One checks eligibility rules
- One drafts the final response
- A human reviews high-risk cases

This is not science fiction. It is a workflow problem. The challenge is designing it safely, measuring it properly, and knowing when a person should step in.

## Module 4 Wrap-up

By the end of Module 4, you have learned:

- Tool design
- ReAct loops
- Custom tool orchestration
- Multi-user context handling
- Multi-agent coordination
- Why tracing and guardrails matter

Now you are ready for the capstone sample project: an insurance validation agent that brings together prompts, retrieval, tools, agents, metrics, and human comparison.

## Feedback

If you try the multi-user or multi-agent notebooks, watch where the state moves. If something feels hard to follow, that is exactly the kind of feedback that can make the workflow explanation better.

## Series Navigation

- Previous: [Module 4.1](https://chanderkant-sharma.medium.com/module-4-1-tools-react-and-agent-loops)
- Next: [Sample Project Intro](https://chanderkant-sharma.medium.com/sample-project-intro-building-an-insurance-validation-agent)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-main-intro)
