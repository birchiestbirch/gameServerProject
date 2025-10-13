def get_data():

    from pydactyl import PterodactylClient

    api = PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH')

    server = api.client.servers.list_servers()

    server_id = server[0]['attributes']['identifier']

    srv_utilization = api.client.servers.get_server_utilization(server_id)
    # Структура возвращаемого массива [Состояние сервера, занятая ОЗУ, забитость процессора, занятость диска, сколько сервер включен]
    serv_data = [
            srv_utilization["current_state"], 
            round(((int(srv_utilization["resources"]["memory_bytes"])/1024)/1024)/1024, 2), 
            srv_utilization["resources"]["cpu_absolute"], 
            round(((int(srv_utilization["resources"]["disk_bytes"])/1024)/1024)/1024, 2), 
            round(srv_utilization["resources"]["uptime"]/1000, 2)
            ]
    secund = serv_data[-1]
    def convert(sec):
        return [int(round((sec//3600), 0)), int(round(((sec%3600) // 60), 0)), int(round((sec % 60), 0))]
    serv_data[-1] = convert(secund)

    return serv_data