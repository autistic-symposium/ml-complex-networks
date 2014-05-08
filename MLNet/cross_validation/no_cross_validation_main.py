#!/usr/bin/python
# marina von steinkirch @2014
# steinkirch at gmail

''' This program put all the sets together '''

import random
import numpy as np


PERCENTAGE = 0.8
INPUT_FILE = ['all_neat',  'all_neat_n2000', 'all_neat_n1500', 'all_neat_n500', "all_nets_entire",'all_neat_n5000', 'all_neat_n1000']



def save_result_split(final, name):
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

    OUTPUT_FILE_TRAIN  = output_file + "_train.data"
    OUTPUT_FILE_TEST   = output_file + "_test.data"

    save_result_split(train_data, OUTPUT_FILE_TRAIN)
    save_result_split(test_data, OUTPUT_FILE_TEST)



def main():

    for net_type in INPUT_FILE:
        input_file = './input/' + net_type + '.data' 
        output_file = './output/no_cv/' + net_type
        split_data(input_file, output_file)
   
    print 'Done!!!'



if __name__ == '__main__':
    main()

