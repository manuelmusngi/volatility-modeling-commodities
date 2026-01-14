from __future__ import annotations
from pathlib import Path
import pandas as pd
import numpy as np

from .validation import (
    validate_price_data,
    validate_weather_data,
    validate_policy_data,
)
from .features_midas import build_midas_factors


def load_returns_with_factors(
    prices_path: Path | str,
    weather_path: Path | str | None = None,
    policy_path: Path | str | None = None,
    date_col: str = "date",
    price_col: str = "settle",
) -> pd.DataFrame:
    prices_path = Path(prices_path)
    prices = pd.read_csv(prices_path, parse_dates=[date_col])
    prices.sort_values(date_col, inplace=True)
    validate_price_data(prices)

    prices["ret"] = np.log(prices[price_col]).diff()
    prices = prices.dropna(subset=["ret"])

    if weather_path is not None:
        weather = pd.read_csv(Path(weather_path), parse_dates=[date_col])
        validate_weather_data(weather)
        prices = prices.merge(weather, on=date_col, how="left")

    if policy_path is not None:
        policy = pd.read_csv(Path(policy_path), parse_dates=[date_col])
        validate_policy_data(policy)
        prices = prices.merge(policy, on=date_col, how="left")

    prices = build_midas_factors(prices, date_col=date_col)
    return prices

