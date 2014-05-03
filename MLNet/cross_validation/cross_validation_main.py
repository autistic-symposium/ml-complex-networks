#!/usr/bin/python
# marina von steinkirch @2014
# steinkirch at gmail

''' This program divide the sets for cross validation '''

import random
import numpy as np
from constants import SAMPLINGS_SETS, PERCENTAGE

INPUT_FILE = ['all_neat', 'all_neat_n500', 'all_neat_n2000', 'all_neat_n3000',]#"all_nets", "all_nets_entire"]


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

        OUTPUT_FILE_TRAIN = output_file + "train_" + str(i) + '_.data' 
        OUTPUT_FILE_TEST = output_file + "test_" + str(i) + '_.data' 

        save_result_split(train_data, OUTPUT_FILE_TRAIN)
        save_result_split(test_data, OUTPUT_FILE_TEST)




def main():
    ''' Load and split data'''

    for data in INPUT_FILE:
        for sam in SAMPLINGS_SETS:
            
            input_file = './input/' + data + '.data' 
            output_file = './output/' + data + '/' + str(sam) + '/'

            # split data in the # of datasets
            split_data(sam, input_file, output_file)

    print 'Done!'



   
if __name__ == '__main__':
    main()

