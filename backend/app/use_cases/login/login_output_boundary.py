from .login_output_data import LoginOutputData

class LoginOutputBoundary:
	def present(self, output_data: LoginOutputData) -> None:
		raise NotImplementedError

