# Module 4: Agentic AI

## Overview

This module covers building intelligent agents that can reason, plan, and use tools to solve complex problems. Learn ReAct agents, multi-agent systems, and conversational AI with tool use. The notebooks now use current LangChain package imports, repository-relative paths, and localhost MLflow tracing.

## Module Contents

### 1. **1_ImplementingToolsForAgenticAI.ipynb**
- Understanding tool/function definitions
- Tool schema and signatures
- Tool validation and error handling
- Integrating custom tools with LLMs

### 2. **2_BuildingToolsReactAgenticAIBuiltin.ipynb**
- ReAct (Reasoning + Acting) pattern
- Using built-in LangChain tools
- Tool selection strategies
- Observation and refinement loops

### 3. **03_BuildingToolsReactAgenticAIScratch.ipynb**
- Building custom tools from scratch
- Tool composition and chaining
- Creating domain-specific toolsets
- Advanced tool orchestration

### 4. **04_BuildingMultiUserConversationalAgenticAI.ipynb**
- Multi-user conversation management
- Session and context handling
- User-specific tool access controls
- Conversation persistence

### 5. **05_BuildingMultiAgentSystem.ipynb**
- Multi-agent coordination
- Agent specialization and roles
- Inter-agent communication
- Consensus and conflict resolution

## Core Concepts

### ReAct Framework
```
Thought → Action → Observation → Thought → ... → Final Answer
```

### Agent Loop
1. **Input**: User query or task
2. **Thought**: Agent reasons about the problem
3. **Action**: Agent selects and executes tools
4. **Observation**: Agent processes tool output
5. **Repeat** until task is complete
6. **Output**: Final response

## Key Technologies

- **LangChain and LangGraph**: Agent framework, graph orchestration, and execution
- **OpenAI or Azure OpenAI**: LLM access
- **Tool Definitions**: Structured tool specifications
- **Memory Systems**: Conversation and context management

## Learning Objectives

- Understand agent reasoning and planning
- Design and implement effective tools
- Build ReAct agents for complex tasks
- Create multi-agent systems
- Handle multi-user scenarios
- Debug and optimize agent behavior

## Running the Notebooks

1. Activate your virtual environment from the repository root.
2. Run the Module 4 setup notebook once:
```bash
jupyter notebook Module4/.setup/learner_setup.ipynb
```
3. Configure API keys in `.env`.
4. Follow notebooks sequentially.

The setup notebook installs:

```bash
uv pip install -r Module4/module4/2/requirements.txt -c Module4/module4/2/constraints.txt
```

Current key package pins include `langchain==1.3.4`, `langchain-community==0.4.2`, `langchain-openai==1.2.2`, `langchain-text-splitters==1.1.2`, `chromadb==1.5.9`, `langgraph==1.2.4`, `tenacity==9.1.4`, and `mlflow==3.13.0`.

## LiteLLM AI Gateway

Module 4 agent notebooks can route chat model calls through LiteLLM using the OpenAI-compatible `OPENAI_BASE_URL`. Set `USE_LITELLM=1`, `LITELLM_MASTER_KEY`, and `CHAT_MODEL_NAME` in `.env` when running through the gateway. Embedding-backed examples can also use `EMBEDDING_MODEL_NAME`.

## MLflow and Paths

Each lab notebook has an `Initial setup` cell that enables tracing through `Module1/notebook_utils.py` via `setup_mlflow_tracing(...)`. Data and cache paths use `repo_path(...)`.

Start MLflow from the repository root before running notebooks if you want traces captured:

```bash
mlflow server \
  --host 127.0.0.1 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns
```

Open the MLflow UI at `http://127.0.0.1:5000`. Module 4 notebooks create separate experiments under names like `llm-rag-agents-gateway-labs/Module4/<notebook-name>`.

If the server is not running, the setup helper skips experiment selection and the notebook continues. You can also override the tracking URI by setting `MLFLOW_TRACKING_URI` before running a notebook.

## Data

`Data/search_data.json` - Sample data for search operations
`Data/sop_documents.json` - Standard Operating Procedures for agent reference

## Agent Design Patterns

- **ReAct**: Reasoning + Action
- **Tool-Use**: Function calling with structured outputs
- **Chain of Thought**: Explicit reasoning steps
- **Self-Reflection**: Agent evaluation and correction
- **Hierarchical**: Master agent coordinating sub-agents

## Best Practices

- Design tools with clear, focused purposes
- Provide detailed tool descriptions
- Handle edge cases and errors gracefully
- Log agent decisions for debugging
- Test with diverse inputs
- Monitor cost and latency

## Next Steps

Apply these concepts in the **Project: Insurance Agent Validation** to build a production system that validates insurance policies using an intelligent agent.
