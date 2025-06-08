import csv
import io
from pathlib import Path
from urllib.parse import urlparse
from datetime import datetime
from urllib.request import urlopen


def load_csv(source: str) -> dict:
    """Load OHLCV data from a local CSV file or URL into dictionaries of lists."""
    file_path = Path(source)

    if file_path.exists():
        raw = file_path.read_text()
    else:
        parsed = urlparse(source)
        if parsed.scheme and parsed.netloc:
            with urlopen(source) as resp:
                raw = resp.read().decode()
        else:
            raise FileNotFoundError(f"Could not find data file: {source}")

    reader = csv.DictReader(io.StringIO(raw))
    data = {key: [] for key in reader.fieldnames}
    for row in reader:
        data["Date"].append(datetime.fromisoformat(row["Date"]))
        data["Open"].append(float(row["Open"]))
        data["High"].append(float(row["High"]))
        data["Low"].append(float(row["Low"]))
        data["Close"].append(float(row["Close"]))
        data["Volume"].append(int(row["Volume"]))
    return data
