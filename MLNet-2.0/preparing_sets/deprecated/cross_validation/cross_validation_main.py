#!/usr/bin/env python
 
 
__author__ = "Mia Stein"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mia Stein"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mia Stein"
__email__ = ""

''' This program divide the sets for cross validation '''

import random, os
import numpy as np
from constants import SAMPLINGS_SETS, PERCENTAGE, INPUT_FILE, OUTPUT_FOLDER


def save_result_split(final, name):
    ''' Save in a file the results of spliting'''

    with open(name , "w") as f:
        for i in range(len(final)):
            f.write(str(final[i]) + "\n")



def split_data(num_sets, input_file, output_file):
    ''' split data for training and test sets '''

    with open(input_file, "rb") as f:
        data = f.read().split('\n')

    border = int(PERCENTAGE*len(data))
    for i in range(num_sets):   

        random.shuffle(data)

        train_data = data[:border][:]
        test_data = data[border:][:]

        out_file_train = output_file + "train_" + str(i) + '_.data' 
        out_file_test = output_file + "test_" + str(i) + '_.data' 

        save_result_split(train_data, out_file_train)
        save_result_split(test_data, out_file_test)



def create_output_folder(nsam):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER) 
    out_cs = OUTPUT_FOLDER + 'cross_validation/'
    if not os.path.exists(out_cs):
        os.makedirs(out_cs)     
    out_v = out_cs + nsam + '/'
    if not os.path.exists(out_v):
        os.makedirs(out_v)     
    return out_v 


def main():
    ''' Load and split data'''

    for nsam in SAMPLINGS_SETS:
            
        input_file = INPUT_FILE
        output_folder = create_output_folder(str(nsam))
        split_data(nsam, input_file, output_folder)

    print 'Done!'


   
if __name__ == '__main__':
    main()
