class CancelOrderOutputBoundary:
    """Use-case output boundary for canceling an order."""

    def present(self, output_data: CancelOrderOutputData) -> None:
        """Present the result of the cancel order use-case."""
        raise NotImplementedError
