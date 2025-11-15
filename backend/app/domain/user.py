class User:
    """the user class. For simplicity purposes, all child classes of User can only override methods but not adding methods
    """
    def __init__(self):
        self.user_id = Id.generate()
        self.positions = {}
        self.balance = 0