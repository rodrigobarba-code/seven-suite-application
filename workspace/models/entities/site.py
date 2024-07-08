class Site:
    def __init__(
        self,
        site_id: int,
        fk_region_id: int,
        site_name: str,
        site_segment: int
    ) -> None:
        self.site_id = site_id
        self.fk_region_id = fk_region_id
        self.site_name = site_name
        self.site_segment = site_segment
