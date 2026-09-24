# Sample Project Part 2: Measuring Agent Performance Against Humans

Subtitle: The real question is not whether the agent sounds smart. It is whether it actually performs.

Tags: AI Evaluation, MLflow, Insurance Tech, Agentic AI, Metrics, LiteLLM

GitHub repo: [agentic-rag-with-ai-gateway-tracing-labs](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/)

![Agent vs human evaluation flow](https://raw.githubusercontent.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/main/blogs/assets/project-claim-approver-flow.png)

Image: Measuring the claim approval agent against human reference decisions is what lifts this project beyond a chatbot demo.

In Part 1, we designed the workflow: three tools, a mandatory sequence, and structured outputs. Now comes the part where the notebook stops being a neat demo and has to prove itself: evaluation.

An agent can write a lovely explanation and still be wrong. In business workflows, especially in insurance and healthcare, that is simply not good enough when real decisions depend on it.

So the project compares the agent's outputs on validation records with human reference decisions and summary metrics. This is the part that turns a neat notebook into something you can genuinely discuss with a team.

## Why Human Comparison Matters

Human comparison gives the agent something honest to stand next to.

The question is not "is the agent perfect?" It is:

- How close is the agent to human reference decisions?
- Where does it agree?
- Where does it disagree?
- Are the mistakes acceptable for an assistant workflow?
- Which cases need human review?

That conversation is far healthier than simply announcing "AI can approve claims."

## Outputs To Inspect

When you run the validation and comparison cells, the notebook can generate:

- agent_validation_records_results.csv
- human_vs_agent_comparison.csv
- comparison_summary_stats.csv
- submission.csv

The first three help you analyze development performance. The final 'submission.csv' is produced from 'Data/test_records.json' and contains the final test predictions.

## Metrics Used In The Project

The project focuses on practical performance metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Agreement rates
- Summary statistics

Each metric tells you something different about performance.

Accuracy gives you the overall correct rate. Precision and recall help when false positives and false negatives carry different costs. F1-score balances the two.

In insurance, mistakes rarely cost the same. Wrongly approving a claim and wrongly routing one for review can have very different business consequences.

## Looking Beyond A Single Score

One score is never the full story.

Even if the agent hits 90 percent accuracy, the real learning often lives in the other 10 percent. Ask:

- Are errors concentrated in one policy type?
- Are certain diagnosis or procedure codes confusing?
- Does the agent fail when data is missing?
- Are explanations correct even when verdicts are wrong?
- Does the workflow need a better tool, better policy summary, or better prompt?

This is the moment evaluation starts to feel like product work.

## Agent As Assistant, Not Final Authority

For many real workflows, the first useful version of an AI system is not full automation.

It is usually assistance for the people already doing the work.

The agent can:

- Pre-check records
- Highlight likely issues
- Draft explanations
- Route uncertain cases to humans
- Reduce repetitive manual work
- Make review queues easier to prioritize

This is especially realistic in regulated or high-stakes domains. You get real value without pretending the system should make every final decision on its own.

## MLflow And Iteration

With MLflow tracing, you can compare project runs as you keep improving the workflow.

You might change:

- Prompt wording
- Tool descriptions
- Policy guideline summaries
- Decision formatting
- Error handling
- Review routing logic

Every change has to earn its place. If the metrics improve and the error examples look better, keep it. If not, you still learn something.

## What This Project Teaches

The capstone pulls the whole series together:

- Module 1 gave you LLM fundamentals
- Module 2 gave you prompts and basic workflows
- Module 3 gave you retrieval and evaluation thinking
- Module 4 gave you tools and agents
- The project adds business metrics and human comparison

This is the path from "I built an AI demo" to "I can evaluate an AI workflow." And that second sentence is the one that gets taken seriously in a review meeting.

## Final Thought

For Indian tech builders, this is where practical AI work is heading.

Companies do not just need chatbots. They need systems that can read, reason, validate, explain, and improve over time.

Healthcare insurance claim approval is one example, but the same pattern applies to banking, healthcare operations, education, logistics, legal operations, customer support, and plenty of internal enterprise workflows.

Build the workflow. Trace it. Measure it. Improve it.

That is the real AI engineering playbook, and it is far more useful than pretending every agent should be autonomous from day one. Thank you for walking this path with me. If you want to revisit any stop along the way, the series index has every post in order.

## Feedback

If you compare the agent with your own reference labels, please do not share only the final score. Share one failure case that taught you something. That is where evaluation becomes genuinely valuable.

## Series Navigation

- Previous: [Sample Project Part 1](https://chanderkant-sharma.medium.com/sample-project-part-1-designing-the-healthcare-claim-approval-workflow-1b6dbf3a5cc4)
- Next: [Back to the series index](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399)
- Series index: [All posts](https://chanderkant-sharma.medium.com/rag-and-agentic-ai-labs-with-litellm-ai-gateway-mlflow-tracing-b2c33dd7d399)
- Lab notebooks: [Project README](https://github.com/chanderkant7/agentic-rag-with-ai-gateway-tracing-labs/blob/main/Project/README.md)
