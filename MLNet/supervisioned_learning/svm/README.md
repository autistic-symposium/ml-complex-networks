Analysing Nets with SVM
===========================================================

Support Vector Machines try to find a combination of samples to build a plane maximizing the margin between the two classes. 

For many estimators, including the SVMs, having datasets with unit standard deviation for each feature is important to get good prediction.


Description
-----------

Here analyse our nets using SVM with one-against-all and all-against all. We report the training and test errors.
Cross validation sets were for 300, 200, 100 and 50.

* Entire Nets folder:
Performed for the entire nets, with the features that were possible to be extracted from these large graphs, divided by cross-validation sets. From these results we can evaluate the vality of the chose division for networks (info, social, bio, and tech).

* Sampling Nets folder:
Perfomed for the sampled nets, divided by cross-validation sets. We test for all features (missing have 0 values) and for the 10 first features (that do not present missing values).


Multiclassification
-------------------

Weimplement the “one-against-one” approach (Knerr et al., 1990) for multi- class classification. If n_class is the number of classes, then:
n_class * (n_class - 1) / 2 
classifiers are constructed and each one trains data from two classes:

We can implement “one-vs-the-rest” multi-class strategy, thus training n_class models. If there are only two classes, only one model is trained.

