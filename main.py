import numpy as np
import networkx as nx
import matplotlib as plt

#TODO
class link:
    def __init__(self, endNode, weight):
        self.endNode = endNode
        self.weight = weight

#TODO
class node:
    def __init__(self, data):
        self.data = data
        self.links = {}
        self.connected = []

    def createLink(self, link):
        self.connected.append(link)
        self.links[self.data] = self.connected

    def printLinks(self):
        for node in self.connected:
            print(f"node {self.data} is connected to node {node.endNode.data} with weight {node.weight} ")
        



#TODO
def ShortestPath (graph, start, end): # usa dijkstra 
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    print(distances)

ShortestPath(['a', 'b', 'c'], 'a', 'c')
node1 = node('a')
node2 = node('b')
node3 = node('c')
link_ab = link(node2, 1)
link_ac = link(node3, 10)
node1.createLink(link_ab)
node1.createLink(link_ac)
node1.printLinks()
