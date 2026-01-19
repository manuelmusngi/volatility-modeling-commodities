import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_volatility_series(returns, output_path: str):
    plt.figure(figsize=(10, 4))
    plt.plot(returns.index, returns**2, label="Squared returns")
    plt.title("Natural Gas Volatility Proxy (Squared Returns)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_regime_probabilities(model, returns, output_path: str):
    probs = model.regime_probabilities(returns)
    plt.figure(figsize=(10, 4))
    for k in range(probs.shape[1]):
        plt.plot(returns.index, probs[:, k], label=f"Regime {k+1}")
    plt.title("Smoothed Regime Probabilities")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_forecast_comparison(eval_df: pd.DataFrame, output_path: str, top_n: int = 10):
    # Expect eval_df with columns ['model', 'MSE', ...]
    if eval_df.empty:
        return
    subset = eval_df.sort_values("MSE").head(top_n)
    plt.figure(figsize=(10, 4))
    plt.bar(subset["model"], subset["MSE"])
    plt.xticks(rotation=45, ha="right")
    plt.title("Top Models by MSE")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
