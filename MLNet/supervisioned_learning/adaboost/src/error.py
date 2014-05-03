#!/usr/bin/python
# marina von steinkirch @2014
# steinkirch at gmail

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
	final.append(wrong/(right+wrong))
    
    return final

