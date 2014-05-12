#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"



import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from itertools import cycle
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import MeanShift, estimate_bandwidth
import os
import json
from constants import FEATURES, INPUT_FOLDER, OUTPUT_FOLDER, TYPE_NOR, FEATURES_WE_WANT,FEATURES_INDEX
from matplotlib.colors import ListedColormap

''' Show below is a logistic-regression classifiers decision boundaries on the iris dataset. The datapoints are colored according to their labels.''' 

def get_input_path(number, typen):
    return INPUT_FOLDER + 'together' + str(number) + '_train_0.8_' + typen + '_with_outlier.data',INPUT_FOLDER + 'together' \
    + str(number) + '_test_0.8_' + typen +'_with_outlier.data'



def get_output_path(typen, number, feat, folder):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    outfolder = OUTPUT_FOLDER +  folder
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)    
    return outfolder + 'set' + number + feat + '_0.8_' + typen 



def get_data_here(inputfile, inputfilet, indexx, indexy, indexz):
    data = np.loadtxt(inputfile, delimiter = ',')
    feat1 = data[:, indexx]
    feat2 = data[:, indexy]
    feat3 = data[:, indexz]
    clas = data[:,-1]
    X = []
    Y = []
    for i, f1 in enumerate(feat1):
        if f1 != 0 and feat2[i] != 0 and feat3[i] != 0:
            X.append([f1, feat2[i], feat3[i]])
            Y.append(clas[i])
    X = np.array(X)
    Y = np.array(Y)
    return X, Y

def get_data_here_entire(inputfile):
    data = np.loadtxt(inputfile, delimiter = ',')
    X = data[:, :-2]
    Y = data[:,-1]
    return X, Y


 

def plotting_kmeans(X, Y, labelx, labely, labelz, outputfile):
    np.random.seed(5)
    centers = [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]
    estimators = {'k_means_3': KMeans(n_clusters=3), 'k_means_iris_4': KMeans(n_clusters=4), 'k_means_iris_6': KMeans(n_clusters=6)}

    fignum = 1  

    #  kmeans  
    for name, est in estimators.iteritems():
        pl.clf()
        pl.cla()
        fig = pl.figure(fignum)
        ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
        est.fit(X)
        labels = est.labels_
        ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=labels.astype(np.float))
        
        ax.w_xaxis.set_ticklabels([])
        ax.w_yaxis.set_ticklabels([])
        ax.w_zaxis.set_ticklabels([])
        ax.set_xlabel(labelx)
        ax.set_ylabel(labely)
        ax.set_zlabel(labelz)

        pl.savefig(outputfile + '_' + name +  '_KMEANS.png' , orientation='landscape')



    pl.clf()
    pl.cla()
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

    ax.scatter(X[Y==1, 0], X[Y==1, 1], X[Y==1, 2], c="r")
    ax.scatter(X[Y==2, 0], X[Y==2, 1], X[Y==2, 2], c='b')
    ax.scatter(X[Y==3, 0], X[Y==3, 1], X[Y==3, 2], c='y')
    ax.scatter(X[Y==4, 0], X[Y==4, 1], X[Y==4, 2], c='g')

    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel(labelx)
    ax.set_xlabel(labelx)
    ax.set_ylabel(labely)
    ax.set_zlabel(labelz)
    pl.savefig(outputfile +  '_GROUND.png' , orientation='landscape')

    fignum = fignum + 1




def plotting_aff(X,  Y, labelx, labely, labelz, outputfile):
    bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)   
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)    
    ms.fit(X)

    labels = ms.labels_    
    cluster_centers = ms.cluster_centers_
    
    labels_unique = np.unique(labels)    
    n_clusters_ = len(labels_unique)
    print("number of estimated clusters : %d" % n_clusters_)

    pl.figure(1)    
    pl.clf()
    pl.cla()
    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')    
    for k, col in zip(range(n_clusters_), colors):
        my_members = labels == k
        cluster_center = cluster_centers[k]
        pl.plot(X[my_members, 0], X[my_members, 1], col + '.')
        pl.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,  markeredgecolor='k', markersize=14)
    pl.title('Estimated number of clusters: %d' % n_clusters_)
    pl.savefig(outputfile + '_' + labelx + '_' +labely + '_'+labelz +  '_aff.png' , orientation='landscape')


