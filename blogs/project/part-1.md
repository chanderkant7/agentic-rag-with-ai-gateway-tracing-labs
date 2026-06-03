# Sample Project Part 1: Designing the Insurance Validation Workflow

Subtitle: Good agent projects start with workflow design, not with asking the model to do everything.

Tags: AI Workflow, Agentic AI, Insurance Tech, LangGraph, LangChain, LiteLLM, MLflow

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

AI Gateway note: These labs can route OpenAI-compatible calls through LiteLLM. Set `USE_LITELLM=1`, `OPENAI_BASE_URL`, `LITELLM_MASTER_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`; see the [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Insurance claim validation workflow diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/project-claim-approver-flow.png)

Image: The project workflow moves from record and policy inputs to tool-backed validation and a final decision.

The insurance validation sample project is a useful reminder that agentic AI is still software engineering.

The model is important, but the workflow matters more.

If you simply paste a record into an LLM and ask "is this valid?", you may get a confident answer. But you will not necessarily get a reliable system.

The sample project takes a more structured approach, because reliability usually comes from the shape of the workflow, not from one heroic prompt.

## The Core Workflow

The workflow looks like this:

```text
Load insurance data
Load reference codes
Inspect validation record
Use tools or lookup logic
Generate agent verdict
Store result
Compare with expected or human result
Calculate metrics
```

Each step has a job. This makes the system easier to debug.

If the final answer is wrong, you can ask:

- Did the record load correctly?
- Was the right reference code available?
- Did the agent use the correct rule?
- Was the verdict format correct?
- Did comparison logic work?

That is much better than staring at one giant prompt and wondering which part of it betrayed you.

## Policy Parser

The policy parser extracts useful information from the insurance data.

In real insurance systems, this can become complex quickly. Policies may contain multiple coverage sections, exclusions, dates, riders, claim conditions, and codes.

For the sample project, the parser keeps the workflow organized. It helps separate raw data handling from agent reasoning.

This separation is important. If parsing is wrong, the agent may reason correctly over bad input and still produce a wrong verdict.

## Notebook Snippet: `Project/code.ipynb`

The sample project starts with tool-style functions that structure raw claim data:

```python
@tool
def summarize_patient_record(record_str: str) -> str:
    """
    Extract and structure patient insurance claim information into
    analysis-ready format.
    """
    # Transforms raw patient records into demographics, policy ID,
    # diagnoses, procedure codes, and preauthorization context.
```

It then registers the complete tool sequence:

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

## Reference Code Engine

The reference code engine provides the rules or codes the validation depends on.

This is where retrieval and lookup thinking from Module 3 becomes useful. The agent should not guess a reference rule. It should use available data.

In real systems, this layer may connect to:

- Rule databases
- Policy documents
- Regulatory guidelines
- Internal SOPs
- Product configuration tables

The sample project keeps it notebook-friendly while preserving the concept.

## Validation Agent

The validation agent brings the reasoning step.

Its job is not just to answer. Its job is to use the available context and produce a verdict with explanation.

A good validation agent should:

- Stay grounded in provided data
- Use tools or lookups when needed
- Avoid inventing missing rules
- Return structured outputs
- Explain the reason for the verdict

This is where Module 4 tool and agent patterns matter.

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

The sample project writes results to CSV files for comparison.

That means the output must be consistent enough to evaluate. If one run says "valid", another says "Approved", and another says "Looks okay", metrics become messy.

For business workflows, structure is your friend.

Use labels, fields, IDs, confidence scores, and explanations consistently. That makes downstream analysis possible.

## MLflow For Workflow Visibility

The sample project notebook includes an `Initial setup` cell for MLflow tracing.

Start MLflow before running:

```bash
mlflow server \
  --host 127.0.0.1 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns
```

Then inspect the sample project experiment at `http://127.0.0.1:5000`.

For a multi-step validation workflow, traces are useful because they help you see what happened before the final CSV output.

## The Takeaway

Part 1 of the sample project is about design discipline.

Do not ask the model to be the whole system. Give it a workflow, tools, data, structure, and evaluation.

That is how agentic AI becomes more than a demo: smaller responsibilities, clearer evidence, and outputs you can compare.

## Feedback

If you adapt this workflow to another domain, tell me which step changed first: parsing, reference lookup, validation, or comparison. That is usually where the real business logic lives.

## Series Navigation

- Previous: [Sample Project Intro](https://chanderkant-sharma.medium.com/sample-project-intro-building-an-insurance-validation-agent)
- Next: [Sample Project Part 2](https://chanderkant-sharma.medium.com/sample-project-part-2-measuring-agent-performance-against-humans)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-main-intro)
