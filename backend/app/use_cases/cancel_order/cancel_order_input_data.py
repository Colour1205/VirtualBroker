from dataclasses import dataclass

@dataclass(frozen=True)
class CancelOrderRequest:
    """Input data for canceling an order."""
    symbol: str
    order_id: str
    reason: str = ""