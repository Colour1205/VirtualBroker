from .register_input_boundary import RegisterInputBoundary
from .register_output_boundary import RegisterOutputBoundary
from .register_input_data import RegisterInputData
from .register_output_data import RegisterOutputData
from .register_data_access_interface import RegisterDataAccessInterface

class RegisterInteractor(RegisterInputBoundary):
	def __init__(self, presenter: RegisterOutputBoundary, data_access: RegisterDataAccessInterface):
		self.presenter = presenter
		self.data_access = data_access

	def execute(self, request: RegisterInputData) -> None:
		if self.data_access.is_username_taken(request.username):
			self.presenter.present(RegisterOutputData(user_id=None, success=False, message="Username already taken"))
			return
		user_id = self.data_access.create_user(request.username, request.password)
		self.presenter.present(RegisterOutputData(user_id=user_id, success=True, message=""))

