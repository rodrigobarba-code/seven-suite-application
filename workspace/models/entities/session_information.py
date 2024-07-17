class SessionInformation:
    def __init__(
        self,
        session_id: int,
        session_ip: str,
        session_mac: str,
        session_username: str,
        session_password: str,
        session_via: str,
        api_port: int,
        api_port_ssl: int,
        allow_scan: bool
    ) -> None:
        self.session_id = session_id
        self.session_ip = session_ip
        self.session_mac = session_mac
        self.session_username = session_username
        self.session_password = session_password
        self.session_via = session_via
        self.api_port = api_port
        self.api_port_ssl = api_port_ssl
        self.allow_scan = allow_scan

