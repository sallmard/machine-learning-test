import pandas as pd


class Backtester:
    """Simple backtest engine."""

    def __init__(self, data: pd.DataFrame, signals: pd.Series, initial_cash: float = 10000.0):
        self.data = data
        self.signals = signals
        self.initial_cash = initial_cash
        self.positions = pd.Series(0, index=self.data.index)
        self.cash = initial_cash
        self.position = 0
        self.trades = []

    def run(self):
        for i in range(1, len(self.data)):
            signal = self.signals.iloc[i]
            price = self.data.loc[i, "Close"]
            if signal == 1 and self.position <= 0:
                # buy
                qty = self.cash // price
                if qty > 0:
                    self.cash -= qty * price
                    self.position += qty
                    self.trades.append({"type": "BUY", "price": price, "qty": qty, "index": i})
            elif signal == -1 and self.position > 0:
                # sell
                self.cash += self.position * price
                self.trades.append({"type": "SELL", "price": price, "qty": self.position, "index": i})
                self.position = 0
            self.positions.iloc[i] = self.position

    @property
    def portfolio_value(self):
        last_price = self.data.iloc[-1]["Close"]
        return self.cash + self.position * last_price
