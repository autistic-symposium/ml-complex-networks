
#!/usr/bin/env python
 
__author__ = "Mia Stein"
__email__ = ""


''' Performs logistic regression to our complex networks '''


import os
import numpy as np
from sklearn import linear_model
from constants import  PERCENTAGE, INPUT_FOLDER, OUTPUT_FOLDER, NORM, NUM_SETS, FEATURE_NAME




def write_accuracies(acc_train, acc_test, output_file, norm_type, set_number, bol_with_outlier):
 
    ''' Save the results for accuracy in a file '''

    with open(output_file, "a") as f:

        f.write(norm_type[:4] + ", " +  str(set_number) + ', ' + str(bol_with_outlier) + ', '  + \
            str(round(acc_train,3)) + ", " + str(round(acc_test, 3)) + "\n")





def write_features_weights(score, output_file_feature, norm_type, set_number, bol_with_outlier):

    ''' Save the results for each feature's weight in a file '''

    good_feature = []


    with open(output_file_feature, "a") as f:

        f.write(norm_type[:4] + ', ' + str(set_number) + ' , ' + str(bol_with_outlier)[:1] + ', ')

        for i, feature in enumerate(score):

            f.write(str(round(feature,1)) + '  ')

            if feature > 0.9:

                good_feature.append([norm_type[:4] + ', '   + str(set_number) +', '+ str(bol_with_outlier)[:1] + ', '\
                 + str(feature) + ', ' + str(FEATURE_NAME[i]) + ', '])

        f.write("\n")


    with open(output_file_feature + 'good_feature', "a") as f:

        for feature in good_feature:

            f.write(feature[0] + '\n')

        f.write("\n")





def find_better_features(data, truth, regularization=1e5, number_renor_models=200):
    '''Resample the train data and compute a Logistic Regression on each resampling 
    http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RandomizedLogisticRegression.html'''

    model = linear_model.RandomizedLogisticRegression(C=regularization, n_resampling=number_renor_models)

    model = model.fit(data, truth) 

    return model




def fit_model(data, truth, regularization=1e5, pen='l1'):
    """ Logistic Regression where the training algorithm uses a one-vs.-all (OvA) scheme 
    http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html """


    model = linear_model.LogisticRegression(penalty=pen, C=regularization)

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

        f.write("# LOG REG RESULTS, TRAIN/TEST FRACTION: " + str(PERCENTAGE)  + "\n")

        f. write("# norm_typealization - Set set_number - Include Outliers? - Accu. Train - Accu Test\n")


    output_file_feature = folder + 'results_features.out'

    with open(output_file_feature, "w") as f:

        f.write("# LOG REG RESULTS, TRAIN/TEST FRACTION: " + str(PERCENTAGE)  + "\n") 

        f.write('# Nor Set OL?  Siz  Ord  Ass  Tra  Deg  Cor  NTr  NCl  Cnu  Clu  Eco  Ecc  Dia  Bet  Den  Rad  Scl  Com  Pag  Cen \n')  



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


            # classify and save
            model = fit_model(X_train, Y_train)

            acc_train = classify_data(model, X_train, Y_train) 

            acc_test = classify_data(model, X_test, Y_test)

            classification.append(str(round(acc_test,3))  +', ' + str(norm_type) + ', ' + str(set_number) + ', ' + str(bol_with_outlier)[0] + '\n') 

            write_accuracies(acc_train, acc_test, output_file,  norm_type, set_number, bol_with_outlier)


            # best feature and save
            model = find_better_features(X_train, Y_train)

            write_features_weights(model.scores_, output_file_feature,  norm_type, set_number, bol_with_outlier)




            ''' without outlier '''

            bol_with_outlier = False

            # get input and output file paths
            input_train =  get_input_data('train', set_number, norm_type,  bol_with_outlier)

            input_test = get_input_data('test', set_number, norm_type,  bol_with_outlier) 


            # get data
            X_train, Y_train = load_data(input_train)

            X_test, Y_test = load_data(input_test)


             # classifier and save
            model = fit_model(X_train, Y_train)

            acc_train = classify_data(model, X_train, Y_train) 

            acc_test = classify_data(model, X_test, Y_test)

            write_accuracies(acc_train, acc_test, output_file,  norm_type, set_number, bol_with_outlier)

            classification.append(str(round(acc_test,3))  +', ' + str(norm_type) + ', ' + str(set_number) + ', ' + str(bol_with_outlier)[0] + '\n') 


            # best feature and save
            model = find_better_features(X_train, Y_train)

            write_features_weights(model.scores_, output_file_feature,  norm_type, set_number, bol_with_outlier)




    ''' Order the best classifications and save in the end of the file, to help analysis'''
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
   
   



 