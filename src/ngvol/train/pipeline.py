# src/ngvol/train/pipeline.py
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
import pandas as pd
from pathlib import Path

from ngvol.config import ExperimentConfig
from ngvol.data.loader import load_returns_with_factors
from ngvol.models.figarch import FIGARCHModel
from ngvol.models.fiaparch import APARCHModel, FIAPARCHModel
from ngvol.models.garch_midas import GARCHMIDASModel
from ngvol.models.ms_garch import MSGARCHModel
from ngvol.models.ml_benchmark import MLVolBenchmark
from ngvol.utils.evaluation import forecast_metrics
from ngvol.utils.logging_utils import get_logger


logger = get_logger(__name__)


@dataclass
class TrainResult:
    metrics: dict
    y_true: np.ndarray
    y_pred: np.ndarray


def _get_model(cfg: ExperimentConfig):
    t = cfg.model.model_type.upper()
    if t == "FIGARCH":
        return FIGARCHModel()
    if t == "FIAPARCH":
        return FIAPARCHModel()
    if t == "APARCH":
        return APARCHModel()
    if t == "GARCH_MIDAS":
        return GARCHMIDASModel()
    if t == "MS_GARCH":
        return MSGARCHModel()
    if t == "ML_BENCH":
        return MLVolBenchmark()
    raise ValueError(f"Unknown model_type: {cfg.model.model_type}")


def run_experiment(cfg: ExperimentConfig) -> TrainResult:
    df = load_returns_with_factors(
        prices_path=Path(cfg.data.prices_path),
        weather_path=Path(cfg.data.weather_factors_path) if cfg.data.weather_factors_path else None,
        policy_path=Path(cfg.data.policy_factors_path) if cfg.data.policy_factors_path else None,
        date_col=cfg.data.date_col,
        price_col=cfg.data.price_col,
    )

    n = len(df)
    test_size = int(cfg.train.test_size * n)
    train_df = df.iloc[:-test_size]
    test_df = df.iloc[-test_size:]

    exog_cols = [c for c in df.columns if c not in {cfg.data.date_col, "ret"}]
    exog_train = train_df[exog_cols].values if exog_cols else None
    exog_test = test_df[exog_cols].values if exog_cols else None

    model = _get_model(cfg)

    logger.info(f"Fitting model {cfg.model.model_type} on {len(train_df)} observations.")
    model.fit(train_df["ret"].values, exog_train)

    logger.info("Forecasting on test set.")
    # For simplicity: 1-step ahead variance forecast repeated
    horizon = 1
    y_true = test_df["ret"].values ** 2
    y_pred = np.zeros_like(y_true)

    full_returns = train_df["ret"].values
    full_exog = exog_train

    for i in range(len(test_df)):
        sub_returns = np.concatenate([full_returns, test_df["ret"].values[:i]])
        if full_exog is not None:
            sub_exog = np.vstack([full_exog, exog_test[:i]])
        else:
            sub_exog = None
        model.fit(sub_returns, sub_exog)
        y_pred[i] = model.forecast(horizon=horizon)[0]

    metrics = forecast_metrics(y_true, y_pred)
    logger.info(f"Metrics: {metrics}")
    return TrainResult(metrics=metrics, y_true=y_true, y_pred=y_pred)
