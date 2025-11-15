# value_objects/order_side.py
from enum import Enum

class OrderSide(str, Enum):
    BUY = "buy"
    SELL = "sell"

    def opposite(self) -> "OrderSide":
        """Return the opposite side (buy <-> sell)."""
        return OrderSide.SELL if self == OrderSide.BUY else OrderSide.BUY
