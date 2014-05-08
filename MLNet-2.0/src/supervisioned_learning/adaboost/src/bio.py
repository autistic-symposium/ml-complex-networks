#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"



import numpy as np

def load_data(datafile_name):
     ''' Load the data and separate it by feature
         and labels '''
     data = np.loadtxt(datafile_name, delimiter = ',')

     # features
     ''' X will be an array with each of the 6 features
         in 6 columns, and each row a data entry '''
     X = data[:,:-1] 

     # label
     ''' The last column of the data is the "selector"  
         field used to split data into two sets, and we
         use it as a label, setting 2 -> -1 '''
         # THIS IS WHERE EVERY NETWORK IS DIFFERENT
     Y = data[:,-1]
     Y[Y==1] = -1  
     Y[Y==2] = -1  
     Y[Y==3] = -1 
     Y[Y==4] = 1 
 
     return X, Y
