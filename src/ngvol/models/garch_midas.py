from __future__ import annotations
import numpy as np
from dataclasses import dataclass
from arch.univariate import ConstantMean, GARCH
from .base import VolatilityModel


@dataclass
class MidasSpec:
    theta: float = 0.95  # exponential decay parameter


def midas_component(factors: np.ndarray, spec: MidasSpec) -> np.ndarray:
    """
    Very simple MIDAS-like component: exponentially weighted average of
    the average factor across columns.
    """
    n = factors.shape[0]
    tau = np.zeros(n, dtype=float)
    for i in range(n):
        w = spec.theta ** np.arange(i + 1)[::-1]
        w /= w.sum()
        tau[i] = (w * factors[: i + 1].mean(axis=1)).sum()
    return tau


class GARCHMIDASModel(VolatilityModel):
    """
    GARCH-MIDAS model: short-run GARCH on returns scaled by long-run MIDAS factor.
    """

    def __init__(self, midas_spec: MidasSpec | None = None):
        self.midas_spec = midas_spec or MidasSpec()
        self._short_run = None
        self._tau = None

    def fit(self, returns: np.ndarray, exog: np.ndarray | None = None) -> "GARCHMIDASModel":
        if exog is None:
            raise ValueError("GARCH-MIDAS requires exogenous macro/weather factors.")
        self._tau = midas_component(exog, self.midas_spec)
        adjusted_returns = returns / np.sqrt(self._tau)

        am = ConstantMean(adjusted_returns)
        am.volatility = GARCH(p=1, q=1)
        self._short_run = am.fit(disp="off")
        return self

    def forecast(self, horizon: int = 1, exog_future: np.ndarray | None = None) -> np.ndarray:
        if self._short_run is None or self._tau is None:
            raise RuntimeError("GARCHMIDASModel must be fit before forecasting.")

        fcast = self._short_run.forecast(horizon=horizon)
        short_var = fcast.variance.values[-1]

        if exog_future is None:
            tau_future = np.full(horizon, self._tau[-1])
        else:
            stacked = np.vstack([exog_future])
            tau_future = midas_component(stacked, self.midas_spec)[-horizon:]

        return tau_future * short_var
