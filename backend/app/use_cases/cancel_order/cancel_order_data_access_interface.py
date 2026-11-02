from domain.portfolio import Portfolio

class CancelOrderDataAccessInterface:
    def load_portfolio(self, user_id: str) -> Portfolio:
        raise NotImplementedError

    def save_portfolio(self, portfolio: Portfolio) -> None:
        raise NotImplementedError