#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

''' This script calculates error '''
import numpy as np


def calculate_error(T, score, Y):
    ''' Calculate error '''
    final = []
    for j in range(T):
        right, wrong = 0, 0
	dataset_for_this_T = score[j]	
	for i in range(len(dataset_for_this_T)):
	    if dataset_for_this_T[i] == Y[i]:
	       right += 1.0
            else:
               wrong += 1.0
	final.append(right/(right+wrong))
    
    return final

