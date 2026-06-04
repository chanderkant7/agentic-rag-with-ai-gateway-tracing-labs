# Module 2: LLM Workflow Basics

Module 2 introduces practical OpenAI-compatible LLM workflows before the deeper RAG and agent labs. The notebooks cover client setup, prompt design, sentiment analysis on patient/caregiver text, and clinical dialogue summarization.

## Lab Sequence

| Order | Notebook | What you build |
| --- | --- | --- |
| 1 | [01_OpenAI_Connection.ipynb](01_OpenAI_Connection.ipynb) | A configured OpenAI-compatible chat and embedding client using `.env` values and MLflow tracing. |
| 2 | [02_Prompt_Ebginnering.ipynb](02_Prompt_Ebginnering.ipynb) | Prompt patterns including zero-shot, few-shot, chain-of-thought, tree-of-thought, and stateful communication. |
| 3 | [03_Seniment_Analysis.ipynb](03_Seniment_Analysis.ipynb) | A structured sentiment workflow for patient and caregiver posts, classifying negative, neutral, and positive emotion signals. |
| 4 | [04_Text_Summarization.ipynb](04_Text_Summarization.ipynb) | A clinical conversation summarizer that turns doctor-patient dialogue into concise, structured notes. |

The second and third notebook filenames contain historical spelling mistakes in the repository. Use the filenames shown above.

## Notebook Details

### OpenAI Connection

The first notebook verifies environment loading, OpenAI-compatible client construction, model selection, response inspection, retries, and basic chat/embedding calls.

### Prompt Engineering

This notebook demonstrates how prompt structure affects model behavior:

- Zero-shot instructions for direct classification or routing
- Few-shot examples for domain-specific decisions
- Chain-of-thought style decomposition for reasoning tasks
- Tree-of-thought style exploration for multiple candidate paths
- Stateful communication patterns for multi-turn interactions

### Sentiment Analysis

The sentiment notebook uses `Data/SentimentAnalysis/Patient_Reviews.csv`, which contains patient and caregiver text from healthcare communities. The task is to classify each post or review as negative, neutral, or positive and extract more specific emotional signals such as grief, relief, joy, or concern.

### Text Summarization

The summarization notebook uses doctor-patient conversation files from `Data/TextSummarization/`. It starts with a basic summary prompt, then refines the prompt into a structured clinical note that captures symptoms, diagnosis, treatment details, and follow-up context.

## Data

- `Data/SentimentAnalysis/Patient_Reviews.csv` - patient and caregiver review text for sentiment classification.
- `Data/TextSummarization/conversation_*.txt` - clinical dialogue samples for summarization.

## Running the Notebooks

1. Activate your virtual environment from the repository root.
2. Copy `.env.example` to `.env` and set `OPENAI_API_KEY`, `CHAT_MODEL_NAME`, and any gateway values.
3. Run [`.setup/learner_setup.ipynb`](.setup/learner_setup.ipynb).
4. Open the notebooks in the order listed above.

For a manual install from the repository root:

```bash
uv pip install -r Module2/module2/2/shim.txt -c Module2/module2/2/constraints.txt
```

Key packages include `openai`, `httpx`, `pandas`, `pydantic`, `python-dotenv`, `tenacity`, and `mlflow`.

## Gateway and Tracing

The notebooks read these values from `.env`:

- `OPENAI_API_KEY`
- `OPENAI_BASE_URL`
- `CHAT_MODEL_NAME`
- `EMBEDDING_MODEL_NAME`

Set `OPENAI_BASE_URL` to a LiteLLM gateway URL when routing through the gateway. Start MLflow from the repository root if you want traces; each notebook creates a separate experiment under `llm-rag-agents-gateway-labs/Module2/...`.

## Learning Outcomes

By the end of Module 2, you should be able to:

- Configure OpenAI-compatible chat and embedding clients
- Design prompts for classification, reasoning, and summarization
- Use structured outputs for downstream processing
- Evaluate whether prompt changes improve task quality
- Prepare for retrieval workflows in Module 3
