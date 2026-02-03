import os
import numpy as np
import pandas as pd


# ---------------------------------------------------------
# Time-series utilities
# ---------------------------------------------------------

def create_lags(series: pd.Series, lags: int = 5) -> pd.DataFrame:
    """Create lagged versions of a time series."""
    df = pd.concat([series.shift(i) for i in range(1, lags + 1)], axis=1)
    df.columns = [f"lag_{i}" for i in range(1, lags + 1)]
    return df


def safe_slice(series: pd.Series, start: int, end: int):
    """Slice a series safely without raising index errors."""
    return series.iloc[max(0, start): min(len(series), end)]


# ---------------------------------------------------------
# Feature engineering utilities
# ---------------------------------------------------------

def build_feature_matrix(returns: pd.Series, residuals: np.ndarray, max_lag: int = 5):
    """Construct feature matrix from lagged returns and residuals."""
    lagged_returns = create_lags(returns, max_lag)
    lagged_resid = create_lags(pd.Series(residuals, index=returns.index), max_lag)

    X = pd.concat([lagged_returns, lagged_resid], axis=1).dropna()
    return X


# ---------------------------------------------------------
# Statistical helpers
# ---------------------------------------------------------

def rmse(y_true, y_pred):
    """Root mean squared error."""
    return np.sqrt(np.mean((y_true - y_pred) ** 2))


def annualize_volatility(daily_vol: float, trading_days: int = 252) -> float:
    """Convert daily volatility to annualized volatility."""
    return np.sqrt(trading_days) * daily_vol


# ---------------------------------------------------------
# Regime utilities
# ---------------------------------------------------------

def most_likely_regime(prob_matrix: np.ndarray) -> np.ndarray:
    """Return the most likely regime at each time step."""
    return np.argmax(prob_matrix, axis=1)


# ---------------------------------------------------------
# File & path utilities
# ---------------------------------------------------------

def ensure_dir(path: str):
    """Create directory if it does not exist."""
    os.makedirs(path, exist_ok=True)


# ---------------------------------------------------------
# General-purpose helpers
# ---------------------------------------------------------

def flatten_dict(d: dict, parent_key: str = "", sep: str = "."):
    """Flatten nested dictionaries for logging or config export."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
