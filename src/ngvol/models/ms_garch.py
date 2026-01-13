# src/ngvol/models/ms_garch.py
from __future__ import annotations
import numpy as np
from arch.univariate import ConstantMean, GARCH
from .base import VolatilityModel


class MSGARCHModel(VolatilityModel):
    """
    Simple 2-regime MS-GARCH skeleton.

    - Two GARCH(1,1) components.
    - Regime probabilities inferred via a crude EM-like loop (placeholder).
    """

    def __init__(self):
        self._garch_low = None
        self._garch_high = None
        self._regime_prob = None

    def fit(self, returns: np.ndarray, exog: np.ndarray | None = None) -> "MSGARCHModel":
        median_abs = np.median(np.abs(returns))
        low_idx = np.abs(returns) <= median_abs
        high_idx = ~low_idx

        am_low = ConstantMean(returns[low_idx])
        am_low.volatility = GARCH(1, 0, 1)
        self._garch_low = am_low.fit(disp="off")

        am_high = ConstantMean(returns[high_idx])
        am_high.volatility = GARCH(1, 0, 1)
        self._garch_high = am_high.fit(disp="off")

        sigma2_low = self._garch_low.conditional_volatility ** 2
        sigma2_high = self._garch_high.conditional_volatility ** 2

        sigma2_low_full = np.interp(
            np.arange(len(returns)),
            np.where(low_idx)[0],
            sigma2_low,
        )
        sigma2_high_full = np.interp(
            np.arange(len(returns)),
            np.where(high_idx)[0],
            sigma2_high,
        )
        p = sigma2_high_full / (sigma2_low_full + sigma2_high_full)
        self._regime_prob = np.clip(p, 0.05, 0.95)
        return self

    def forecast(self, horizon: int = 1, exog_future: np.ndarray | None = None) -> np.ndarray:
        if self._garch_low is None or self._garch_high is None or self._regime_prob is None:
            raise RuntimeError("Model must be fit before forecasting.")
        f_low = self._garch_low.forecast(horizon=horizon).variance.values[-1]
        f_high = self._garch_high.forecast(horizon=horizon).variance.values[-1]
        p_last = self._regime_prob[-1]
        return (1 - p_last) * f_low + p_last * f_high
