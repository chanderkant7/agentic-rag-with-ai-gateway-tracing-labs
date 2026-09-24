# Sample Project Part 1: Designing the Healthcare Claim Approval Workflow

Subtitle: Good agent projects start with workflow design, not one heroic prompt.

Tags: AI Workflow, Agentic AI, Insurance Tech, LangGraph, LangChain, LiteLLM, MLflow

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

Quick setup note: The notebooks use OpenAI-compatible clients. If you run LiteLLM, point `OPENAI_BASE_URL` at the gateway, set `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`, and keep `LITELLM_MASTER_KEY` aligned with your gateway config. The details are in [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Healthcare claim approval workflow](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/project-claim-approver-flow.png)

Image: The workflow moves from patient records and policy inputs, through tool-backed claim evaluation, to a final decision.

The Sample Project Intro set the goal: a claim approval agent whose decisions can be traced and measured. This post is about designing it, and it comes with a gentle reminder: agentic AI is still software engineering.

The model matters. The workflow matters more.

If you simply paste a claim record into an LLM and ask "should this be approved?", you may well get a confident answer. What you will not necessarily get is a reliable system.

So the project takes a more structured approach, because reliability usually comes from the shape of the workflow, not from one heroic prompt at the end.

## The Core Workflow

Here is the workflow, step by step:

```text
Load insurance policies
Load ICD-10 and CPT reference codes
Load validation or test patient records
Summarize the patient record
Summarize the relevant policy guideline
Evaluate coverage criteria
Return APPROVE or ROUTE FOR REVIEW
Store the result
Compare with human reference decisions
```

Every step has one job. That alone makes the system far easier to debug.

When the final answer is wrong, you can ask:

- Did the record load correctly?
- Was the patient's age at service calculated correctly?
- Did the diagnosis or procedure code map correctly?
- Did the policy summary include the relevant restriction?
- Did the agent apply preauthorization rules properly?
- Was the final decision format consistent?

That beats staring at one giant prompt and wondering which part of it drifted.

## Patient Record Summarization

The first tool pulls the useful claim information out of the patient record.

In real insurance systems, this gets complex quickly. Records can include demographics, dates of service, diagnoses, procedure codes, policy IDs, preauthorization status, and billed amounts.

For the project, `summarize_patient_record` keeps the workflow organized. It separates raw record handling from final agent reasoning.

That separation matters. If parsing goes wrong, the agent can reason perfectly over bad input and still reach the wrong verdict.

## Notebook Snippet: `Project/code.ipynb`

The project begins with tool-style functions that bring structure to raw claim data:

```python
@tool
def summarize_patient_record(record_str: str) -> str:
    """
    Extract and structure patient insurance claim information into
    analysis-ready format.
    """
```

The full tool sequence is then registered with the agent, along with instructions that make the order mandatory:

```python
tools = [
    summarize_patient_record,
    summarize_policy_guideline,
    check_claim_coverage,
]

system_message = """
You are an expert insurance claims analyst agent.

MANDATORY WORKFLOW:
1. FIRST: Use summarize_patient_record tool with the patient record data
2. SECOND: Use summarize_policy_guideline tool with the policy ID
3. THIRD: Use check_claim_coverage tool with results from tools 1 and 2
"""
```

## Policy Guideline Summarization

The second tool interprets the policy rules that apply to the claim.

This is where the project uses the same discipline you learned in the RAG and tool-calling modules: the agent should never guess a rule. It should work from the policy data it has.

A good policy summary captures:

- Covered procedures
- Required diagnoses
- Age restrictions
- Gender restrictions
- Preauthorization requirements
- Any rule that affects approval

In real systems, this layer might connect to policy documents, product configuration tables, regulatory rules, or internal review manuals. The notebook keeps it JSON-based so the workflow stays easy to read.

## Coverage Evaluation

The third tool is where the reasoning happens.

`check_claim_coverage` compares the patient summary against the policy summary and returns a decision.

A good claim approval agent should:

- Stay grounded in provided data
- Use all required tools
- Avoid inventing missing rules
- Return one of the expected decisions
- Explain the reason clearly
- Route uncertain cases to review

This is where the Module 4 agent patterns really pay off. The LLM is not "the whole system." It is the reasoning component inside a tool-backed workflow.

## Notebook Snippet: Agent Execution Wrapper

`Project/code.ipynb` wraps the agent call so every record can be processed and exported:

```python
def call_claim_approval_agent(
    agent,
    query,
    verbose=False,
    patient_id=None,
    submission_file_name=None,
):
    events = agent.stream(
        {"messages": [{"role": "user", "content": query}]},
        stream_mode="values",
    )

    for event in events:
        if verbose:
            event["messages"][-1].pretty_print()

    final_response = event["messages"][-1].content
    return final_response
```

## Why Structured Outputs Matter

The project writes its results to CSV files so they can be compared.

That means the output must be consistent enough to evaluate. If one run says `APPROVE`, another says "approved", and another says "looks fine", metrics become messy.

For business workflows, structure is your best friend.

Use labels, IDs, decision text, and explanations consistently, just as we practised back in Module 2.1. That is what makes downstream analysis possible.

## MLflow For Workflow Visibility

The project notebook includes the same initial setup cell for MLflow tracing that you have used throughout the series.

Start MLflow before running it:

```bash
mlflow server \
  --host 127.0.0.1 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns
```

Then inspect the project experiment at `http://127.0.0.1:5000`.

For a multi-step claim approval workflow, traces are invaluable, because they show you everything that happened before the final CSV output.

## The Takeaway

Part 1 of the project is all about design discipline.

Do not ask the model to be the whole system. Give it a workflow, tools, data, structure, and evaluation.

That is how agentic AI becomes more than a demo: smaller responsibilities, clearer evidence, and outputs you can compare. In Part 2, we do exactly that, measuring the agent against human decisions.

## Feedback

If you adapt this workflow to another domain, tell me which step changed first: record parsing, policy lookup, coverage evaluation, or comparison. That is usually where the real business logic lives.

## Series Navigation

- Previous: [Sample Project Intro](https://chanderkant-sharma.medium.com/sample-project-intro-building-a-healthcare-insurance-claim-approval-agent-a1e3915b712a)
- Next: [Sample Project Part 2: Measuring Agent Performance Against Humans](https://chanderkant-sharma.medium.com/sample-project-part-2-measuring-agent-performance-against-humans-2f4c03798b72)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399)
- Lab notebooks: [Project README](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/Project/README.md)
