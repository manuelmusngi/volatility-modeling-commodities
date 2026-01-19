import pandas as pd


def run_rolling_forecasts(
    returns,
    models: dict,
    window_size: int,
    forecast_horizon: int,
    refit_frequency: int,
    evaluation_start: int,
):
    """Run rolling forecasts for all models (stub)."""
    results = []
    # Implement rolling window loop and store forecasts in `results`.
    return pd.DataFrame(results)
