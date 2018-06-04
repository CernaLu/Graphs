import sys
import numpy as np
import pandas as pd
from pylab import rcParams
import seaborn as sb
import matplotlib.pyplot as plt
import networkx as nx
from math import sqrt

rcParams['figure.figsize'] = 14, 8
sb.set_style('whitegrid')

srcfile = sys.argv[1]

increment_per_unit = np.loadtxt(srcfile, float, skiprows=1, usecols=1)
#n_of_units = np.loadtxt(srcfile, float, skiprows=1, usecols=(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49))
#edges_from_txt = np.genfromtxt(srcfile, str, max_rows=1,  usecols=(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49))
n_of_units = np.loadtxt(srcfile, float, skiprows=1, usecols=(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40))
edges_from_txt = np.genfromtxt(srcfile, str, max_rows=1,  usecols=(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40))

weight = np.matmul(increment_per_unit, n_of_units)
weigth = np.around(weight, decimals = 3)
G = nx.DiGraph()

nodes_labels = []
n = {}
i = 0
for ascii_decimal in range(65, 84, 1): #65 is A, 90 is Z
    ascii_letter = chr(ascii_decimal) 
    nodes_labels.append(ascii_letter)
    n[i] = ascii_letter
    i += 1

# NODES DEMANDS
G.add_node('a', demand = -12)
G.add_node('b', demand = 5)
G.add_node('l', demand = 6)
G.add_node('i', demand = 8)
G.add_node('n', demand = 4)
G.add_node('j', demand = 5)
G.add_node('p', demand = -16)

# NODE WEIGHT 

edges = {}
e = 0
for edge in edges_from_txt:
    char = list(edge)
    edges[e] = (char[1], char[2])
    G.add_edge(char[1], char[2], weight =  np.around(weight[e], 3))
    e+=1
    
flowCost, flowDict = nx.network_simplex(G)
print('flow cost = ', flowCost)
print('flow dict = ', flowDict)

#l= 1 / sqrt(2000)
l = 80 
position = nx.spring_layout(G, k=l, iterations=500, scale=1) #CHANGE FOR OVERLAPS
edges_labels = nx.get_edge_attributes(G,'weight')

# PRINT PROBLEM

nx.draw(G, position, with_labels=True)
nx.draw_networkx_edges(G, position, edge_color='r', width=2)
nx.draw_networkx_edge_labels(G, position, edge_labels=edges_labels, label_pos=0.3, font_size=4)
plt.axis('equal')
plt.show()

# PRINT SOLUTION
F = nx.DiGraph(flowDict)

# READ DICTIONARY

#for ascii_decimal in flowDict:
#    node1 = chr(ascii_decimal)
#    for node2 in flowDict[node1]:
#        F.add_edge(edges[i], weight = np.around(flowDict[node1][node2], 3))
#        i+=1

sol_edges = []
i = 0
for key1, key2 in flowDict.items():
    for key, value in key2.items():
        F.add_edge(key1, key, weight = value)
        i+=1

sol_edges_labels = nx.get_edge_attributes(F,'weight')

nx.draw(F, position, with_labels=True)
nx.draw_networkx_edges(F, position, edge_color='y', width=2)
nx.draw_networkx_edge_labels(F, position, edge_labels=sol_edges_labels, label_pos=0.3, font_size=4)
plt.axis('equal')
plt.show()
