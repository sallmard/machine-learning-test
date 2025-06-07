from abc import ABC, abstractmethod
import pandas as pd


class Strategy(ABC):
    """Base class for trading strategies."""

    @abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> pd.Series:
        """Return a pandas Series of trading signals (1 for buy, -1 for sell, 0 for hold)."""
        pass


class MovingAverageCrossoverStrategy(Strategy):
    """Simple moving average crossover."""

    def __init__(self, fast: int = 5, slow: int = 10):
        if fast >= slow:
            raise ValueError("Fast MA should be less than slow MA")
        self.fast = fast
        self.slow = slow

    def generate_signals(self, data: pd.DataFrame) -> pd.Series:
        df = data.copy()
        df["fast_ma"] = df["Close"].rolling(window=self.fast, min_periods=1).mean()
        df["slow_ma"] = df["Close"].rolling(window=self.slow, min_periods=1).mean()
        signals = pd.Series(0, index=df.index)
        prev_signal = 0
        for i in range(1, len(df)):
            if df.loc[i - 1, "fast_ma"] <= df.loc[i - 1, "slow_ma"] and df.loc[i, "fast_ma"] > df.loc[i, "slow_ma"]:
                prev_signal = 1
            elif df.loc[i - 1, "fast_ma"] >= df.loc[i - 1, "slow_ma"] and df.loc[i, "fast_ma"] < df.loc[i, "slow_ma"]:
                prev_signal = -1
            signals.iloc[i] = prev_signal
        return signals
