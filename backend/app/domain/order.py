from __future__ import annotations

from value_objects.quantity import Quantity
from value_objects.order_type import OrderType
from value_objects.order_side import OrderSide
from value_objects.order_status import OrderStatus
from value_objects.id import Id
from value_objects.id import Time

class Order:
    """
    Order class stores the different attributes of an order
    """
    _order_id: Id
    _user_id: Id
    _symbol: str
    _order_type: OrderType
    _quantity: Quantity
    _time: Time

    def __init__(self, Id, user_id: Id, symbol: str, order_side: OrderSide, order_type: OrderType, quantity: float):
        self._order_id = Id.generate()
        self._user_id = user_id
        self._symbol = symbol
        self._quantity = quantity
        self._order_side = order_side
        self._order_type = order_type
        self._time = Time.now()

    @property
    def order_id(self) -> "Id":
        return self._order_id

    @property
    def user_id(self) -> "Id":
        return self._user_id

    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def order_side(self) -> "OrderSide":
        return self._order_side

    @property
    def order_type(self) -> "OrderType":
        return self._order_type

    @property
    def time(self) -> "Time":
        return self._time

    @property
    def quantity(self) -> "Quantity":
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity: "Quantity") -> None:
        if new_quantity <= 0:
            raise ValueError("Quantity must be positive")
        self._quantity = new_quantity
        self._time = Time.now()  # optionally update time when quantity changes

    def update_time(self) -> None:
        """Manually update the order time (optional)."""
        self._time = Time.now()

    def get_id(self) -> "Id":
        return self._order_id


class OrderBuilder:

    def __init__(self):
        self._user_id = None
        self._symbol = None
        self._order_type = None
        self._order_side = None
        self._quantity = None

    def user_id(self, user_id: str) -> OrderBuilder:
        self._user_id = user_id
        return self
    
    def symbol(self, symbol: str) -> OrderBuilder:
        self._symbol = symbol
        return self

    def order_type(self, order_type: OrderType) -> OrderBuilder:
        self._order_type = order_type
        return self

    def order_side(self, order_side: OrderSide) -> OrderBuilder:
        self._order_side = order_side
        return self
    
    def quantity(self, quantity: Quantity | float) -> OrderBuilder:
        if isinstance(quantity, float):
            self._quantity = Quantity(quantity)
        else:
            self._quantity = quantity
        return self
    
    def build(self) -> Order:
        return Order(self._id, self._user_id, self._symbol, self._order_side, self._order_type, self._quantity)