class IPAddressesConfiguration:
    def __init__(
        self,
        ip_address_id: int,
        fk_ip_address_interface: int,
        ip_address_alias: str,
        ip_address_state: str,
        ip_address: str,
        ip_address_netmask: str,
        ip_address_network: str,
        ip_address_gateway: str
    ) -> None:
        self.ip_address_id = ip_address_id
        self.fk_ip_address_interface = fk_ip_address_interface
        self.ip_address_alias = ip_address_alias
        self.ip_address_state = ip_address_state
        self.ip_address = ip_address
        self.ip_address_netmask = ip_address_netmask
        self.ip_address_network = ip_address_network
        self.ip_address_gateway = ip_address_gateway
