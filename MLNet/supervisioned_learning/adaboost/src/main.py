#!/usr/bin/python
# marina von steinkirch @2014
# steinkirch at gmail

''' This program shows the application of boosting for weak
    classifiers given by decision stumps '''


import numpy as np
from adaboost import AdaBoost
from decision_stump import DecisionStump
from error import calculate_error
from constants import  SAMPLINGS_SETS, PERCENTAGE
import bio
import tech 
import info 
import social



INPUT_FILE = ['all_neat', 'all_neat_n500', 'all_neat_n1500', 'all_neat_n2000', 'all_neat_n3000', "entire_net"]#, "sampled"]



def save_result_final(final, output_file):
    ''' Save in a file the final result '''

    with open(output_file, "w") as f:
        for i in range(len(final)):
            f.write(str(final[i]) + "," + str(i+1) + "\n")


def main():
    ''' Load data, split data, creates adaboost algorithm 
    with decision stump, calculates errors, save final file.
    Since this is a binary classifier, we will do for each of the 
    4 networks, one at time'''

    # chose classifier
    classifier = AdaBoost(DecisionStump)

    #for boosting interation
    T = 50  



    '''
        BIO networks
    '''
    OUT = '../output/BIO'

    for net_type in INPUT_FILE:
        for NUM_SETS  in SAMPLINGS_SETS:
            
            # create arrays 
            all_errors_train = []
            all_errors_test = []    
            aver_error_train = []
            aver_error_test = []

            # run  for all datasets
            for i in range(NUM_SETS):

                DATA_TRAIN = '../data/' + net_type + '/' + str(NUM_SETS) + '/train_' + str(i) + "_.data"
                DATA_TEST  = '../data/' + net_type + '/' + str(NUM_SETS) +'/test_' + str(i) + "_.data"

                # HERE IS THE DIFFERENCE FOR EACH NET
                X_train, Y_train = bio.load_data(DATA_TRAIN)
                X_test, Y_test = bio.load_data(DATA_TEST)

                print 'Calculating adaboost for set ' + DATA_TRAIN 
                score_train, score_test = classifier.run_adaboost(X_train, Y_train, T, X_test)

                print 'Calculating errors ...'        
                error_train = calculate_error(T, score_train, Y_train)    
                error_test = calculate_error(T, score_test, Y_test)
                all_errors_train.append(error_train)    
                all_errors_test.append(error_test)
           

            # calculates the average errors
            print 'Calculating errors ...'  
            for j in range(T):
                a_e_train = 0
                a_e_test = 0
                for i in range(NUM_SETS):
                    a_e_train += all_errors_train[i][j]
                    a_e_test += all_errors_test[i][j]
                
                aver_error_train.append(a_e_train/NUM_SETS)
                aver_error_test.append(a_e_test/NUM_SETS)
          

            # save to file to plot
            print 'Saving final files ...'  
            OUTPUT_FILE_TRAIN = OUT + '_train_' + net_type + str(NUM_SETS) + '_.data' 
            OUTPUT_FILE_TEST =  OUT + '_test_'   + net_type + str(NUM_SETS) + '_.data' 
            
            save_result_final(aver_error_train, OUTPUT_FILE_TRAIN)
            save_result_final(aver_error_test, OUTPUT_FILE_TEST)









    '''
        INFO networks
    '''
    OUT = '../output/INFO'

    for net_type in INPUT_FILE:
        for NUM_SETS  in SAMPLINGS_SETS:
            
            # create arrays 
            all_errors_train = []
            all_errors_test = []    
            aver_error_train = []
            aver_error_test = []

            # run  for all datasets
            for i in range(NUM_SETS):

                DATA_TRAIN = '../data/input_' + net_type + '/' + str(NUM_SETS) + '/train_' + str(i) + "_.data"
                DATA_TEST  = '../data/input_' + net_type + '/' + str(NUM_SETS) +'/test_' + str(i) + "_.data"

                # HERE IS THE DIFFERENCE FOR EACH NET
                X_train, Y_train = info.load_data(DATA_TRAIN)
                X_test, Y_test = info.load_data(DATA_TEST)

                print 'Calculating adaboost for set ' + DATA_TRAIN 
                score_train, score_test = classifier.run_adaboost(X_train, Y_train, T, X_test)

                print 'Calculating errors ...'        
                error_train = calculate_error(T, score_train, Y_train)    
                error_test = calculate_error(T, score_test, Y_test)
                all_errors_train.append(error_train)    
                all_errors_test.append(error_test)
           

            # calculates the average errors
            print 'Calculating errors ...'  
            for j in range(T):
                a_e_train = 0
                a_e_test = 0
                for i in range(NUM_SETS):
                    a_e_train += all_errors_train[i][j]
                    a_e_test += all_errors_test[i][j]
                
                aver_error_train.append(a_e_train/NUM_SETS)
                aver_error_test.append(a_e_test/NUM_SETS)
          

            # save to file to plot
            print 'Saving final files ...'  
            OUTPUT_FILE_TRAIN = OUT + '_train_' + net_type + str(NUM_SETS) + '_.data' 
            OUTPUT_FILE_TEST =  OUT + '_test_'   + net_type + str(NUM_SETS) + '_.data' 
            
            save_result_final(aver_error_train, OUTPUT_FILE_TRAIN)
            save_result_final(aver_error_test, OUTPUT_FILE_TEST)




    '''
        TECH networks
    '''
    OUT = '../output/TECH'

    for net_type in INPUT_FILE:
        for NUM_SETS  in SAMPLINGS_SETS:
            
            # create arrays 
            all_errors_train = []
            all_errors_test = []    
            aver_error_train = []
            aver_error_test = []

            # run  for all datasets
            for i in range(NUM_SETS):

                DATA_TRAIN = '../data/input_' + net_type + '/' + str(NUM_SETS) + '/train_' + str(i) + "_.data"
                DATA_TEST  = '../data/input_' + net_type + '/' + str(NUM_SETS) +'/test_' + str(i) + "_.data"

                # HERE IS THE DIFFERENCE FOR EACH NET
                X_train, Y_train = tech.load_data(DATA_TRAIN)
                X_test, Y_test = tech.load_data(DATA_TEST)

                print 'Calculating adaboost for set ' + DATA_TRAIN 
                score_train, score_test = classifier.run_adaboost(X_train, Y_train, T, X_test)

                print 'Calculating errors ...'        
                error_train = calculate_error(T, score_train, Y_train)    
                error_test = calculate_error(T, score_test, Y_test)
                all_errors_train.append(error_train)    
                all_errors_test.append(error_test)
           

            # calculates the average errors
            print 'Calculating errors ...'  
            for j in range(T):
                a_e_train = 0
                a_e_test = 0
                for i in range(NUM_SETS):
                    a_e_train += all_errors_train[i][j]
                    a_e_test += all_errors_test[i][j]
                
                aver_error_train.append(a_e_train/NUM_SETS)
                aver_error_test.append(a_e_test/NUM_SETS)
          

            # save to file to plot
            print 'Saving final files ...'  
            OUTPUT_FILE_TRAIN = OUT + '_train_' + net_type + str(NUM_SETS) + '_.data' 
            OUTPUT_FILE_TEST =  OUT + '_test_'   + net_type + str(NUM_SETS) + '_.data' 
            
            save_result_final(aver_error_train, OUTPUT_FILE_TRAIN)
            save_result_final(aver_error_test, OUTPUT_FILE_TEST)









    '''
        SOCIAL networks
    '''
    OUT = '../output/SOCIAL'

    for net_type in INPUT_FILE:
        for NUM_SETS  in SAMPLINGS_SETS:
            
            # create arrays 
            all_errors_train = []
            all_errors_test = []    
            aver_error_train = []
            aver_error_test = []

            # run  for all datasets
            for i in range(NUM_SETS):

                DATA_TRAIN = '../data/input_' + net_type + '/' + str(NUM_SETS) + '/train_' + str(i) + "_.data"
                DATA_TEST  = '../data/input_' + net_type + '/' + str(NUM_SETS) +'/test_' + str(i) + "_.data"

                # HERE IS THE DIFFERENCE FOR EACH NET
                X_train, Y_train = social.load_data(DATA_TRAIN)
                X_test, Y_test = social.load_data(DATA_TEST)

                print 'Calculating adaboost for set ' + DATA_TRAIN 
                score_train, score_test = classifier.run_adaboost(X_train, Y_train, T, X_test)

                print 'Calculating errors ...'        
                error_train = calculate_error(T, score_train, Y_train)    
                error_test = calculate_error(T, score_test, Y_test)
                all_errors_train.append(error_train)    
                all_errors_test.append(error_test)
           

            # calculates the average errors
            print 'Calculating errors ...'  
            for j in range(T):
                a_e_train = 0
                a_e_test = 0
                for i in range(NUM_SETS):
                    a_e_train += all_errors_train[i][j]
                    a_e_test += all_errors_test[i][j]
                
                aver_error_train.append(a_e_train/NUM_SETS)
                aver_error_test.append(a_e_test/NUM_SETS)
          

            # save to file to plot
            print 'Saving final files ...'  
            OUTPUT_FILE_TRAIN = OUT + '_train_' + net_type + str(NUM_SETS) + '_.data' 
            OUTPUT_FILE_TEST =  OUT + '_test_'   + net_type + str(NUM_SETS) + '_.data' 
            
            save_result_final(aver_error_train, OUTPUT_FILE_TRAIN)
            save_result_final(aver_error_test, OUTPUT_FILE_TEST)




        print 'Done!!!'


if __name__ == '__main__':
    main()
