# Classe da rede para definição do anel
class Network:
    def __init__(self):
        self.nodes = []
     
    #Registra os nós na rede
    def register_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            print(f"Nó de ID:{node.id} //registrado na rede: ")        
        return True
    #Definie o nó sucessor e o anterior 
    def set_order(self):
        for index, node in enumerate(self.nodes):
            successor_index = (index + 1) % len(self.nodes)
            node.successor = f"http://localhost:{8000 + successor_index + 1}/RPC2"
            node.previous = f"http://localhost:{8000 + (index - 1) % len(self.nodes) + 1}/RPC2"
            print(f"Nó de ID:{node.id} configurado: Sucessor = {node.successor}, Anterior = {node.previous}")
 
