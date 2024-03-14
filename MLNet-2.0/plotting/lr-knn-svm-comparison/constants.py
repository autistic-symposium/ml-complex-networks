
#!/usr/bin/env python
 
 
__author__ = "Mia Stein"
__copyright__ = "Copyright 2014"
__credits__ = ["Mia Stein"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mia Stein"
__email__ = ""

# features
FEATURES   = ['Size', 'Order', 'Assortativity', 'Transitivity', 'Degree', 'Coreness', 'Number_Triangles', 'Number_Cliques', 'Clique_number', 'Clustering', \
'Edge_connectivity', 'Eccentricity', 'Diameter', 'Betweeness', 'Density', 'Radius', 'Square_clustering', 'Communicability', 'Pagerank', 'Centrality']


FEATURES_WE_WANT = ['Number_Cliques',  'Clustering', 'Pagerank', 'Centrality', 'Square_clustering', 'Assortativity', 'Transitivity'] 
FEATURES_INDEX = [7,  9, 18, 19, 16,  2, 3] 



OUTPUT_FOLDER = '../../output/'
INPUT_FOLDER = '../../data/normalize_data/'

TYPE_NOR = ['xmin', 'gauss', 'none'] 