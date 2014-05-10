#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"


'''
Normalization plots for each feature and each type of graphs.
The normalization shows the feature in tersm of the order of the network.

mari wahl @ 2014
'''


import pylab as plt
import os
import json
import numpy as np
from constants import FEATURES, INPUT_FOLDER, OUTPUT_FOLDER, TYPE_NOR, FEATURES_WE_WANT




def get_input_path(number, typen):
    return INPUT_FOLDER + 'together' + str(number) + '_test_0.8_' + typen +'.data'



def get_output_path(typen, number, feat):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    outfolder = OUTPUT_FOLDER +  'plots_normalization/'
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)    

    return outfolder + 'set' + number + feat + '_0.8_' + typen  +'.png'



def get_data_here(inputfile, index, range_other=10e7):
    data = np.loadtxt(inputfile, delimiter = ',')
    X = data[:,:-1] 
    Y = data[:,-1]
    bio = []
    tech = []
    info = []
    social = []

    for i, value in enumerate(Y):

        if value == 1 and X[i][index] !=0: # tech
            tech.append(X[i][index])
        elif value == 2 and X[i][index] !=0:
            info.append(X[i][index])
        elif value == 3 and X[i][index] !=0:
            social.append(X[i][index])
        elif value == 4 and X[i][index] !=0:
            bio.append(X[i][index])

    range_here = min(len(info), len(tech), len(social), len(bio), range_other)
    return info, bio, tech, social, range_here


 

def plotting(infox, biox, techx, socialx, infoy, bioy, techy, socialy , n, labelx, labely):
    vs = 50
    al = 0.5
    color = ['r', 'b', 'g',  'y']
    marker = ['o', '*', 's', '>'] #, 'D', '>', '<', 'p']

    #111" means "1x1 grid, first subplot" and "234" means "2x3 grid, 4th subplot
    plt.subplot(2, 2, n+1)
    plt.scatter(infox, infoy,  c=color[0], s=70, alpha=0.7, marker=marker[0], label='Information')
    plt.scatter(biox, bioy,   c=color[1], s=90, alpha=0.7, marker=marker[1], label='Biological')
    plt.scatter(techx, techy,  c=color[2], s=vs, alpha=0.4, marker=marker[2], label='Technological')
    plt.scatter(socialx, socialy,  c=color[3], s=vs, alpha=al, marker=marker[3], label='Social')

    plt.ylabel(labely)      
    plt.xlabel('')      
    plt.legend(loc=1)


def main():  

    ''' OH MY GOD SO MANY FORS... I HOPE NOBODY SEES THIS'''

    # plot config
    with open("conf.json") as json_file:
       s = json.load(json_file)
    plt.rcParams.update(s)
   

    # for each type norm
    for typen in TYPE_NOR:
        print('\nStarting to plot for ' + typen)

        # for each set
        for number in range(1, 6):

            # for each feature
            for nx, axisx in enumerate(FEATURES_WE_WANT):

                for n, feat in enumerate(FEATURES): 
  
                    if axisx == feat:

                        # start plotting
                        print('... ploting  ' + axisx ) 

                        plt.cla()
                        plt.clf()
                        plt.figure()
                        range_here  = 1e5

                        outputfile = get_output_path(typen, str(number), feat)
                        plt.title(feat + '- Set: ' + str(number) + ' - Normalization: ' + typen)
                        inputfile = get_input_path(number, typen)

                        infox, biox, techx, socialx, range_here  = get_data_here(inputfile, n, range_here )
                        labelx = feat
                
                        for n, feat in enumerate(FEATURES):         
                            for ny, axisy in enumerate(FEATURES_WE_WANT[nx+1:] + FEATURES_WE_WANT[:nx]):
               
                                if axisy == feat :
                                    labely = feat
                                    infoy, bioy, techy, socialy, range_here  = get_data_here(inputfile, n, range_here )
                                    plotting(infox[:range_here], biox[:range_here], techx[:range_here], socialx[:range_here], infoy[:range_here],\
                                     bioy[:range_here], techy[:range_here], socialy[:range_here], ny, labelx, labely)
                        
                        plt.savefig(outputfile, orientation='landscape')

    print('Done!\n')





if __name__ == '__main__':
    main()

