def get_data():

    from pydactyl import PterodactylClient

    api = PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH')

    server = api.client.servers.list_servers()

    server_id = server[0]['attributes']['identifier']

    srv_utilization = api.client.servers.get_server_utilization(server_id)
    # Структура возвращаемого массива [Состояние сервера, занятая ОЗУ, забитость процессора, занятость диска, сколько сервер включен]
    return [
            srv_utilization["current_state"], 
            round(((int(srv_utilization["resources"]["memory_bytes"])/1024)/1024)/1024, 2), 
            srv_utilization["resources"]["cpu_absolute"], 
            round(((int(srv_utilization["resources"]["disk_bytes"])/1024)/1024)/1024, 2), 
            srv_utilization["resources"]["uptime"]
            ]