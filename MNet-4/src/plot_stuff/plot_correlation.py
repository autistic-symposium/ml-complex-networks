'''
Correlation plots for each feature and each type of network.
The correlation plots show how a feature change with the size of the network and
it is useful to decide about the normalization.

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


# features
FEATURES = ['Average Clustering Coefficient',  'Number of Triangles', 'Fraction of Closed Triangles', 'Diameter', 'Assortativity', 'Transitivity']  
FEATURES_NAME = ['avg',  'nt', 'fct', 'dia', 'ass', 'tra']      







def plot_45(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT):
        figure_name =   PATH_TO_OUTPUT + FEATURES_NAME[5] + '_' + FEATURES_NAME[4] + '.ps'
        pylab.clf()
        pylab.cla()  
        pylab.xlabel(FEATURES[5], fontsize=14)   
        pylab.ylabel(FEATURES[4], fontsize=14) 
   


   	for j, net in enumerate(datalist_tech):   
            net_x = net[2][5]
            net_y = net[2][4] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[1], alpha=0.5, label=net[0])
	    
   	for j, net in enumerate(datalist_info):   
            net_x = net[2][5]
            net_y = net[2][4] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[3], alpha=0.5, label=net[0])

   	for j, net in enumerate(datalist_social):   
            net_x = net[2][5]
            net_y = net[2][4] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[4], alpha=0.5, label=net[0])            
        pylab.legend(loc=1, prop={'size':8})	    
        pylab.savefig(figure_name, orientation='landscape')




def plot_35(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT):
        figure_name =   PATH_TO_OUTPUT + FEATURES_NAME[3] + '_' + FEATURES_NAME[5] + '.ps'
        pylab.clf()
        pylab.cla()  
        pylab.xlabel(FEATURES[3], fontsize=14)   
        pylab.ylabel(FEATURES[5], fontsize=14) 
   


   	for j, net in enumerate(datalist_tech):   
            net_x = net[2][3]
            net_y = net[2][5] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[1], alpha=0.5, label=net[0])
	    
   	for j, net in enumerate(datalist_info):   
            net_x = net[2][3]
            net_y = net[2][5] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[3], alpha=0.5, label=net[0])

   	for j, net in enumerate(datalist_social):   
            net_x = net[2][3]
            net_y = net[2][5] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[4], alpha=0.5, label=net[0])            
        pylab.legend(loc=1, prop={'size':8})	    
        pylab.savefig(figure_name, orientation='landscape')





def plot_34(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT):
        figure_name =   PATH_TO_OUTPUT + FEATURES_NAME[3] + '_' + FEATURES_NAME[4] + '.ps'
        pylab.clf()
        pylab.cla()  
        pylab.xlabel(FEATURES[3], fontsize=14)   
        pylab.ylabel(FEATURES[4], fontsize=14) 
   


   	for j, net in enumerate(datalist_tech):   
            net_x = net[2][3]
            net_y = net[2][4] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[1], alpha=0.5, label=net[0])
	    
   	for j, net in enumerate(datalist_info):   
            net_x = net[2][3]
            net_y = net[2][4] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[3], alpha=0.5, label=net[0])

   	for j, net in enumerate(datalist_social):   
            net_x = net[2][3]
            net_y = net[2][4] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[4], alpha=0.5, label=net[0])            
        pylab.legend(loc=1, prop={'size':8})	    
        pylab.savefig(figure_name, orientation='landscape')


def plot_25(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT):
        figure_name =   PATH_TO_OUTPUT + FEATURES_NAME[2] + '_' + FEATURES_NAME[5] + '.ps'
        pylab.clf()
        pylab.cla()  
        pylab.xlabel(FEATURES[2], fontsize=14)   
        pylab.ylabel(FEATURES[5], fontsize=14) 
   


   	for j, net in enumerate(datalist_tech):   
            net_x = net[2][2]
            net_y = net[2][5] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[1], alpha=0.5, label=net[0])
	    
   	for j, net in enumerate(datalist_info):   
            net_x = net[2][2]
            net_y = net[2][5] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[3], alpha=0.5, label=net[0])

   	for j, net in enumerate(datalist_social):   
            net_x = net[2][2]
            net_y = net[2][5] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[4], alpha=0.5, label=net[0])            
        pylab.legend(loc=1, prop={'size':8})	    
        pylab.savefig(figure_name, orientation='landscape')



def plot_24(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT):
        figure_name =   PATH_TO_OUTPUT + FEATURES_NAME[2] + '_' + FEATURES_NAME[4] + '.ps'
        pylab.clf()
        pylab.cla()  
        pylab.xlabel(FEATURES[2], fontsize=14)   
        pylab.ylabel(FEATURES[4], fontsize=14) 
     


   	for j, net in enumerate(datalist_tech):   
            net_x = net[2][2]
            net_y = net[2][4] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[1], alpha=0.5, label=net[0])
	    
   	for j, net in enumerate(datalist_info):   
            net_x = net[2][2]
            net_y = net[2][4] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[3], alpha=0.5, label=net[0])

   	for j, net in enumerate(datalist_social):   
            net_x = net[2][2]
            net_y = net[2][4] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[4], alpha=0.5, label=net[0])            
        pylab.legend(loc=1, prop={'size':8})	    
        pylab.savefig(figure_name, orientation='landscape')


def plot_23(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT):
        figure_name =   PATH_TO_OUTPUT + FEATURES_NAME[2] + '_' + FEATURES_NAME[3] + '.ps'
        pylab.clf()
        pylab.cla()  
        pylab.xlabel(FEATURES[2], fontsize=14)   
        pylab.ylabel(FEATURES[3], fontsize=14) 
    


   	for j, net in enumerate(datalist_tech):   
            net_x = net[2][2]
            net_y = net[2][3] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[1], alpha=0.5, label=net[0])
	    
   	for j, net in enumerate(datalist_info):   
            net_x = net[2][2]
            net_y = net[2][3] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[3], alpha=0.5, label=net[0])

   	for j, net in enumerate(datalist_social):   
            net_x = net[2][2]
            net_y = net[2][3] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[4], alpha=0.5, label=net[0])            
        pylab.legend(loc=1, prop={'size':8})	    
        pylab.savefig(figure_name, orientation='landscape')






def plot_05(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT):
        figure_name =   PATH_TO_OUTPUT + FEATURES_NAME[0] + '_' + FEATURES_NAME[5] + '.ps'
        pylab.clf()
        pylab.cla()  
        pylab.xlabel(FEATURES[0], fontsize=14)   
        pylab.ylabel(FEATURES[5], fontsize=14) 
  


   	for j, net in enumerate(datalist_tech):   
            net_x = net[2][0]
            net_y = net[2][5] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[1], alpha=0.5, label=net[0])
	    
   	for j, net in enumerate(datalist_info):   
            net_x = net[2][0]
            net_y = net[2][5] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[3], alpha=0.5, label=net[0])

   	for j, net in enumerate(datalist_social):   
            net_x = net[2][0]
            net_y = net[2][5] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[4], alpha=0.5, label=net[0])            
        pylab.legend(loc=1, prop={'size':8})	    
        pylab.savefig(figure_name, orientation='landscape')





def plot_04(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT):
        figure_name =   PATH_TO_OUTPUT + FEATURES_NAME[0] + '_' + FEATURES_NAME[4] + '.ps'
        pylab.clf()
        pylab.cla()  
        pylab.xlabel(FEATURES[0], fontsize=14)   
        pylab.ylabel(FEATURES[4], fontsize=14) 
     


   	for j, net in enumerate(datalist_tech):   
            net_x = net[2][0]
            net_y = net[2][4] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[1], alpha=0.5, label=net[0])
	    
   	for j, net in enumerate(datalist_info):   
            net_x = net[2][0]
            net_y = net[2][4] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[3], alpha=0.5, label=net[0])

   	for j, net in enumerate(datalist_social):   
            net_x = net[2][0]
            net_y = net[2][4] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[4], alpha=0.5, label=net[0])            
        pylab.legend(loc=1, prop={'size':8})	    
        pylab.savefig(figure_name, orientation='landscape')





def plot_03(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT):
        figure_name =   PATH_TO_OUTPUT + FEATURES_NAME[0] + '_' + FEATURES_NAME[3] + '.ps'
        pylab.clf()
        pylab.cla()  
        pylab.xlabel(FEATURES[0], fontsize=14)   
        pylab.ylabel(FEATURES[3], fontsize=14) 
    


   	for j, net in enumerate(datalist_tech):   
            net_x = net[2][0]
            net_y = net[2][3] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[1], alpha=0.5, label=net[0])
	    
   	for j, net in enumerate(datalist_info):   
            net_x = net[2][0]
            net_y = net[2][3] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[3], alpha=0.5, label=net[0])

   	for j, net in enumerate(datalist_social):   
            net_x = net[2][0]
            net_y = net[2][3] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[4], alpha=0.5, label=net[0])            
        pylab.legend(loc=1, prop={'size':8})	    
        pylab.savefig(figure_name, orientation='landscape')





def plot_02(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT):
        figure_name =   PATH_TO_OUTPUT + FEATURES_NAME[0] + '_' + FEATURES_NAME[2] + '.ps'
        pylab.clf()
        pylab.cla()  
        pylab.xlabel(FEATURES[0], fontsize=14)   
        pylab.ylabel(FEATURES[2], fontsize=14) 
    


   	for j, net in enumerate(datalist_tech):   
            net_x = net[2][0]
            net_y = net[2][2] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[1], alpha=0.5, label=net[0])
	    
   	for j, net in enumerate(datalist_info):   
            net_x = net[2][0]
            net_y = net[2][2] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[3], alpha=0.5, label=net[0])

   	for j, net in enumerate(datalist_social):   
            net_x = net[2][0]
            net_y = net[2][2] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[4], alpha=0.5, label=net[0])            
        pylab.legend(loc=1, prop={'size':8})	    
        pylab.savefig(figure_name, orientation='landscape')






def plot_01(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT):
        figure_name =   PATH_TO_OUTPUT + FEATURES_NAME[0] + '_' + FEATURES_NAME[1] + '.ps'
        pylab.clf()
        pylab.cla()  
        pylab.xlabel(FEATURES[0], fontsize=14)   
        pylab.ylabel(FEATURES[1], fontsize=14) 
    


   	for j, net in enumerate(datalist_tech):   
            net_x = net[2][0]
            net_y = net[2][1] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[1], alpha=0.5, label=net[0])
	    
   	for j, net in enumerate(datalist_info):   
            net_x = net[2][0]
            net_y = net[2][1] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[3], alpha=0.5, label=net[0])

   	for j, net in enumerate(datalist_social):   
            net_x = net[2][0]
            net_y = net[2][1] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[4], alpha=0.5, label=net[0])            
        pylab.legend(loc=1, prop={'size':8})	    
        pylab.savefig(figure_name, orientation='landscape')





def plot_15(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT):
        figure_name =   PATH_TO_OUTPUT + FEATURES_NAME[1] + '_' + FEATURES_NAME[5] + '.ps'
        pylab.clf()
        pylab.cla()  
        pylab.xlabel(FEATURES[1], fontsize=14)   
        pylab.ylabel(FEATURES[5], fontsize=14) 
     


   	for j, net in enumerate(datalist_tech):   
            net_x = net[2][1]
            net_y = net[2][5] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[1], alpha=0.5, label=net[0])
	    
   	for j, net in enumerate(datalist_info):   
            net_x = net[2][1]
            net_y = net[2][5] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[3], alpha=0.5, label=net[0])

   	for j, net in enumerate(datalist_social):   
            net_x = net[2][1]
            net_y = net[2][5] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[4], alpha=0.5, label=net[0])            
        pylab.legend(loc=1, prop={'size':8})	    
        pylab.savefig(figure_name, orientation='landscape')




def plot_14(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT):
        figure_name =   PATH_TO_OUTPUT + FEATURES_NAME[1] + '_' + FEATURES_NAME[4] + '.ps'
        pylab.clf()
        pylab.cla()  
        pylab.xlabel(FEATURES[1], fontsize=14)   
        pylab.ylabel(FEATURES[4], fontsize=14) 
  


   	for j, net in enumerate(datalist_tech):   
            net_x = net[2][1]
            net_y = net[2][4] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[1], alpha=0.5, label=net[0])
	    
   	for j, net in enumerate(datalist_info):   
            net_x = net[2][1]
            net_y = net[2][4] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[3], alpha=0.5, label=net[0])

   	for j, net in enumerate(datalist_social):   
            net_x = net[2][1]
            net_y = net[2][4] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[4], alpha=0.5, label=net[0])            
        pylab.legend(loc=1, prop={'size':8})	    
        pylab.savefig(figure_name, orientation='landscape')




def plot_13(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT):
        figure_name =   PATH_TO_OUTPUT + FEATURES_NAME[1] + '_' + FEATURES_NAME[3] + '.ps'
        pylab.clf()
        pylab.cla()  
        pylab.xlabel(FEATURES[1], fontsize=14)   
        pylab.ylabel(FEATURES[3], fontsize=14) 
    


   	for j, net in enumerate(datalist_tech):   
            net_x = net[2][1]
            net_y = net[2][3] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[1], alpha=0.5, label=net[0])
	    
   	for j, net in enumerate(datalist_info):   
            net_x = net[2][1]
            net_y = net[2][3] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[3], alpha=0.5, label=net[0])

   	for j, net in enumerate(datalist_social):   
            net_x = net[2][1]
            net_y = net[2][3] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[4], alpha=0.5, label=net[0])            
        pylab.legend(loc=1, prop={'size':8})	    
        pylab.savefig(figure_name, orientation='landscape')




def plot_12(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT):
        figure_name =   PATH_TO_OUTPUT + FEATURES_NAME[1] + '_' + FEATURES_NAME[2] + '.ps'
        pylab.clf()
        pylab.cla()  
        pylab.xlabel(FEATURES[1], fontsize=14)   
        pylab.ylabel(FEATURES[2], fontsize=14)      


   	for j, net in enumerate(datalist_tech):   
            net_x = net[2][1]
            net_y = net[2][2] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[1], alpha=0.5, label=net[0])
	    
   	for j, net in enumerate(datalist_info):   
            net_x = net[2][1]
            net_y = net[2][2] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[3], alpha=0.5, label=net[0])

   	for j, net in enumerate(datalist_social):   
            net_x = net[2][1]
            net_y = net[2][2] 
	    pylab.scatter(net_x, net_y, s= 200, c=color[j], marker=marker[4], alpha=0.5, label=net[0])            
        pylab.legend(loc=1, prop={'size':8})	    
        pylab.savefig(figure_name, orientation='landscape')



   

def main():  



    datalist_info = []
    datalist_tech = []
    datalist_social = []    
    PATH_TO_OUTPUT = "../../results/plots_correlation/"


    for m, net_here in enumerate(INFO_NET):	
	    PATH_TO_INPUT_INFO = "../../results/features_vector_global/INFO-NET/"  + net_here + "/GLOBAL_FEATURES_VECTOR.dat"
            aux = pylab.loadtxt(PATH_TO_INPUT_INFO,dtype = str, unpack=True)
            axis_x = map(float, aux[1])
            axis_y_clust = map(float, aux[7]) 
            axis_y_num_trian = map(float, aux[8])
            axis_y_fract_closed = map(float, aux[9])
            axis_y_diameter = map(float, aux[10])
            axis_y_assort = map(float, aux[12])
            axis_y_trans = map(float, aux[13])
            axis_y = [axis_y_clust, axis_y_num_trian, axis_y_fract_closed , axis_y_diameter, axis_y_assort , axis_y_trans]
	    datalist_info.append([INFO_NET_NAME[m], axis_x, axis_y])



    for m, net_here in enumerate(TECH_NET):	
	    PATH_TO_INPUT_TECH = "../../results/features_vector_global/TECH-NET/"  + net_here + "/GLOBAL_FEATURES_VECTOR.dat"	    
            aux = pylab.loadtxt(PATH_TO_INPUT_TECH,dtype = str, unpack=True)
            axis_x = map(float, aux[1])
            axis_y_clust = map(float, aux[7]) 
            axis_y_num_trian = map(float, aux[8])
            axis_y_fract_closed = map(float, aux[9])
            axis_y_diameter = map(float, aux[10])
            axis_y_assort = map(float, aux[12])
            axis_y_trans = map(float, aux[13])
            axis_y = [axis_y_clust, axis_y_num_trian, axis_y_fract_closed , axis_y_diameter, axis_y_assort , axis_y_trans]
	    datalist_tech.append([TECH_NET_NAME[m], axis_x, axis_y])



    for m, net_here in enumerate(SOCIAL_NET):	
	    PATH_TO_INPUT_SOCIAL = "../../results/features_vector_global/SOCIAL-NET/"  + net_here + "/GLOBAL_FEATURES_VECTOR.dat"
            aux = pylab.loadtxt(PATH_TO_INPUT_SOCIAL,dtype = str, unpack=True)
            axis_x = map(float, aux[1])
            axis_y_clust = map(float, aux[7]) 
            axis_y_num_trian = map(float, aux[8])
            axis_y_fract_closed = map(float, aux[9])
            axis_y_diameter = map(float, aux[10])

    	    if PATH_TO_INPUT_SOCIAL != "../../results/features_vector_global/SOCIAL-NET/social/GLOBAL_FEATURES_VECTOR.dat":
                axis_y_assort = map(float, aux[12])
                axis_y_trans = map(float, aux[13])

    	    else:
		axis_y_assort = []
		axis_y_trans = []	
		for i in range(len(axis_y_diameter)):
			axis_y_assort.append(0)
			axis_y_trans.append(0)
    
	    axis_y = [axis_y_clust, axis_y_num_trian, axis_y_fract_closed , axis_y_diameter, axis_y_assort , axis_y_trans]
	    datalist_social.append([SOCIAL_NET_NAME[m], axis_x, axis_y])




    plot_01(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT)
    plot_02(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT)
    plot_03(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT)
    plot_04(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT)
    plot_05(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT)
    plot_12(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT)
    plot_13(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT)
    plot_14(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT)
    plot_15(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT)
    plot_23(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT)
    plot_24(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT)
    plot_25(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT)
    plot_34(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT)
    plot_35(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT)
    plot_45(datalist_info, datalist_tech, datalist_social, PATH_TO_OUTPUT)








if __name__ == '__main__':
    main()

