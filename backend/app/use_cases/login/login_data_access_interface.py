from typing import Optional

class LoginDataAccessInterface:
	def authenticate(self, username: str, password: str) -> Optional[str]:
		raise NotImplementedError

