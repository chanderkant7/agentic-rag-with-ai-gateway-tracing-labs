# Project: Healthcare Insurance Claim Approval Agent

This capstone notebook builds an agentic healthcare insurance claim approval system. The agent interprets patient records, retrieves and summarizes policy guidelines, checks coverage criteria, compares its decisions with human reference results, and generates a final submission file.

## Project Objective

Build a transparent claim approval assistant that can:

- Interpret semi-structured patient health records and submitted claims
- Translate ICD-10 and CPT codes into human-readable clinical context
- Reason over policy guidelines and coverage restrictions
- Decide whether a claim should be `APPROVE` or `ROUTE FOR REVIEW`
- Explain each decision with evidence from the patient record and policy
- Benchmark agent decisions against human validation results

## Main Notebook

- [code.ipynb](code.ipynb) - complete implementation, validation, comparison, and final test processing workflow.

## Architecture

The notebook implements a single ReAct-style agent with three required tools:

| Tool | Purpose |
| --- | --- |
| `summarize_patient_record(record_str)` | Extract demographics, patient age at service, diagnoses, procedures, policy ID, preauthorization status, and billed amount. |
| `summarize_policy_guideline(policy_id)` | Interpret the relevant insurance policy, including covered procedures, required diagnoses, age/gender restrictions, and preauthorization rules. |
| `check_claim_coverage(record_summary, policy_summary)` | Compare the patient summary against policy rules and produce an approval or manual-review decision with reasoning. |

The agent is instructed to use the tools in sequence: patient analysis, policy analysis, then final coverage evaluation.

## Workflow

```text
Patient claim record
  -> Patient record summarization
  -> Policy guideline summarization
  -> Coverage evaluation
  -> APPROVE or ROUTE FOR REVIEW
  -> Human-vs-agent comparison
  -> Final submission export
```

## Data Files

All source data lives under [Data](Data):

- `insurance_policies.json` - insurance policy documents and coverage rules.
- `reference_codes.json` - ICD-10 diagnosis codes and CPT procedure codes.
- `validation_records.json` - development records for validation and refinement.
- `validation_reference_results.csv` - human reference decisions for validation comparison.
- `test_records.json` - final records used to generate `submission.csv`.
- `claim_approver_agent_arch.png` - architecture diagram used by the notebook.
- `claim_approver_agent_flow.png` - workflow diagram used by the notebook.

## Generated Outputs

The notebook writes these files when the relevant cells are run:

- `agent_validation_records_results.csv` - agent outputs on validation records.
- `human_vs_agent_comparison.csv` - detailed human-vs-agent comparison.
- `comparison_summary_stats.csv` - summary metrics from the comparison.
- `submission.csv` - final predictions for the test records with `patient_id` and `generated_response`.

These outputs are generated artifacts and may not exist until you run the notebook.

## Evaluation

The validation section compares agent decisions against human reference results and supports:

- Case-by-case agreement review
- False positive and false negative analysis
- Approval vs review distribution checks
- Summary statistics for decision quality
- Manual inspection of disagreement patterns

The goal is not just to produce a label, but to produce an auditable decision path that explains why the claim was approved or routed for review.

## Running the Project

1. Complete Modules 1-4 or be comfortable with RAG, tool calling, and LangGraph ReAct agents.
2. Activate your virtual environment from the repository root.
3. Configure `.env` with `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and any gateway values.
4. Run [`.setup/learner_setup.ipynb`](.setup/learner_setup.ipynb).
5. Open [code.ipynb](code.ipynb) and run the workflow from top to bottom.

For a manual install from the repository root:

```bash
uv pip install -r Project/project/2/shim.txt -c Project/project/2/constraints.txt
```

Key packages include `openai`, `pandas`, `langchain`, `langchain-openai`, `langgraph`, `chromadb`, `rank-bm25`, and `mlflow`.

## Gateway and Tracing

The project reads `OPENAI_API_KEY`, `OPENAI_BASE_URL`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME` from `.env`. Set `OPENAI_BASE_URL` to a LiteLLM gateway URL when routing calls through LiteLLM.

Start MLflow from the repository root if you want traces. The project creates an experiment under `llm-rag-agents-gateway-labs/Project/code`.

## Extension Ideas

- Add more policy edge cases and disagreement categories.
- Introduce retrieval over longer policy documents instead of direct JSON lookup.
- Add confidence calibration and threshold-based manual review.
- Turn the notebook workflow into a service with audit logging.
- Add monitoring for cost, latency, and decision drift.
