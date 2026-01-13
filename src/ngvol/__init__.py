"""
ngvol: Natural Gas Volatility Modeling Framework

This package provides a modular, research‑grade toolkit for modeling and forecasting
natural gas price volatility using advanced econometric and machine‑learning methods.
It implements a unified interface for long‑memory GARCH models (FIGARCH, FIAPARCH),
asymmetric power models (APARCH), macro‑driven GARCH‑MIDAS specifications, and
regime‑switching volatility structures. The design emphasizes reproducibility,
transparent experimentation, and extensibility, enabling researchers and practitioners
to evaluate competing volatility models, integrate weather and policy factors, and
run systematic forecasting pipelines.
"""

from .config import load_config  # convenience re-export
