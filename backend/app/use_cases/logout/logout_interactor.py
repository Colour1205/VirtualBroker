from .logout_input_boundary import LogoutInputBoundary
from .logout_output_boundary import LogoutOutputBoundary
from .logout_input_data import LogoutInputData
from .logout_output_data import LogoutOutputData
from .logout_data_access_interface import LogoutDataAccessInterface

class LogoutInteractor(LogoutInputBoundary):
	def __init__(self, presenter: LogoutOutputBoundary, data_access: LogoutDataAccessInterface):
		self.presenter = presenter
		self.data_access = data_access

	def execute(self, request: LogoutInputData) -> None:
		success = self.data_access.logout(request.user_id)
		message = "" if success else "Logout failed"
		self.presenter.present(LogoutOutputData(success=success, message=message))

