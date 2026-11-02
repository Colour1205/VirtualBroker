from dataclasses import dataclass

@dataclass(frozen=True)
class RegisterInputData:
	username: str
	password: str

