import numpy as np


def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def mae(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))


def qlike(y_true, y_pred):
    """QLIKE loss for volatility forecasts."""
    return np.mean(np.log(y_pred) + (y_true / y_pred))
