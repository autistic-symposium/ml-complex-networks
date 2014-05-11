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
from constants import  PERCENTAGE, INPUT_FOLDER, OUTPUT_FOLDER, NET_NAMES, T, NORM, NUM_SETS
import one_against_all



def save_result_final(error_train, error_test, output_file, net_name, norm, number, with_outlier):
    ''' Save in a file the final result '''

    with open(output_file, "a") as f:
        f.write(net_name[:3] + "     " + norm + "    " +  str(number) + '     '  + str(with_outlier)[:1] + '       '  + \
            str(round(error_train,3)) + "        " + str(round(error_test, 3)) + "\n")


def get_input_data(sett, number, norm,  with_outlier):
    if with_outlier:
        return INPUT_FOLDER + 'together' + str(number) + "_" + sett + "_" + str(PERCENTAGE) + '_' + norm + '_with_outlier' + ".data"
    else:
        return INPUT_FOLDER + 'together' + str(number) +  "_" + sett + "_" + str(PERCENTAGE) + '_' + norm + ".data"



def main():
    ''' Load data, split data, creates adaboost algorithm 
    with decision stump, calculates errors, save final file.
    Since this is a binary classifier, we will do for each of the 
    4 networks, one at time'''

    classification = []
    ada_folder = OUTPUT_FOLDER + 'adaboost/'
    if not os.path.exists(ada_folder):
        os.makedirs(ada_folder) 
    output_file = ada_folder + 'results.out'
    with open(output_file, "w") as f:
        f.write("# ADABOOST RESULTS, TRAIN/TEST FRACTION: " + str(PERCENTAGE)  + "\n")
        f. write("# Net   Norm   Set   OL?   Accu. Train   Accu Test\n")

    # chose classifier
    classifier = AdaBoost(DecisionStump)

    # for each normalization:
    for norm in NORM:

        # for each set
        for number in range(1, NUM_SETS+1):

            ''' with with_outlier '''
            with_outlier = True
            # get input and output file paths
            input_train =  get_input_data('train', number, norm,  with_outlier)
            input_test = get_input_data('test', number, norm,  with_outlier)


            # for each network type:
            for net_name in NET_NAMES:
                # get data
                X_train, Y_train = one_against_all.load_data(input_train, net_name)
                X_test, Y_test = one_against_all.load_data(input_test, net_name)

                print 'Calculating adaboost for net ' + net_name + ' with  normalization ' + norm + ' and set ' + str(number)
                score_train, score_test = classifier.run_adaboost(X_train, Y_train, T, X_test)
     
                error_train = calculate_error(T, score_train, Y_train)    
                error_test = calculate_error(T, score_test, Y_test)

                error_train_total = sum(error_train)/len(error_train)
                error_test_total = sum(error_test)/len(error_test)    
                
                save_result_final(error_train_total, error_test_total, output_file, net_name, norm, number, with_outlier)
                classification.append(str(round(error_test_total,3))  +', ' + str(norm) + ', ' + str(number) + ', ' + str(with_outlier)[0] + '\n') 

            ''' with no outlier '''
            with_outlier = False
            # get input and output file paths
            input_train =  get_input_data('train', number, norm,  with_outlier)
            input_test = get_input_data('test', number, norm,  with_outlier)


            # for each network type:
            for net_name in NET_NAMES:
                # get data
                X_train, Y_train = one_against_all.load_data(input_train, net_name)
                X_test, Y_test = one_against_all.load_data(input_test, net_name)

                score_train, score_test = classifier.run_adaboost(X_train, Y_train, T, X_test)
      
                error_train = calculate_error(T, score_train, Y_train)    
                error_test = calculate_error(T, score_test, Y_test)

                error_train_total = sum(error_train)/len(error_train)
                error_test_total = sum(error_test)/len(error_test)    
                
                save_result_final(error_train_total, error_test_total, output_file, net_name, norm, number, with_outlier)                
                classification.append(str(round(error_test_total,3))  +', ' + str(norm) + ', ' + str(number) + ', ' + str(with_outlier)[0] + '\n') 


    #find best classfiers
    classification.sort()
    with open(output_file + 'good_classification', "w") as f:
        f.write("\n\n\nClassification\n\n")
        for feat in classification:
            f.write(feat + '\n')
        f.write("\n")


    print 'Results saved at ' +  ada_folder
    print 'Done!!!'


if __name__ == '__main__':
    main()
