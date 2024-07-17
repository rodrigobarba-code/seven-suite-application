class Router:
    def __init__(
        self,
        router_id: int,
        router_name: str,
        router_description: str,
        fk_site_id: int,
        fk_session_id: int
    ) -> None:
        self.router_id = router_id
        self.router_name = router_name
        self.router_description = router_description
        self.fk_site_id = fk_site_id
        self.fk_session_id = fk_session_id
