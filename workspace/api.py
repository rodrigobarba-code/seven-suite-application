import ros_api


class RouterOSAPI:
    router = None
    credentials = None

    def __init__(self, host, user, password):
        self.credentials = {
            'host': host,
            'user': user,
            'password': password
        }

    def get_credentials(self):
        return self.credentials

    def set_credentials(self, host=None, user=None, password=None):
        self.credentials = {
            'host': host,
            'user': user,
            'password': password
        }

    def get_api(self):
        return self.router

    def set_api(self):
        self.router = ros_api.Api(
            self.credentials['host'],
            self.credentials['user'],
            self.credentials['password'],
            port=7371,
            use_ssl=True
        )

    def retrieve_data(self, command):
        self.set_api()
        return self.router.talk(command)


if __name__ == '__main__':
    router = RouterOSAPI('10.1.3.254', 'AccesoN0C', 'N0c#2024.@!!')
    print(router.retrieve_data('/ip/address/print'))
