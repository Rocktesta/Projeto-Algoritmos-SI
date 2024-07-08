import numpy as np
import networkx as nx
import matplotlib as plt

node1 = 'a'
node2 = 'b'
node3 = 'c'
node4 = 'd'

class Graph:
    def __init__(self, links):
        self.link_list = links

class Node:
    def __init__(self, value):
        self.value = value

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
        
graph = Graph({node1: {node2: 2, node3: 1},
               node2: {node4: 10},
               node3: {},
               node4: {}})
print(ShortestPath(graph, node1, node4))
