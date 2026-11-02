from dataclasses import dataclass

@dataclass(frozen=True)
class CancelOrderInputData:
    """Input data for canceling an order."""
    symbol: str
    user_id: str
    order_id: str
    reason: str = ""