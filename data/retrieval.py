import yfinance as yf
import pandas as pd
from utils.helpers import ensure_dir


def download_yahoo_data(ticker: str, start: str, end: str, save_path: str):
    """Download Henry Hub data from Yahoo Finance."""
    ensure_dir(save_path.rsplit("/", 1)[0])
    df = yf.download(ticker, start=start, end=end)
    df = df.rename(columns={"Adj Close": "price"})
    df.to_csv(save_path)
    return df
