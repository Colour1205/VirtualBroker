from backend.app.use_cases.cancel_order.cancel_order_input_data import CancelOrderInputData


class CancelOrderInputBoundary:
    def execute(self, request: CancelOrderInputData) -> None:
        """Process the cancellation of an order."""
        raise NotImplementedError