MLNet - Classifying Complex Networks with Machine Learning
===========================================================

Summary
-------

The study of  complex networks pervades all of the science. We can assign complex networks into four general classes (although there is some overlap between them):  technological networks (e.g., internet, the telephone network, power grids, transportation network),  information networks (e.g., the world wide web, citation networks),   biological networks (e.g., biochemical network, neutral networks, ecological networks), and  social networks. 

Characterizing complex network's structure is a key to understand any unifying principles underlying their topology. Several previous works  have shown that many topological properties can vary for different types of system. However these works generally focus only a few characteristics at time.   In this project, we present the first part of a method to characterize complex networks by performing an extensive analysis of the global and local topological features of networks. In a  second part, these features  are used into input vectors for a SVN classifier, establishing an efficient way of learning the classification of complex networks. 

Features
--------

The feature vectors were extracting using MNet:
https://github.com/mariwahl/MNet-Network-Analysis

We have vectors for different normalization (Snowball and Metropolis Hastings Random Walk samplings) for different sizes. We also have vectors for the entire graphs for some of the features (that were possible to be calculated).

These vectors are parsed and cleansed using MNetClean, available inside this package.

Feature Section and Classifiers
------------------------------

We perform classification of the network features using many classifiers:
- SVM
- Naive Bayes
- Logistic Regression
- EM
- KNN

The source code is available under the MLNet folder.


Analysis and Plots
------------------

The comparisons of the the many classifiers and the plots are available under the MNetPlot folder.
