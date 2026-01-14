from __future__ import annotations
import numpy as np
from arch.univariate import ConstantMean, APARCH
from .base import VolatilityModel


class APARCHModel(VolatilityModel):
    """
    Asymmetric Power ARCH (APARCH) model.

    Uses arch's APARCH implementation to capture asymmetry and power effects.
    """

    def __init__(self, p: int = 1, o: int = 1, q: int = 1, power: float = 1.0):
        self.p = p
        self.o = o
        self.q = q
        self.power = power
        self._fitted = None

    def fit(self, returns: np.ndarray, exog: np.ndarray | None = None) -> "APARCHModel":
        am = ConstantMean(returns)
        am.volatility = APARCH(p=self.p, o=self.o, q=self.q, power=self.power)
        self._fitted = am.fit(disp="off")
        return self

    def forecast(self, horizon: int = 1, exog_future: np.ndarray | None = None) -> np.ndarray:
        if self._fitted is None:
            raise RuntimeError("APARCHModel must be fit before forecasting.")
        fcast = self._fitted.forecast(horizon=horizon)
        var = fcast.variance.values[-1]
        return var


class FIAPARCHModel(APARCHModel):
    """
    Skeleton for FIAPARCH model.

    Extends APARCHModel with a fractional differencing parameter `d`.
    Numerical implementation of true FIAPARCH is nontrivial and is left
    as a research extension; this class documents the intended interface.
    """

    def __init__(self, p: int = 1, o: int = 1, q: int = 1, d: float = 0.3, power: float = 1.0):
        super().__init__(p=p, o=o, q=q, power=power)
        self.d = d
        # TODO: implement proper fractional integration for FIAPARCH
