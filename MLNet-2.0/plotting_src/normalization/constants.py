
#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

# features
FEATURES   = ['Size', 'Order', 'Assortativity', 'Transitivity', 'Degree', 'Coreness', 'Number_Triangles', 'Number_Cliques', 'Clique_number', 'Clustering', \
'Edge_connectivity', 'Eccentricity', 'Diameter', 'Betweeness', 'Density', 'Radius', 'Square_clustering', 'Communicability', 'Pagerank', 'Centrality']
FEATURES_WE_WANT = ['Assortativity',  'Clustering', 'Density', 'Pagerank', 'Centrality']


OUTPUT_FOLDER = '../../output/'
INPUT_FOLDER = '../../data/normalize_data/'

TYPE_NOR = ['xmin', 'gauss', 'none'] 