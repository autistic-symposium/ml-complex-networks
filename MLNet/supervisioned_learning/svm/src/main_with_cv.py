#!/usr/bin/python
# marina von steinkirch @2014
# steinkirch at gmail

''' This program shows the application of svm for sampled '''


import sklearn.svm  as sklsvm
import numpy as np
from constants import  SAMPLINGS_SETS, PERCENTAGE


INPUT_FILE = ['all_neat', 'all_neat_n1500', 'all_neat_n2000', 'all_neat_n500', "all_nets_entire"]#,  'all_neat_n500', 'all_neat_n3000',"sampled"]



def load_data(datafile_name):
     ''' Load the data and separate it by feature
         and labels '''
     data = np.loadtxt(datafile_name, delimiter = ',')

     # features
     X = data[:,:-1] 

     # label
     Y = data[:,-1]
     return X, Y


def save_result_final(final, output_file):
    ''' Save in a file the final result '''

    with open(output_file, "w") as f:
        for i in range(len(final)):
            f.write(str(final[i]) + ',' + str(i+1) + "\n")


def fit_model_linear(data, truth):
    model = sklsvm.LinearSVC() 
    model = model.fit(data, truth) 
    return model


def classify_data(model, data, truth):
    guesses = model.predict(data)
    right = np.sum(guesses == truth)
    return float(right) / truth.shape[0]
    


def main():


    NET_NAMES = ['bio', 'info',  'social', 'tech']
    
    for i,net_name in enumerate(NET_NAMES):
        print 'Starting ' + net_name + '...'
        for net_type in INPUT_FILE:
            for NUM_SETS  in SAMPLINGS_SETS:
    	    aver_error_train = []
                aver_error_test = []

                # run  for all datasets
                for i in range(NUM_SETS):

                    print 'Calculating for nsets ', i

                    DATA_TRAIN = '../data/' + net_type + '/' + str(NUM_SETS) + '/train_' + str(i) + "_.data"
                    DATA_TEST  = '../data/' + net_type + '/' + str(NUM_SETS) +'/test_' + str(i) + "_.data"

                    # HERE IS THE DIFFERENCE FOR EACH NET
                    learn_data_X, learn_data_Y = load_data(DATA_TRAIN)
                    predict_data_X, predict_data_Y = load_data(DATA_TEST)

                    # classifier
                    model = fit_model_linear(learn_data_X, learn_data_Y)
                    accuracy_train  = classify_data(model, learn_data_X, learn_data_Y) 
                    accuracy_test = classify_data(model, predict_data_X, predict_data_Y)
                                           
                    aver_error_train.append(accuracy_train)    
                    aver_error_test.append(accuracy_test)    

                # save to file to plot
                print 'Saving final files ...'  
                OUTPUT_FILE_TRAIN = '../output/' + net_name + '_train_' + net_type + str(NUM_SETS) + '_.data' 
                OUTPUT_FILE_TEST =  '../output/' + net_name +  + '_test_'   + net_type + str(NUM_SETS) + '_.data' 
                
                save_result_final(aver_error_train, OUTPUT_FILE_TRAIN)
                save_result_final(aver_error_test, OUTPUT_FILE_TEST)



    print 'Done!!!'




if __name__ == '__main__':
    main()
