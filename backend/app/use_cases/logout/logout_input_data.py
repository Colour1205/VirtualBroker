from dataclasses import dataclass

@dataclass(frozen=True)
class LogoutInputData:
	user_id: str

