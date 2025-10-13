from pydactyl import PterodactylClient

class server():
    def __init__(self):
        self.api = PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH')
        self.server = self.api.client.servers.list_servers()
        self.server_id = self.server[0]['attributes']['identifier']
    def test(self, a: int):
        print("Test"*a)

    def start(self):
        self.api.client.servers.send_power_action(server_id=self.server_id, signal='start')
        return 'server started' 
    
    def stop(self):
        self.api.client.servers.send_power_action(server_id=self.server_id, signal='stop')
        return 'server stopped' 
    
    def reload(self):
        from time import sleep as s
        self.api.client.servers.send_power_action(server_id=self.server_id, signal='stop')
        for i in range(5):
            s(0.5)
            print(f"{i}...")
        self.api.client.servers.send_power_action(server_id=self.server_id, signal="start")
        return 'server restarted' 

    def get_data(self):
        self.server_util = self.api.client.servers.get_server_utilization(server_id=self.server_id)
        self.server_data = [
            self.server_util["current_state"],
            round(((int(self.server_util["resources"]["memory_bytes"])/1024)/1024)/1024, 2),
            self.server_util["resources"]["cpu_absolute"],
            round(((int(self.server_util["resources"]["disk_bytes"])/1024)/1024)/1024, 2),
            round(self.server_util["resources"]["uptime"]/1000, 2)
        ]
        self.sec = self.server_data[-1]
        def convert(secund):
            return [int(round((secund//3600), 0)), int(round(((secund%3600) // 60), 0)), int(round((secund % 60), 0))]
        self.server_data[-1] = convert(self.sec)

        return self.server_data


if __name__ == "__main__":
    test = server()
    print(test.stop())