import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network



class Graph:
    def __init__(self, links):
        self.link_list = links
   

def ShortestPath (graph, start, end):   # utiliza Dijkstra
    previous = {node: None for node in graph.link_list.keys()}
    visited = {node: False for node in graph.link_list.keys()}
    distances = {node: float('inf') for node in graph.link_list.keys()}
    distances[start] = 0
    visited[start] = True
    priority = [(0, start)]
   
    while priority:
        distance, current = priority[0]
        priority.pop(0)
        visited[current] = True
        if current == end:
            return f"distancia de {distance} de {start} para {end}"
        
        for node in graph.link_list[current]:
            if visited[node] == False:
                new_distance = distance + graph.link_list[current][node]
            if new_distance < distances[node]:
                distances[node] = new_distance
                previous[node] = current
                priority.append((new_distance, node))
                priority.sort()
    return
        
        

graph = Graph({
    'A': {'B': 2, 'C': 1, 'D': 3},
    'B': {'E': 5, 'F': 2},
    'C': {'D': 4, 'G': 3},
    'D': {'H': 6},
    'E': {'I': 2},
    'F': {'J': 3, 'K': 1},
    'G': {'L': 2},
    'H': {'M': 1},
    'I': {'N': 4},
    'J': {'L': 100},
    'K': {'O': 2},
    'L': {'P': 1},
    'M': {'Q': 3},
    'N': {},
    'O': {'R': 4},
    'P': {},
    'Q': {},
    'R': {'S': 5},
    'S': {'A': 20}
})

nx_graph = nx.DiGraph()

for node, links in graph.link_list.items():
    for end_node, weight in links.items():
        nx_graph.add_edge(node, end_node, weight=weight)

net = Network(height='750px', width='100%', notebook=True)

for node in graph.link_list:
    net.add_node(node, label=node)

for node, edges in graph.link_list.items():
    for end_node, weight in edges.items():
        net.add_edge(node, end_node, label=str(weight))
net.show('example.html')

print(ShortestPath(graph, 'A', 'Q'))
