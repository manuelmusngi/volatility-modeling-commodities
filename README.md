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

- 🎯 Objectives
- Model natural gas volatility using GARCH, EGARCH, FIGARCH, and MS‑GARCH / HMM‑GARCH.

- Benchmark econometric models against ML regressors (RF, XGBoost, LSTM optional).

- Detect and interpret volatility regimes in natural gas markets.

- Produce rolling forecasts, regime probabilities, and forecast error comparisons.

- Provide a clean, modular, production‑ready architecture.

- 📚 Research Foundations
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

🧩 Project Structure
natural-gas-volatility/\
│
├── README.md\
├── main.py\
│
├── config/\
│   ├── settings.py\              # Global configs (paths, model params, rolling windows)\
│   └── model_params.yaml        # GARCH, HMM, ML hyperparameters\
│
├── data/\
│   ├── raw/                     # Raw Henry Hub data\
│   ├── processed/               # Cleaned returns, volatility proxies\
│   └── loader.py                # Data ingestion + preprocessing\
│
├── models/\
│   ├── garch/
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
│   ├── figures/                 # Plots (regimes, forecasts, comparisons)\
│   └── results.csv              # Forecast error summary\
│
└── requirements.txt



#### License
This project is licensed under the [MIT License](https://github.com/manuelmusngi/regime_switching_models/edit/main/LICENSE).  
