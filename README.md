<p align="center">
  <img src="https://img.shields.io/badge/Language-Python_3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/Models-GARCH | FIGARCH | FIAPARCH | MIDAS | MS--GARCH-green.svg" />
  <img src="https://img.shields.io/badge/Domain-Natural_Gas_Volatility-orange.svg" />
  <img src="https://img.shields.io/badge/Research-Backed_Models-purple.svg" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" />
</p>


📘 Project Summary

Natural Gas Volatility Modeling with GARCH‑Family, Long‑Memory, MIDAS, and Regime‑Switching Frameworks

This project implements a complete, modular, end‑to‑end research framework for modeling and forecasting natural gas price volatility using advanced econometric and machine‑learning methods. The architecture integrates long‑memory GARCH models, asymmetric power models, macro‑driven MIDAS components, regime‑switching volatility, and ML benchmarks—reflecting the evolution of volatility modeling in both academic literature and practitioner workflows.

The codebase is structured for reproducible research, systematic experimentation, and production‑grade extensibility, making it suitable for quantitative researchers, energy analysts, and algorithmic trading teams.

⭐ Highlights
📈 1. Full GARCH‑Family Implementation
FIGARCH for long‑memory volatility (Baillie, Bollerslev & Mikkelsen, 1996).

APARCH / FIAPARCH for asymmetric power effects and heavy‑tailed shocks (Ding et al., 1993; Conrad et al., 2011).

Unified model interface for clean experimentation and benchmarking.

🌦️ 2. GARCH‑MIDAS with Weather & Climate Factors
Incorporates extreme weather, temperature anomalies, and climate‑policy uncertainty into long‑run volatility.

Implements MIDAS‑style low‑frequency components inspired by Liang (2022) and Guo (2023).

Supports arbitrary macro factor inputs for flexible scenario analysis.

🔄 3. Regime‑Switching Volatility
Prototype MS‑GARCH / HMM‑GARCH capturing structural breaks and volatility regimes.

Reflects empirical findings from Arouri et al. (2012) and Kang et al. (2009) on regime‑dependent energy volatility.

🤖 4. Machine Learning Benchmark
Random‑Forest‑based volatility forecaster for squared returns.

Provides a modern baseline for comparing classical econometrics vs ML (Chung, 2024).

🧱 5. Modular, Extensible Project Architecture

Clean separation of:

data loading

MIDAS factor engineering

model definitions

training pipelines

evaluation utilities

Designed for reproducibility, rolling‑window backtests, and rapid model iteration.

📊 6. End‑to‑End Experiment Pipeline

YAML‑driven configuration for experiments.

Rolling forecasts, variance prediction, and evaluation metrics (RMSE, MAE).

Visualization of realized vs forecasted variance.

🎯 Key Takeaways

1. Natural gas volatility exhibits strong long‑memory behavior.
FIGARCH and FIAPARCH models capture persistence far better than standard GARCH, consistent with empirical findings in energy markets.

2. Asymmetry and power effects matter.
APARCH‑style models reflect the nonlinear response of volatility to positive vs negative shocks—important for commodities with storage constraints and seasonal demand.

3. Macro and weather factors significantly improve forecasts.
GARCH‑MIDAS models show that extreme weather, climate risks, and policy uncertainty meaningfully shape long‑run volatility.

4. Volatility regimes are real and economically meaningful.
Regime‑switching models capture structural breaks, crisis periods, and shifts in market microstructure.

5. ML models are competitive but not universally superior.
Machine‑learning benchmarks provide robustness checks and highlight when nonlinear models outperform classical GARCH.

6. A unified research framework accelerates experimentation.
The modular design allows researchers to plug in new models, factors, or datasets without rewriting the pipeline.

#### Project Architecture

├── src/\
│   └── ngvol/\
│       ├── __init__.py\
│       │\
│       ├── config.py\
│       │   # YAML-driven experiment configuration\
│       │\
│       ├── data/\
│       │   ├── __init__.py\
│       │   ├── loader.py\
│       │   ├── features_midas.py\
│       │   └── validation.py\
│       │   # Data ingestion, merging, MIDAS feature engineering, validation\
│       │\
│       ├── models/\
│       │   ├── __init__.py\
│       │   ├── base.py\
│       │   ├── figarch.py\
│       │   ├── fiaparch.py\
│       │   ├── garch_midas.py\
│       │   ├── ms_garch.py\
│       │   └── ml_benchmark.py\
│       │   # FIGARCH, FIAPARCH, APARCH, GARCH-MIDAS, MS-GARCH, ML baselines\
│       │
│       ├── train/\
│       │   ├── __init__.py\
│       │   └── pipeline.py\
│       │   # End-to-end training, rolling forecasts, evaluation\
│       │
│       └── utils/\
│           ├── __init__.py\
│           ├── logging_utils.py\
│           └── evaluation.py\
│           # Logging, metrics, shared utilities\
│
├── data/\
│   ├── ng_prices.csv\
│   ├── weather_factors.csv\
│   └── policy_factors.csv\
│   # Raw datasets for prices, weather/climate, policy uncertainty\
│
├── experiments/\
│   └── config_example.yaml\
│   # Experiment configuration files\
│
├── scripts/\
│   └── download_data.py\
│   # Public data download helpers\
│
├── main.py\
│   # Entry point for running full experiments\
│
├── README.md\
├── pyproject.toml\
└── requirements.txt\




#### Reference Research Papers

📊 Core GARCH‑Family Foundations in Natural Gas
🔹 Long‑Memory & Fractional Volatility
Baillie, Bollerslev & Mikkelsen (1996) – Fractionally Integrated GARCH  
Introduces FIGARCH, foundational for persistent volatility in energy markets.

Elder & Serletis (2008) – Long memory in energy futures volatility  
Empirical evidence of fractional integration in natural gas futures volatility.

⚖️ Asymmetry, Power Effects & Heavy Tails
🔹 APARCH / FIAPARCH‑Relevant
Ding, Granger & Engle (1993) – A long memory property of stock market returns  
Establishes power‑transformed volatility dynamics underlying APARCH.

Conrad, Karanasos & Zeng (2011) – Multivariate FIAPARCH models  
Extends FIAPARCH to capture asymmetric long‑memory volatility spillovers.

🌦️ Macro‑Driven & MIDAS Extensions (Highly Relevant)
🔹 Weather, Climate, and Macro Factors
Liang et al. (2022) – Natural gas volatility prediction with extreme weather  
GARCH‑MIDAS‑ES model incorporating weather extremes improves NG volatility forecasts.

Guo et al. (2023) – Climate risks and natural gas futures volatility  
GARCH‑MIDAS with climate policy uncertainty and disaster frequency.

Sources: 

🔄 Regime Switching & Structural Breaks
🔹 MS‑GARCH / HMM‑GARCH
Arouri, Lahiani & Nguyen (2012) – Regime‑switching volatility in energy prices  
Shows distinct volatility regimes in natural gas and oil markets.

Kang, Kang & Yoon (2009) – Structural breaks and volatility forecasting  
Demonstrates regime‑aware GARCH superiority for energy commodities.

🧠 Hybrid & Comparative Modeling
🔹 GARCH vs ML (Benchmarking)
Chung (2024) – GARCH vs Machine Learning for energy volatility  
Natural gas volatility shows weaker spillovers but strong persistence; hybrid models recommended.




#### License
This project is licensed under the [MIT License](https://github.com/manuelmusngi/regime_switching_models/edit/main/LICENSE).  
