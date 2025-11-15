from domain.value_objects.order_status import OrderStatus

class CancelORderInteractor(CancelOrderInputBoundary):
    def __init__(self, presenter: CancelOrderOutputBoundary, data_access: CancelOrderDataAccessInterface):
        self.presenter = presenter
        self.data_access = data_access

    def execute(self, request: CancelOrderInputData) -> None:
        portfolio = self.data_access.load_portfolio(request.user_id)
        position = portfolio[request.symbol]
        order = position[request.order_id]
        order.set_status(OrderStatus.CANCELLED)

        