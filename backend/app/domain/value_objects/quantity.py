class Quantity:
    def __init__(self, amount: int | float):
        self._amount = float(amount)  # store internally as float

    def value(self) -> float:
        """TODO: Return quantity for display (rounded to nearest integer for now)."""
        return round(self._amount, 0)

    # ---------------- Arithmetic ----------------
    def _to_number(self, other: "Quantity" | int | float) -> float:
        if isinstance(other, Quantity):
            return other._amount
        return float(other)

    def __add__(self, other: "Quantity" | int | float) -> "Quantity":
        return Quantity(self._amount + self._to_number(other))

    def __radd__(self, other: int | float) -> "Quantity":
        return self + other

    def __sub__(self, other: "Quantity" | int | float) -> "Quantity":
        return Quantity(self._amount - self._to_number(other))

    def __rsub__(self, other: int | float) -> "Quantity":
        return Quantity(self._to_number(other) - self._amount)

    def __mul__(self, other: int | float) -> "Quantity":
        return Quantity(self._amount * float(other))

    def __rmul__(self, other: int | float) -> "Quantity":
        return self * other

    def __truediv__(self, other: int | float) -> "Quantity":
        return Quantity(self._amount / float(other))

    def __abs__(self) -> "Quantity":
        return Quantity(abs(self._amount))


    # ---------------- Comparisons ----------------
    def __eq__(self, other: "Quantity" | int | float) -> bool:
        return self._amount == self._to_number(other)

    def __lt__(self, other: "Quantity" | int | float) -> bool:
        return self._amount < self._to_number(other)

    def __le__(self, other: "Quantity" | int | float) -> bool:
        return self._amount <= self._to_number(other)

    def __gt__(self, other: "Quantity" | int | float) -> bool:
        return self._amount > self._to_number(other)

    def __ge__(self, other: "Quantity" | int | float) -> bool:
        return self._amount >= self._to_number(other)

    # ---------------- Representation ----------------
    def __str__(self):
        return f"{self.value():.2f}"

    def __repr__(self):
        return f"Quantity({self._amount})"
