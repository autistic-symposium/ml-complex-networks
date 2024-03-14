
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


FEATURES_WE_WANT1T = ['Number_Cliques',  'Clustering', 'Pagerank', 'Centrality', 'Square_clustering']
FEATURES_WE_WANT2T = ['Density',  'Square_clustering', 'Communicability', 'Pagerank', 'Clustering']
FEATURES_WE_WANT3T = ['Transitivity',  'Number_Triangles', 'Pagerank', 'Square_clustering']
FEATURES_WE_WANT4T = ['Clique_number',  'Centrality', 'Number_Cliques']
FEATURES_WE_WANT5T = ['Coreness']

FEATURES_WE_WANT = [FEATURES_WE_WANT1T, FEATURES_WE_WANT2T,FEATURES_WE_WANT3T, FEATURES_WE_WANT4T, FEATURES_WE_WANT5T]


OUTPUT_FOLDER = '../../output/'
INPUT_FOLDER = '../../data/normalize_data/'

TYPE_NOR = ['xmin', 'gauss', 'none'] 