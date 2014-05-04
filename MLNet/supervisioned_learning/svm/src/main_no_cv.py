#!/usr/bin/python
# marina von steinkirch @2014
# steinkirch at gmail

''' This program shows the application svm for entire sets '''

import random
import sklearn.svm  as sklsvm
import numpy as np
import bio
import tech 
import info 
import social


PERCENTAGE = 0.8
INPUT_FILE = ['all_neat',  'all_neat_n2000', "all_nets_entire"]#,  'all_neat_n1500','all_neat_n500', 'all_neat_n3000',"sampled"]



def save_result_final(final, score, output_file):
    ''' Save in a file the final result '''

    with open(output_file, "w") as f:
        for i in range(len(final)):
            f.write(str(final[i]) + "," + str(score[i])+ ',' + str(i+1) + "\n")



def fit_model(data, truth):
    model = sklsvm.LinearSVC() 
    model = model.fit(data, truth) 
    return model



def classify_data(model, data, truth):
    guesses = model.predict(data)
    right = np.sum(guesses == truth)
    return float(right) / truth.shape[0]
    


def save_result_split(final, name):
    with open(name , "w") as f:
        for i in range(len(final)):
            f.write(str(final[i]) + "\n")



def split_data(input_file, output_file):
    ''' split data for training and test sets '''

    with open(input_file, "rb") as f:
        data = f.read().split('\n')

    border = int(PERCENTAGE*len(data))
    random.shuffle(data)

    train_data = data[:border][:]
    test_data = data[border:][:]

    OUTPUT_FILE_TRAIN  = output_file + "_train_.data"
    OUTPUT_FILE_TEST   = output_file + "_test_.data"

    save_result_split(train_data, OUTPUT_FILE_TRAIN)
    save_result_split(test_data, OUTPUT_FILE_TEST)



