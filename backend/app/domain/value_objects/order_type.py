from enum import Enum

class OrderType(str, Enum):
    MARKET = "market"
    LIMIT = "limit"
    STOP = "stop"
    STOP_LIMIT = "stop_limit"

    def is_price_required(self) -> bool:
        """Return True if the order type requires a price."""
        return self in (OrderType.LIMIT, OrderType.STOP_LIMIT)

    def is_market_order(self) -> bool:
        return self == OrderType.MARKET