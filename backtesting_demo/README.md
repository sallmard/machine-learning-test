# Backtesting Demo

This folder contains a very small Python application that demonstrates how a simple backtest works using a Moving Average Crossover strategy on daily OHLCV data.

## Structure

- `data_loader.py` – helper to load CSV data.
- `strategy.py` – contains a base `Strategy` class and a `MovingAverageCrossoverStrategy` implementation.
- `backtester.py` – very small backtest engine.
- `run_backtest.py` – command line entry point.
- `data/` – contains a small sample dataset (`AAPL.csv`).

## Requirements

Install the dependencies with:

```bash
pip install pandas requests yfinance
```

## Running

The `data` argument can be a local file path, a URL to a CSV file, or a ticker symbol.

```bash
python -m backtesting_demo.run_backtest backtesting_demo/data/AAPL.csv
```

You can also provide a URL to a CSV file. The script will download it
automatically if the local path doesn't exist:

```bash
python -m backtesting_demo.run_backtest "https://example.com/AAPL.csv"
```

Alternatively, pass a ticker symbol and the data will be fetched using
`yfinance`:

```bash
python -m backtesting_demo.run_backtest AAPL
```

You can override the moving average windows:

```bash
python -m backtesting_demo.run_backtest backtesting_demo/data/AAPL.csv --fast 3 --slow 7
```
