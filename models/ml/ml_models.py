from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor


def build_ml_model(name: str, params: dict):
    """Instantiate ML regressors based on type."""
    model_type = params.get("type")

    if model_type == "RandomForestRegressor":
        model = RandomForestRegressor(
            n_estimators=params.get("n_estimators", 300),
            max_depth=params.get("max_depth", 6),
            min_samples_leaf=params.get("min_samples_leaf", 5),
            random_state=params.get("random_state", 42),
        )
    elif model_type == "XGBRegressor":
        model = XGBRegressor(
            n_estimators=params.get("n_estimators", 500),
            learning_rate=params.get("learning_rate", 0.05),
            max_depth=params.get("max_depth", 4),
            subsample=params.get("subsample", 0.8),
            colsample_bytree=params.get("colsample_bytree", 0.8),
            random_state=params.get("random_state", 42),
        )
    else:
        raise ValueError(f"Unsupported ML model type: {model_type}")

    return model
