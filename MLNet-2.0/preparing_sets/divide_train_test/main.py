#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

''' This program divide the sets for cross validation '''

import random, os
import numpy as np
from constants import PERCENTAGE, INPUT_FOLDER, OUTPUT_FOLDER


def save_result_split(final, name):
    ''' Save in a file the results of spliting'''

    with open(name , "w") as f:
        for i in range(len(final)):
            f.write(str(final[i]) + "\n")



def split_data(input_file, output_file):
    ''' split data for training and test sets '''

    with open(input_file, "rb") as f:
        data = f.read().split('\n')

    border = int(PERCENTAGE*len(data))
    random.shuffle(data)

    train_data = data[:border][:]
    test_data = data[border:][:]

    out_file_train = output_file + "_train_" + str(PERCENTAGE) + ".data" 
    out_file_test = output_file + "_test_" + str(PERCENTAGE) + ".data" 
    
    save_result_split(train_data, out_file_train)
    save_result_split(test_data, out_file_test)



def main():
    ''' Load and split data from entire file'''

    input_folder = INPUT_FOLDER
    output_folder = OUTPUT_FOLDER

    if not os.path.exists(output_folder):
        os.makedirs(output_folder) 

    ''' Load and split data from files divided by order'''

    output_folder = OUTPUT_FOLDER
    if not os.path.exists(output_folder):
        os.makedirs(output_folder) 

    # for each set of files
    input_file = INPUT_FOLDER + 'together1.data'
    split_data(input_file, output_folder + 'together1')
    
    input_file = INPUT_FOLDER + 'together2.data'
    split_data(input_file, output_folder + 'together2')

    input_file = INPUT_FOLDER + 'together3.data'
    split_data(input_file, output_folder + 'together3')

    input_file = INPUT_FOLDER + 'together4.data'
    split_data(input_file, output_folder + 'together4')        

    input_file = INPUT_FOLDER + 'together5.data'
    split_data(input_file, output_folder + 'together5')   

    # with outliers
    input_file = INPUT_FOLDER + 'together1.data' + '_with_outlier'
    split_data(input_file, output_folder + 'together1_' + 'with_outlier')
    
    input_file = INPUT_FOLDER + 'together2.data' + '_with_outlier'
    split_data(input_file, output_folder + 'together2_'+ 'with_outlier')

    input_file = INPUT_FOLDER + 'together3.data' + '_with_outlier'
    split_data(input_file, output_folder + 'together3_'+ 'with_outlier')

    input_file = INPUT_FOLDER + 'together4.data' + '_with_outlier'
    split_data(input_file, output_folder + 'together4_'+ 'with_outlier')        

    input_file = INPUT_FOLDER + 'together5.data' + '_with_outlier'
    split_data(input_file, output_folder + 'together5_'+ 'with_outlier')    


    print 'Output generate at ' + output_folder

    print 'Done!'


   
if __name__ == '__main__':
    main()
