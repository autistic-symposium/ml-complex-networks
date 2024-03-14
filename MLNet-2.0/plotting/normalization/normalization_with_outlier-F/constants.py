
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


FEATURES_WE_WANT1F = ['Number_Cliques',  'Clustering', 'Pagerank', 'Centrality', 'Square_clustering']
FEATURES_WE_WANT2F = ['Assortativity',  'Clustering', 'Pagerank', 'Centrality',  'Number_Cliques']
FEATURES_WE_WANT3F = ['Transitivity',  'Clustering', 'Pagerank', 'Centrality', 'Square_clustering']
FEATURES_WE_WANT4F = ['Assortativity',  'Clustering', 'Pagerank', 'Centrality',    'Transitivity']
FEATURES_WE_WANT5F = ['Transitivity',  'Clustering', 'Pagerank', 'Centrality', 'Assortativity']

FEATURES_WE_WANT = [FEATURES_WE_WANT1F, FEATURES_WE_WANT2F,FEATURES_WE_WANT3F, FEATURES_WE_WANT4F, FEATURES_WE_WANT5F]


OUTPUT_FOLDER = '../../output/'
INPUT_FOLDER = '../../data/normalize_data/'

TYPE_NOR = ['xmin', 'gauss', 'none'] 