from __future__ import annotations
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from .base import VolatilityModel


class MLVolBenchmark(VolatilityModel):
    """
    Simple ML benchmark: predict squared returns using lagged features
    and optional exogenous variables.
    """

    def __init__(self, n_lags: int = 5, **rf_kwargs):
        self.n_lags = n_lags
        self.model = RandomForestRegressor(**rf_kwargs)
        self._last_features = None

    def _build_design(self, returns: np.ndarray, exog: np.ndarray | None):
        y2 = returns ** 2
        X = []
        for t in range(self.n_lags, len(returns)):
            row = [y2[t - l - 1] for l in range(self.n_lags)]
            if exog is not None:
                row.extend(exog[t])
            X.append(row)
        X = np.array(X)
        y = y2[self.n_lags:]
        return X, y

    def fit(self, returns: np.ndarray, exog: np.ndarray | None = None) -> "MLVolBenchmark":
        X, y = self._build_design(returns, exog)
        self.model.fit(X, y)
        self._last_features = X[-1]
        return self

    def forecast(self, horizon: int = 1, exog_future: np.ndarray | None = None) -> np.ndarray:
        if self._last_features is None:
            raise RuntimeError("MLVolBenchmark must be fit before forecasting.")
        # 1-step ahead forecast only
        return np.array([self.model.predict(self._last_features.reshape(1, -1))[0]])
