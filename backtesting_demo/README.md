# Backtesting Demo

This folder contains a very small Python application that demonstrates how a simple backtest works using a Moving Average Crossover strategy on daily OHLCV data.

## Structure

- `data_loader.py` – helper to load CSV data.
- `strategy.py` – contains a base `Strategy` class and a `MovingAverageCrossoverStrategy` implementation.
- `backtester.py` – very small backtest engine.
- `run_backtest.py` – command line entry point.
- `data/` – contains a small sample dataset (`AAPL.csv`).

## Running

```bash
python -m backtesting_demo.run_backtest backtesting_demo/data/AAPL.csv
```

You can override the moving average windows:

```bash
python -m backtesting_demo.run_backtest backtesting_demo/data/AAPL.csv --fast 3 --slow 7
```
