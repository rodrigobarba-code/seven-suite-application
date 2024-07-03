class Interface:
    def __init__(
        self,
        interface_id: int,
        fk_router_id: int,
        interface_state: bool,
        interface_name: str,
        interface_type: str,
        interface_mtu: float
    ) -> None:
        self.interface_id = interface_id
        self.fk_router_id = fk_router_id
        self.interface_state = interface_state
        self.interface_name = interface_name
        self.interface_type = interface_type
        self.interface_mtu = interface_mtu
