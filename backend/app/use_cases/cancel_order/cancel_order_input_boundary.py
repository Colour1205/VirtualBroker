from .cancel_order_input_data import CancelOrderInputData

class CancelOrderInputBoundary:
    def execute(self, request: CancelOrderInputData) -> None:
        raise NotImplementedError