from .cancel_order_output_data import CancelOrderOutputData

class CancelOrderOutputBoundary:
    def present(self, output_data: CancelOrderOutputData) -> None:
        raise NotImplementedError
