#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"


'''
Normalization plots for each feature and each type of graophs.
The normalization shows the feature in tersm of the order of the network.

mari wahl @ 2014
'''


import pylab as plt
import os
import numpy as np
from constants import NETWORKS, NETWORKS_NAMES, FEATURES, INPUT_FOLDER, OUTPUT_FOLDER 



# plot config
plt.rcParams.update({'font.size': 10})

info = ['#0000CC', '#0099CC', '#00FFCC', '#0066CC', '#000099', '#66FFFF', '#99FFFF']
social = ['#006600', '#00FF33', '#66FF66']
tech = ['#FF9933', '#FFCC00']
bio = ['#9933CC', '#CC0066', '#FF33CC', '#CC3366', '#FF6666']

color = [info, social, tech, bio]


marker = ['o', '*', 's', '>'] #, 'D', '>', '<', 'p']


def get_input_path(subnetwork):
    return INPUT_FOLDER + subnetwork + '.data'


def get_output_path(feat):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    outfolder = OUTPUT_FOLDER +  'normalization/'
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)    
    return outfolder + feat + '.png'
   


def main():  

    # for each feature
    # we dont need order (number of nodes) nor size (edge)
    for n, feat in enumerate(FEATURES[2:]): 
        outputfile = get_output_path(feat)
        plt.clf()
        plt.cla()

        print('Start to plot feature ' + feat)
 
        # for each type of network
        for i, network in enumerate(NETWORKS): 
            
            # for each subnetwork
            for j, subnetwork in enumerate(NETWORKS[i]):
             
                print('... plotting  network ' + NETWORKS_NAMES[i][j])

                inputfile = get_input_path(subnetwork)

                data = np.loadtxt(inputfile, unpack=True, delimiter = ',')

                axis_x_order = data[1]
                axis_y = data[n+2]

                # plot this data
                plt.scatter(axis_x_order, axis_y, s= 20, c=color[i][j], marker=marker[i], alpha=0.5, label=NETWORKS_NAMES[i][j])
        

        # save final plot
        plt.ylabel(FEATURES[n+2])      
        plt.xlabel(FEATURES[1])      
        plt.legend(loc=1, prop={'size':8})
        plt.xlim([0, 3000])    
        plt.savefig(outputfile, orientation='landscape')
    


    print('Done!\n')





if __name__ == '__main__':
    main()

