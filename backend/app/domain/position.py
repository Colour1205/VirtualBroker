from typing import List

class Position:
    """stores the order / avg_price / current hold history of a stock
    
    === Representation Invariants ===
    SYMBOL must be fixed for a position
    """
    SYMBOL: str
    history: List[Order]
    book_cost: Money
    quantity: Quantity
    
    def __init__(self, symbol: str):
        self.SYMBOL = symbol
        self.history = []
        self.book_cost = Money(0)
        self.quantity = Quantity(0)

    def add(self, order: Order) -> bool:
        # if order is not filled, return
        if not order.filled():
            return False
        
        self.history.append(order)
        
        # check if order is sell or buy
        if order.order_side == OrderSide.BUY:
            self.quantity += order.quantity
            self.book_cost += order.amount
        else:
            self.quantity -= order.quantity
            self.book_cost -= order.amount

    def get_position_type(self) -> (str | None):
        """return whether this is a long position or short position

        return None if no position is opened
        """
        if self.quantity < 0:
            return "short"
        elif self.quantity > 0:
            return "long"
        else:
            return None

    def is_closed(self) -> bool:
        """method to check if the position is closed."""
        return self.quantity == 0

    def get_average_price(self) -> (Money | None):
        """Returns the average price of the position.
        
        If quantity is 0, returns None.
        """
        if self.quantity == 0:
            return None
        
        return self.book_cost / abs(self.quantity)

    def market_value(self, market_price: Money) -> (Money | None):
        if market_price:
            return self.quantity * market_price

    def unrealized_pnl(self, current_price: Money) -> Money:
        """
        Calculate unrealized P&L as (current market value - book cost)
        """
        if self.is_closed():
            return Money(0)

        return self.quantity * current_price - self.book_cost