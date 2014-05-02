#!/usr/bin/python
# marina von steinkirch @2014
# steinkirch at gmail

''' This program shows the application of boosting for weak
    classifiers given by decision stumps '''


import numpy as np
from adaboost import AdaBoost
from decision_stump import DecisionStump
from error import calculate_error

INPUT_FILE = ["sampled"]
SAMPLINGS_SETS = [300, 200, 100, 50]
PERCENTAGE = 0.9 # percentage for training and test sets


def load_data(datafile_name):
     ''' Load the data and separate it by feature
         and labels '''
     data = np.loadtxt(datafile_name, delimiter = ',')

     # features
     ''' X will be an array with each of the 6 features
         in 6 columns, and each row a data entry '''
     X = data[:,:10] 

     # label
     ''' The last column of the data is the "selector"  
         field used to split data into two sets, and we
         use it as a label, setting 2 -> -1 '''
         # THIS IS WHERE EVERY NETWORK IS DIFFERENT
     Y = data[:,-1]
     Y[Y==1] = -1  
     Y[Y==2] = -1  
     Y[Y==3] = -1 
     Y[Y==4] = 1 
 
     return X, Y



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
    T = 80  

    for net_type in INPUT_FILE:
        for NUM_SETS  in SAMPLINGS_SETS:
            
            # create arrays 
            all_errors_train = []
            all_errors_test = []    
            aver_error_train = []
            aver_error_test = []

            # run  for all datasets
            for i in range(NUM_SETS):

                DATA_TRAIN = './input_' + net_type + '/' + str(NUM_SETS) + '/train_' + str(i) + "_.data"
                DATA_TEST  = './input_' + net_type + '/' + str(NUM_SETS) +'/test_' + str(i) + "_.data"

                X_train, Y_train = load_data(DATA_TRAIN)
                X_test, Y_test = load_data(DATA_TEST)

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
            OUTPUT_FILE_TRAIN = './output/tech_f10_train_' + net_type + str(NUM_SETS) + '_.data' 
            OUTPUT_FILE_TEST = './output/tech_f10_test_'   + net_type + str(NUM_SETS) + '_.data' 
            
            save_result_final(aver_error_train, OUTPUT_FILE_TRAIN)
            save_result_final(aver_error_test, OUTPUT_FILE_TEST)

        print 'Done!!!'


if __name__ == '__main__':
    main()
