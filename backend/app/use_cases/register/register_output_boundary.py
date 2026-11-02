from .register_output_data import RegisterOutputData

class RegisterOutputBoundary:
	def present(self, output_data: RegisterOutputData) -> None:
		raise NotImplementedError

