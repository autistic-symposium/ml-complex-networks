#!/usr/bin/env python

import networkx as nx
import random


__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "4.1"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"




def mhrw_sampling(network, desired_order): 
    ''' MHRV algorithm '''
    
    # variables here
    g = nx.Graph()
    order = 0
    go_more = True
    
    # Try to get the first node that is not isolated 
    trycount = 0
    found_node = False

    while trycount < 10 and not found_node:
        v = random.choice(network.nodes())
        neighbors = nx.neighbors(network, v)
        if not neighbors: 
            trycount += 1
        else: 
            found_node = True

    # if didnt find the node, just return
    if not found_node:       
        return False, g, 0
    
    # now, with the first node, we start our graph
    g.add_node(v)

    while order < desired_order and go_more:
        
        # If don't find more neighboors, but almost have the order
        neighbors = nx.neighbors(network, v)
        if not neighbors:
            if order < 0.9*desired_order:
                return False, g, order
            else:
                return True, g, order

        # If find neighboors keep going
        for i in range(len(neighbors)): 
            g.add_edge(v, neighbors[i])   

        order_new = g.order()
        # If we are too big now (more than 30%), lets try again
        if order_new > 1.3*desired_order:
            return False, g, order

        # or If we reach the order we want 
        if order_new >= desired_order:
            go_more = False
         
        # If nothing happened, keep going...
        v = random.choice(neighbors) 
        order = order_new

    return True, g, order
        


      
    


def make_sample(network, desired_order, desired_min_size, desired_attempt=20):
    ''' 
        This is the main function, we get a network and a desired size and try to make the samples.
    '''

    # Check whether the graph is large enough, if not, just reproduce it 
    net_order = network.order()
    if network.order() < desired_order:
        print ('COPYING THE ORGINAL GRAPH!')
        return network, False, net_order


    # Create counter variables
    attempt = 0
    worked = False

    # Try to get the graph sample
    while attempt < desired_attempt and not worked:
        attempt += 1
        worked, g, order = mhrw_sampling(network, desired_order)
            
    if g.size() >= desired_min_size or attempt < desired_attempt:   
        print ("IT WORKED!") 
        return g, True, order

    else:
        print("I'M AFFRAID IT DIDN'T WORK, JAMES")
        return network, False, net_order





