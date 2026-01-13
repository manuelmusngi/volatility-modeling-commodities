# src/ngvol/models/base.py
from __future__ import annotations
from abc import ABC, abstractmethod
import numpy as np
import pandas as pd


class VolatilityModel(ABC):
    @abstractmethod
    def fit(self, returns: np.ndarray, exog: np.ndarray | None = None) -> "VolatilityModel":
        ...

    @abstractmethod
    def forecast(
        self,
        horizon: int = 1,
        exog_future: np.ndarray | None = None,
    ) -> np.ndarray:
        ...

    def fit_from_dataframe(
        self,
        df: pd.DataFrame,
        ret_col: str = "ret",
        exog_cols: list[str] | None = None,
    ) -> "VolatilityModel":
        returns = df[ret_col].values
        exog = df[exog_cols].values if exog_cols else None
        return self.fit(returns, exog)

    def forecast_from_dataframe(
        self,
        df_future: pd.DataFrame,
        horizon: int = 1,
        exog_cols: list[str] | None = None,
    ) -> np.ndarray:
        exog_future = df_future[exog_cols].values if exog_cols else None
        return self.forecast(horizon=horizon, exog_future=exog_future)
