#!/usr/bin/python
# marina von steinkirch @2014
# steinkirch at gmail

''' This program shows the application svm for entire sets '''

import random
import sklearn.svm  as sklsvm
import numpy as np


INPUT_FILE = ['all_neat', 'all_neat_n1500', 'all_neat_n2000', 'all_neat_n500', "all_nets_entire"]



def save_result_final(net_type, output_file, aver_error, aver_error_SVC):
    ''' Save in a file the final result '''

    with open(output_file, "a") as f:
        f.write(net_type +',' + str(aver_error) + ","  + str(aver_error_SVC) + "\n")


def fit_model(data, truth, Chere=1.0):
    # Dual select the algorithm to either solve the dual or primal optimization problem. Prefer dual=False when n_samples > n_features.
    model = sklsvm.LinearSVC(dual=False, C=Chere) 
    model = model.fit(data, truth) 
    return model


def fit_model_SVC(data, truth):
    model = sklsvm.SVC() 
    model = model.fit(data, truth) 
    return model   


def classify_data(model, data, truth):
    guesses = model.predict(data)
    right = np.sum(guesses == truth)
    return float(right) / truth.shape[0]
    

def load_data(datafile_name):
     ''' Load the data and separate it by feature
         and labels '''
     data = np.loadtxt(datafile_name, delimiter = ',')

     # features
     X = data[:,:-1] 

     # label
     Y = data[:,-1]
     return X, Y




def main():


    OUTPUT_FILE_TRAIN = '../output/ALL_NO_CV_train.data'
    with open(OUTPUT_FILE_TRAIN , "w") as f:
        f.write('# net name, net number, dataset, accur LinearSVC, accur SVC(rgb)\n')

    OUTPUT_FILE_TEST = '../output/ALL_NO_CV_test.data'
    with open(OUTPUT_FILE_TEST , "w") as f:
        f.write('# net name, net number, dataset, accur LinearSVC, accur SVC(rgb)\n')
        
   
    for net_type in INPUT_FILE:
        DATA_TRAIN = '../data/no_cv/' + net_type + '_train.data' 
        DATA_TEST = '../data/no_cv/' + net_type + '_test.data' 

        # HERE IS THE DIFFERENCE FOR EACH NET
        learn_data_X, learn_data_Y = load_data(DATA_TRAIN)
        predict_data_X, predict_data_Y = load_data(DATA_TEST)

        # classifier linear
        model = fit_model(learn_data_X, learn_data_Y)
        aver_error_train = classify_data(model, learn_data_X, learn_data_Y) 
        aver_error_test = classify_data(model, predict_data_X, predict_data_Y)

        # classifier SVC
        model_SVC = fit_model_SVC(learn_data_X, learn_data_Y)
        aver_error_train_SVC = classify_data(model_SVC, learn_data_X, learn_data_Y) 
        aver_error_test_SVC = classify_data(model_SVC, predict_data_X, predict_data_Y)

        # Saving
        save_result_final(net_type, OUTPUT_FILE_TRAIN, aver_error_train, aver_error_train_SVC)
        save_result_final(net_type, OUTPUT_FILE_TEST, aver_error_test, aver_error_test_SVC)



    print 'Done!!!'




if __name__ == '__main__':
    main()

