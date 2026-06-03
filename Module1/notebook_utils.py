from __future__ import annotations

import os
import signal
from pathlib import Path
from typing import Any


def repo_root(start: str | os.PathLike[str] | None = None) -> Path:
    """Return the repository root from a notebook or script working directory."""
    current = Path(start or os.getcwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists() or (candidate / "Module1" / "notebook_utils.py").exists():
            return candidate
    return current


def repo_path(*parts: str) -> str:
    """Build an absolute path inside this repository."""
    return str(repo_root().joinpath(*parts))


def _run_with_timeout(fn: Any, timeout_seconds: int) -> Any:
    if not hasattr(signal, "SIGALRM"):
        return fn()

    previous_handler = signal.getsignal(signal.SIGALRM)

    def timeout_handler(signum: int, frame: Any) -> None:
        raise TimeoutError("MLflow experiment selection timed out")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)
    try:
        return fn()
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous_handler)


def setup_mlflow_tracing(
    experiment_name: str,
    tracking_uri: str | None = None,
    timeout_seconds: int = 5,
) -> None:
    """Configure localhost MLflow tracing and optional autolog integrations."""
    import mlflow

    tracking_uri = tracking_uri or os.getenv("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000")
    os.environ["MLFLOW_TRACKING_URI"] = tracking_uri
    os.environ["MLFLOW_EXPERIMENT_NAME"] = experiment_name

    mlflow.set_tracking_uri(tracking_uri)

    try:
        _run_with_timeout(lambda: mlflow.set_experiment(experiment_name), timeout_seconds)
    except Exception as exc:
        print(f"MLflow experiment selection skipped: {exc}")

    try:
        import mlflow.openai

        mlflow.openai.autolog()
    except Exception as exc:
        print(f"MLflow OpenAI autolog setup skipped: {exc}")

    try:
        import mlflow.langchain

        mlflow.langchain.autolog()
    except Exception as exc:
        print(f"MLflow LangChain autolog setup skipped: {exc}")

    print(f"MLflow tracing enabled: {tracking_uri} -> {experiment_name}")
