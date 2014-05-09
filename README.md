MLNet - Classifying Complex Networks with Machine Learning
==============================================================

Summary
-------

The study of  complex networks pervades all of the science. We can assign complex networks into four general classes (although there is some overlap between them):  technological networks (e.g., internet, the telephone network, power grids, transportation network),  information networks (e.g., the world wide web, citation networks),   biological networks (e.g., biochemical network, neutral networks, ecological networks), and  social networks. 

Characterizing complex network's structure is a key to understand any unifying principles underlying their topology. Several previous works  have shown that many topological properties can vary for different types of system. However these works generally focus only a few characteristics at time.   In this project, we present the first part of a method to characterize complex networks by performing an extensive analysis of the global and local topological features of networks. In a  second part, these features  are used into input vectors for a SVN classifier, establishing an efficient way of learning the classification of complex networks. 


Data
-----

To use this software you can extract the data and calculate the features with: 
https://github.com/mariwahl/NetAna-Complex-Network-Analysis

And cleanse the data with:
https://github.com/mariwahl/NetClean-Complex-Networks-Data-Cleanser



Features
--------

The feature vectors were extracting using MNet:
https://github.com/mariwahl/NetAna-Complex-Network-Analysis

We have vectors for different normalization (Snowball and Metropolis Hastings Random Walk samplings) for different sizes. We also have vectors for the entire graphs for some of the features (that were possible to be calculated).

These vectors are parsed and cleansed using:
https://github.com/mariwahl/NetClean-Complex-Networks-Data-Cleanser


Feature Section and Classifiers
------------------------------

We perform classification of the network features using many classifiers:
- SVM (supervisioned)
- Logistic Regression (supervisioned)
- Adaboost (supervisioned)
- EM (unsupervisioned)




Analysis and Plots
------------------

The comparisons of the the many classifiers and the plots are available under each classifier's folder.


***** RESULTS ******
====================

We obtain excellent results for our classifiers:

1) SVM RESULTS, (train/test PERCENTAGE: 0.8)
--------------------------------------------
linear xmin,    atrain: 0.815,   atest: 0.809

SVC xmin,       atrain: 0.734,   atest: 0.739

linear gauss,   atrain: 0.821,   atest: 0.816

SVC gauss,      atrain: 0.916,   atest: 0.914

linear none,    atrain: 0.6,     atest: 0.611

SVC none,       atrain: 0.998,   atest: 0.993  ---> ALMOST 100% ACCURARY!!!!!



2) ADABOOST RESULTS, (train/test PERCENTAGE: 0.8)
------------------------------------------------
tech, xmin ,     atrain: 0.906114845197 , atest: 0.905554614733

info, xmin ,     atrain: 0.961694628209 , atest: 0.95816045724

social, xmin ,   atrain: 0.932485842816 , atest: 0.924731160034

bio, xmin ,      atrain: 0.977130457793 , atest: 0.979229466554

tech, gauss ,    atrain: 0.904228631913 , atest: 0.905944115157

info, gauss ,    atrain: 0.959289229955 , atest: 0.955270956816

social, gauss ,  atrain: 0.930746229161 , atest: 0.925279424217

bio, gauss ,     atrain: 0.977036782218 , atest: 0.979362828112



3) LOGISTIC REGRESSION, (train/test PERCENTAGE: 0.8)
----------------------------------------------------
xmin,     atrain: 0.821,   atest: 0.814

gauss,    atrain: 0.827,   atest: 0.823   ---> 83% ACCURACY

none,     atrain: 0.745,   atest: 0.748


Feature Pairwise:
-----------------
Type   Siz   Ord   Ass   Tra   Deg   Cor   NTr   NCl   Cnu   Clu   Eco   Ecc   Dia   Bet   Den   Rad   Scl   Com   Pag   Cen 

xmin   0.145 0.545 1.0  0.34  0.845 0.585 0.655 0.0   0.32  1.0   0.0  0.505  0.465 0.715  0.97 0.54  0.45  0.0   1.0   1.0  

gauss  0.155 0.52  1.0  0.365 0.785 0.605 0.585 0.0   0.415 1.0   0.0  0.51   0.48  0.7    0.96 0.57  0.41  0.0   1.0   1.0  

none   0.155 0.565 1.0  0.3   0.845 0.55  0.6   0.0   0.48  1.0   0.0  0.5    0.495 0.69   0.97 0.475 0.47  0.0   1.0   1.0   
