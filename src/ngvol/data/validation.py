from __future__ import annotations
import pandas as pd

REQUIRED_PRICE_COLS = ["date", "settle"]
REQUIRED_WEATHER_COLS = ["date"]
REQUIRED_POLICY_COLS = ["date"]


def _validate_columns(df: pd.DataFrame, required: list[str], name: str):
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"{name} missing required columns: {missing}")


def _validate_dates(df: pd.DataFrame, name: str):
    if "date" not in df.columns:
        raise ValueError(f"{name} must have a 'date' column")
    if not pd.api.types.is_datetime64_any_dtype(df["date"]):
        raise TypeError(f"{name} 'date' column must be datetime64 dtype")


def _validate_not_empty(df: pd.DataFrame, name: str):
    if df.empty:
        raise ValueError(f"{name} is empty")


def validate_price_data(df: pd.DataFrame):
    name = "Price data"
    _validate_columns(df, REQUIRED_PRICE_COLS, name)
    _validate_not_empty(df, name)
    _validate_dates(df, name)


def validate_weather_data(df: pd.DataFrame):
    name = "Weather data"
    _validate_columns(df, REQUIRED_WEATHER_COLS, name)
    _validate_not_empty(df, name)
    _validate_dates(df, name)


def validate_policy_data(df: pd.DataFrame):
    name = "Policy data"
    _validate_columns(df, REQUIRED_POLICY_COLS, name)
    _validate_not_empty(df, name)
    _validate_dates(df, name)
