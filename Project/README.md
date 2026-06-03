# Project: Insurance Agent Validation System

## Overview

An end-to-end implementation of an intelligent insurance validation agent that automatically validates insurance policies against reference codes and benchmarks performance against human validators. The project notebook now uses current LangChain/LangGraph dependencies, repository-relative paths, and localhost MLflow tracing.

## Project Objectives

- Build a multi-agent system for policy validation
- Compare agent performance with human validators
- Measure accuracy, precision, recall, and F1-score
- Generate comprehensive validation reports
- Demonstrate enterprise-grade agent architecture

## Key Files

### Main Implementation
- **code.ipynb** - Complete agent implementation and validation workflow

### Data Files
- `Data/insurance_policies.json` - Insurance policy documents to validate
- `Data/reference_codes.json` - Reference validation codes and rules
- `Data/test_records.json` - Test cases for validation
- `Data/validation_records.json` - Ground truth validation results

### Results & Analysis
- **agent_validation_records_results.csv** - Agent validation outputs
- **human_vs_agent_comparison.csv** - Performance comparison metrics
- **comparison_summary_stats.csv** - Statistical summary
- **submission.csv** - Final submission format
- **validation_reference_results.csv** - Expected results

## Architecture

### Components

1. **Policy Parser**
   - Extracts policy information
   - Validates document structure
   - Handles multiple policy formats

2. **Reference Code Engine**
   - Loads and indexes reference codes
   - Matches policies to codes
   - Applies validation rules

3. **Validation Agent**
   - Reasons about policy details
   - Uses tools for code lookup
   - Generates validation verdicts

4. **Performance Analyzer**
   - Compares agent vs human results
   - Calculates metrics
   - Generates reports

## Validation Metrics

### Performance Metrics
- **Accuracy**: Percentage of correct validations
- **Precision**: True positives / (TP + FP)
- **Recall**: True positives / (TP + FN)
- **F1-Score**: Harmonic mean of precision and recall

### Efficiency Metrics
- **Latency**: Average validation time per policy
- **Cost**: API calls and token usage
- **Throughput**: Policies processed per minute

## How to Run

1. **Setup Environment**
```bash
source .venv/bin/activate
jupyter notebook Project/.setup/learner_setup.ipynb
```

The setup notebook installs:

```bash
uv pip install -r Project/project/2/requirements.txt -c Project/project/2/constraints.txt
```

2. **Configure Credentials**
   - Add API keys to `.env` file
   - Ensure OpenAI or Azure OpenAI credentials are available for the notebook cells you run

3. **Run Validation**
```bash
jupyter notebook code.ipynb
```

4. **Analyze Results**
   - Review CSV files in project root
   - Compare agent vs human performance
   - Check validation_reference_results.csv

## Project Workflow

```
Insurance Policies
       ↓
   Policy Parser
       ↓
Reference Code Lookup
       ↓
Validation Agent (ReAct)
       ↓
Generate Verdict
       ↓
Compare with Human Results
       ↓
Generate Report
```

## Expected Outputs

1. **Validation Results**
   - Policy ID
   - Predicted validation code
   - Confidence score
   - Reasoning explanation

2. **Comparison Report**
   - Agent accuracy vs human accuracy
   - Agreement rates
   - Disagreement analysis
   - Performance statistics

3. **Submission File**
   - Formatted for evaluation
   - Contains all validation verdicts

## Key Technologies

- **LangChain and LangGraph**: Agent framework and graph orchestration
- **OpenAI or Azure OpenAI**: LLM access
- **Pandas**: Data analysis and CSV handling
- **ChromaDB and rank-bm25**: Retrieval support
- **MLflow**: Local tracing for model and chain calls
- **JSON**: Data storage and configuration

Current key package pins include `openai==2.40.0`, `httpx==0.28.1`, `pandas==2.3.3`, `chromadb==1.5.9`, `langchain==1.3.4`, `langchain-community==0.4.2`, `langchain-openai==1.2.2`, `langgraph==1.2.4`, and `mlflow==3.13.0`.

## LiteLLM AI Gateway

The sample project notebook reads gateway-aware settings from `.env`, including `OPENAI_BASE_URL`, `CHAT_MODEL_NAME`, and `EMBEDDING_MODEL_NAME`. Use `USE_LITELLM=1` and `LITELLM_MASTER_KEY` from the root `.env.example` when routing validation-agent calls through a LiteLLM AI Gateway.

## MLflow and Paths

The project notebook has an `Initial setup` cell that enables tracing through `Module1/notebook_utils.py` via `setup_mlflow_tracing(...)`. File paths use `repo_path(...)`, which avoids duplicated folder names when the notebook working directory changes.

Start MLflow from the repository root before running the project if you want traces captured:

```bash
mlflow server \
  --host 127.0.0.1 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns
```

Open the MLflow UI at `http://127.0.0.1:5000`. The project notebook creates an experiment named `llm-rag-agents-gateway-labs/Project/code`.

If the server is not running, the setup helper skips experiment selection and the notebook continues. You can also override the tracking URI by setting `MLFLOW_TRACKING_URI` before running the notebook.

## Challenges & Solutions

### Challenge: Policy Complexity
**Solution**: Multi-step reasoning with tool use to break down complex validations

### Challenge: Reference Code Matching
**Solution**: Vector similarity search combined with exact matching

### Challenge: Handling Edge Cases
**Solution**: Fallback strategies and error handling in agent loop

## Performance Targets

- **Accuracy**: >90% vs ground truth
- **Agent vs Human**: Within 5% of human performance
- **Latency**: <5 seconds per policy
- **Cost**: <$0.10 per policy validation

## Lessons Learned

- Agent design significantly impacts accuracy
- Tool definition quality is critical
- Multiple validation passes improve results
- Hybrid approaches (agent + rules) work best

## Deployment Considerations

- Scale to thousands of policies
- Real-time validation API
- Audit trail and explainability
- Continuous learning from human feedback
- Cost optimization strategies

## Next Steps

- Integrate with production systems
- Set up monitoring and alerting
- Implement feedback loops
- Scale to full policy database
