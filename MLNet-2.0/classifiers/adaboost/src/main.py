#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"


''' This program shows the application of boosting for weak
    classifiers given by decision stumps '''

import os
import numpy as np
from adaboost import AdaBoost
from decision_stump import DecisionStump
from error import calculate_error
from constants import  PERCENTAGE, INPUT_FILE, OUTPUT_FOLDER, NET_NAMES, T, NORM
import one_against_all



def save_result_final(error_train, error_test, output_file, net_name, norm):
    ''' Save in a file the final result '''

    with open(output_file, "a") as f:
        f.write(net_name + ", " + norm + " , " + "etrain: " + str(error_train) + " , etest: " + str(error_test) + "\n")



def main():
    ''' Load data, split data, creates adaboost algorithm 
    with decision stump, calculates errors, save final file.
    Since this is a binary classifier, we will do for each of the 
    4 networks, one at time'''

    # chose classifier
    classifier = AdaBoost(DecisionStump)

    # for each normalization:
    for norm in NORM:
        # get input and output file paths
        input_train = INPUT_FILE + "train_" + str(PERCENTAGE) + '_' + norm + ".data" 
        input_test = INPUT_FILE + "test_" + str(PERCENTAGE) + '_' + norm + ".data"  

        ada_folder = OUTPUT_FOLDER + 'adaboost/'
        if not os.path.exists(ada_folder):
            os.makedirs(ada_folder) 
        output_file = ada_folder + 'results.out'
        with open(output_file, "a") as f:
            f.write("# PERCENTAGE: " + str(PERCENTAGE)  + "\n")


        # for each network type:
        for net_name in NET_NAMES:
            # get data
            X_train, Y_train = one_against_all.load_data(input_train, net_name)
            X_test, Y_test = one_against_all.load_data(input_test, net_name)

            print 'Calculating adaboost for set ' + input_train 
            score_train, score_test = classifier.run_adaboost(X_train, Y_train, T, X_test)

            print 'Calculating errors ...'        
            error_train = calculate_error(T, score_train, Y_train)    
            error_test = calculate_error(T, score_test, Y_test)

            error_train_total = sum(error_train)/len(error_train)
            error_test_total = sum(error_test)/len(error_test)    
            
            save_result_final(error_train_total, error_test_total, output_file, net_name, norm)


    print 'Results saved at ' +  OUTPUT_FOLDER
    print 'Done!!!'


if __name__ == '__main__':
    main()
