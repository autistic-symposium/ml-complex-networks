Analysing Nets with SVM
===========================================================

Support Vector Machines try to find a combination of samples to build a plane maximizing the margin between the two classes. 

For many estimators, including the SVMs, having datasets with unit standard deviation for each feature is important to get good prediction.



Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.
The advantages of support vector machines are:

- Effective in high dimensional spaces.
- Still effective in cases where number of dimensions is greater than the number of samples.
- Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.
- Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

- If the number of features is much greater than the number of samples, the method is likely to give poor performances.
- SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation




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

SVC and NuSVC are similar methods, but accept slightly different sets of parameters and have different mathematical formulations (see section Mathematical formulation). On the other hand, LinearSVC is another implementation of Support Vector Classification for the case of a linear kernel.

For “one-vs-rest” LinearSVC the attributes coef_ and intercept_ have the shape [n_class, n_features] and [n_class] respectively. Each row of the coefficients corresponds to one of the n_class many “one-vs-rest” classifiers and similar for the intercepts, in the order of the “one” class.

In the case of “one-vs-one” SVC, the layout of the attributes is a little more involved. In the case of having a linear kernel, The layout of coef_ and intercept_ is similar to the one described for LinearSVC described above, except that the shape of coef_ is [n_class * (n_class - 1) / 2, n_features], corresponding to as many binary classifiers. The order for classes 0 to n is “0 vs 1”, “0 vs 2” , ... “0 vs n”, “1 vs 2”, “1 vs 3”, “1 vs n”, . . . “n-1 vs n”.


Preprocessing
-------------
Support Vector Machine algorithms are not scale invariant, so it is highly recommended to scale your data. For example, scale each attribute on the input vector X to [0,1] or [-1,+1], or standardize it to have mean 0 and variance 1. Note that the same scaling must be applied to the test vector to obtain meaningful results. See section Preprocessing data for more details on scaling and normalization.



Scalling
--------
Standardization of datasets is a common requirement for many machine learning estimators implemented in the scikit: they might behave badly if the individual feature do not more or less look like standard normally distributed data: Gaussian with zero mean and unit variance.
In practice we often ignore the shape of the distribution and just transform the data to center it by removing the mean value of each feature, then scale it by dividing non-constant features by their standard deviation.
For instance, many elements used in the objective function of a learning algorithm (such as the RBF kernel of Support Vector Machines or the l1 and l2 regularizers of linear models) assume that all features are centered around zero and have variance in the same order. If a feature has a variance that is orders of magnitude larger that others, it might dominate the objective function and make the estimator unable to learn from other features correctly as expected.

An alternative standardization is scaling features to lie between a given minimum and maximum value, often between zero and one. This can be achieved using MinMaxScaler.
The motivation to use this scaling include robustness to very small standard deviations of features and preserving zero entries in sparse data.