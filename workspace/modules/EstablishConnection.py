from workspace.modules.entities.Router import Router

import paramiko as p
import json as j


class EstablishConnection:
    def read_settings(self, json_file):
        print('Reading settings...')
        with open(json_file, 'r') as file:
            data = j.load(file)
            router = Router(
                data['session_information']['ip_address'],
                data['session_information']['username'],
                data['session_information']['password'],
                [[port, data['session_information']['ports'][port]] for port in data['session_information']['ports']],
                data['session_information']['connection_via']
            )
        file.close()
        return self.get_router_data(router)

    @staticmethod
    def get_port_via_connection(router, connection_via):
        return router.ports[0][1] if connection_via == 'ssh' else router.ports[1][1] if connection_via == 'api' else \
            router.ports[2][1]

    def get_router_data(self, router):
        port = self.get_port_via_connection(router, router.connection_via)

        print('Connecting to router...')
        ssh = p.SSHClient()
        ssh.set_missing_host_key_policy(p.AutoAddPolicy())
        ssh.connect(
            router.ip_address,
            port,
            router.username,
            router.password)

        print('Connected to router')
        return ssh

    def connect(self, router_file):
        return self.read_settings(router_file)
