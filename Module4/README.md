# Module 4: Agentic AI

Module 4 is where the model stops only answering and starts acting. You begin with basic tool calling and grow into full LangGraph agent systems. The main healthcare assistant, HealthBuddy, starts with a few custom tools and becomes a ReAct agent with conversation memory, multi-user sessions, and doctor appointment tools. The module closes with a separate multi-agent SOP assistant.

One idea runs through every notebook: good agents come from well-designed tools and clear boundaries, not from giving the model free rein.

## Read the Articles

- [Module 4 Intro: From Chatbots to Agents That Use Tools](https://chanderkant-sharma.medium.com/module-4-intro-from-chatbots-to-agents-that-use-tools-848d84b62a6e)
- [Module 4.1: Tools, ReAct, and Agent Loops](https://chanderkant-sharma.medium.com/module-4-1-tools-react-and-agent-loops-1fc5334d5b14)
- [Module 4.2: Multi-user and Multi-agent Systems](https://chanderkant-sharma.medium.com/module-4-2-multi-user-and-multi-agent-systems-e45f19a14bb3)

## Lab Sequence

| Order | Notebook | What you build |
| --- | --- | --- |
| 1 | [01_ImplementingToolsForAgenticAI.ipynb](01_ImplementingToolsForAgenticAI.ipynb) | Custom health tools and manual LLM tool-call execution. |
| 2 | [02_BuildingToolsReactAgenticAIBuiltin.ipynb](02_BuildingToolsReactAgenticAIBuiltin.ipynb) | A HealthBuddy ReAct agent using LangGraph's `create_react_agent`. |
| 3 | [03_BuildingToolsReactAgenticAIScratch.ipynb](03_BuildingToolsReactAgenticAIScratch.ipynb) | The same ReAct workflow built from explicit LangGraph state, nodes, and edges. |
| 4 | [04_BuildingMultiUserConversationalAgenticAI.ipynb](04_BuildingMultiUserConversationalAgenticAI.ipynb) | A multi-user conversational HealthBuddy with memory, slots, and bookings. |
| 5 | [05_BuildingMultiAgentSystem.ipynb](05_BuildingMultiAgentSystem.ipynb) | A multi-agent SOP assistant with classifier, retriever, answer generator, and supervisor agents. |

## HealthBuddy Progression

The first four notebooks progressively build a healthcare assistant that can:

- Search simulated web content for general health information
- Search simulated PubMed content for medical research
- Recommend doctors based on symptoms or specialties
- List doctors and available appointment slots
- Book appointments after collecting patient details
- Maintain independent memory for multiple users

The tools use local JSON data and ChromaDB-backed retrieval to simulate production-style tool use without depending on live external search APIs.

## Notebook Details

### 01: Tools and Tool Calling

You define focused tools, register them with an LLM, inspect tool call requests, and manually execute tool responses. The homework asks you to add a simple healthcare tool such as a BMI calculator, medication lookup, or symptom checker.

### 02: Built-in ReAct Agent

You use LangGraph's `create_react_agent()` to connect HealthBuddy tools into a ReAct loop. The agent reasons about a query, selects a tool, observes tool output, and continues until it can answer.

### 03: ReAct from Scratch

You rebuild the same workflow with `StateGraph`, a `TypedDict` state schema, explicit nodes, conditional edges, `ToolNode`, and routing logic. This makes the agent loop easier to customize and debug.

### 04: Multi-User Conversational Agent

You add conversation memory with user-specific session IDs, appointment availability tools, booking state, and multi-turn interaction tests. The homework extends HealthBuddy with an insurance eligibility checker tool.

### 05: Multi-Agent SOP Assistant

The final notebook shifts to an enterprise SOP assistant. A supervisor routes work across specialized agents:

- `intent_classifier_agent` classifies HR, Finance, or IT queries.
- `sop_retriever_agent` fetches the relevant SOP entry.
- `answer_generator_agent` turns policy text into a clear response.
- The supervisor manages the workflow until the task is complete.

## Data and Assets

- `Data/search_data.json` - simulated web and PubMed-like health content.
- `Data/sop_documents.json` - HR, Finance, and IT SOP entries for the multi-agent assistant.
- `Data/tool_calling.png`, `Data/tool_use_agent.png`, `Data/conversational_agent.png`, and `Data/multi_agent.png` - notebook diagrams.
- `Data/*_arch.png` - architecture diagrams used in the notebooks.

## Running the Notebooks

1. Activate your virtual environment from the repository root.
2. Configure `.env` with `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME`.
3. Run [`.setup/learner_setup.ipynb`](.setup/learner_setup.ipynb).
4. Run the notebooks in order.

For a manual install from the repository root:

```bash
uv pip install -r Module4/module4/2/shim.txt -c Module4/module4/2/constraints.txt
```

Key packages include `langchain`, `langchain-community`, `langchain-openai`, `langchain-chroma`, `langgraph`, `chromadb`, `tenacity`, and `mlflow`.

## Gateway and Tracing

Module 4 notebooks read `OPENAI_API_KEY`, `OPENAI_BASE_URL`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` from `.env`. Set `OPENAI_BASE_URL` to a LiteLLM gateway URL when routing calls through LiteLLM.

Start MLflow from the repository root if you want traces. Module 4 notebooks create experiments under `llm-rag-agents-gateway-labs/Module4/...`.

## Learning Outcomes

By the end of Module 4, you should be able to:

- Design tools with clear schemas and responsibilities
- Understand LLM tool-call requests and tool responses
- Build ReAct agents with LangGraph
- Implement custom graph-based agent loops
- Add multi-turn and multi-user memory
- Coordinate multiple task-specific agents with a supervisor

## Next Step

You are ready for the capstone: the [Healthcare Insurance Claim Approval Agent](../Project/README.md), which brings prompts, retrieval, tools, agents, metrics, and a comparison with human decisions together in one workflow.
