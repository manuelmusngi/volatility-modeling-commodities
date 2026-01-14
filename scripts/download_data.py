from __future__ import annotations
from pathlib import Path
import requests


DATA_DIR = Path("data")


def download_file(url: str, filename: str):
    DATA_DIR.mkdir(exist_ok=True)
    path = DATA_DIR / filename
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    path.write_bytes(resp.content)
    print(f"Downloaded {url} -> {path}")


def main():
    # TODO: replace with real sources you choose
    print("Add real data URLs in scripts/download_data.py:main()")


if __name__ == "__main__":
    main()
