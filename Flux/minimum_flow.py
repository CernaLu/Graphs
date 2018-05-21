#demand:
    # Nodes of the graph G are expected to have an attribute demand that indicates
    # how much flow a node wants to send (negative demand) or receive (positive demand).
    # Note that the sum of the demands should be 0 otherwise the problem in not feasible.
    # If this attribute is not present, a node is considered to have 0 demand. Default
    # value: ‘demand’.

#capacity:
    #Edges of the graph G are expected to have an attribute capacity that indicates how
    # much flow the edge can support. If this attribute is not present, the edge is
    # considered to have infinite capacity. Default value: ‘capacity’.

#weight:
    # Edges of the graph G are expected to have an attribute weight that indicates
    # the cost incurred by sending one unit of flow on that edge. If not present, the
    # weight is considered to be 0. Default value: ‘weight’.




import sys
import numpy as numpy
import pandas as pd
from pylab import rcParams
import seaborn as sb
import matplotlib.pyplot as plt
import networkx as nx
from math import sqrt

rcParams['figure.figsize'] = 10, 6
sb.set_style('whitegrid')

G = nx.DiGraph()
F = nx.DiGraph()
H = nx.DiGraph()

k = 1 / sqrt(5)
pos = nx.spring_layout(G, k=k, iterations=20, scale=0.8) #CHANGE FOR OVERLAPS

G.add_node('a', demand = -5)
G.add_node('d', demand = 5)
G.add_edge('a', 'b', weight = 3, capacity = 4)
G.add_edge('a', 'c', weight = 6, capacity = 10)
G.add_edge('b', 'd', weight = 1, capacity = 9)
G.add_edge('c', 'd', weight = 2, capacity = 5)
flowCost, flowDict = nx.network_simplex(G)
print('flow cost = ', flowCost)
print('flow dict = ', flowDict)



nodes_labels = []
n = {}
i = 0
for ascii_decimal in range(65, 69, 1): #65 is A, 90 is Z
    ascii_letter = chr(ascii_decimal) 
    nodes_labels.append(ascii_letter)
    n[i] = ascii_letter
    i += 1

edges = { (n[0], n[1], 4), \
          (n[0], n[2], 10), \
          (n[1], n[3], 9), \
          (n[2], n[3], 5), }

print(nodes_labels)
F.add_nodes_from(nodes_labels)
F.add_weighted_edges_from(edges)
position = nx.spring_layout(F, k=k, iterations=20, scale=0.8) #CHANGE FOR OVERLAPS
edges_labels = nx.get_edge_attributes(F,'weight')


status = nx.info(F) 
print (status)
nx.draw(F, position, with_labels=True)
nx.draw_networkx_edge_labels(F, position, edge_labels=edges_labels)
plt.axis('equal')
plt.show()

nx.draw(G, pos, with_labels=True)
path = nx.shortest_path(G, source=n[0], target=n[7], weight='weight')
path_edges = list(zip(path,path[1:]))
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='y')
nx.draw_networkx_edges(G,pos, edgelist=path_edges, edge_color='r', width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edges_labels)
plt.axis('equal')
plt.show()

flowDict['a']['b']
flowDict['a']['c']

