class IPAddress:
    def __init__(
        self,
        address_id: int,
        fk_router_id: int,
        address_alias: str,
        address_state: str,
        address_ip: str,
        address_netmask: str,
        address_interface: str,
        address_network: str
    ) -> None:
        self.address_id = address_id
        self.fk_router_id = fk_router_id
        self.address_alias = address_alias
        self.address_state = address_state
        self.address_ip = address_ip
        self.address_netmask = address_netmask
        self.address_interface = address_interface
        self.address_network = address_network
