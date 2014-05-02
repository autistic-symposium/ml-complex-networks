
'''
This script add all the feature vectors into a big file

mari wahl @ 2014
'''


import os


SUBFILES = ['atlas', 'auto', 'carbon', 'cellular', 'citation','collaboration','communication', 'ground','location','meme','metabolic','onlinecom','p2p','products','road','signed','social','webgraphs','wiki','yeast']


if __name__ == '__main__':

    final_file = open('all_nets.data', "w")

    # Loop into all the network folders
    for i in range(len(SUBFILES)):

        INPUT_PATH = 'vectors/' + SUBFILES[i] + '.data'
        tempfile = open(INPUT_PATH)

        print 'Processing ' + INPUT_PATH 
        final_file.write(tempfile.read())
          

    print '\nDone!!!'