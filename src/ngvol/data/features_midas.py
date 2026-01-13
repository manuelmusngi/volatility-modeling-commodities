from __future__ import annotations
import pandas as pd
import numpy as np


def _rolling_mean(series: pd.Series, window: int) -> pd.Series:
    return series.rolling(window=window, min_periods=1).mean()


def build_midas_factors(df: pd.DataFrame, date_col: str = "date") -> pd.DataFrame:
    """
    Create simple MIDAS-style low-frequency factors (e.g., 22- and 66-day rolling means)
    for all numeric non-return, non-date columns.
    """
    df = df.copy()

    numeric_cols = [
        c
        for c in df.columns
        if c not in {date_col, "ret"} and pd.api.types.is_numeric_dtype(df[c])
    ]

    for col in numeric_cols:
        df[f"{col}_midas_22"] = _rolling_mean(df[col], 22)
        df[f"{col}_midas_66"] = _rolling_mean(df[col], 66)

    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(subset=["ret"], inplace=True)
    return df
