import time
import uuid

class Id:
    """
    id class generates a random and unique id 
    """
    @staticmethod
    def generate(self) -> Id:
        timestamp = int(time.time() * 1000)
        random_part = uuid.uuid4().hex[:6]
        return f"{timestamp}-{random_part}"
