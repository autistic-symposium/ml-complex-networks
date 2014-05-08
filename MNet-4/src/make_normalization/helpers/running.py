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
import mhrw
from constants import ORDER_SAMPLING, NUM_SAMPLES, PATH_2_OUTPUT, PATH_2_INPUT,  PATH_2_GRAPH_GLOBAL, PATH_2_GRAPH_SAMPLED, MIN_SIZE

PATH_2_GRAPH_GLOBAL = PATH_2_OUTPUT + PATH_2_GRAPH_GLOBAL
PATH_2_GRAPH_SAMPLED = PATH_2_OUTPUT + PATH_2_GRAPH_SAMPLED

'''
    Here we define the sampling function. Note that we have some special cases that need some
    handling, and that's why they are defined slightly different.
    We also handle directed and undirected graphs here. We could have another step/module just for this
    but it became natural to just incorporate in these functions.
'''

def define_path_to_input(net, n, j):
    if j:
        return PATH_2_INPUT + net + n + j +'gpickle.1'
    else:
        return PATH_2_INPUT + net + n + 'gpickle.1'


def define_path_to_output(PATH, net, n, s, r, j):
    if j:
        return PATH + net + n + '_' + str(s) + '_' + str(r) + '_' + j + 'gpickle'
    else:
        return PATH + net + n + '_' + str(s) + '_' + str(r) + '.gpickle'



def running(path_to_input, net_name, n, j):
    ''' 
        Run the sampling and save the resulting graphs (or log errors if not possible to sample)
    '''
    network = nx.read_gpickle(path_to_input)
    network = network.to_undirected()

    print '\n ----- Starting to compute ' + path_to_input + ' -----'

    for r in range(NUM_SAMPLES):

        for s_count, s in enumerate(ORDER_SAMPLING): 
            if network.order() < s:
                record_global = True
            else:
                record_global = False        
                net, print_please, order_net = mhrw.make_sample(network, s, MIN_SIZE[s_count])

                if print_please:
                    path_to_output = define_path_to_output(PATH_2_GRAPH_SAMPLED, net_name, n, s, r, j) 
                
                    if not os.path.exists(PATH_2_GRAPH_SAMPLED):
                        os.makedirs(PATH_2_GRAPH_SAMPLED)
                    if not os.path.exists(PATH_2_GRAPH_SAMPLED + net_name):
                        os.makedirs(PATH_2_GRAPH_SAMPLED + net_name)

                    nx.write_gpickle(net, path_to_output)
                    print("Sample " + str(r) + " generated at " + path_to_output)
                    print("For desired order: " + str(s) + ', we had resulting order: ' +  str(order_net))

                else:
                     record_global = True

    if record_global:
        path_to_output_error = define_path_to_output(PATH_2_GRAPH_GLOBAL, net_name, n, 0, 0, j) 
        if not os.path.exists(PATH_2_GRAPH_GLOBAL):
            os.makedirs(PATH_2_GRAPH_GLOBAL)
        if not os.path.exists(PATH_2_GRAPH_GLOBAL + net_name):
            os.makedirs(PATH_2_GRAPH_GLOBAL + net_name)   

        nx.write_gpickle(network, path_to_output_error)
        print("Sample " + str(r) + ", for desired order: " + str(s) + " did not work...")
        print("Because of this, the entire graph was saved at  " + path_to_output_error)






def sampling_tar(NETWORK_FILES, TYPE_NET_DIR, NUMBER_OF_NETWORKS):
    ''' This function is for the social network graphs that were obtained in tar format, such as twitter, 
        facebook, g+, etc. Here we deal with the directed graphs. 
    '''
    if not os.path.exists(PATH_2_OUTPUT):
        os.makedirs(PATH_2_OUTPUT) 

    for i, n in enumerate(NETWORK_FILES): 
        net_here = NUMBER_OF_NETWORKS[i]
        print net_here
        for j in range(net_here):
            print j
            path_to_input = define_path_to_input(TYPE_NET_DIR, n, str(j))
            running(path_to_input, TYPE_NET_DIR, n, str(j))



def sampling(NETWORK_FILES, TYPE_NET_DIR):
    if not os.path.exists(PATH_2_OUTPUT):
        os.makedirs(PATH_2_OUTPUT)  

    for n in NETWORK_FILES: 
        path_to_input =  define_path_to_input(TYPE_NET_DIR, n, "")
        running(path_to_input, TYPE_NET_DIR, n, '')

