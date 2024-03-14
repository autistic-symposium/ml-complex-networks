#!/usr/bin/env python
 
 
__author__ = "Mia Stein"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mia Stein"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mia Stein"
__email__ = ""



import numpy as np

def load_data(datafile_name, net_name):
    ''' Load the data and separate it by feature
         and labels '''
    data = np.loadtxt(datafile_name, delimiter = ',')

    # features
    X = data[:,:-1] 

    # label
    Y = data[:,-1]

    # one against all
    if net_name == 'bio':
        Y[Y==1] = -1  
        Y[Y==2] = -1  
        Y[Y==3] = -1 
        Y[Y==4] = 1 

    if net_name == 'tech':
        Y[Y==1] = 1  
        Y[Y==2] = -1  
        Y[Y==3] = -1 
        Y[Y==4] = -1 

    if net_name == 'info':
        Y[Y==1] = -1  
        Y[Y==2] = 1  
        Y[Y==3] = -1 
        Y[Y==4] = -1 

    if net_name == 'social':
        Y[Y==1] = -1  
        Y[Y==2] = -1  
        Y[Y==3] = 1 
        Y[Y==4] = -1   

    return X, Y
