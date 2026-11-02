from .register_input_data import RegisterInputData

class RegisterInputBoundary:
	def execute(self, request: RegisterInputData) -> None:
		raise NotImplementedError

