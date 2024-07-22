class Router:
    def __init__(
        self,
        router_id: str,
        router_name: str,
        router_description: str,
        router_brand: str,
        router_model: str,
        fk_site_id: int,
        fk_session_id: int
    ) -> None:
        self.router_id = router_id
        self.router_name = router_name
        self.router_description = router_description
        self.router_brand = router_brand
        self.router_model = router_model
        self.fk_site_id = fk_site_id
        self.fk_session_id = fk_session_id
