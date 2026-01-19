import pandas as pd
from .metrics import mse, mae, qlike


def evaluate_and_compare_models(
    rolling_results: pd.DataFrame,
    regime_results: pd.DataFrame,
    metrics: list,
    output_path: str,
):
    """Aggregate forecast results and compute loss metrics (stub)."""
    # Expect rolling_results/regime_results to contain columns:
    # ['model', 'target', 'forecast', 'timestamp', ...]
    records = []

    # Placeholder aggregation logic.
    eval_df = pd.DataFrame(records)
    eval_df.to_csv(output_path, index=False)
    return eval_df
