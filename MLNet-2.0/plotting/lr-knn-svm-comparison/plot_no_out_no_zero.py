#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"



import numpy as np
import pylab as pl
from sklearn import neighbors, linear_model, svm, ensemble, naive_bayes, lda, qda, cross_validation
import os
import json
from constants import FEATURES, INPUT_FOLDER, OUTPUT_FOLDER, TYPE_NOR, FEATURES_WE_WANT,FEATURES_INDEX
from matplotlib.colors import ListedColormap



def get_input_path(number, typen):
    return INPUT_FOLDER + 'together' + str(number) + '_train_0.8_' + typen + '.data',INPUT_FOLDER + 'together' \
    + str(number) + '_test_0.8_' + typen +'.data'




def get_output_path(typen, number, feat):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    outfolder = OUTPUT_FOLDER +  'plots-svm-lr-knn_no_out_no_zero/'
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)    

    return outfolder + 'set' + number + feat + '_0.8_' + typen 




def get_output_path_score():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    outfolder = OUTPUT_FOLDER +  'plots-svm-lr-knn_no_out_no_zero/'
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)  

    return outfolder +'SCORE.txt'




def get_data_here(inputfile, inputfilet, indexx, indexy ):
    data = np.loadtxt(inputfile, delimiter = ',')
    feat1 = data[:, indexx]
    feat2 = data[:, indexy]
    clas = data[:,-1]
    X = []
    Y = []
    for i, f1 in enumerate(feat1):
            #if f1 != 0 and feat2[i] != 0:
            X.append([f1, feat2[i]])
            Y.append(clas[i])
    X = np.array(X)

    data = np.loadtxt(inputfilet, delimiter = ',')
    feat1 = data[:, indexx]
    feat2 = data[:, indexy]
    Xt = []
    for i, f1 in enumerate(feat1):
        Xt.append([f1, feat2[i]])
    Xt = np.array(Xt)
    Yt = data[:,-1]

    return X, Y, Xt, Yt

 



def plotting(X, Y, Xt, Yt, labelx, labely, outputfile):
    h = .02  # step size in the mesh
    classifiers = dict(
    knn=neighbors.KNeighborsClassifier(4),
    logistic=linear_model.LogisticRegression(C=1e4, penalty=l1),
    svm=svm.SVC(C=1e4),
    svmlinear=svm.LinearSVC(C=1e4),
    adaboost=ensemble.AdaBoostClassifier(),
    naivebay=naive_bayes.GaussianNB())

    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
    
    fignum = 1
    # we create an instance of Neighbours Classifier and fit the data.
    for name, clf in classifiers.iteritems():
        clf.fit(X, Y)
        score = clf.score(Xt, Yt)
        
        if score > 0.85:
            print '....... plotting for ' + name 
            pl.cla()
            pl.clf()

            # Plot the decision boundary. For that, we will assign a color to each
            # point in the mesh [x_min, m_max]x[y_min, y_max].
            x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
            y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
            xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
            Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

            # Put the result into a color plot
            Z = Z.reshape(xx.shape)
            pl.figure(fignum, figsize=(4, 3))
            pl.pcolormesh(xx, yy, Z, cmap=cmap_light)

            # Plot also the training points
            pl.scatter(X[:, 0], X[:, 1], s=30,  c=Y, edgecolors='k',cmap=cmap_bold)
            pl.xlim(xx.min(), xx.max())
            pl.ylim(yy.min(), yy.max())
            pl.xticks(())
            pl.yticks(())
            fignum += 1
            pl.ylabel(labely)      
            pl.xlabel(labelx)     
            pl.text(xx.min(), yy.min(), name + " - Accuracy " + str(round(score,2)),ha='left',fontsize=14, style='italic')
            if score > 0.95:
                pl.savefig(outputfile + '_' + name+  '_SUPERGOOD.png' , orientation='landscape')
            else:
                pl.savefig(outputfile + '_' + name+  '.png' , orientation='landscape')

    return score, name





def main():  

    ''' OH MY GOD SO MANY FORS... I HOPE NOBODY SEES THIS'''
    print '\n\n*** Starting without outliers and no zero ****\n'
    output_file_score =  get_output_path_score()
    score_array = []
    pl.figure()

    # plot config
    with open("conf.json") as json_file:
       s = json.load(json_file)
    pl.rcParams.update(s)
   

    # for each type norm
    for typen in TYPE_NOR:


        # for each set
        for number in range(1, 6):
            print '... Starting set ' + str(number) + ' for norm ' + typen
            alread = set()
            for nx, axisx in enumerate(FEATURES_WE_WANT):
                                        # start plotting
                inputfile, inputfilet = get_input_path(number, typen)

                indexx = FEATURES_INDEX[nx]
                alread.add(axisx)

                for ny, axisy in enumerate(FEATURES_WE_WANT):
                    if axisy != axisx and axisy not in alread:
                        outputfile = get_output_path(typen, str(number), axisx)
                        indexy = FEATURES_INDEX[ny]
                        labelx = axisx
                        labely = axisy

                        X, Y, Xt, Yt = get_data_here(inputfile, inputfilet, indexx, indexy )
                        
                        score, lab = plotting(X, Y, Xt, Yt, labelx, labely, outputfile)
                        score_array.append(lab + ', ' + str(number) + ', ' + typen + ', '  + axisx + ' vs. ' + axisy + \
                        	': ' + str(score) + "\n")



    with open(output_file_score , "a") as f:
        for score in score_array:
            f.write(score)


    print('Done!\n')





if __name__ == '__main__':
    main()


