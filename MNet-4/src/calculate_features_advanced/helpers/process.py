#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "4.1"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

'''
    Processes the feature vector values
'''

import time
from features import betweeness, centrality, communicability, density, diameter, eccentricity, node_connectivity, pagerank, radius, square_clustering
from save import save_feature


def process_all(network, path_to_output):



    # betweeness
    feature_name = 'Betweeness' 
    print("Calculating " + feature_name)
    f = betweeness.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))

    # centrality
    feature_name = 'Centrality' 
    print("Calculating " + feature_name)
    f = centrality.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))

    # communicability, 
    feature_name = 'Communicability' 
    print("Calculating " + feature_name)
    f = communicability.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))   

    # density, 
    feature_name = 'Density' 
    print("Calculating " + feature_name)
    f = density.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))      

    # diameter, 
    feature_name = 'Diameter'
    print("Calculating " + feature_name) 
    f = diameter.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))   

    # eccentricity, 
    feature_name = 'Eccentricity' 
    print("Calculating " + feature_name)
    f = eccentricity.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))       

    # node_connectivity,
    feature_name = 'Node_connectivity' 
    print("Calculating " + feature_name)
    f = node_connectivity.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))       

    #  pagerank, 
    feature_name = 'Pagerank' 
    print("Calculating " + feature_name)
    f = pagerank.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))       

    # radius, 
    feature_name = 'Radius' 
    print("Calculating " + feature_name)
    f = radius.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))   

    # square_clustering
    feature_name = 'Square_clustering' 
    print("Calculating " + feature_name)
    f = square_clustering.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))       

  
