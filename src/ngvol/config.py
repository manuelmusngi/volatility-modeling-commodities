from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import yaml


@dataclass
class DataConfig:
    prices_path: str
    weather_factors_path: str | None = None
    policy_factors_path: str | None = None
    date_col: str = "date"
    price_col: str = "settle"


@dataclass
class ModelConfig:
    model_type: str  # "FIGARCH", "FIAPARCH", "APARCH", "GARCH_MIDAS", "MS_GARCH", "ML_BENCH"
    horizon: int = 1


@dataclass
class TrainConfig:
    test_size: float = 0.2
    rolling_window: int | None = None
    random_state: int = 42


@dataclass
class ExperimentConfig:
    data: DataConfig
    model: ModelConfig
    train: TrainConfig


def load_config(path: str | Path) -> ExperimentConfig:
    path = Path(path)
    with path.open("r") as f:
        raw = yaml.safe_load(f)

    data_cfg = DataConfig(**raw["data"])
    model_cfg = ModelConfig(**raw["model"])
    train_cfg = TrainConfig(**raw["train"])

    return ExperimentConfig(data=data_cfg, model=model_cfg, train=train_cfg)
