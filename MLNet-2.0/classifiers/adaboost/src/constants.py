
#!/usr/bin/env python
 
 
__author__ = "Mia Stein"
__copyright__ = "Copyright 2014"
__credits__ = ["Mia Stein"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mia Stein"
__email__ = ""

PERCENTAGE = 0.8
INPUT_FOLDER = "../../../data/normalize_data/"
OUTPUT_FOLDER = '../../../output/'
NET_NAMES = ['tech', 'info', 'social', 'bio']
NORM = ['xmin', 'gauss', 'none']
NUM_SETS = 5
T = 100  #for boosting interation