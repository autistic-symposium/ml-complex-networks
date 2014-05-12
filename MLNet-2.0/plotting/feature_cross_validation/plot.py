#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"




import pylab as plt
import os
import json
import numpy as np
from sklearn.svm import SVC
from sklearn.cross_validation import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.datasets import make_classification
from sklearn.metrics import zero_one_loss
from constants import  INPUT_FOLDER, OUTPUT_FOLDER, TYPE_NOR



def get_input_path(number, typen):
    return INPUT_FOLDER + 'together' + str(number) + '_train_0.8_' + typen +'.data'



def get_output_path(typen):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    outfolder = OUTPUT_FOLDER +  'feature_CV/'
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)    
    return outfolder + 'FEATURE_CV_set'  +  '_0.8_' + typen  +'.png'



def get_data_here(inputfile):
    data = np.loadtxt(inputfile, delimiter = ',')
    X = data[:,:-1] 
    Y = data[:,-1]
    return X, Y

 
def main():  
    color = ['r', 'b', 'y', 'g', 'c', 'm']
    # plot config
    with open("conf.json") as json_file:
       s = json.load(json_file)
    plt.rcParams.update(s)
   
    # for each type norm
    for typen in TYPE_NOR:
        print('\nStarting to plot for ' + typen)
        plt.cla()
        plt.clf()
        plt.figure()
        # for each set
        for number in range(1, 6):


            outputfile = get_output_path(typen)
            inputfile = get_input_path(number, typen)

            X, Y  = get_data_here(inputfile)
            svc = SVC()
            rfecv = RFECV(estimator=svc,  cv=StratifiedKFold(Y, 2), step=0.3,
                      scoring='accuracy', estimator_params={'kernel': 'linear'})
            rfecv.fit(X, Y)
            print("Optimal number of features : %d" % rfecv.n_features_)

            plt.ylim(0, 3)
            plt.xlim(1, 5.5)
            plt.xlabel("Number of features selected")
            plt.ylabel("Cross validation score (nb of misclassifications)")
            plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_, c=color[number-1], label="Set " +str(number))
                    
        plt.legend(loc='best', fontsize=10)
        plt.savefig(outputfile, orientation='landscape')

    print('Done!\n')





if __name__ == '__main__':
    main()


