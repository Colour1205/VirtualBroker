from dataclasses import dataclass

@dataclass(frozen=True)
class LoginInputData:
	username: str
	password: str

