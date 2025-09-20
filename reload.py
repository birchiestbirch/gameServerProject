def reload():
    from pydactyl import PterodactylClient
    from time import sleep

    api = PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH')

    server = api.client.servers.list_servers()

    server_id = server[0]['attributes']['identifier']

    api.client.servers.send_power_action(server_id, 'stop')
    
    sleep(5)

    api.client.servers.send_power_action(server_id, 'start')

    return "Сервер рестартует"