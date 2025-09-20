def get_data():

    from pydactyl import PterodactylClient

    api = PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH')

    server = api.client.servers.list_servers()

    server_id = server[0]['attributes']['identifier']

    srv_utilization = api.client.servers.get_server_utilization(server_id)
    return srv_utilization