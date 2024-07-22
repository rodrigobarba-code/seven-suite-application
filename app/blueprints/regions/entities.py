class RegionEntity:
    def __init__(self, region_id, region_name):
        self.region_id = region_id
        self.region_name = region_name

    def validate(self):
        try:
            assert isinstance(self.region_id, int)
            assert isinstance(self.region_name, str)
        except AssertionError:
            raise ValueError('Invalid Region Entity')
