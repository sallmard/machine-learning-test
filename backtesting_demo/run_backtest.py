import argparse
from pathlib import Path

from backtesting_demo.data_loader import load_csv
from backtesting_demo.strategy import MovingAverageCrossoverStrategy
from backtesting_demo.backtester import Backtester


def main():
    parser = argparse.ArgumentParser(description="Simple backtesting demo")
    parser.add_argument("data", type=str, help="Path to OHLCV CSV file")
    parser.add_argument("--fast", type=int, default=5, help="Fast moving average window")
    parser.add_argument("--slow", type=int, default=10, help="Slow moving average window")
    args = parser.parse_args()

    df = load_csv(args.data)
    strategy = MovingAverageCrossoverStrategy(fast=args.fast, slow=args.slow)
    signals = strategy.generate_signals(df)

    backtester = Backtester(df, signals)
    backtester.run()
    print(f"Final portfolio value: {backtester.portfolio_value:.2f}")
    print("Trades:")
    for trade in backtester.trades:
        date = df.loc[trade["index"], "Date"].date()
        print(f"  {date} {trade['type']} {trade['qty']} @ {trade['price']}")


if __name__ == "__main__":
    main()
