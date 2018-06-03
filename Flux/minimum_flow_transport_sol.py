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
f = nx.DiGraph()

k = 1 / sqrt(5)
pos = nx.spring_layout(G, k=k, iterations=20, scale=0.8) #CHANGE FOR OVERLAPS

G.add_node('a', demand = -50)
G.add_node('b', demand = -40)
G.add_node('d', demand = 30)
G.add_node('e', demand = 60)
G.add_node('c', demand = 0)
G.add_edge('a', 'b', weight = 200, capacity = 10)
G.add_edge('a', 'c', weight = 400)
G.add_edge('b', 'c', weight = 300)
G.add_edge('a', 'd', weight = 900)
G.add_edge('d', 'e', weight = 300)
G.add_edge('e', 'd', weight = 200)
G.add_edge('c', 'e', weight = 100, capacity = 80)

flowCost, flowDict = nx.network_simplex(G)
print('flow cost = ', flowCost)
print('flow dict = ', flowDict)



nodes_labels = []
n = {}
i = 0
for ascii_decimal in range(65, 70, 1): #65 is A, 90 is Z
    ascii_letter = chr(ascii_decimal) 
    nodes_labels.append(ascii_letter)
    n[i] = ascii_letter
    i += 1

edges = { (n[0], n[1], 0), \
          (n[0], n[2], 40), \
          (n[0], n[3], 10), \
          (n[1], n[2], 40), \
          (n[3], n[4], 0), \
          (n[4], n[3], 20), \
          (n[2], n[4], 80) } 

f.add_edge('a', 'b', capacity = 10)
f.add_edge('a', 'c')
f.add_edge('b', 'c')
f.add_edge('a', 'd')
f.add_edge('d', 'e')
f.add_edge('e', 'd')
f.add_edge('c', 'e', capacity= 80)

#F.add_nodes_from(nodes_labels)
#F.add_weighted_edges_from(edges)
#position = nx.spring_layout(F, k=k, iterations=20, scale=0.8) #CHANGE FOR OVERLAPS
#edges_labels = nx.get_edge_attributes(F,'weight')

f.add_nodes_from(nodes_labels)
position = nx.spring_layout(f, k=k, iterations=20, scale=0.8) #CHANGE FOR OVERLAPS
#edges_label = nx.get_edge_attributes(f,'capacity')

#simplex_edge = edges

#status = nx.info(F) 
#print (status)
#nx.draw(F, position, with_labels=True)
nx.draw(f, position, with_labels=True)
#nx.draw_networkx_edges(F, position, edgelist=simplex_edge, edge_color='y', width=2)
#nx.draw_networkx_edge_labels(F, position, edge_labels=edges_labels)
nx.draw_networkx_edge_labels(f, position, edge_labels=edges_label)
plt.axis('equal')
plt.show()

