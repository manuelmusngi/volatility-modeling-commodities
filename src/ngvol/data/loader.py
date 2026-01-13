# src/ngvol/data/loader.py
from pathlib import Path
import pandas as pd
import numpy as np
from .features_midas import build_midas_factors


def load_returns_with_factors(
    prices_path: Path,
    weather_path: Path | None = None,
    policy_path: Path | None = None,
    date_col: str = "date",
    price_col: str = "price",
) -> pd.DataFrame:
    prices = pd.read_csv(prices_path, parse_dates=[date_col])
    prices = prices.sort_values(date_col)
    prices["ret"] = np.log(prices[price_col]).diff()
    prices = prices.dropna(subset=["ret"])

    if weather_path is not None:
        weather = pd.read_csv(weather_path, parse_dates=[date_col])
        prices = prices.merge(weather, on=date_col, how="left")

    if policy_path is not None:
        policy = pd.read_csv(policy_path, parse_dates=[date_col])
        prices = prices.merge(policy, on=date_col, how="left")

    prices = build_midas_factors(prices, date_col=date_col)
    return prices
