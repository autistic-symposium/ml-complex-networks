
#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

# networks by type
INFO_NET = [ 'citation', 'collaboration', 'communication', 'p2p', 'products', 'webgraphs', 'wiki']
INFO_NET_NAME = [ 'Citation', 'Collaboration', 'Communication', 'Peer-to-peer', 'Product co-purchasing', 'Webgraphs', 'Wikipedia']

SOCIAL_NET = [ "ground", "location",  "social"]
SOCIAL_NET_NAME = [ "Ground-truth", "Location based", "Online social"]

TECH_NET = [ "auto", "road"]
TECH_NET_NAME = [ "Autonomous systems", "Roads"]

BIO_NET = [ "atlas", "carbon", "cellular", "metabolic", "yeast"]
BIO_NET_NAME = [ "Atlas food web", "Carbon cycle", "Cellular transport", "Metabolic process", "Yeast protein interation"]

NETWORKS = [INFO_NET, SOCIAL_NET, TECH_NET, BIO_NET]
NETWORKS_NAMES = [INFO_NET_NAME, SOCIAL_NET_NAME, TECH_NET_NAME, BIO_NET_NAME]

# features
FEATURES   = ['Size', 'Order', 'Assortativity', 'Transitivity', 'Degree', 'Coreness', 'Number_Triangles', 'Number_Cliques', 'Clique_number', 'Clustering', 'Edge_connectivity', 'Eccentricity', 'Diameter', 'Betweeness', 'Density', 'Radius', 'Square_clustering', 'Communicability', 'Pagerank', 'Centrality']

INPUT_FOLDER = '../../data/vectors_proc/'
OUTPUT_FOLDER = '../../output/plots_results/'

