"""
===================================================
Recursive feature elimination with cross-validation
===================================================

A recursive feature elimination example with automatic tuning of the
number of features selected with cross-validation.
"""
print(__doc__)

import numpy as np
from sklearn.svm import SVC
from sklearn.cross_validation import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.datasets import make_classification
from sklearn.metrics import zero_one_loss

INPUT_FILE = ['all_neat_n500']#, 'all_neat_n1000', 'all_neat_n1500', 'all_neat_n2000', 'all_neat_n5000', 'all_neat']

net_type = 'all_neat_n500'

DATA_TRAIN = './data/' + net_type + '_train.data' 
data = np.loadtxt(DATA_TRAIN, delimiter = ',')

X = data[:,:-1]
y = data[:,-1]

# Create the RFE object and compute a cross-validated score.
svc = SVC(kernel="linear")
rfecv = RFECV(estimator=svc, step=1, cv=StratifiedKFold(y, 2),
              scoring='accuracy')
rfecv.fit(X, y)

print("Optimal number of features : %d" % rfecv.n_features_)

# Plot number of features VS. cross-validation scores
import pylab as pl
pl.figure()
pl.xlabel("Number of features selected")
pl.ylabel("Cross validation score (nb of misclassifications)")
pl.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
print 'Done!'
pplt.savefig('feature_cs.png')
