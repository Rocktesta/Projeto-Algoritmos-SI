from pyvis.network import Network
from importacao import importacao_db


#classe do grafo, self.link_dict é um dicionario de dicionarios
class Graph:
    def __init__(self, links):
        self.link_dict = links  #links representam as arestas do grafo
   

def ShortestPath (graph, start, end):   # utiliza Dijkstra
    visited = {node: False for node in graph.link_dict.keys()}  # pontos visitados
    distances = {node: float('inf') for node in graph.link_dict.keys()} # distancias dos pontos até o ponto inicial/start
    paths = {node: [] for node in graph.link_dict.keys()}   # caminhos possiveis ate um determinado ponto
    paths[start] = [start]
    distances[start] = 0
    visited[start] = True
    priority = [(0, start)] #lista de prioridades, pontos com pesos menores possuem prioridade maior    (pilha)
   
    while priority:
        distance, current = priority[0] #visita-se sempre a primeira prioridade
        priority.pop(0) 
        visited[current] = True
        if current == end:
            return f"distância de {distance} do nó {start} para o nó final {end}\nPath: {' -> '.join(paths[end])}", paths[end]
        
        for node in graph.link_dict[current]:
            if visited[node] == False:
                new_distance = distance + graph.link_dict[current][node]
            if new_distance < distances[node]:
                distances[node] = new_distance
                paths[node] = paths[current] + [node]
                priority.append((new_distance, node))
                priority.sort() # garante a ordem correta de prioridades
    return
        
        
dicionario = importacao_db()    # funcao do script importacao.py, transforma arquivo .mtx em banco de dados .db
graph = Graph(dicionario)   # objeto grafo

start = int(input("Nó inicial: "))
end = int(input("Nó de destino: "))
while True:
    try:
        if (start < 0 or start > 331) or (end < 0 or end > 331): 
            start = int(input("Nó inicial(de 0 até 331): "))
            end = int(input("Nó de destino(de 0 até 331): "))
        elif (start >= 0 or start <= 331) and (end >= 0 or end <= 331):
            break
    except:
        start = int(input("Nó inicial(valor númerico): "))
        end = int(input("Nó de destino(valor númerico): "))
        if (start < 0 or start > 331) or (end < 0 or end > 331): 
            start = int(input("Nó inicial(de 0 até 331): "))
            end = int(input("Nó de destino(de 0 até 331): "))
        elif (start >= 0 or start <= 331) or (end >= 0 or end <= 331):
            break
    

txt_out, short_path = ShortestPath(graph, str(start), str(end))


net = Network(height='1280px', width='100%', notebook=True, select_menu=True, filter_menu=True, bgcolor="#222222") # utilizando pyvis lib 

# construcao do grafo com pyvis
for node in graph.link_dict:
    if node not in short_path:
        net.add_node(str(node), label=str(node), size=10, font={'color': 'white'})
    else:
        if node == str(start) or node == str(end):
            if node == str(start):
                net.add_node(str(node), label=str(node), size=10, color='#0EE616', font={'color': 'white'})
            else:
                net.add_node(str(node), label=str(node), size=10, color='#008D13', font={'color': 'white'})
        else:
            net.add_node(str(node), label=str(node), size=10, color='red', font={'color': 'white'})
        

for node, edges in graph.link_dict.items():
    for end_node, weight in edges.items():
        if node in short_path and end_node in short_path:
            net.add_edge(str(node), str(end_node), label=str(weight))
        else:
            net.add_edge(str(node), str(end_node), label=str(weight))

for edge in net.get_edges():
    if edge['from'] in short_path and edge['to'] in short_path:
        edge['color'] = 'red' 
    else:
        edge['color'] = '#2B9BE6'


net.force_atlas_2based()
net.toggle_physics(True)    # fisica do grafo
net.show_buttons(filter_=['physics']) 


net.repulsion(node_distance=100, spring_length=200, spring_strength=0.05, central_gravity=0.05)  #layout dos pontos e links
net.show('USAir97_graph.html')  # grafo exportado

print(txt_out)
