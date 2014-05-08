"""
=========================================
SVM: Maximum margin separating hyperplane
=========================================

Plot the maximum margin separating hyperplane within a two-class
separable dataset using a Support Vector Machines classifier with
linear kernel.
"""


import numpy as np
import pylab as pl
from sklearn import svm, preprocessing

# we create 40 separable points
INPUT_FILE = ['all_neat_n5000', 'all_neat_n1000', 'all_neat_n1500', 'all_neat_n2000', 'all_neat_n5000', 'all_neat']


for net_type in INPUT_FILE:
  	# import data
  	DATA_TRAIN = './data/' + net_type + '_test.data' 
  	data = np.loadtxt(DATA_TRAIN, delimiter = ',')

  	X = data[:,:-1] 
  	Y = data[:,-1]

	#X  = preprocessing.scale(X)

	min_max_scaler = preprocessing.MinMaxScaler()
	X = min_max_scaler.fit_transform(X)

	# fit the model
	clf = svm.SVC()
	clf.fit(X, Y)

	# get the separating hyperplane
	#w = clf.coef_[0]
	#a = -w[0] / w[1]
	#xx = np.linspace(-5, 5)
	#yy = a * xx - (clf.intercept_[0]) / w[1]

	# plot the parallels to the separating hyperplane that pass through the
	# support vectors
	#b = clf.support_vectors_[0]
	#yy_down = a * xx + (b[1] - a * b[0])
	#b = clf.support_vectors_[-1]
	#yy_up = a * xx + (b[1] - a * b[0])

	# plot the line, the points, and the nearest vectors to the plane
	#pl.plot(xx, yy, 'k-')
	#pl.plot(xx, yy_down, 'k--')
	#pl.plot(xx, yy_up, 'k--')



	pl.cla()  
	pl.clf()

	x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	y = [125, 32, 54, 253, 67, 87, 233, 56, 67]
	color = [str(item/255.) for item in y]

	pl.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
	           s=80, facecolors='none')
	pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)
	#pl.scatter(X[:, 2], X[:, 3], c=Y, cmap=pl.cm.Paired)
	#pl.scatter(X[:, 4], X[:, 5], c=Y, cmap=pl.cm.Paired)
	#pl.scatter(X[:, 6], X[:, 7], c=Y, cmap=pl.cm.Paired)

	pl.axis('tight')
	pl.savefig('svm_' + net_type + '.png')
