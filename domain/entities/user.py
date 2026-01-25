class User:
    def __init__(self, user_id: int = None, username: str = None, email: str = None, password_hash: str = None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        
        self.practice_sessions = []
        self.configuration = None
