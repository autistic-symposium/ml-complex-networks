
#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

''' This performs logistic regression to our networks '''


import os
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import RandomizedLogisticRegression
from constants import  PERCENTAGE, INPUT_FOLDER, OUTPUT_FOLDER,  NORM, NUM_SETS, FEATURE_NAME


def save_result_final(error_train, error_test, output_file, norm, number, with_outlier):
    ''' Save in a file the final result '''

    with open(output_file, "a") as f:
        f.write(norm[:4] + "         -  " +  str(number) + '      -     '  + str(with_outlier) + '        -        '  + \
            str(round(error_train,3)) + "     -   " + str(round(error_test, 3)) + "\n")


def save_result_features(score, output_file_feature,  norm, number, with_outlier):
    good_feature = []
    with open(output_file_feature, "a") as f:
        f.write(norm[:4] + '  '   + str(number) +'  '+ str(with_outlier)[:1] + '     ')
        for i, feat in enumerate(score):
            f.write(str(round(feat,1)) + '  ')
            if feat > 0.9:
                good_feature.append([norm[:4] + ', '   + str(number) +', '+ str(with_outlier)[:1] + ', ' + str(feat) + ', ' + str(FEATURE_NAME[i]) + ', '])
        f.write("\n")

    with open(output_file_feature + 'good_feature', "a") as f:
        for feat in good_feature:
            f.write(feat[0] + '\n')
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


def get_input_data(sett, number, norm,  with_outlier):
    if with_outlier:
        return INPUT_FOLDER + 'together' + str(number) + "_" + sett + "_" + str(PERCENTAGE) + '_' + norm + '_with_outlier' + ".data"
    else:
        return INPUT_FOLDER + 'together' + str(number) +  "_" + sett + "_" + str(PERCENTAGE) + '_' + norm + ".data"


def main():
 
    classification = []

    folder = OUTPUT_FOLDER + 'log_reg/'
    if not os.path.exists(folder):
       os.makedirs(folder) 
    output_file = folder + 'results.out'
    with open(output_file, "w") as f:
        f.write("# LOG REG RESULTS, TRAIN/TEST FRACTION: " + str(PERCENTAGE)  + "\n")
        f. write("# Normalization - Set Number - Include Outliers? - Accu. Train - Accu Test\n")


    output_file_feature = folder + 'results_features.out'
    with open(output_file_feature, "w") as f:
        f.write("# LOG REG RESULTS, TRAIN/TEST FRACTION: " + str(PERCENTAGE)  + "\n") 
        f.write('# Nor Set OL?  Siz  Ord  Ass  Tra  Deg  Cor  NTr  NCl  Cnu  Clu  Eco  Ecc  Dia  Bet  Den  Rad  Scl  Com  Pag  Cen \n')  


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


            print 'Calculating logistic regression for data with normalization ' + norm + ' and set ' + str(number)

             # classifier 
            model = fit_model(X_train, Y_train)
            error_train = classify_data(model, X_train, Y_train) 
            error_test = classify_data(model, X_test, Y_test)
            classification.append(str(round(error_test,3))  +', ' + str(norm) + ', ' + str(number) + ', ' + str(with_outlier)[0] + '\n') 

            save_result_final(error_train, error_test, output_file,  norm, number, with_outlier)

            # best feature
            model = find_better_features(X_train, Y_train)
            save_result_features(model.scores_, output_file_feature,  norm, number, with_outlier)


            ''' with with_outlier '''
            with_outlier = False
            # get input and output file paths
            input_train =  get_input_data('train', number, norm,  with_outlier)
            input_test = get_input_data('test', number, norm,  with_outlier) 

            # get data
            X_train, Y_train = load_data(input_train)
            X_test, Y_test = load_data(input_test)


             # classifier 
            model = fit_model(X_train, Y_train)
            error_train = classify_data(model, X_train, Y_train) 
            error_test = classify_data(model, X_test, Y_test)
            save_result_final(error_train, error_test, output_file,  norm, number, with_outlier)
            classification.append(str(round(error_test,3))  +', ' + str(norm) + ', ' + str(number) + ', ' + str(with_outlier)[0] + '\n') 

            # best feature
            model = find_better_features(X_train, Y_train)
            save_result_features(model.scores_, output_file_feature,  norm, number, with_outlier)

    #find best classfiers
    classification.sort()
    with open(output_file_feature + 'good_feature', "a") as f:
        f.write("\n\n\nClassification\n\n")
        for feat in classification:
            f.write(feat + '\n')
        f.write("\n")


          

    print 'Results saved at ' +  folder
    print 'Done!!!'


if __name__ == '__main__':
    main()
   
   



 