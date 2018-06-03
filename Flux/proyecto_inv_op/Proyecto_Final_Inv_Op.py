import sys
import numpy as np
import pandas as pd
from pylab import rcParams
import seaborn as sb
import matplotlib.pyplot as plt
import networkx as nx
from math import sqrt

rcParams['figure.figsize'] = 10, 6
sb.set_style('whitegrid')

srcfile = sys.argv[1]

increment_per_unit = np.loadtxt(srcfile, float, skiprows=1, usecols=1)
n_of_units = np.loadtxt(srcfile, float, skiprows=1, usecols=(2,3,4,5,6,7,8,9,10,11,12,13))

size = np.size(n_of_units)

weight = np.matmul(increment_per_unit, n_of_units)

G = nx.DiGraph()

nodes_labels = []
n = {}
i = 0
for ascii_decimal in range(65, 69, 1): #65 is A, 90 is Z
    ascii_letter = chr(ascii_decimal) 
    nodes_labels.append(ascii_letter)
    n[i] = ascii_letter
    i += 1

# NODES DEMANDS
G.add_node('A', demand = -100)
G.add_node('B', demand = 20)
G.add_node('C', demand = 50)
G.add_node('D', demand = 30)

# NODE WEIGHT 
k = 0
for i in range(4):
    for j in range(4):
        if i != j:
            G.add_edge(n[i], n[j], weight = weight[k])
            k += k

flowCost, flowDict = nx.network_simplex(G)
print('flow cost = ', flowCost)
print('flow dict = ', flowDict)

l= 1 / sqrt(5)
position = nx.spring_layout(G, k=l, iterations=20, scale=0.8) #CHANGE FOR OVERLAPS
edges_labels = nx.get_edge_attributes(G,'weight')

# PRINT PROBLEM

nx.draw(G, position, with_labels=True)
nx.draw_networkx_edges(G, position, edge_color='y', width=2)
nx.draw_networkx_edge_labels(G, position, edge_labels=edges_labels)
plt.axis('equal')
plt.show()

# PRINT SOLUTION

