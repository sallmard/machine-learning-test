import io
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd
import requests
import yfinance as yf


def load_csv(source: str) -> pd.DataFrame:
    """Load OHLCV data from a CSV file, URL, or ticker symbol."""
    file_path = Path(source)

    if file_path.exists():
        df = pd.read_csv(file_path, parse_dates=["Date"])
    else:
        parsed = urlparse(source)
        if parsed.scheme and parsed.netloc:
            resp = requests.get(source)
            resp.raise_for_status()
            df = pd.read_csv(io.StringIO(resp.text), parse_dates=["Date"])
        else:
            data = yf.download(source, progress=False)
            if data.empty:
                raise FileNotFoundError(
                    f"Could not find data file or download symbol: {source}"
                )
            data.index.name = "Date"
            data.reset_index(inplace=True)
            df = data

    df = df.sort_values("Date").reset_index(drop=True)
    return df
