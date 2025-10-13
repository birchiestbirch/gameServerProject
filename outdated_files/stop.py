def stop():

    """
    Функция для отключения сервера
    """

    from pydactyl import PterodactylClient

    api = PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH')

    server = api.client.servers.list_servers()

    server_id = server[0]['attributes']['identifier']

    api.client.servers.send_power_action(server_id, 'stop')

    return "Сервер останавливается"