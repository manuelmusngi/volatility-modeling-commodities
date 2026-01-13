# src/ngvol/data/features_midas.py
import pandas as pd
import numpy as np


def _lagged_average(series: pd.Series, window: int) -> pd.Series:
    return series.rolling(window=window, min_periods=1).mean()


def build_midas_factors(df: pd.DataFrame, date_col: str = "date") -> pd.DataFrame:
    df = df.copy()

    candidate_cols = [
        c
        for c in df.columns
        if c not in {date_col, "ret", "price", "settle"} and df[c].dtype != "O"
    ]

    for col in candidate_cols:
        df[f"{col}_midas_22"] = _lagged_average(df[col], window=22)
        df[f"{col}_midas_66"] = _lagged_average(df[col], window=66)

    df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=["ret"])
    return df
