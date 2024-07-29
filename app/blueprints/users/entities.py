class UserEntity:
    def __init__(
            self,
            user_id,
            user_username,
            user_password,
            user_name,
            user_lastname,
            user_privileges,
            user_state
    ):
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


class UserLogEntity:
    def __init__(
            self,
            user_log_id,
            fk_user_id,
            user_log_description,
            user_log_action,
            user_log_table,
            user_log_date,
            user_log_public_ip,
            user_log_local_ip
    ):
        self.user_log_id = user_log_id
        self.fk_user_id = fk_user_id
        self.user_log_description = user_log_description
        self.user_log_action = user_log_action
        self.user_log_table = user_log_table
        self.user_log_date = user_log_date
        self.user_log_public_ip = user_log_public_ip
        self.user_log_local_ip = user_log_local_ip

    def validate(self):
        try:
            assert self.user_log_id is not None
            assert self.fk_user_id is not None
            assert self.user_log_description is not None
            assert self.user_log_action is not None
            assert self.user_log_table is not None
            assert self.user_log_date is not None
            assert self.user_log_public_ip is not None
            assert self.user_log_local_ip is not None
        except AssertionError:
            raise ValueError('Invalid User Log Entity')
