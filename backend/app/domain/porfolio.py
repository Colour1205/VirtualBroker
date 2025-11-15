from typing import Dict, Optional

class Portfolio:
    """
    Pure entity: manages positions (symbol -> Position).
    No I/O or use-case logic here; just domain rules and state updates.
    """

    def __init__(self) -> None:
        self.positions: Dict[str, Position] = {}

    def get_market_value(self, market_prices: Dict[str, float]) -> float:
        """
        Calculate total market value across all positions using provided prices.
        """
        total = 0.0
        for symbol, pos in self.positions.items():
            price = market_prices[symbol]
            if price is None:
                continue
            total += pos.market_value(price)
        return total

    def get_unrealized_pnl(self, market_prices: Dict[str, float]) -> float:
        """
        Calculate total unrealized P&L using provided prices.
        """
        total = 0.0
        for symbol, pos in self.positions.items():
            price = market_prices.get(symbol)
            if price is None:
                continue
            total += pos.unrealized_pnl(price)
        return total

    def add_position(self, position: Position) -> None:
        """Add an already-built Position aggregate to the portfolio."""
        if position.SYMBOL in self.positions:
            return
        self.positions[position.SYMBOL] = position

    def get_position(self, symbol: str) -> Optional[Position]:
        """Return position or None."""
        return self.positions.get(symbol)