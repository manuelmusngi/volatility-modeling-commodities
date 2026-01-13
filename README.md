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


#### License
This project is licensed under the [MIT License](https://github.com/manuelmusngi/regime_switching_models/edit/main/LICENSE).  
