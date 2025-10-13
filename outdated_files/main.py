from pydactyl import PterodactylClient # Импортируем из модуля PyDactyl клиент Pterodactyl
from outdated_files.start import start
from outdated_files.stop import stop
from outdated_files.get_data import get_data
from outdated_files.reload import reload

# Импортируем нужные функции из модулей

api = PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH') # Дёргаем данные сервера и АПИ-ключ с сайта, где арендован сервер

server = api.client.servers.list_servers() # Эта строка отвечает за записывание всех арендованных серверов и их данных в один массив

server_id = server[0]['attributes']['identifier'] # Берём из списка арендованных серверов первый (нулевой если угодно) сервер

srv_utilization = api.client.servers.get_server_utilization(server_id) # Получаем все аттрибуты сервера

choice = input("1 - Включить сервер\n2 - Выключить сервер\n3 - Получить данные о сервере\n4 - Перезапуск сервера\n") # Получаем этот самый выбор

def choice_action(choice: int): # Функция, принимающая на вход числовое значение для выбора действия

    if choice == "1": # Если выбрано 1, то включить сервер
        print(start())
        choice = input("1 - Включить сервер\n2 - Выключить сервер\n3 - Получить данные о сервере\n4 - Перезапуск сервера\n")
        choice_action(choice)
    elif choice == "2": # Если выбрано 2, то выключить сервер
        print(stop())
        choice = input("1 - Включить сервер\n2 - Выключить сервер\n3 - Получить данные о сервере\n4 - Перезапуск сервера\n")
        choice_action(choice)
    elif choice == "3": # Если выбрано 3, то получаем информацию о сервере
        data = get_data()
        print(f"Сервер: {data[0]}, Память: {data[1]}, Процессор: {data[2]}, Диск: {data[3]}, Время работы: {data[4]}")
        choice = input("1 - Включить сервер\n2 - Выключить сервер\n3 - Получить данные о сервере\n4 - Перезапуск сервера\n")
        choice_action(choice)
    elif choice == "4": # Если выбрано 4, то сервер перезапускается
        print(reload())
        choice = input("1 - Включить сервер\n2 - Выключить сервер\n3 - Получить данные о сервере\n4 - Перезапуск сервера\n")
        choice_action(choice)

choice_action(choice) # Запускаем, для выхода пишем в консоль exit()
