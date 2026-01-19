from .garch.garch_models import build_garch_model
from .garch.ms_garch import MSGARCHModel
from .hmm.hmm_volatility import HMMVolatilityModel
from .ml.ml_models import build_ml_model
from .ml.hybrid_models import HybridGARCHML


def build_garch_models(config: dict):
    models = {}
    for name, params in config.items():
        models[name] = build_garch_model(name, params)
    return models


def build_ms_garch_models(config: dict):
    models = {}
    for name, params in config.items():
        models[name] = MSGARCHModel(params)
    return models


def build_hmm_models(config: dict):
    models = {}
    for name, params in config.items():
        models[name] = HMMVolatilityModel(params)
    return models


def build_ml_models(config: dict):
    models = {}
    for name, params in config.items():
        models[name] = build_ml_model(name, params)
    return models


def build_hybrid_models(config: dict):
    # Requires access to base GARCH factories and ML models in practice.
    # Here we just return an empty dict as a placeholder.
    return {}
