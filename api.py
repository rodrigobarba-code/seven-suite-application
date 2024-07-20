# Import the RouterOS API
import ros_api
# Import the RouterOS API


# Class to handle the RouterOS API
class RouterOSAPI:
    # Variables
    router = None
    credentials = None
    # Variables

    # Constructor
    def __init__(self, host, user, password):
        self.credentials = {
            'host': host,
            'user': user,
            'password': password
        }
    # Constructor

    # Getters and Setters
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
            port=7372,
            use_ssl=True
        )
    # Getters and Setters

    # Method to retrieve data from the RouterOS
    def retrieve_data(self, command):
        self.set_api()
        return self.router.talk(command)
    # Method to retrieve data from the RouterOS
# Class to handle the RouterOS API


# Main method
"""
if __name__ == '__main__':
    router = RouterOSAPI('10.1.3.254', '', '')
    print(router.retrieve_data('/ip/arp/print'))
"""
# Main method