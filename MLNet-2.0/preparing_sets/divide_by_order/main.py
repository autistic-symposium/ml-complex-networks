#!/usr/bin/env python
 
 
__author__ = "Mia Stein"
__copyright__ = "Copyright 2014"
__credits__ = ["Mia Stein"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mia Stein"
__email__ = ""

''' This program divide the data into the sets of different graph order and clean some outliers (found from normalization plots)'''

import os, math
import numpy as np
from constants import INPUT_FILE, OUTPUT_FOLDER, ORDER_MIN, ORDER_MAX


def save_result_split(final, output_folder_file):

    with open(output_folder_file , "w") as f:
        for i in range(len(final)):
            f.write(str(final[i]) + "\n")


def save_each_file(output_folder_file, file1, size, ORDER, ass, trans, degree, core, ntrian, ncliq, cliqnum, clust, edge, ecc, diam, betwe, dens, rad, scl, comm, page, cent, LABEL, with_outlier):
    final = []

    for i in file1:
        good_data = True

        f1 = size[i]
        f2 = ORDER[i]
        f3 = ass[i]
        f4 = trans[i]
        f5 = degree[i]
        f6 = core[i]
        f7 = ntrian[i]
        f8 = ncliq[i]
        f9 = cliqnum[i]
        f10 = clust[i]
        f11 = edge[i]
        f12 = ecc[i]
        f13 = diam[i]
        f14 = betwe[i]
        f15 = dens[i]
        f16 = rad[i]
        f17 = scl[i]
        f18 = comm[i]
        f19 = page[i]
        f20 = cent[i]
        l = LABEL[i]
        ftotal = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20]

        for f in ftotal:
            if f == 123456789012345:
                good_data = False

        if good_data:        
            final.append(str(f1) + ',' + str(f2) + ',' + str(f3) + ',' + str(f4) + ',' + str(f5) + ',' + str(f6) + ',' + str(f7) + ',' \
        + str(f8) + ',' + str(f9) + ',' + str(f10) + ',' + str(f11) + ',' + str(f12) + ',' + str(f13) + ',' + str(f14) + ',' + str(f15) + ',' + \
        str(f16) + ',' + str(f17) + ',' + str(f18) + ',' + str(f19) + ',' + str(f20) + ',' + str(l))


    if with_outlier: 
        output_folder_file += '_with_outlier'

    save_result_split(final, output_folder_file)




def clean_outlier(vector, min_, max_):
    for index, item in enumerate(vector):
        if item < min_ or item > max_:
            vector[index] = 123456789012345




def get_indices(ORDER):
    file1 = []
    file2 = []
    file3 = []
    file4 = []
    file5 = []

    for index, order in enumerate(ORDER):
        if order > ORDER_MIN[0] and order <= ORDER_MAX[0]:
            file1.append(index)
        elif order > ORDER_MIN[1] and order <= ORDER_MAX[1]:
            file2.append(index)
        elif order > ORDER_MIN[2] and order <= ORDER_MAX[2]:
            file3.append(index)
        elif order > ORDER_MIN[3] and order <= ORDER_MAX[3]:
            file4.append(index)
        elif order > ORDER_MIN[4] and order <= ORDER_MAX[4]:
            file5.append(index)
    
    return file1, file2, file3, file4, file5




def get_output(nam):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)    
    return OUTPUT_FOLDER +  'together' + nam + '.data'



def main():
    ''' Load and split data'''

    # define outfile/infile paths
    input_file = INPUT_FILE

    output_folder_file1 = get_output('1') 
    output_folder_file2 = get_output('2') 
    output_folder_file3 = get_output('3') 
    output_folder_file4 = get_output('4') 
    output_folder_file5 = get_output('5') 


    #Size Order Assortativity Transitivity Degree Coreness Number_Triangles Number_Cliques Clique_number Clustering Edge_connectivity Eccentricity Diameter 
    #Betweeness Density Radius Square_clustering Communicability Pagerank Centrality 
    size, ORDER, ass, trans, degree, core, ntrian, ncliq, cliqnum, clust, edge, ecc, diam, betwe, dens, rad, scl, comm, page, cent, LABEL = np.loadtxt(input_file, delimiter=',' , unpack=True)

    file1, file2, file3, file4, file5 = get_indices(ORDER)   


    ''' first we keep outliers '''
    with_outlier = False

    # save new files
    save_each_file(output_folder_file1, file1, size, ORDER, ass, trans, degree, core, ntrian, ncliq, cliqnum, clust, edge, ecc, diam, betwe, \
     dens, rad, scl, comm, page, cent, LABEL, with_outlier)
    save_each_file(output_folder_file2, file2, size, ORDER, ass, trans, degree, core, ntrian, ncliq, cliqnum, clust, edge, ecc, diam, betwe,\
     dens, rad, scl, comm, page, cent, LABEL, with_outlier)
    save_each_file(output_folder_file3, file3, size, ORDER, ass, trans, degree, core, ntrian, ncliq, cliqnum, clust, edge, ecc, diam, betwe, \
     dens, rad, scl, comm, page, cent, LABEL, with_outlier)
    save_each_file(output_folder_file4, file4, size, ORDER, ass, trans, degree, core, ntrian, ncliq, cliqnum, clust, edge, ecc, diam, betwe, \
        dens, rad, scl, comm, page, cent, LABEL,with_outlier)
    save_each_file(output_folder_file5, file5, size, ORDER, ass, trans, degree, core, ntrian, ncliq, cliqnum, clust, edge, ecc, diam, betwe, \
        dens, rad, scl, comm, page, cent, LABEL, with_outlier)



    ''' then we detect outlier, manually from plots '''
    with_outlier = True
    clean_outlier(betwe, 0, 0.1)
    clean_outlier(comm, 0, 0.1e6)
    clean_outlier(diam, 0, 110)
    clean_outlier(ecc, 0, 110)
    clean_outlier(edge, 0, 10)
    clean_outlier(ncliq, 0, 200000)
    clean_outlier(ntrian, 0, 800)    
    clean_outlier(rad, 0, 80)

    # save new files   
    save_each_file(output_folder_file1, file1, size, ORDER, ass, trans, degree, core, ntrian, ncliq, cliqnum, clust, edge, ecc, diam, betwe, \
     dens, rad, scl, comm, page, cent, LABEL, with_outlier)
    save_each_file(output_folder_file2, file2, size, ORDER, ass, trans, degree, core, ntrian, ncliq, cliqnum, clust, edge, ecc, diam, betwe,\
     dens, rad, scl, comm, page, cent, LABEL, with_outlier)
    save_each_file(output_folder_file3, file3, size, ORDER, ass, trans, degree, core, ntrian, ncliq, cliqnum, clust, edge, ecc, diam, betwe, \
     dens, rad, scl, comm, page, cent, LABEL, with_outlier)
    save_each_file(output_folder_file4, file4, size, ORDER, ass, trans, degree, core, ntrian, ncliq, cliqnum, clust, edge, ecc, diam, betwe, \
        dens, rad, scl, comm, page, cent, LABEL,with_outlier)
    save_each_file(output_folder_file5, file5, size, ORDER, ass, trans, degree, core, ntrian, ncliq, cliqnum, clust, edge, ecc, diam, betwe, \
        dens, rad, scl, comm, page, cent, LABEL, with_outlier)




    print 'Output generate at ' + OUTPUT_FOLDER
    print 'Done!'


   
if __name__ == '__main__':
    main()
