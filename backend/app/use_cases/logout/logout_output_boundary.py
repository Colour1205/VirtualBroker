from .logout_output_data import LogoutOutputData

class LogoutOutputBoundary:
	def present(self, output_data: LogoutOutputData) -> None:
		raise NotImplementedError

