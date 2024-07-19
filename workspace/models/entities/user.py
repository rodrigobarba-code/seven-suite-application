class User:
    def __init__(
        self,
        user_id: int,
        user_username: str,
        user_password: str,
        user_name: str,
        user_lastname: str,
        user_privileges: str,
        user_state: str
    ) -> None:
        self.user_id = user_id
        self.user_username = user_username
        self.user_password = user_password
        self.user_name = user_name
        self.user_lastname = user_lastname
        self.user_privileges = user_privileges
        self.user_state = user_state