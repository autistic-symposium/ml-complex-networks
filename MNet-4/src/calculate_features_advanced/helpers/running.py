#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "4.1"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"


import networkx as nx
import os
from process import process_all
from constants import ORDER_SAMPLING, NUM_SAMPLES, PATH_2_GRAPH_SAMPLED, PATH_2_GRAPH_GLOBAL, PATH_2_FEATURES_SAMPLED, PATH_2_FEATURES_GLOBAL, PATH_2_OUTPUT   


PATH_2_GRAPH_GLOBAL = PATH_2_OUTPUT + PATH_2_GRAPH_GLOBAL
PATH_2_GRAPH_SAMPLED = PATH_2_OUTPUT + PATH_2_GRAPH_SAMPLED


PATH_2_FEATURES_SAMPLED = PATH_2_OUTPUT + PATH_2_FEATURES_SAMPLED
PATH_2_FEATURES_GLOBAL = PATH_2_OUTPUT + PATH_2_FEATURES_GLOBAL


def define_path_to_output(folder, net, n, s, r, j):
    if j:
        return folder + net + n + '_' + str(s) + '_' + str(r) + '_' + str(j) + '_vector.dat'
    else:
        return folder + net + n + '_' + str(s) + '_' + str(r) + '_vector.dat'


def get_path_to_input(folder, net, n, s, r, j):
    if j:
        return folder + net + n + '_' + str(s) + '_' + str(r) + '_' + str(j) + 'gpickle'
    else:
        return folder + net + n + '_' + str(s) + '_' + str(r) + '.gpickle'



def process_feature(n, TYPE_NET_DIR, j):

    for r in range(NUM_SAMPLES):

        for s in ORDER_SAMPLING:

            path_to_net = get_path_to_input(PATH_2_GRAPH_SAMPLED, TYPE_NET_DIR, n, s ,r, j)
                             
            if os.path.isfile(path_to_net):
                print 'Starting processing for ' + path_to_net

                network = nx.read_gpickle(path_to_net) 
                path_to_output = define_path_to_output(PATH_2_FEATURES_SAMPLED, TYPE_NET_DIR, n, s, r, j) 

                if not os.path.exists(PATH_2_FEATURES_SAMPLED):
                    os.makedirs(PATH_2_FEATURES_SAMPLED)
                if not os.path.exists(PATH_2_FEATURES_SAMPLED + TYPE_NET_DIR):
                    os.makedirs(PATH_2_FEATURES_SAMPLED+ TYPE_NET_DIR)       

                process_all(network, path_to_output)
                print("All feature saved in the output file: " +  path_to_output + '\n')


            path_to_net_error = get_path_to_input(PATH_2_GRAPH_GLOBAL, TYPE_NET_DIR , n, 0 ,0, j)

            if os.path.isfile(path_to_net_error):
                print 'Starting processing for ' + path_to_net

                network = nx.read_gpickle(path_to_net_error) 
                path_to_output_error = define_path_to_output(PATH_2_FEATURES_GLOBAL, TYPE_NET_DIR, n, s, r, j)
                
                if not os.path.exists(PATH_2_FEATURES_GLOBAL):
                    os.makedirs(PATH_2_FEATURES_GLOBAL)
                if not os.path.exists(PATH_2_FEATURES_GLOBAL+ TYPE_NET_DIR):
                    os.makedirs(PATH_2_FEATURES_GLOBAL+ TYPE_NET_DIR)
                
                process_all(network, path_to_output_error)
                print("All feature saved in the output file: " +  path_to_output_error + '\n')




def sampling(NETWORK_FILES_DIR, TYPE_NET_DIR, NUMBER_OF_NETWORKS_DIR):

    if not os.path.exists(PATH_2_OUTPUT):
        os.makedirs(PATH_2_OUTPUT)

    for i, n in enumerate(NETWORK_FILES_DIR): 

        if not NUMBER_OF_NETWORKS_DIR: 
            process_feature(n, TYPE_NET_DIR, 0)
            
        else:
            num_net_here = NUMBER_OF_NETWORKS_DIR[i]
            for j in range(num_net_here):
                process_feature(n, TYPE_NET_DIR, j)

           