class RegisterDataAccessInterface:
	def is_username_taken(self, username: str) -> bool:
		raise NotImplementedError

	def create_user(self, username: str, password: str) -> str:
		raise NotImplementedError