def main():

    for net_type in INPUT_FILE:
        input_file = '../data/no_cv/' + net_type + '.data' 
        output_file = '../data/no_cv/' + net_type
        split_data(input_file, output_file)
   

    '''
        INFO networks
    '''
    OUT = '../output/INFO_NO_CV_'
    print 'Starting info nets...'


    for net_type in INPUT_FILE:
        aver_error_train = []
        aver_error_test = []
        score_train = []
        score_test = []

        DATA_TRAIN = '../data/no_cv/' + net_type + '_test_.data' 
        DATA_TEST = '../data/no_cv/' + net_type + '_test_.data' 

        # HERE IS THE DIFFERENCE FOR EACH NET
        learn_data_X, learn_data_Y = info.load_data(DATA_TRAIN)
        predict_data_X, predict_data_Y = info.load_data(DATA_TEST)

        # classifier
        model = fit_model(learn_data_X, learn_data_Y)
 
        accuracy_train = classify_data(model, learn_data_X, learn_data_Y) 
        accuracy_test = classify_data(model, predict_data_X, predict_data_Y)
        
        aver_error_train.append(accuracy_train)    
        aver_error_test.append(accuracy_test) 

        score_train.append(model.score(learn_data_X, learn_data_Y))    
        score_test.append(model.score(predict_data_X, predict_data_Y))   

        # save to file to plot
        print 'Saving final files ...'  
        OUTPUT_FILE_TRAIN = OUT + '_train_' + net_type + '_.data' 
        OUTPUT_FILE_TEST =  OUT + '_test_'  + net_type + '_.data' 
            
        save_result_final(aver_error_train, score_train, OUTPUT_FILE_TRAIN)
        save_result_final(aver_error_test, score_test, OUTPUT_FILE_TEST)


    '''
        TECH networks
    '''
    OUT = '../output/TECH_NO_CV_'
    print 'Starting info nets...'

    for net_type in INPUT_FILE:
        aver_error_train = []
        aver_error_test = []
        score_train = []
        score_test = []

        DATA_TRAIN = '../data/no_cv/' + net_type + '_test_.data' 
        DATA_TEST = '../data/no_cv/' + net_type + '_test_.data' 

        # HERE IS THE DIFFERENCE FOR EACH NET
        learn_data_X, learn_data_Y = tech.load_data(DATA_TRAIN)
        predict_data_X, predict_data_Y = tech.load_data(DATA_TEST)

        # classifier
        model = fit_model(learn_data_X, learn_data_Y)
        accuracy_train = classify_data(model, learn_data_X, learn_data_Y) 
        accuracy_test = classify_data(model, predict_data_X, predict_data_Y)
                                       
        aver_error_train.append(accuracy_train)    
        aver_error_test.append(accuracy_test) 

        score_train.append(model.score(learn_data_X, learn_data_Y))    
        score_test.append(model.score(predict_data_X, predict_data_Y))      

        # save to file to plot
        print 'Saving final files ...'  
        OUTPUT_FILE_TRAIN = OUT + '_train_' + net_type + '_.data' 
        OUTPUT_FILE_TEST =  OUT + '_test_'  + net_type + '_.data' 
            
        save_result_final(aver_error_train, score_train, OUTPUT_FILE_TRAIN)
        save_result_final(aver_error_test, score_test, OUTPUT_FILE_TEST)


    '''
        SOCIAL networks
    '''
    OUT = '../output/SOCIAL_NO_CV_'
    print 'Starting info nets...'

    for net_type in INPUT_FILE:
        aver_error_train = []
        aver_error_test = []
        score_train = []
        score_test = []

        DATA_TRAIN = '../data/no_cv/' + net_type + '_test_.data' 
        DATA_TEST = '../data/no_cv/' + net_type + '_test_.data' 

        # HERE IS THE DIFFERENCE FOR EACH NET
        learn_data_X, learn_data_Y = social.load_data(DATA_TRAIN)
        predict_data_X, predict_data_Y = social.load_data(DATA_TEST)

        # classifier
        model = fit_model(learn_data_X, learn_data_Y)
        accuracy_train = classify_data(model, learn_data_X, learn_data_Y) 
        accuracy_test = classify_data(model, predict_data_X, predict_data_Y)
                                       
        aver_error_train.append(accuracy_train)    
        aver_error_test.append(accuracy_test) 

        score_train.append(model.score(learn_data_X, learn_data_Y))    
        score_test.append(model.score(predict_data_X, predict_data_Y))      

        # save to file to plot
        print 'Saving final files ...'  
        OUTPUT_FILE_TRAIN = OUT + '_train_' + net_type + '_.data' 
        OUTPUT_FILE_TEST =  OUT + '_test_'  + net_type + '_.data' 
            
        save_result_final(aver_error_train, score_train, OUTPUT_FILE_TRAIN)
        save_result_final(aver_error_test, score_test, OUTPUT_FILE_TEST)


    '''
        BIO networks
    '''
    OUT = '../output/BIO_NO_CV_'
    print 'Starting info nets...'

    for net_type in INPUT_FILE:
        aver_error_train = []
        aver_error_test = []
        score_train = []
        score_test = []

        DATA_TRAIN = '../data/no_cv/' + net_type + '_test_.data' 
        DATA_TEST = '../data/no_cv/' + net_type + '_test_.data' 

        # HERE IS THE DIFFERENCE FOR EACH NET
        learn_data_X, learn_data_Y = bio.load_data(DATA_TRAIN)
        predict_data_X, predict_data_Y = bio.load_data(DATA_TEST)

        # classifier
        model = fit_model(learn_data_X, learn_data_Y)
        accuracy_train = classify_data(model, learn_data_X, learn_data_Y) 
        accuracy_test = classify_data(model, predict_data_X, predict_data_Y)
                                       
        aver_error_train.append(accuracy_train)    
        aver_error_test.append(accuracy_test) 

        score_train.append(model.score(learn_data_X, learn_data_Y))    
        score_test.append(model.score(predict_data_X, predict_data_Y))      

        # save to file to plot
        print 'Saving final files ...'  
        OUTPUT_FILE_TRAIN = OUT + '_train_' + net_type + '_.data' 
        OUTPUT_FILE_TEST =  OUT + '_test_'  + net_type + '_.data' 
            
        save_result_final(aver_error_train, score_train, OUTPUT_FILE_TRAIN)
        save_result_final(aver_error_test, score_test, OUTPUT_FILE_TEST)


    print 'Done!!!'




if __name__ == '__main__':
    main()

