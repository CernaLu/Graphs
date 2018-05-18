import sys
import numpy as numpy
import pandas as pd
from pylab import rcParams
import seaborn as sb
import matplotlib.pyplot as plt
import networkx as nx

rcParams['figure.figsize'] = 10, 6
sb.set_style('whitegrid')

G = nx.DiGraph()

nodes_labels = []
n = {}
i = 0
for ascii_decimal in range(65, 73, 1): #65 is A, 90 is Z
    ascii_letter = chr(ascii_decimal) 
    nodes_labels.append(ascii_letter)
    n[i] = ascii_letter
    i += 1
    
#EDGES CONNECTIONS
#          from | to | lenght
edges = { (n[0], n[1], 5), \
          (n[0], n[2], 5), \
          (n[0], n[3], 9), \
          (n[1], n[2], 3), \
          (n[1], n[4], 2), \
          (n[3], n[5], 7), \
          (n[2], n[6], 2), \
          (n[2], n[5], 4), \
          (n[5], n[6], 2), \
          (n[4], n[6], 1), \
          (n[6], n[7], 2),
          (n[5], n[7], 5), }

G.add_nodes_from(nodes_labels)
G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G)
edges_labels = nx.get_edge_attributes(G,'weight')


status = nx.info(G) 
print (status)
print('Sortest path lenght = ', nx.shortest_path_length(G, source=n[0], target=n[7], weight='weight'))

nx.draw(G, pos, with_labels=True)
path = nx.shortest_path(G, source=n[0], target=n[7], weight='weight')
path_edges = list(zip(path,path[1:]))
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='y')
nx.draw_networkx_edges(G,pos, edgelist=path_edges, edge_color='r', width=3)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edges_labels)
plt.axis('equal')
plt.show()