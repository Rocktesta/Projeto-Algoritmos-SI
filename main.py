import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
from importacao import importacao_db



class Graph:
    def __init__(self, links):
        self.link_list = links
   

def ShortestPath (graph, start, end):   # utiliza Dijkstra
    visited = {node: False for node in graph.link_list.keys()}
    distances = {node: float('inf') for node in graph.link_list.keys()}
    paths = {node: [] for node in graph.link_list.keys()}
    paths[start] = [start]
    distances[start] = 0
    visited[start] = True
    priority = [(0, start)]
   
    while priority:
        distance, current = priority[0]
        priority.pop(0)
        visited[current] = True
        if current == end:
            return f"distancia de {distance} de {start} para {end}\nPath: {' -> '.join(paths[end])}"
        
        for node in graph.link_list[current]:
            if visited[node] == False:
                new_distance = distance + graph.link_list[current][node]
            if new_distance < distances[node]:
                distances[node] = new_distance
                paths[node] = paths[current] + [node]
                priority.append((new_distance, node))
                priority.sort()
                print(current)
    return
        
        
dicionario = importacao_db()
graph = Graph(dicionario)

nx_graph = nx.DiGraph()

for node, links in graph.link_list.items():
    for end_node, weight in links.items():
        nx_graph.add_edge(str(node), str(end_node), weight=weight)

net = Network(height='750px', width='100%', notebook=True)

# Add nodes to the PyVis network, ensuring node IDs are strings
for node in graph.link_list:
    net.add_node(str(node), label=str(node))

# Add edges to the PyVis network with weights as labels, ensuring node IDs are strings
for node, edges in graph.link_list.items():
    for end_node, weight in edges.items():
        net.add_edge(str(node), str(end_node), label=str(weight))

# Generate and show the network visualization
net.show('example.html')

print(ShortestPath(graph, '0', '300'))
