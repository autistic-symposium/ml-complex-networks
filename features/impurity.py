'''
The impurity degree of a node $u$ belonging to a graph G, having a label L(u) and neighborhood (adjacent nodes) $N(u)$ is defined as: 
I(u)=| L(v): v \in N(u), L(u) \neq L(v)|.

The average neighborhood impurity of a graph $G$ represents the average impurity degree over all nodes with all positive impurity:
\bar I (G) = \frac{1}{n} \sum |L(v) : v \in N(u),L(u)\neq (v)|.

If all nodes in the neighborhood of $u$ have the same node label, the impurity degree is 0. For the whole graph, we are only interested in the nodes that have impurity degree larger than 0 (nodes which have a least one neighbor whose label is different). 

'''
