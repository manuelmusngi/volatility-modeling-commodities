import os
import yaml
from dataclasses import dataclass, field


@dataclass
class DataConfig:
    raw_path: str = "data/raw/henry_hub.csv"
    processed_path: str = "data/processed/returns.csv"
    price_column: str = "price"
    date_column: str = "date"
    frequency: str = "D"


@dataclass
class ForecastingConfig:
    window_size: int = 1000
    horizon: int = 1
    refit_frequency: int = 50
    evaluation_start: int = 1200


@dataclass
class EvaluationConfig:
    metrics: list = field(default_factory=lambda: ["MSE", "MAE", "QLIKE"])


@dataclass
class ReportsConfig:
    results_path: str = "reports/results.csv"
    figures_path: str = "reports/figures"


class Settings:
    def __init__(self, params_path: str = "config/model_params.yaml"):
        self.data = DataConfig()
        self.forecasting = ForecastingConfig()
        self.evaluation = EvaluationConfig()
        self.reports = ReportsConfig()
        self.model_params = self._load_model_params(params_path)

    @staticmethod
    def _load_model_params(path: str):
        with open(path, "r") as f:
            return yaml.safe_load(f)
