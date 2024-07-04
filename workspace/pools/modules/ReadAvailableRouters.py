import json as j


class ReadAvailableRouters:
    def __init__(self):
        self.available_routers = []

    def read(self):
        try:
            print("Reading available routers...")
            with open('routers/routers.json', 'r') as file:
                data = j.load(file)
                self.available_routers = data['available_routers']
            file.close()
        except Exception as e:
            print(e)

    def get_available_routers(self):
        return self.available_routers