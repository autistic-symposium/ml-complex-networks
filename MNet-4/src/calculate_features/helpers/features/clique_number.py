'''
Return the clique number (size of the largest clique) for G.
'''

import networkx as nx


def calculate(network):
    try:
        n = nx.graph_clique_number(network)
    except:
        n = 0
    return n
