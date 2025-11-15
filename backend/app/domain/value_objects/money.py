from decimal import Decimal, ROUND_DOWN

Number = int | float | Decimal

class Money:
    def __init__(self, amount: Number):
        self._amount = Decimal(str(amount))

    def amount(self) -> float:
        """Return the amount rounded to 2 decimal places for display."""
        return float(self._amount.quantize(Decimal("0.01"), rounding=ROUND_DOWN))

    # ------------------ Arithmetic ------------------
    def _to_decimal(self, other: "Money" | Number) -> Decimal:
        if isinstance(other, Money):
            return other._amount
        return Decimal(str(other))

    def __add__(self, other: "Money" | Number) -> "Money":
        return Money(self._amount + self._to_decimal(other))

    def __radd__(self, other: Number) -> "Money":
        return self + other

    def __sub__(self, other: "Money" | Number) -> "Money":
        return Money(self._amount - self._to_decimal(other))

    def __rsub__(self, other: Number) -> "Money":
        return Money(self._to_decimal(other) - self._amount)

    def __mul__(self, other: Number) -> "Money":
        return Money(self._amount * Decimal(str(other)))

    def __rmul__(self, other: Number) -> "Money":
        return self * other

    def __truediv__(self, other: Number | "Quantity") -> "Money":
        """Divide Money by a number or Quantity. Returns Money per unit."""
        if hasattr(other, "value"):  # simple duck typing for Quantity
            divisor = Decimal(str(other.value()))
        else:
            divisor = Decimal(str(other))
        return Money(self._amount / divisor)

    # ------------------ Comparisons ------------------
    def __eq__(self, other: "Money" | Number) -> bool:
        return self._amount == self._to_decimal(other)

    def __lt__(self, other: "Money" | Number) -> bool:
        return self._amount < self._to_decimal(other)

    def __le__(self, other: "Money" | Number) -> bool:
        return self._amount <= self._to_decimal(other)

    def __gt__(self, other: "Money" | Number) -> bool:
        return self._amount > self._to_decimal(other)

    def __ge__(self, other: "Money" | Number) -> bool:
        return self._amount >= self._to_decimal(other)

    # ------------------ Representation ------------------
    def __str__(self):
        return f"{self.amount():.2f}"

    def __repr__(self):
        return f"Money({str(self._amount)})"

    # Optional: negate operator
    def __neg__(self) -> "Money":
        return Money(-self._amount)
