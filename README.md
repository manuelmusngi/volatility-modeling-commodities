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

#### License
This project is licensed under the [MIT License](https://github.com/manuelmusngi/regime_switching_models/edit/main/LICENSE).  
