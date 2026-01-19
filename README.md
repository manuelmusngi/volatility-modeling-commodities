⚡ Natural Gas Volatility Modeling: MS‑GARCH, HMM‑GARCH & Hybrid ML Benchmarks

📘 Project Summary
This project implements a research‑grade volatility modeling framework for Henry Hub natural gas using:

- 🔄 MS‑GARCH / HMM‑GARCH (Arouri, Lahiani & Nguyen, 2012)
Captures regime‑switching volatility, distinguishing calm vs turbulent market states.
- 🤖 Machine Learning Benchmarks (Chung, 2024)
Compares GARCH‑family models vs ML regressors, highlighting natural gas’s
high persistence, weak spillovers, and the value of hybrid modeling.
- 🧠 Hybrid Volatility Forecasting  
Combines econometric structure with ML flexibility for improved out‑of‑sample performance.
- 📊 Full Pipeline  
Data ingestion → preprocessing → model estimation → regime detection → forecasting → evaluation → reporting.

The project is designed for quantitative researchers, energy analysts, energy traders, and risk managers who need a reproducible, extensible, and academically grounded volatility modeling toolkit.

🎯 Objectives
- Model natural gas volatility using GARCH, EGARCH, FIGARCH, and MS‑GARCH / HMM‑GARCH.
- Benchmark econometric models against ML regressors (RF, XGBoost, LSTM optional).
- Detect and interpret volatility regimes in natural gas markets.
- Produce rolling forecasts, regime probabilities, and forecast error comparisons.
- Provide a clean, modular, production‑ready architecture.

📚 Research Foundations
  
1. Regime‑Switching Volatility (MS‑GARCH / HMM‑GARCH)
Arouri, Lahiani & Nguyen (2012) show that natural gas and oil exhibit distinct volatility regimes, often linked to structural market events.
This project implements:
- Hidden Markov Models (HMM)
- Markov‑Switching GARCH (MS‑GARCH)
- Regime‑dependent volatility forecasts
- Smoothed and filtered regime probabilities

2. GARCH vs Machine Learning (Hybrid Benchmarking)
Chung (2024) demonstrates:
- Natural gas volatility has strong persistence
- Spillovers from other markets are weak
- Hybrid models outperform standalone GARCH or ML

This project integrates:
- Pure econometric models
- Pure ML models
- Hybrid GARCH‑residual‑ML models
- Comparative evaluation (MSE, MAE, QLIKE)

🧩 Project Architecture

