class UserEntity:
    def __init__(self, user_id, user_username, user_password, user_name, user_lastname, user_privileges, user_state):
        self.user_id = user_id
        self.user_username = user_username
        self.user_password = user_password
        self.user_name = user_name
        self.user_lastname = user_lastname
        self.user_privileges = user_privileges
        self.user_state = user_state

    def validate(self):
        try:
            assert self.user_id is not None
            assert self.user_username is not None
            assert self.user_password is not None
            assert self.user_name is not None
            assert self.user_lastname is not None
            assert self.user_privileges is not None
            assert self.user_state is not None
        except AssertionError:
            raise ValueError('Invalid User Entity')
