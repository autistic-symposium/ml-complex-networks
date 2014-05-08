'''
Here we draw graph samples for all our graph files.

mari wahl @ 2014
'''


import os
import matplotlib.pyplot as plt
import networkx as nx



__author__ = """Mari Wahl"""


# networks by type
NET = [ 'citation', 
        'collaboration', 
        'communication', 
        'meme', 
         'p2p', 
         'products', 
         "webgraphs", 
         "signed", 
          "social", 
         "auto"]
INFO_NET_NAME = [  
        'Citation', 
         'Collaboration', 
         'Communication', 
         'Higgs meme', 
          'Peer-to-peer', 
         'Product co-purchasing', 
         'Webgraphs', 
         "Signed", 
         "Social",
          "Autonomous systems" ]

EXAMPLE_NET =  [ 
        'cit-HepPh.txt0_SAMPLED_gpickle.1', 
         'ca-AstroPh.txt0_SAMPLED_gpickle.1',  
        'email-EuAll.txt1_SAMPLED_gpickle.1',  
        'higgs-mention_network.edgelist0_SAMPLED_gpickle.1',  
        'p2p-Gnutella04.txt0_SAMPLED_gpickle.1', 
	'amazon0302.txt0_SAMPLED_gpickle.1',
         'web-BerkStan.txt0_SAMPLED_gpickle.1', 
         'com-amazon.ungraph.txtgpickle.1', 
        'loc-brightkite_edges.txtgpickle.1', 
        'soc-sign-epinions.txt0_SAMPLED_gpickle.1', 
         "soc-Slashdot0902.txt2_SAMPLED_gpickle.1",  
        "as20000102.txt0_SAMPLED_gpickle.1"]







def draw_1(network, PATH_TO_OUTPUT):
        nx.draw_random(network)
        plt.savefig(PATH_TO_OUTPUT)

def draw_2(network, PATH_TO_OUTPUT):
        nx.draw_circular(network)
        plt.savefig(PATH_TO_OUTPUT)

def draw_3(network, PATH_TO_OUTPUT):
        nx.draw_spectral(network)
        plt.savefig(PATH_TO_OUTPUT)


   

def main():  

    for m, net_here in enumerate(NET):	

	    PATH_TO_INPUT = "../../output/partial_graphs_sampled_n4/"  + net_here + '/' + EXAMPLE_NET[m]
	    PATH_TO_OUTPUT1 = "../../results/plot_graphs/some_sample/" + net_here + '_' + str(m) + '1.ps'
	    PATH_TO_OUTPUT2 = "../../results/plot_graphs/some_sample/" + net_here + '_' + str(m) + '2.ps'
	    PATH_TO_OUTPUT3 = "../../results/plot_graphs/some_sample/" + net_here + '_' + str(m) + '3.ps'

            print('Opening ' + PATH_TO_INPUT)
	    network = nx.read_gpickle(PATH_TO_INPUT)
    
            print('Drawing 1...')
	    draw_1(network, PATH_TO_OUTPUT1)

            print('Drawing 2...')
	    draw_2(network, PATH_TO_OUTPUT2)

            print('Drawing 3...')
	    draw_3(network, PATH_TO_OUTPUT3)
             
            print('Graph ' + net_here + ' done!\n')



if __name__ == '__main__':
    main()

