class SessionPort:
    def __init__(
        self,
        session_port_id: int,
        fk_session_id: int,
        port_number: int,
        port_status: bool,
        port_protocol: str
    ) -> None:
        self.session_port_id = session_port_id
        self.fk_session_id = fk_session_id
        self.port_number = port_number
        self.port_status = port_status
        self.port_protocol = port_protocol
