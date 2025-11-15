import time

class Time:
    def __init__(self, timestamp: float):
        self._time = timestamp

    @staticmethod
    def now() -> "Time":
        """Return a Time object representing the current time in nanoseconds."""
        return Time(time.time_ns())

    def get(self) -> float:
        """Get the internal timestamp."""
        return self._time

    def __str__(self) -> str:
        return str(self._time)

    def __repr__(self) -> str:
        return f"Time({self._time})"
