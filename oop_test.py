from pydactyl import PterodactylClient

class server():
    def __init__(self):
        self.api = PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH')
        self.server = self.api.client.servers.list_servers()
        self.server_id = self.server[0]['attributes']['identifier']
        self.server_util = self.api.client.servers.get_server_utilization(server_id=self.server_id)
        