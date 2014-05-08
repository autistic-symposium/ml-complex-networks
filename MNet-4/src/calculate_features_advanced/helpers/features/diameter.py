'''
Return the diameter of the graph G.
'''

import networkx as nx



def calculate(network):
    try:
        n = nx.diameter(network)
    except:
        return 0
 
    return round(n, 7) 
