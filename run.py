from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import threading
from Network import Network
from Node import Node
import datetime
import random
import time
from datetime import timedelta


# Classe para manipular requisições XML-RPC
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Inicializa a rede
network = Network()

def start_client_server(node, port):
    node_server = SimpleXMLRPCServer(("localhost", port), requestHandler=RequestHandler, allow_none=True, logRequests=True)
    node_server.register_instance(node)
    node_server.register_function(node.send_message, "send_message")
    node_server.register_function(node.receive_message, "receive_message")
    node_server.register_function(node.process_message, "process_message")
    print(f"Servidor iniciado para Nó de ID:{node.id} na porta {port}")
    
    thread = threading.Thread(target=node_server.serve_forever)
    thread.daemon = True
    thread.start()
    return thread

node1 = Node(1, datetime.datetime.now() - timedelta(seconds=random.randint(1, 59)), network)
node2 = Node(2, datetime.datetime.now() - timedelta(seconds=random.randint(1, 59)), network)
node3 = Node(3, datetime.datetime.now() - timedelta(seconds=random.randint(1, 59)), network)
node4 = Node(4, datetime.datetime.now() - timedelta(seconds=random.randint(1, 59)), network)

network.register_node(node1)
network.register_node(node2)
network.register_node(node3)
network.register_node(node4)
network.set_order()



threads = []
threads.append(start_client_server(node1, 8001))
threads.append(start_client_server(node2, 8002))
threads.append(start_client_server(node3, 8003))
threads.append(start_client_server(node4, 8004))

# Sincroniza os relógios após os servidores estarem ativos
# Mantém o script ativo
node1.send_message()
try:
    while True:
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nEncerrando servidores.")