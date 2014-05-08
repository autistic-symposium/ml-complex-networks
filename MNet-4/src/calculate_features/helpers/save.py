#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "4.1"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"



''' 
    Save the feature vectors into a output file.
'''


def save_feature(path_to_output, feature_value, feature_name, last = False):
    file_feature = open(path_to_output, 'a')
    file_feature.write(feature_name + ': ')
    file_feature.write(str(feature_value) + '\n') 
    if last:
		file_feature.write('\n****************************\n')
    file_feature.close()


