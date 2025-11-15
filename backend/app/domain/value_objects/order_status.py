from enum import Enum

class OrderStatus(str, Enum):
    NEW = "new"
    PARTIAL = "partial"
    FILLED = "filled"
    CANCELLED = "cancelled"

    def is_final(self) -> bool:
        """Return True if order is in a final state (cannot be modified)."""
        return self in (OrderStatus.FILLED, OrderStatus.CANCELLED)

    def can_fill(self) -> bool:
        """Return True if order can still be filled."""
        return self in (OrderStatus.NEW, OrderStatus.PARTIAL)