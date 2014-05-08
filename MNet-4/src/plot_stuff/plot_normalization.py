'''
Normalization plots for each feature and each type of graophs.
The normalization shows the feature in tersm of the order of the network.

mari wahl @ 2014
'''


import pylab
import os
import numpy as np

__author__ = """Mari Wahl"""

# plot config
pylab.rcParams.update({'font.size': 12})
color = ['#FF4848', '#800080', '#5757FF', '#1FCB4A', '#D9C400', '#F70000', '#0000CE', '#FF800D', '#23819C']
marker = ['o', 'v', 's', '*', 'D', '>', '<', 'p', '8']


# networks by type
INFO_NET = [ 'citation', 'collaboration', 'communication', 'meme', 'p2p', 'products', 'webgraphs', 'wiki', 'onlinecom']
INFO_NET_NAME = [ 'Citation', 'Collaboration', 'Communication', 'Higgs meme',  'Peer-to-peer', 'Product co-purchasing', 'Webgraphs', 'Wikipedia', 'Flick']

SOCIAL_NET = [ "ground", "location", "signed",  "social", 'onlinecom']
SOCIAL_NET_NAME = [ "Ground-truth", "Location based", "Signed", "Online social", 'Flick']


TECH_NET = [ "auto", "road"]
TECH_NET_NAME = [ "Autonomous systems", "Roads"]

SIZE_NETS = [1000000, 2000000, 400000]


# features
FEATURES = ['Average Clustering Coefficient',  'Number of Triangles', 'Fraction of Closed Triangles', 'Diameter', 'Assortativity', 'Transitivity']  
FEATURES_NAME = ['avg',  'nt', 'fct', 'dia', 'ass', 'tra']      






def plot_features(datalist, PATH_TO_OUTPUT, K):
    ''' 
        Plot correlation vectors.
    '''    
    
    for i, feat in enumerate(FEATURES):
   	print("Plotting " + feat + '...')
        figure_name =   PATH_TO_OUTPUT + FEATURES_NAME[i] + '.png'
        pylab.clf()
        pylab.cla()  

   	for j, net in enumerate(datalist):   
            net_x = net[1]
            net_y = net[2][i] 

            
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[j], alpha=0.5, label=net[0])
	    pylab.ylabel(FEATURES[i], fontsize=14)  
	    pylab.xlabel('Number of Nodes', fontsize=14)       
	    pylab.legend(loc=1, prop={'size':10})
            pylab.xlim([-1000, SIZE_NETS[K]])
		    
        pylab.savefig(figure_name, orientation='landscape')



   

def main():  


    print('\nPrinting INFO-NET...')
    datalist = []
    for m, net_here in enumerate(INFO_NET):	

	    PATH_TO_INPUT = "../../results/features_vector_global/INFO-NET/"  + net_here + "/GLOBAL_FEATURES_VECTOR.dat"
	    PATH_TO_OUTPUT = "../../results/plots_normalization/INFO-NET/"

	    if not os.path.exists(PATH_TO_OUTPUT):
		os.makedirs(PATH_TO_OUTPUT)

	    try:
		os.path.exists(PATH_TO_INPUT)
	    except IOError:
		print("Feature vectors not found.")

 
            aux = pylab.loadtxt(PATH_TO_INPUT,dtype = str, unpack=True)

            axis_x = map(float, aux[1])

            axis_y_clust = map(float, aux[7]) 
            axis_y_num_trian = map(float, aux[8])
            axis_y_fract_closed = map(float, aux[9])
            axis_y_diameter = map(float, aux[10])
            axis_y_assort = map(float, aux[12])
            axis_y_trans = map(float, aux[13])

            axis_y = [axis_y_clust, axis_y_num_trian, axis_y_fract_closed , axis_y_diameter, axis_y_assort , axis_y_trans]
    
	    datalist.append([INFO_NET_NAME[m], axis_x, axis_y])

    plot_features(datalist, PATH_TO_OUTPUT, 0)
    print('INFO-NET done!\n')





    print('\nPrinting TECH-NET...')
    datalist = []
    for m, net_here in enumerate(TECH_NET):	

	    PATH_TO_INPUT = "../../results/features_vector_global/TECH-NET/"  + net_here + "/GLOBAL_FEATURES_VECTOR.dat"
	    PATH_TO_OUTPUT = "../../results/plots_normalization/TECH-NET/"

	    if not os.path.exists(PATH_TO_OUTPUT):
		os.makedirs(PATH_TO_OUTPUT)

	    try:
		os.path.exists(PATH_TO_INPUT)
	    except IOError:
		print("Feature vectors not found.")

 
            aux = pylab.loadtxt(PATH_TO_INPUT,dtype = str, unpack=True)

            axis_x = map(float, aux[1])

            axis_y_clust = map(float, aux[7]) 
            axis_y_num_trian = map(float, aux[8])
            axis_y_fract_closed = map(float, aux[9])
            axis_y_diameter = map(float, aux[10])
            axis_y_assort = map(float, aux[12])
            axis_y_trans = map(float, aux[13])

            axis_y = [axis_y_clust, axis_y_num_trian, axis_y_fract_closed , axis_y_diameter, axis_y_assort , axis_y_trans]
    
	    datalist.append([TECH_NET_NAME[m], axis_x, axis_y])

    plot_features(datalist, PATH_TO_OUTPUT, 1)
    print('TECH-NET done!\n')





    print('\nPrinting SOCIAL-NET...')
    datalist = []
    for m, net_here in enumerate(SOCIAL_NET):	

	    PATH_TO_INPUT = "../../results/features_vector_global/SOCIAL-NET/"  + net_here + "/GLOBAL_FEATURES_VECTOR.dat"
	    PATH_TO_OUTPUT = "../../results/plots_normalization/SOCIAL-NET/"

	    if not os.path.exists(PATH_TO_OUTPUT):
		os.makedirs(PATH_TO_OUTPUT)

	    try:
		os.path.exists(PATH_TO_INPUT)
	    except IOError:
		print("Feature vectors not found.")

 
            aux = pylab.loadtxt(PATH_TO_INPUT,dtype = str, unpack=True)

            axis_x = map(float, aux[1])

            axis_y_clust = map(float, aux[7]) 
            axis_y_num_trian = map(float, aux[8])
            axis_y_fract_closed = map(float, aux[9])
            axis_y_diameter = map(float, aux[10])


    	    if PATH_TO_INPUT != "../../results/features_vector_global/SOCIAL-NET/social/GLOBAL_FEATURES_VECTOR.dat":
                axis_y_assort = map(float, aux[12])
                axis_y_trans = map(float, aux[13])

    	    else:
		axis_y_assort = []
		axis_y_trans = []	
		for i in range(len(axis_y_diameter)):
			axis_y_assort.append(0)
			axis_y_trans.append(0)
    
 
	    axis_y = [axis_y_clust, axis_y_num_trian, axis_y_fract_closed , axis_y_diameter, axis_y_assort , axis_y_trans]
	    datalist.append([SOCIAL_NET_NAME[m], axis_x, axis_y])

    plot_features(datalist, PATH_TO_OUTPUT, 2)
    print('SOCIAL-NET done!\n')





if __name__ == '__main__':
    main()

