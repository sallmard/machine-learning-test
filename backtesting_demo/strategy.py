from abc import ABC, abstractmethod
from typing import Dict, List


class Strategy(ABC):
    """Base class for trading strategies."""

    @abstractmethod
    def generate_signals(self, data: Dict[str, List[float]]) -> List[int]:
        """Return a list of trading signals (1 for buy, -1 for sell, 0 for hold)."""
        pass


class MovingAverageCrossoverStrategy(Strategy):
    """Simple moving average crossover."""

    def __init__(self, fast: int = 5, slow: int = 10):
        if fast >= slow:
            raise ValueError("Fast MA should be less than slow MA")
        self.fast = fast
        self.slow = slow

    def generate_signals(self, data: Dict[str, List[float]]) -> List[int]:
        close = data["Close"]
        fast_ma: List[float] = []
        slow_ma: List[float] = []
        for i in range(len(close)):
            fast_window = close[max(0, i - self.fast + 1): i + 1]
            slow_window = close[max(0, i - self.slow + 1): i + 1]
            fast_ma.append(sum(fast_window) / len(fast_window))
            slow_ma.append(sum(slow_window) / len(slow_window))

        signals = [0] * len(close)
        prev_signal = 0
        for i in range(1, len(close)):
            if fast_ma[i - 1] <= slow_ma[i - 1] and fast_ma[i] > slow_ma[i]:
                prev_signal = 1
            elif fast_ma[i - 1] >= slow_ma[i - 1] and fast_ma[i] < slow_ma[i]:
                prev_signal = -1
            signals[i] = prev_signal
        return signals
