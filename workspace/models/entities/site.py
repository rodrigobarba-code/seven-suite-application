class Site:
    def __init__(
        self,
        site_id: int,
        fk_region_id: int,
        site_name: str
    ) -> None:
        self.site_id = site_id
        self.fk_region_id = fk_region_id
        self.site_name = site_name