def plotting_aff_dbscan(X,  labels_true, outputfile):
    X = StandardScaler().fit_transform(X)
    db = DBSCAN(eps=0.5, min_samples=70).fit(X)    
    core_samples = db.core_sample_indices_    
    labels = db.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    print('Estimated number of clusters: %d' % n_clusters_)
    print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
    print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
    print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
    print("Adjusted Rand Index: %0.3f" % metrics.adjusted_rand_score(labels_true, labels))
    print("Adjusted Mutual Information: %0.3f" % metrics.adjusted_mutual_info_score(labels_true, labels)) 
    print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))

    pl.clf()
    pl.cla()
    unique_labels = set(labels)
    colors = pl.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = 'k'
            markersize = 6
        class_members = [index[0] for index in np.argwhere(labels == k)]
        cluster_core_samples = [index for index in core_samples if labels[index] == k]
        for index in class_members:
            x = X[index]
            if index in core_samples and k != -1: markersize = 14
            else: markersize = 6
            pl.plot(x[0], x[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=markersize)
    pl.title('Estimated number of clusters: %d' % n_clusters_)
    pl.savefig(outputfile + '_aff_dbscan.png' , orientation='landscape')



def main():  


    ''' OH MY GOD SO MANY FORS... I HOPE NOBODY SEES THIS'''


    # plot config
    with open("conf.json") as json_file:
       s = json.load(json_file)
    pl.rcParams.update(s)
   



    # for each set
    for number in range(1, 6):
            print '... Starting set ' + str(number) + ' for norm ' + 'xmin'
            alread = set()
            for nx, axisx in enumerate(FEATURES_WE_WANT):
                inputfile, inputfilet = get_input_path(number, 'xmin')
                indexx = FEATURES_INDEX[nx]
                alread.add(axisx)

                for ny, axisy in enumerate(FEATURES_WE_WANT):
                    if axisy not in alread:
                        indexy = FEATURES_INDEX[ny]
                        alread.add(axisy)

                        for nz, axisz in enumerate(FEATURES_WE_WANT):
                            if axisz not in alread:
                                indexz = FEATURES_INDEX[nz]
                                alread.add(axisz)

                                print 'Features: ' + axisx + '_' + axisy + '_' + axisz

                                X, Y = get_data_here(inputfile, inputfilet, indexx, indexy, indexz)
                                labelx = axisx
                                labely = axisy
                                labelz = axisz

                                # plot kmeans
                                outputfile = get_output_path('xmin', str(number), axisx + '_' + axisy + '_' + axisz, 'plots_kmeans/')
                                plotting_kmeans(X, Y, labelx, labely, labelz, outputfile)
		 
		                        # plot clust
                                outputfile = get_output_path('xmin', str(number), axisx + '_' + axisy + '_' + axisz, 'plots_aff/')
                                plotting_aff(X, Y, labelx, labely, labelz, outputfile)


            # plot clust all
            print '\nStarting affinity all ...'
            X, Y = get_data_here_entire(inputfile)
            outputfile = get_output_path('xmin', str(number), axisx + '_' + axisy + '_' + axisz, 'plots_aff_all/') 
            plotting_aff(X, Y, labelx, labely, labelz, outputfile)



            # plot clust all
            print '\nStarting dbsc scan ...'
            X, Y = get_data_here_entire(inputfile)
            outputfile = get_output_path('xmin', str(number), axisx + '_' + axisy + '_' + axisz, 'plots_aff_dbscan/') 
            plotting_aff_dbscan(X, Y, outputfile)


    print('Done!\n')





if __name__ == '__main__':
    main()


