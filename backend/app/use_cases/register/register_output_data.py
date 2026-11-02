from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class RegisterOutputData:
	user_id: Optional[str]
	success: bool
	message: str = ""

