
#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

''' This program shows the application svm to classify our complex networks '''


import os
import sklearn.svm  as sklsvm
import numpy as np
from constants import  PERCENTAGE, INPUT_FOLDER, OUTPUT_FOLDER,  NORM, NUM_SETS


def save_result_final(error_train, error_test, output_file, norm, number, with_outlier):
    ''' Save in a file the final result '''

    with open(output_file, "a") as f:
        f.write(norm[:10] + "           " +  str(number) + '           '  + str(with_outlier)[0] + '                '  + \
            str(round(error_train,3)) + "        " + str(round(error_test, 3)) + "\n")

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



def get_input_data(sett, number, norm,  with_outlier):
    if with_outlier:
        return INPUT_FOLDER + 'together' + str(number) + "_" + sett + "_" + str(PERCENTAGE) + '_' + norm + '_with_outlier' + ".data"
    else:
        return INPUT_FOLDER + 'together' + str(number) +  "_" + sett + "_" + str(PERCENTAGE) + '_' + norm + ".data"



def main():
    classification = []
    svm_folder = OUTPUT_FOLDER + 'svm/'
    if not os.path.exists(svm_folder):
       os.makedirs(svm_folder) 
    output_file = svm_folder + 'results.out'
    with open(output_file, "w") as f:
        f.write("# SVM RESULTS, TRAIN/TEST FRACTION: " + str(PERCENTAGE)  + "\n")
        f. write("# Normalization - Set Number - Outliers?      Accu. Train   Accu Test\n")


    # for each normalization:
    for norm in NORM:


        # for each set
        for number in range(1, NUM_SETS+1):

            ''' with with_outlier '''
            with_outlier = True
            # get input and output file paths
            input_train =  get_input_data('train', number, norm,  with_outlier)
            input_test = get_input_data('test', number, norm,  with_outlier)


            # get data
            X_train, Y_train = load_data(input_train)
            X_test, Y_test = load_data(input_test)


            print 'Calculating svm for with  normalization ' + norm + ' and set ' + str(number)

             # classifier linear
            model = fit_model(X_train, Y_train)
            error_train = classify_data(model, X_train, Y_train) 
            error_test = classify_data(model, X_test, Y_test)
            save_result_final(error_train, error_test, output_file, 'linear ' + norm, number, with_outlier)
            classification.append(str(round(error_test,3))  +', ' + 'linear ' + str(norm) + ', ' + str(number) + ', ' + str(with_outlier)[0] + '\n') 

            # classifier SVC
            model = fit_model_SVC(X_train, Y_train)
            error_train = classify_data(model, X_train, Y_train) 
            error_test = classify_data(model, X_test, Y_test)
            save_result_final(error_train, error_test, output_file, '   SVC ' + norm, number, with_outlier)


            ''' with no outlier '''
            with_outlier = False
            # get input and output file paths
            input_train =  get_input_data('train', number, norm,  with_outlier)
            input_test = get_input_data('test', number, norm,  with_outlier)


            # get data
            X_train, Y_train = load_data(input_train)
            X_test, Y_test = load_data(input_test)


             # classifier linear
            model = fit_model(X_train, Y_train)
            error_train = classify_data(model, X_train, Y_train) 
            error_test = classify_data(model, X_test, Y_test)
            save_result_final(error_train, error_test, output_file, 'linear ' + norm, number, with_outlier)
            classification.append(str(round(error_test,3))  +', ' + 'linear ' + str(norm) + ', ' + str(number) + ', ' + str(with_outlier)[0] + '\n') 

            # classifier SVC
            model = fit_model_SVC(X_train, Y_train)
            error_train = classify_data(model, X_train, Y_train) 
            error_test = classify_data(model, X_test, Y_test)
            save_result_final(error_train, error_test, output_file, '   SVC ' + norm, number, with_outlier)
            classification.append(str(round(error_test,3))  +', ' + 'SVC ' + str(norm) + ', ' + str(number) + ', ' + str(with_outlier)[0] + '\n') 


    #find best classfiers
    classification.sort()
    with open(output_file + 'good_classification', "w") as f:
        f.write("\n\n\nClassification\n\n")
        for feat in classification:
            f.write(feat + '\n')
        f.write("\n")


    print 'Results saved at ' +  svm_folder
    print 'Done!!!'


if __name__ == '__main__':
    main()
   
   



 