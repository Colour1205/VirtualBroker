from dataclasses import dataclass

@dataclass(frozen=True)
class CancelOrderOutputData:
    """Output data returned after attempting to cancel an order."""
    order_id: str
    success: bool
    message: str = ""