from domain.value_objects.order_status import OrderStatus
from .cancel_order_input_boundary import CancelOrderInputBoundary
from .cancel_order_output_boundary import CancelOrderOutputBoundary
from .cancel_order_data_access_interface import CancelOrderDataAccessInterface
from .cancel_order_input_data import CancelOrderInputData

class CancelOrderInteractor(CancelOrderInputBoundary):
    def __init__(self, presenter: CancelOrderOutputBoundary, data_access: CancelOrderDataAccessInterface):
        self.presenter = presenter
        self.data_access = data_access

    def execute(self, request: CancelOrderInputData) -> None:
        portfolio = self.data_access.load_portfolio(request.user_id)
        position = portfolio[request.symbol]
        order = position[request.order_id]
        order.set_status(OrderStatus.CANCELLED)

        