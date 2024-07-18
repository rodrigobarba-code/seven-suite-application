class ARPList:
    def __init__(
        self,
        arp_id: int,
        fk_router_id: int,
        arp_state: str,
        arp_ip: str,
        arp_mac: str,
        arp_interface: str,
        arp_netbios: str,
        arp_set_date: str
    ) -> None:
        self.arp_id = arp_id
        self.fk_router_id = fk_router_id
        self.arp_state = arp_state
        self.arp_ip = arp_ip
        self.arp_mac = arp_mac
        self.arp_interface = arp_interface
        self.arp_netbios = arp_netbios
        self.arp_set_date = arp_set_date
