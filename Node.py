from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy
from datetime import datetime


class Node:
    def __init__(self, id, time, network):
        self.id = id
        self.time = time
        self.network = network
        self.successor = None # Nó sucessor no anel
        self.previous = None  # Nó anterior no anel
        self.type = 0 # 1 para coordenador, 0 para nó comum  

    def set_type(self, type_value):
        self.type = type_value

    def set_time(self, time_value):
        self.time = time_value    

    def send_message(self, origin=None):
        if origin is None:
            origin = self.id  # Define o nó atual como o originador
        message = (self.time.timestamp(), self.id, origin)
        print(f"Nó de ID:{self.id} : Enviando mensagem com hora {self.time} e origem {origin}")
        try:
            with ServerProxy(self.successor) as proxy:
                proxy.receive_message(message)
        except Exception as e:
            print(f"Erro ao enviar mensagem para {self.successor}: {e}")

    
    def receive_message(self, message):
        print(f"Nó de ID:{self.id} : Recebeu mensagem {message}")
        self.process_message(message)


    def process_message(self, message):
        print(f"Nó de ID:{self.id} : Processando a mensagem {message}")
        if message[2] == self.id: #verifica se o nó atual é a origin: caso for, o seu antecessor será o nó de maior Id e será definido como coordenador
            print(f"Nó de ID:{self.id} : Delegando coordenação ao nó anterior.")
            node_address = f"http://localhost:{8000 + len(self.network.nodes)}/RPC2"
            with ServerProxy(node_address) as previous_proxy:
                previous_proxy.set_type(1)  # Define o tipo como coordenador
            print(f"Nó de ID anterior ({self.previous.id}) : Agora é o coordenador.")
        
            # Calcula o tempo médio
            total_time = sum(node.time.timestamp() for node in self.network.nodes)
            avg_time = datetime.fromtimestamp(total_time / len(self.network.nodes))
        
            # Atualiza o tempo em todos os nós
            for node in self.network.nodes:
                node_address = f"http://localhost:{8000 + node.id}/RPC2"
                with ServerProxy(node_address) as node_proxy:
                    node_proxy.set_time(avg_time)
                    print(f"Nó de ID:{node.id} atualizado para o tempo médio: {avg_time}")
        else:
            print(f"Nó de ID:{self.id} : Passando mensagem para o próximo nó.")
            self.send_message(origin=message[2])
