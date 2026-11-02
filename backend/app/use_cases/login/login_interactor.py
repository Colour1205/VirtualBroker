from .login_input_boundary import LoginInputBoundary
from .login_output_boundary import LoginOutputBoundary
from .login_input_data import LoginInputData
from .login_output_data import LoginOutputData
from .login_data_access_interface import LoginDataAccessInterface

class LoginInteractor(LoginInputBoundary):
	def __init__(self, presenter: LoginOutputBoundary, data_access: LoginDataAccessInterface):
		self.presenter = presenter
		self.data_access = data_access

	def execute(self, request: LoginInputData) -> None:
		user_id = self.data_access.authenticate(request.username, request.password)
		if user_id:
			self.presenter.present(LoginOutputData(user_id=user_id, success=True, message=""))
		else:
			self.presenter.present(LoginOutputData(user_id=None, success=False, message="Invalid credentials"))

