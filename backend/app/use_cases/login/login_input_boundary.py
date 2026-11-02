from .login_input_data import LoginInputData

class LoginInputBoundary:
	def execute(self, request: LoginInputData) -> None:
		raise NotImplementedError

