
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
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import RandomizedLogisticRegression
from constants import  PERCENTAGE, INPUT_FILE, OUTPUT_FOLDER,  NORM


def save_result_final(error_train, error_test, output_file, norm):
    with open(output_file, "a") as f:
        f.write( norm  + ',    atrain: ' + str(round(error_train,3)) + ",   atest: "  + str(round(error_test,3)) +"\n")


def save_result_features(score, output_file_feature,  norm):
     with open(output_file_feature, "a") as f:
        f.write(norm + '    ')
        for feat in score:
            f.write(str(round(feat,3)) + '   ')
        f.write("\n")



def find_better_features(data, truth):
    model = RandomizedLogisticRegression()
    model = model.fit(data, truth) 
    return model



def fit_model(data, truth):
    model = linear_model.LogisticRegression(penalty='l1', C=10e5)
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

    folder = OUTPUT_FOLDER + 'log_reg/'
    if not os.path.exists(folder):
       os.makedirs(folder) 
    output_file = folder + 'results.out'
    with open(output_file, "w") as f:
       f.write("# RESULTS FOR LOGISTIC REGRESSION, PERCENTAGE: " + str(PERCENTAGE)  + "\n")

    output_file_feature = folder + 'results_features.out'
    with open(output_file_feature, "w") as f:
       f.write("# RESULTS FEATURES, PERCENTAGE: " + str(PERCENTAGE)  + "\n")  
       f.write('Type    Siz    Ord    Ass    Tra    Deg    Cor    NTr    NCl    Cnu    Clu    Eco    Ecc    Dia    Bet    Den    Rad    Scl    Com    Pag    Cen \n')  

    # for each normalization:
    for norm in NORM:

        # get input and output file paths
        input_train = INPUT_FILE + "train_" + str(PERCENTAGE) + '_' + norm + ".data" 
        input_test = INPUT_FILE + "test_" + str(PERCENTAGE) + '_' + norm + ".data"  

        # get data
        X_train, Y_train = load_data(input_train)
        X_test, Y_test = load_data(input_test)

        print 'Calculating for set ' + input_train 

         # classifier 
        model = fit_model(X_train, Y_train)
        error_train = classify_data(model, X_train, Y_train) 
        error_test = classify_data(model, X_test, Y_test)
        save_result_final(error_train, error_test, output_file,  norm)

        # best feature
        model = find_better_features(X_train, Y_train)
        save_result_features(model.scores_, output_file_feature,  norm)


    print 'Results saved at ' +  OUTPUT_FOLDER
    print 'Done!!!'


if __name__ == '__main__':
    main()
   
   



 