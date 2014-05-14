
#!/usr/bin/env python
 
__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"


''' Uses the support vector machine machinery to our complex networks '''


import os
import sklearn.svm  as sklsvm
import numpy as np
from constants import PERCENTAGE, INPUT_FOLDER, OUTPUT_FOLDER,  NORM, NUM_SETS



def write_accuracies(acc_train, acc_test, output_file, norm_type, set_number, bol_with_outlier):
 
    ''' Save the results for accuracy in a file '''

    with open(output_file, "a") as f:

        f.write(norm_type[:4] + ", " +  str(set_number) + ', ' + str(bol_with_outlier) + ', '  + \
            str(round(acc_train,3)) + ", " + str(round(acc_test, 3)) + "\n")




def fit_model_linear(data, truth, Chere=10e5):  
    ''' Linear Support Vector Classification.
    http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html
    Dual select the algorithm to either solve the dual or primal optimization problem. 
    Prefer dual=False when n_samples > n_features. '''

    model = sklsvm.LinearSVC(dual=False, C=Chere) 

    model = model.fit(data, truth) 

    return model




def fit_model_SVC(data, truth):
    ''' Support Vector Classification. The implementations is a based on libsvm. 
    http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html '''

    model = sklsvm.SVC() 

    model = model.fit(data, truth) 

    return model   




def classify_data(model, data, truth):
    """ Returns the accuracy score. Same as the method 'score()'"""

    guesses = model.predict(data)

    right = np.sum(guesses == truth)

    return float(right) / truth.shape[0]
    



def load_data(datafile_name):
     ''' Load the data and separate it by feature and labels '''

     data = np.loadtxt(datafile_name, delimiter = ',')

     # features
     X = data[:,:-1]  

     # label
     Y = data[:,-1]

     return X, Y




def get_input_data(sett, set_number, norm_type,  bol_with_outlier):
    """ Return the name of the file for the parameters """

    if bol_with_outlier:

        return INPUT_FOLDER + 'together' + str(set_number) + "_" + sett + "_" + str(PERCENTAGE) + '_' + \
         norm_type + '_with_outlier' + ".data"

    else:

        return INPUT_FOLDER + 'together' + str(set_number) +  "_" + sett + "_" + str(PERCENTAGE) + '_' + \
        norm_type + ".data"





def main():

    ''' Set input/output variables '''

    folder = OUTPUT_FOLDER + 'log_reg/'

    if not os.path.exists(folder):
       os.makedirs(folder) 

    output_file = folder + 'results.out'

    with open(output_file, "w") as f:

        f.write("# SVM RESULTS, TRAIN/TEST FRACTION: " + str(PERCENTAGE)  + "\n")

        f. write("# Normalization,  Set set_number, Outliers?,  Accu. Train, Accu Test\n")




    ''' Loop to each case file:
        - normalization type 
        - set order number 
        - with outlier or without outlier '''

    classification = []
    
    for norm_type in NORM:

        for set_number in range(1, NUM_SETS+1):


            ''' with outlier '''

            bol_with_outlier = True

            # get input and output file 
            input_train =  get_input_data('train', set_number, norm_type,  bol_with_outlier)

            input_test = get_input_data('test', set_number, norm_type,  bol_with_outlier) 


            # get data
            X_train, Y_train = load_data(input_train)

            X_test, Y_test = load_data(input_test)


            # classify linear and save
            model = fit_model_linear(X_train, Y_train)

            acc_train = classify_data(model, X_train, Y_train) 

            acc_test = classify_data(model, X_test, Y_test)

            classification.append(str(round(acc_test,3))  +', ' + norm_type + ', ' + str(set_number) + ', ' + \
                str(bol_with_outlier)[0] + '\n') 

            write_accuracies(acc_train, acc_test, output_file,  'linear ' + norm_type, set_number, bol_with_outlier)


            # classify linear and save
            model = fit_model_SVC(X_train, Y_train)

            acc_train = classify_data(model, X_train, Y_train) 

            acc_test = classify_data(model, X_test, Y_test)

            classification.append(str(round(acc_test,3))  +', ' + norm_type + ', ' + str(set_number) + ', ' + \
                str(bol_with_outlier)[0] + '\n') 

            write_accuracies(acc_train, acc_test, output_file,  'SVC ' + norm_type, set_number, bol_with_outlier)



            ''' withOUT outlier '''

            bol_with_outlier = False

            # get input and output file 
            input_train =  get_input_data('train', set_number, norm_type,  bol_with_outlier)

            input_test = get_input_data('test', set_number, norm_type,  bol_with_outlier) 


            # get data
            X_train, Y_train = load_data(input_train)

            X_test, Y_test = load_data(input_test)


            # classify linear and save
            model = fit_model_linear(X_train, Y_train)

            acc_train = classify_data(model, X_train, Y_train) 

            acc_test = classify_data(model, X_test, Y_test)

            classification.append(str(round(acc_test,3))  +', ' + norm_type + ', ' + str(set_number) + ', ' + \
                str(bol_with_outlier)[0] + '\n') 

            write_accuracies(acc_train, acc_test, output_file,  'linear ' + norm_type, set_number, bol_with_outlier)


            # classify linear and save
            model = fit_model_SVC(X_train, Y_train)

            acc_train = classify_data(model, X_train, Y_train) 

            acc_test = classify_data(model, X_test, Y_test)

            classification.append(str(round(acc_test,3))  +', ' + norm_type + ', ' + str(set_number) + ', ' + \
                str(bol_with_outlier)[0] + '\n') 

            write_accuracies(acc_train, acc_test, output_file,  'SVC ' + norm_type, set_number, bol_with_outlier)






    ''' Order the best classifications and save in the end of the file, to help analysis'''
    classification.sort()

    with open(output_file + 'good_feature', "a") as f:

        f.write("\n\n\nClassification\n\n")

        for feat in classification:

            f.write(feat + '\n')

        f.write("\n")


          

    print 'Results saved at ' +  folder

    print 'Done!!!'




if __name__ == '__main__':
    main()
   
   



 