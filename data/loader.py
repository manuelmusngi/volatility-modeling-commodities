import pandas as pd
import numpy as np


def load_raw_data(path: str) -> pd.DataFrame:
    """Load raw Henry Hub data from CSV (or other source)."""
    df = pd.read_csv(path)
    return df


def preprocess_data(
    df: pd.DataFrame,
    price_col: str,
    date_col: str,
    freq: str = "D",
) -> dict:
    """Clean data, compute log‑returns, and align frequency."""
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.sort_values(date_col).set_index(date_col)
    df = df.asfreq(freq)

    df["returns"] = 100 * np.log(df[price_col] / df[price_col].shift(1))
    df = df.dropna(subset=["returns"])

    return {"returns": df["returns"], "df": df}
