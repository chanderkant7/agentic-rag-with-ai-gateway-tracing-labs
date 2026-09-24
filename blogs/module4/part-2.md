# Module 4.2: Multi-user and Multi-agent Systems

Subtitle: Real agentic apps need user context, coordination, and clear lines of responsibility.

Tags: Multi-agent Systems, LangGraph, AI Agents, Conversational AI, MLflow, LiteLLM

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

Quick setup note: The notebooks use OpenAI-compatible clients. If you run LiteLLM, point `OPENAI_BASE_URL` at the gateway, set `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`, and keep `LITELLM_MASTER_KEY` aligned with your gateway config. The details are in [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Multi-agent architecture diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/module4-multi-agent-arch.png)

Image: Multi-user and multi-agent systems need routing, state, specialist agents, and good observability.

In Module 4.1, we built a single agent that could pick tools, observe results, and loop until it had an answer. Once that works, the next challenge is scale.

Not scale as in millions of users on day one. Scale as in realistic complexity:

- More than one user
- More than one conversation
- More than one agent role
- More than one tool
- More than one step before the final answer

This post explores multi-user conversational agents and multi-agent systems, the point where clean demos start needing real boundaries.

## Multi-user Agents Need Context

A single-user notebook demo can keep things simple. Real applications almost always serve many users at once.

So the system needs to know:

- Who is asking?
- What conversation are they in?
- What context belongs to them?
- Which tools are they allowed to use?
- What should not leak between users?

This matters in any serious domain. A customer support assistant must never mix up two customers' histories. An insurance workflow must never leak one policyholder's data into someone else's conversation.

Multi-user design is not just a feature. It is a safety requirement, and users should never have to hope the system remembers who is who.

## Notebook Snippet: `Module4/04_BuildingMultiUserConversationalAgenticAI.ipynb`

The multi-user notebook keeps each conversation's state separate using a session or thread ID:

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

That keeps the agent practical during long conversations, instead of blindly sending the entire history forever and running into the context limits we talked about back in Module 1.1.

## Conversation Persistence

Agents need memory too, but memory needs careful handling.

There is a real difference between:

- Short-term conversation history
- User profile context
- Retrieved document context
- Tool outputs
- Long-term stored memory

Mixing all of these casually leads to confusing behavior. Module 4 helps you think about conversation state and context management far more deliberately.

## Multi-agent Systems

Multi-agent systems split responsibilities across several agents.

Instead of one agent doing everything, you might have:

- A retrieval agent
- A validation agent
- A summarization agent
- A planner agent
- A reviewer agent

This can make complex workflows easier to manage, but it also adds coordination overhead.

More agents do not automatically mean better results. Sometimes one well-designed agent with good tools beats five agents passing vague messages to each other.

The trick is to reach for multiple agents only when the roles are genuinely distinct.

## Notebook Snippet: `Module4/05_BuildingMultiAgentSystem.ipynb`

The multi-agent notebook begins by classifying each request into the right department workflow:

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

A supervisor then decides which agent should act next:

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

And every worker node hands control back to the supervisor:

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

LangGraph earns its place here because agent workflows usually look like graphs, not straight lines.

A workflow might branch like this:

```text
Input -> classify request -> choose path -> call tool -> review -> answer
```

Some paths loop. Some stop early. Some need escalation to a person.

Graph-based orchestration lets you represent those flows clearly, instead of hiding them inside one enormous prompt.

## Observability Becomes Even More Important

In a multi-agent workflow, a wrong final answer can come from many places:

- Wrong routing
- Weak retrieved context
- Bad tool output
- Bad agent handoff
- Missing user context
- Poor final synthesis

That is why MLflow tracing is so valuable here. You need visibility into every step, not just the final output.

While learning, tracing helps you understand the notebook. In production, it helps you debug incidents and keep improving the workflow.

## A Practical India Tech Example

Picture a bank support assistant:

- One agent understands the customer query
- One retrieves policy or FAQ content
- One checks eligibility rules
- One drafts the final response
- A human reviews high-risk cases

This is not science fiction. It is workflow design. The real challenge is building it safely, measuring it properly, and knowing when a person should step in.

## Module 4 Wrap-up

By the end of Module 4, you have learned:

- Tool design
- ReAct loops
- Custom tool orchestration
- Multi-user context handling
- Multi-agent coordination
- Why tracing and guardrails matter

Now you are ready for the capstone. The Sample Project Intro brings everything together in a healthcare insurance claim approval agent that combines prompts, retrieval, tools, agents, metrics, and a comparison with human decisions.

## Feedback

If you try the multi-user or multi-agent notebooks, keep an eye on where the state moves. If something feels hard to follow, that is exactly the feedback that can make these explanations better.

## Series Navigation

- Previous: [Module 4.1](https://chanderkant-sharma.medium.com/module-4-1-tools-react-and-agent-loops-1fc5334d5b14)
- Next: [Sample Project Intro: Building a Healthcare Insurance Claim Approval Agent](https://chanderkant-sharma.medium.com/sample-project-intro-building-a-healthcare-insurance-claim-approval-agent-a1e3915b712a)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399)
- Lab notebooks: [Module4 README](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/Module4/README.md)
