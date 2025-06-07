import pandas as pd
from pathlib import Path


def load_csv(path: str) -> pd.DataFrame:
    """Load OHLCV data from a CSV file."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Could not find data file: {file_path}")
    df = pd.read_csv(file_path, parse_dates=["Date"])
    df = df.sort_values("Date").reset_index(drop=True)
    return df
