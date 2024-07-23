class RouterEntity:
    def __init__(
            self,
            router_id,
            router_name,
            router_description,
            router_brand,
            router_model,
            fk_site_id,
            router_ip,
            router_mac,
            router_username,
            router_password,
            allow_scan
    ):
        self.router_id = router_id
        self.router_name = router_name
        self.router_description = router_description
        self.router_brand = router_brand
        self.router_model = router_model
        self.fk_site_id = fk_site_id
        self.router_ip = router_ip
        self.router_mac = router_mac
        self.router_username = router_username
        self.router_password = router_password
        self.allow_scan = allow_scan

    def validate(self):
        try:
            assert isinstance(self.router_id, int)
            assert isinstance(self.router_name, str)
            assert isinstance(self.router_description, str)
            assert isinstance(self.router_brand, str)
            assert isinstance(self.router_model, str)
            assert isinstance(self.fk_site_id, int)
            assert isinstance(self.router_ip, str)
            assert isinstance(self.router_mac, str)
            assert isinstance(self.router_username, str)
            assert isinstance(self.router_password, str)
            assert isinstance(self.allow_scan, bool)
        except AssertionError:
            raise ValueError('Invalid Router Entity')
