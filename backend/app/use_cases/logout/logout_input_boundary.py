from .logout_input_data import LogoutInputData

class LogoutInputBoundary:
	def execute(self, request: LogoutInputData) -> None:
		raise NotImplementedError

