#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "4.1"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"


from helpers import running, constants


# change here for type of net:
NETWORK_FILES = constants.NETWORK_FILES_UN_GROUND
TYPE_NET_DIR = "ground/"


def main():


    running.sampling(NETWORK_FILES, TYPE_NET_DIR)
    print("All graphs for " + TYPE_NET_DIR + " were processed. The end! \n")
 
   


if __name__ == '__main__':
    main()
