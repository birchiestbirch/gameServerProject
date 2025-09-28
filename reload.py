def reload():

    """
    Функция для перезапуска сервера
    """

    from pydactyl import PterodactylClient # Импортируем библиотеку
    from time import sleep # из модуля time дёргаем функцию sleep, что бы не перегружать сервер командами

    api = PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH') 
    # Получаем доступ к серверу
    server = api.client.servers.list_servers()

    server_id = server[0]['attributes']['identifier']

    api.client.servers.send_power_action(server_id, 'stop') # Выключаем сервер
    
    sleep(5) # Немного ждём

    api.client.servers.send_power_action(server_id, 'start') # Запускаем сервер снова

    return "Сервер рестартует" # Возвращаем информацию о том, что сервер перезапускается