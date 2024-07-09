class Router:
    def __init__(
        self,
        router_id: str,
        router_name: str,
        fk_site_id: int,
        fk_session_id: int,
        fk_ip_address_id: int
    ) -> None:
        self.router_id = router_id
        self.router_name = router_name
        self.fk_site_id = fk_site_id
        self.fk_session_id = fk_session_id
        self.fk_ip_address_id = fk_ip_address_id
