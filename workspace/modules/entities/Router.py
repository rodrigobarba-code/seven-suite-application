class Router:
    def __init__(
        self,
        ip_address: str,
        username: str,
        password: str,
        ports: list,
        connection_via: str,
        ip_addresses: list = []
    ):
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.ports = ports
        self.connection_via = connection_via
        self.ip_addresses = ip_addresses

    def __repr__(self):
        return f'Router({self.ip_address}, {self.username}, {self.password}, {self.ports}, {self.connection_via}, {self.ip_addresses})'
