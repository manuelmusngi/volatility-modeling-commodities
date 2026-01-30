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

📚 Research Reference Foundations
  
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
├── [main.py](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/main.py)\
│
├── config/\
│   ├── [settings.py](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/config/settings.py)               
│   └── [model_params.yaml](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/config/model_params.yaml)        
│
├── data/\            
│   └── [loader.py](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/data/loader.py)                
│
├── models/\
│   ├── garch/\
│   ├── [garch_models.py](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/models/garch/garch_models.py)       
│   │   └── [ms_garch.py](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/models/garch/ms_garch.py)          
│   │
│   ├── hmm/\
│   │   └──[hmm_volatility.py](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/models/hmm/hmm_volatility.py)   
│   │
│   ├── ml/\
│   │   ├── [ml_models.py](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/models/ml/ml_models.py)         
│   │   └── [hybrid_models.py](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/models/ml/hybrid_models.py)      
│   │
│   └──[model_factory.py](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/models/model_factory.py)         
│
├── forecasting/\
│   ├── [rolling_forecast.py](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/forecasting/rolling_forecast.py)       
│   └── [regime_forecast.py](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/forecasting/regime_forecast.py)        
│
├── evaluation/\
│   ├── [metrics.py](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/evaluation/metrics.py)               
│   └── [comparison.py](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/evaluation/comparison.py)           
│
├── utils/\
│   ├── [logger.py](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/utils/logger.py)                
│   ├── [plotter.py](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/utils/plotter.py)                
│   └── helpers.py                
│
├── reports/\
│   ├── figures/                 
│   └── results.csv              
│
└── [requirements.txt](https://github.com/manuelmusngi/volatility-modeling-energy-commodities/blob/main/requirements.txt)


#### License
This project is licensed under the [MIT License](https://github.com/manuelmusngi/regime_switching_models/edit/main/LICENSE).  
