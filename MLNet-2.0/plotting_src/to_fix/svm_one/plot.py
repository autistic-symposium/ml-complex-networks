"""
======================
SVM with custom kernel
======================

Simple usage of Support Vector Machines to classify a sample. It will
plot the decision surface and the support vectors.

"""
print(__doc__)

import numpy as np
import pylab as pl
from sklearn import svm, datasets

INPUT_FILE = ['all_neat_n500']#, 'all_neat_n1000', 'all_neat_n1500', 'all_neat_n2000', 'all_neat_n5000', 'all_neat']

net_type = 'all_neat_n500'

DATA_TRAIN = './data/' + net_type + '_train.data' 
data = np.loadtxt(DATA_TRAIN, delimiter = ',')

X = data[:,:2]
Y = data[:,-1]


def my_kernel(x, y):
    """
    We create a custom kernel:

                 (2  0)
    k(x, y) = x  (    ) y.T
                 (0  1)
    """
    M = np.array([[2, 0], [0, 1.0]])
    return np.dot(np.dot(x, M), y.T)


h = .02  # step size in the mesh

# we create an instance of SVM and fit out data.
clf = svm.SVC(kernel=my_kernel)
clf.fit(X, Y)

# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, m_max]x[y_min, y_max].
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
pl.pcolormesh(xx, yy, Z, cmap=pl.cm.Paired)

# Plot also the training points
pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)
pl.title('3-Class classification using Support Vector Machine with custom'
         ' kernel')
pl.axis('tight')
pl.show()
