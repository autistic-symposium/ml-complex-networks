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
from features import size, order, assortativity, transitivity, degree, coreness, number_of_triangles, number_of_cliques, clique_number, clustering, edge_connectivity
from save import save_feature


def process_all(network, path_to_output):
    # create a new file to not make a mess with the past
    file_feature = open(path_to_output, 'w')


    # Size
    feature_name = 'Size' 
    print("Calculating " + feature_name)
    f = size.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))

    # Order
    feature_name = 'Order' 
    print("Calculating " + feature_name)
    f = order.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))

    # Assortativity
    feature_name = 'Assortativity' 
    print("Calculating " + feature_name)
    f = assortativity.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))   

    # Transitivity
    feature_name = 'Transitivity' 
    print("Calculating " + feature_name)
    f = transitivity.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))      

    # Degree
    feature_name = 'Degree'
    print("Calculating " + feature_name) 
    f = degree.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))   

    # Coreness
    feature_name = 'Coreness' 
    print("Calculating " + feature_name)
    f = coreness.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))       

    # number_of_triangles
    feature_name = 'Number_Triangles' 
    print("Calculating " + feature_name)
    f = number_of_triangles.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))       

    # number_of_cliques
    feature_name = 'Number_Cliques' 
    print("Calculating " + feature_name)
    f = number_of_cliques.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))       

    # clique_number
    feature_name = 'Clique_number' 
    print("Calculating " + feature_name)
    f = clique_number.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))       

    # clustering
    feature_name = 'Clustering' 
    print("Calculating " + feature_name)
    f = clustering.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))       

    # edge_connectivity
    feature_name = 'Edge_connectivity' 
    print("Calculating " + feature_name)
    f = edge_connectivity.calculate(network)
    save_feature(path_to_output, f, feature_name)    
    if not f:
        print(feature_name + ' was 0!\n')
    print("Done! Time: " + time.strftime("%I:%M:%S"))       


 