natural-gas-volatility/\
│
├── [README.md](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/edit/main/README.md)\
├── [main.py](import os
from config.settings import Settings
from data.loader import load_raw_data, preprocess_data
from models.model_factory import (
    build_garch_models,
    build_ms_garch_models,
    build_hmm_models,
    build_ml_models,
    build_hybrid_models,
)
from forecasting.rolling_forecast import run_rolling_forecasts
from forecasting.regime_forecast import run_regime_forecasts
from evaluation.comparison import evaluate_and_compare_models
from utils.logger import get_logger
from utils.plotter import (
    plot_volatility_series,
    plot_regime_probabilities,
    plot_forecast_comparison,
)

logger = get_logger(__name__)


def main():
    # -------------------------------------------------------------------------
    # 1. Load configuration
    # -------------------------------------------------------------------------
    settings = Settings()
    logger.info("Loaded configuration.")

    # -------------------------------------------------------------------------
    # 2. Data ingestion & preprocessing
    # -------------------------------------------------------------------------
    logger.info("Loading raw data...")
    raw_df = load_raw_data(settings.data.raw_path)

    logger.info("Preprocessing data (returns, alignment, filters)...")
    data = preprocess_data(
        raw_df,
        price_col=settings.data.price_column,
        date_col=settings.data.date_column,
        freq=settings.data.frequency,
    )

    returns = data["returns"]
    logger.info(f"Data ready. Sample size: {len(returns)}")

    # -------------------------------------------------------------------------
    # 3. Build model universe
    # -------------------------------------------------------------------------
    logger.info("Building GARCH-family models...")
    garch_models = build_garch_models(settings.model_params["garch"])

    logger.info("Building MS-GARCH models...")
    ms_garch_models = build_ms_garch_models(settings.model_params["ms_garch"])

    logger.info("Building HMM models...")
    hmm_models = build_hmm_models(settings.model_params["hmm"])

    logger.info("Building ML models...")
    ml_models = build_ml_models(settings.model_params["ml"])

    logger.info("Building hybrid models...")
    hybrid_models = build_hybrid_models(settings.model_params["hybrid"])

    all_models = {
        **garch_models,
        **ms_garch_models,
        **hmm_models,
        **ml_models,
        **hybrid_models,
    }
    logger.info(f"Total models instantiated: {len(all_models)}")

    # -------------------------------------------------------------------------
    # 4. Rolling forecasts (unconditional / non‑regime)
    # -------------------------------------------------------------------------
    logger.info("Running rolling forecasts for all models...")
    rolling_results = run_rolling_forecasts(
        returns=returns,
        models=all_models,
        window_size=settings.forecasting.window_size,
        forecast_horizon=settings.forecasting.horizon,
        refit_frequency=settings.forecasting.refit_frequency,
        evaluation_start=settings.forecasting.evaluation_start,
    )

    # -------------------------------------------------------------------------
    # 5. Regime‑aware forecasts (HMM / MS‑GARCH)
    # -------------------------------------------------------------------------
    logger.info("Running regime‑aware forecasts...")
    regime_results = run_regime_forecasts(
        returns=returns,
        hmm_models=hmm_models,
        ms_garch_models=ms_garch_models,
        horizon=settings.forecasting.horizon,
    )

    # -------------------------------------------------------------------------
    # 6. Evaluation & comparison
    # -------------------------------------------------------------------------
    logger.info("Evaluating and comparing models...")
    eval_df = evaluate_and_compare_models(
        rolling_results=rolling_results,
        regime_results=regime_results,
        metrics=settings.evaluation.metrics,
        output_path=settings.reports.results_path,
    )
    logger.info("Evaluation complete.")
    logger.info(f"Top models:\n{eval_df.head()}")

    # -------------------------------------------------------------------------
    # 7. Visualization & reporting
    # -------------------------------------------------------------------------
    logger.info("Generating plots...")
    os.makedirs(settings.reports.figures_path, exist_ok=True)

    plot_volatility_series(
        returns=returns,
        output_path=os.path.join(settings.reports.figures_path, "volatility_series.png"),
    )

    for name, hmm_model in hmm_models.items():
        plot_regime_probabilities(
            model=hmm_model,
            returns=returns,
            output_path=os.path.join(
                settings.reports.figures_path, f"regime_probs_{name}.png"
            ),
        )

    plot_forecast_comparison(
        eval_df=eval_df,
        output_path=os.path.join(
            settings.reports.figures_path, "forecast_comparison.png"
        ),
        top_n=10,
    )

    logger.info("Pipeline completed successfully.")


if __name__ == "__main__":
    main()
)\
│
├── config/\
│   ├── settings.py              # Global configs (paths, model params, rolling windows)\
│   └── model_params.yaml        # GARCH, HMM, ML hyperparameters\
│
├── data/\
│   ├── raw/                     # Raw Henry Hub data\
│   ├── processed/               # Cleaned returns, volatility proxies\
│   └── loader.py                # Data ingestion + preprocessing\
│
├── models/\
│   ├── garch/\
│   │   ├── garch_models.py      # GARCH, EGARCH, FIGARCH\
│   │   └── ms_garch.py          # MS‑GARCH implementation\
│   │
│   ├── hmm/\
│   │   └── hmm_volatility.py    # HMM regime detection\
│   │
│   ├── ml/\
│   │   ├── ml_models.py         # RF, XGB, LSTM (optional)\
│   │   └── hybrid_models.py     # GARCH‑residual‑ML hybrids\
│   │
│   └── model_factory.py         # Unified interface for all models\
│
├── forecasting/\
│   ├── rolling_forecast.py      # Rolling window forecasting engine\
│   └── regime_forecast.py       # Regime‑aware forecasting logic\
│
├── evaluation/\
│   ├── metrics.py               # MSE, MAE, QLIKE, Diebold‑Mariano tests\
│   └── comparison.py            # Benchmarking across all models\
│
├── utils/\
│   ├── logger.py                # Structured logging\
│   ├── plotter.py               # Volatility, regimes, forecast plots\
│   └── helpers.py               # Misc utilities\
│
├── reports/\
│   ├── figures/\                 # Plots (regimes, forecasts, comparisons)\
│   └── results.csv              # Forecast error summary\
│
└── requirements.txt


#### License
This project is licensed under the [MIT License](https://github.com/manuelmusngi/regime_switching_models/edit/main/LICENSE).  
