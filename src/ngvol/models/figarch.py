# src/ngvol/models/figarch.py
import numpy as np
from arch.univariate import ConstantMean, FIGARCH
from .base import VolatilityModel


class FIGARCHModel(VolatilityModel):
    """
    Fractionally Integrated GARCH wrapper using arch's FIGARCH.

    Baillie, Bollerslev & Mikkelsen (1996).
    Elder & Serletis (2008) motivate its use for energy futures.
    """

    def __init__(self, p: int = 1, q: int = 1):
        self.p = p
        self.q = q
        self._fitted = None

    def fit(self, returns: np.ndarray, exog: np.ndarray | None = None) -> "FIGARCHModel":
        am = ConstantMean(returns)
        am.volatility = FIGARCH(p=self.p, q=self.q)
        self._fitted = am.fit(disp="off")
        return self

    def forecast(self, horizon: int = 1, exog_future: np.ndarray | None = None) -> np.ndarray:
        if self._fitted is None:
            raise RuntimeError("Model must be fit before forecasting.")
        fcast = self._fitted.forecast(horizon=horizon)
        var = fcast.variance.values[-1]
        return var
