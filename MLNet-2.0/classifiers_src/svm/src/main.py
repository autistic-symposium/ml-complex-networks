
#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

''' This program shows the application svm  '''


import os
import sklearn.svm  as sklsvm
import numpy as np
from constants import  PERCENTAGE, INPUT_FILE, OUTPUT_FOLDER,  NORM


def save_result_final(error_train, error_test, output_file, norm):
    ''' Save in a file the final result '''

    with open(output_file, "a") as f:
        f.write( norm  + ',    atrain: ' + str(round(error_train,3)) + ",   atest: "  + str(round(error_test,3)) +"\n")



def fit_model(data, truth, Chere=10e5):
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

    svm_folder = OUTPUT_FOLDER + 'svm/'
    if not os.path.exists(svm_folder):
       os.makedirs(svm_folder) 
    output_file = svm_folder + 'results.out'
    with open(output_file, "w") as f:
       f.write("# SVM RESULTS, PERCENTAGE: " + str(PERCENTAGE)  + "\n")


    # for each normalization:
    for norm in NORM:

        # get input and output file paths
        input_train = INPUT_FILE + "train_" + str(PERCENTAGE) + '_' + norm + ".data" 
        input_test = INPUT_FILE + "test_" + str(PERCENTAGE) + '_' + norm + ".data"  


        # get data
        X_train, Y_train = load_data(input_train)
        X_test, Y_test = load_data(input_test)

        print 'Calculating for set ' + input_train 

         # classifier linear
        model = fit_model(X_train, Y_train)
        error_train = classify_data(model, X_train, Y_train) 
        error_test = classify_data(model, X_test, Y_test)
        save_result_final(error_train, error_test, output_file, 'linear ' + norm)


        # classifier SVC
        model = fit_model_SVC(X_train, Y_train)
        error_train = classify_data(model, X_train, Y_train) 
        error_test = classify_data(model, X_test, Y_test)
        save_result_final(error_train, error_test, output_file, 'SVC ' + norm)


    print 'Results saved at ' +  OUTPUT_FOLDER
    print 'Done!!!'


if __name__ == '__main__':
    main()
   
   



 