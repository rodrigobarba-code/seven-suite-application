class SessionInformation:
    def __init__(
        self,
        session_id: int,
        session_ip_address: str,
        session_mac_address: str,
        session_username: str,
        session_password: str,
        session_connection_type: str,
        session_brand: str,
        session_model: str,
        allow_remote_access: bool
    ) -> None:
        self.session_id = session_id
        self.session_ip_address = session_ip_address
        self.session_mac_address = session_mac_address
        self.session_username = session_username
        self.session_password = session_password
        self.session_connection_type = session_connection_type
        self.session_brand = session_brand
        self.session_model = session_model
        self.allow_remote_access = allow_remote_access

