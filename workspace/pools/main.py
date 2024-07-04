from workspace.pools.modules.EstablishConnection import EstablishConnection
from workspace.pools.modules.ReadAvailableRouters import ReadAvailableRouters


def main():
    # Read available routers.
    available_routers = ReadAvailableRouters()
    available_routers.read()
    router_list = available_routers.get_available_routers()

    # Establish connection for each router.
    for router in router_list:
        try:
            ssh = EstablishConnection().connect("routers/sections/" + router + ".json")
            stdin, stdout, stderr = ssh.exec_command('ip address print')
            print(stdout.read().decode())
            ssh.close()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
