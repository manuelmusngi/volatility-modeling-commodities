import os
import pandas as pd
from datetime import datetime


# ---------------------------------------------------------
# Path & directory utilities
# ---------------------------------------------------------

def ensure_dir(path: str):
    """Create a directory if it does not exist."""
    os.makedirs(path, exist_ok=True)


def build_report_path(base_dir: str, filename: str) -> str:
    """Construct a full path inside the reports directory."""
    ensure_dir(base_dir)
    return os.path.join(base_dir, filename)


# ---------------------------------------------------------
# Results saving utilities
# ---------------------------------------------------------

def save_results(df: pd.DataFrame, path: str):
    """Save evaluation or forecast results to CSV."""
    ensure_dir(os.path.dirname(path))
    df.to_csv(path, index=False)


def append_results(df: pd.DataFrame, path: str):
    """Append new results to an existing CSV, creating it if needed."""
    ensure_dir(os.path.dirname(path))
    if os.path.exists(path):
        existing = pd.read_csv(path)
        combined = pd.concat([existing, df], ignore_index=True)
        combined.to_csv(path, index=False)
    else:
        df.to_csv(path, index=False)


# ---------------------------------------------------------
# Timestamp utilities
# ---------------------------------------------------------

def timestamp() -> str:
    """Return a clean timestamp string for filenames."""
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def timestamped_filename(prefix: str, ext: str = "csv") -> str:
    """Generate a timestamped filename for reports."""
    return f"{prefix}_{timestamp()}.{ext}"


# ---------------------------------------------------------
# Formatting utilities
# ---------------------------------------------------------

def format_metric(value: float, decimals: int = 6) -> float:
    """Round metrics consistently for reporting."""
    return round(float(value), decimals)


def flatten_dict(d: dict, parent_key: str = "", sep: str = "."):
    """Flatten nested dictionaries for logging or config export."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

