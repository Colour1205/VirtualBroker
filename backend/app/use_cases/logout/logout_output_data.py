from dataclasses import dataclass

@dataclass(frozen=True)
class LogoutOutputData:
	success: bool
	message: str = ""

