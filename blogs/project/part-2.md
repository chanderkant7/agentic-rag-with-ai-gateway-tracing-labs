# Sample Project Part 2: Measuring Agent Performance Against Humans

Subtitle: The real question is not whether the agent sounds smart. It is whether it performs.

Tags: AI Evaluation, MLflow, Insurance Tech, Agentic AI, Metrics, LiteLLM

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

AI Gateway note: These labs can route OpenAI-compatible calls through LiteLLM. Set `USE_LITELLM=1`, `OPENAI_BASE_URL`, `LITELLM_MASTER_KEY`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` in `.env`; see the [`.env.example`](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/.env.example).

![Insurance claim approver architecture diagram](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/project-claim-approver-arch.png)

Image: Measuring the agent against human validation makes the project more than a chatbot demo.

The final part of the sample project is where things become serious: evaluation.

An agent can produce a neat explanation and still be wrong. In business workflows, especially insurance and compliance-style use cases, that is not good enough.

So the sample project compares agent validation results with human validation and summary metrics. This is the part that turns a neat notebook into something you can actually discuss with a team.

## Why Human Comparison Matters

Human comparison gives the agent a practical benchmark.

The question is not "is the agent perfect?" It is:

- How close is the agent to human validation?
- Where does it agree?
- Where does it disagree?
- Are the mistakes acceptable for an assistant workflow?
- Which cases need human review?

This is a much more useful conversation than simply saying "AI can validate policies."

## Notebook Snippet: `Project/code.ipynb`

The evaluation section loads both human reference responses and agent-generated results:

```python
reference_df = pd.read_csv("Data/validation_reference_results.csv")
agent_submission_results_df = pd.read_csv("agent_validation_records_results.csv")

print(f"Loaded {len(reference_df)} human reference responses")
print(f"Loaded {len(agent_submission_results_df)} agent responses")
```

It also normalizes human decision text into categories:

```python
def improved_extract_decision_from_human_response(response_text):
    response_lower = response_text.lower()

    if "has been approved" in response_lower:
        return "approved"
    elif "manual review" in response_lower or "needs to be routed" in response_lower:
        return "review"
    elif "denied" in response_lower or "not covered" in response_lower:
        return "denied"
    else:
        return "review"
```

## Metrics Used In The Sample Project

The sample project focuses on common performance metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Agreement rates
- Summary statistics

These metrics help you understand different types of performance.

Accuracy gives the overall correct rate. Precision and recall help when false positives and false negatives have different costs. F1-score gives a balance between them.

In insurance, the cost of mistakes may not be equal. Incorrectly approving something and incorrectly rejecting something can have very different business consequences.

## Notebook Snippet: Case-by-case Inspection

The notebook includes manual inspection so metrics do not hide bad failure modes:

```python
for i, row in reference_df.head(3).iterrows():
    print(f"Patient {row['patient_id']}:")
    print(f"Response: {row['reference_response'][:150]}...")
    print(f"Parsed decision: {row['human_decision']}")
```

This is a simple but important habit: look at examples, not only aggregate scores. A metric tells you that something happened; examples tell you what kind of thing happened.

## Looking Beyond A Single Score

One score is never the full story.

If the agent has 90 percent accuracy, you still need to inspect the 10 percent failures.

Ask:

- Are errors concentrated in one policy type?
- Are certain reference codes confusing?
- Does the agent fail when data is missing?
- Are explanations correct even when verdicts are wrong?
- Does the agent need a better tool or better prompt?

This is where evaluation becomes product learning.

## Agent As Assistant, Not Final Authority

For many real workflows, the first useful version of an AI system is not full automation.

It is human assistance.

The agent can:

- Pre-check records
- Highlight likely issues
- Suggest validation codes
- Draft explanations
- Route uncertain cases to humans
- Reduce repetitive manual work

This is especially realistic for regulated or high-stakes domains. You get value without pretending the system should make every final decision.

## MLflow And Iteration

With MLflow tracing, you can compare sample project runs as you improve the workflow.

You might change:

- Prompt wording
- Tool descriptions
- Reference code lookup
- Output format
- Validation thresholds
- Error handling

Each change should be evaluated. If metrics improve, you keep it. If not, you learn.

That is the engineering loop:

```text
Change -> run -> trace -> measure -> inspect errors -> improve
```

## What This Sample Project Teaches

The capstone sample project pulls the full series together:

- Module 1 gave you LLM fundamentals
- Module 2 gave you prompts and basic workflows
- Module 3 gave you retrieval and evaluation thinking
- Module 4 gave you tools and agents
- The sample project adds business metrics and human comparison

This is the path from "I built an AI demo" to "I can evaluate an AI workflow."

## Final Thought

For India tech builders, this is the practical direction AI work is moving.

Companies do not only need chatbots. They need systems that can read, reason, validate, explain, and improve over time.

The insurance validation sample project is one example, but the same pattern can apply to banking, healthcare, education, logistics, legal operations, customer support, and internal enterprise workflows.

Build the workflow. Trace it. Measure it. Improve it.

That is the real AI engineering playbook, and it is much more useful than pretending every agent should be autonomous from day one.

## Feedback

If you compare the agent with your own reference labels, do not only share the final score. Share one failure case that taught you something. That is where evaluation becomes genuinely valuable.

## Series Navigation

- Previous: [Sample Project Part 1](https://chanderkant-sharma.medium.com/sample-project-part-1-designing-the-insurance-validation-workflow)
- Next: [Series index](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-main-intro)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-main-intro)
