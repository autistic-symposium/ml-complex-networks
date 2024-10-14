## MLNet: classifying complex graph networks with machine learning

<br>

##### the study of  complex networks permeates all of the science

* we can assign complex networks into four general classes (although there is some overlap between them):
  * technological networks (e.g., Internet, the telephone network, power grids, transportation network)
  * information networks (e.g., the world wide web, citation networks)
  * biological networks (e.g., biochemical network, neural networks, ecological networks)
  * social networks

##### characterizing complex network's structures is a key to understanding any unifying principles underlying their topology

* previous works have shown that many topological properties can vary for different types of system, however these works generally focus only a few characteristics at the time
* in this project, we present the first part of a method to characterize complex networks by performing an extensive analysis of the global and local topological features of networks
* in a second part, these features are used into input vectors for a SVN classifier, establishing an efficient way of learning the classification of complex networks  

##### [👉 read the final research paper here](https://github.com/autistic-symposium/ml-graph-network-analyser/blob/master/on-classifying-complex-networks-by-their-features.pdf)

<br>

---

### the input data and features

<br>

* prior to using this software:
  * all vectors must be parsed and cleansed using my **[ml-netclean](https://github.com/autistic-symposium/ml-netclean)**
  * all features must be extracted using my **[ml-graph-network-analyser](https://github.com/autistic-symposium/ml-graph-network-analyser)**
* vectors can have different normalizations (snowball and metropolis hastings random walk samplings for different sizes)
* vectors can contain entire graphs for some of the features (that were possible to be calculated)

<br>

----

### feature selection and classifiers

<br>

* we perform the classification of the network features using several classifiers:
  * SVM (supervised)
  * logistic regression (supervised)
  * adaboost (supervised)
  * EM (unsupervised)

<br>

-----

### analysis and plots

<br>

* comparisons of many classifiers and the plots are available under each classifier's folder.

<br>

----

### installation

<br>

```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

<br>
