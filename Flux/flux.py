import sys
import numpy as numpy
import pandas as pd
from pylab import rcParams
import seaborn as sb
import matplotlib.pyplot as plt
import networkx as nx

rcParams['figure.figsize'] = 10, 6
sb.set_style('whitegrid')

F = nx.DiGraph()

#f = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',\
#    6: 'F', 7: 'G', 8: 'H', 9}

f = {}
    
for ascii_letter in range(65, 90, 1):
    char = chr(ascii_letter)
    f.append( char )

fnodes = {'A', 'B', 'C', 'D', 'E', 'F'}

edges = { (f[1],f[2],5), (f[1],f[3],5), (f[1],f[4],13),\
            (f[4],f[5],3), (f[4],f[6],2), (f[3],f[6],7) }

#pos = {1: (f[1],f[2]), 2: (f[1],f[2]), 3: (f[1],f[2]), \
#       4: (f[1],f[2]), 5: (f[1],f[2]), 6: (f[1],f[2]) }

F.add_nodes_from(fnodes)
F.add_weighted_edges_from(edges)

pos = nx.spring_layout(F)
labels = nx.get_edge_attributes(F,'weight')


status = nx.info(F) 
print (status)
print(nx.shortest_path_length(F,source=f[1],target=f[6], weight='weight'))

nx.draw(F, pos, with_labels=True)
nx.draw_networkx_edge_labels(F, pos, edge_labels=labels)

plt.show()