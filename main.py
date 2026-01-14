from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt

from src.ngvol.config import load_config
from src.ngvol.train import run_experiment


def main():
    cfg_path = Path("experiments/config_example.yaml")
    cfg = load_config(cfg_path)

    result = run_experiment(cfg)

    print("Evaluation metrics:")
    for k, v in result.metrics.items():
        print(f"  {k}: {v:.6f}")

    plt.figure(figsize=(10, 4))
    plt.plot(result.y_true, label="Realized variance (ret^2)", alpha=0.7)
    plt.plot(result.y_pred, label="Forecast variance", alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
