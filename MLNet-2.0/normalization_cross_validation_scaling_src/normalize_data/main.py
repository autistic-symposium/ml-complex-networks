#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"


import  os
import numpy as np
from sklearn import preprocessing
from constants import PERCENTAGE, OUTPUT_FOLDER, INPUT_FOLDER, NORM_TYPE


def save_results(X, Y, output_file):
    ''' Save in a file the results of spliting'''

    with open(output_file , "w") as f:
        for i in range(len(X)):
            for j in range(len(X[i])):
                f.write(str(X[i][j]) + ',')
            f.write(str(Y[i])  + "\n")




def load_data(datafile_name):
     ''' Load the data and separate it by feature
         and labels '''
     data = np.loadtxt(datafile_name, delimiter = ',')

     # features
     X = data[:,:-1] 

     # label
     Y = data[:,-1]
     return X, Y



def create_input_file(ntype, number, with_outlier):
    if with_outlier:
        return INPUT_FOLDER + "together" + str(number) + '_with_outlier_' + ntype + "_" + str(PERCENTAGE) + ".data" 
    else:
        return INPUT_FOLDER + "together" + str(number) + '_' + ntype + "_" + str(PERCENTAGE) + ".data"        


def create_output_file(dtype, number, ntype, with_outlier):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER) 
    if with_outlier:
        return OUTPUT_FOLDER + "together" + number + "_" + ntype + "_" + str(PERCENTAGE) + "_" + dtype + "_with_outlier.data" 
    else:
        return OUTPUT_FOLDER + "together" + number + "_" + ntype + "_" + str(PERCENTAGE) + "_" + dtype + ".data" 

def main():

    ''' without outliers '''

    for number in range(1,6) :
        with_outlier = False

        # get paths and create output folder
        input_train = create_input_file('train', str(number), with_outlier)
        input_test = create_input_file('test', str(number), with_outlier)
               
        output_train_g = create_output_file(NORM_TYPE[0], str(number), 'train', with_outlier)
        output_test_g =  create_output_file(NORM_TYPE[0], str(number), 'test',with_outlier)
        output_train_m =  create_output_file(NORM_TYPE[1], str(number), 'train', with_outlier)
        output_test_m =  create_output_file(NORM_TYPE[1], str(number), 'test', with_outlier)
        output_train_n =  create_output_file(NORM_TYPE[2], str(number), 'train', with_outlier)
        output_test_n =  create_output_file(NORM_TYPE[2], str(number), 'test',with_outlier)


        # open files
        learn_data_X, learn_data_Y = load_data(input_train)
        predict_data_X, predict_data_Y = load_data(input_test)


        '''
           No normlization
        '''
        # save results
        save_results(learn_data_X, learn_data_Y, output_train_n)
        save_results(predict_data_X, predict_data_Y, output_test_n)


        '''
           Run normalizer xmin, xmax
        '''
        # run normalizer gaussian
        scaler = preprocessing.StandardScaler().fit(learn_data_X)
        learn_data_X_1 = scaler.transform(learn_data_X)
        predict_data_X_1 = scaler.transform(predict_data_X) 

        # save results
        save_results(learn_data_X_1, learn_data_Y, output_train_g)
        save_results(predict_data_X_1, predict_data_Y, output_test_g)


        '''
           Run normalizer xmin, xmax
        '''
        min_max_scaler = preprocessing.MinMaxScaler()
        learn_data_X_2 = min_max_scaler.fit_transform(learn_data_X) 
        predict_data_X_2 = min_max_scaler.transform(predict_data_X)
     
        # save results
        save_results(learn_data_X_2, learn_data_Y, output_train_m)
        save_results(predict_data_X_2, predict_data_Y, output_test_m)




    ''' with outliers '''
    with_outlier = True

    for number in range(1,6) :
        
        # get paths and create output folder
        input_train = create_input_file('train', str(number), with_outlier)
        input_test = create_input_file('test', str(number), with_outlier)
               
        output_train_g = create_output_file(NORM_TYPE[0], str(number), 'train', with_outlier)
        output_test_g =  create_output_file(NORM_TYPE[0], str(number), 'test', with_outlier)
        output_train_m =  create_output_file(NORM_TYPE[1], str(number), 'train', with_outlier)
        output_test_m =  create_output_file(NORM_TYPE[1], str(number), 'test', with_outlier)
        output_train_n =  create_output_file(NORM_TYPE[2], str(number), 'train',with_outlier)
        output_test_n =  create_output_file(NORM_TYPE[2], str(number), 'test', with_outlier)


        # open files
        learn_data_X, learn_data_Y = load_data(input_train)
        predict_data_X, predict_data_Y = load_data(input_test)


        '''
           No normlization
        '''
        # save results
        save_results(learn_data_X, learn_data_Y, output_train_n)
        save_results(predict_data_X, predict_data_Y, output_test_n)


        '''
           Run normalizer xmin, xmax
        '''
        # run normalizer gaussian
        scaler = preprocessing.StandardScaler().fit(learn_data_X)
        learn_data_X_1 = scaler.transform(learn_data_X)
        predict_data_X_1 = scaler.transform(predict_data_X) 

        # save results
        save_results(learn_data_X_1, learn_data_Y, output_train_g)
        save_results(predict_data_X_1, predict_data_Y, output_test_g)


        '''
           Run normalizer xmin, xmax
        '''
        min_max_scaler = preprocessing.MinMaxScaler()
        learn_data_X_2 = min_max_scaler.fit_transform(learn_data_X) 
        predict_data_X_2 = min_max_scaler.transform(predict_data_X)
     
        # save results
        save_results(learn_data_X_2, learn_data_Y, output_train_m)
        save_results(predict_data_X_2, predict_data_Y, output_test_m)



    print 'Results saved at ' + OUTPUT_FOLDER

    print 'Done!'


   


if __name__ == '__main__':
    main()
