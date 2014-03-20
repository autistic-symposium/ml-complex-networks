'''
For a node $u$, the clustering coefficient c(u), also called local transitivity, represents the likelihood that any two neighbors of u are connected. Denoting lambda(u) as the number of triangles (complete graph with three nodes) of a node u and tau(u) the number of triples a node u has:

c(u) = \frac{2e}{k_u (k_u-1)},
where $k_u$ is the number of neighbors of $u$ and $e_u$ is the number of connected pairs of neighbors. If all the neighbors nodes of $u$ are connected, then, the neighborhood of $u$ is complete and we have a clustering coefficient of 1. If no nodes in the neighborhood of $u$ are connected, then the clustering coefficient is 0. The clustering coefficient for node $u$ can be defined also as the ratio of the number of possible edges between them. 

The average clustering coefficient \bar c(G) of a graph is the average of c(u) taken over all the nodes in the graph. It is defined  as the fraction of all
possible triangles in each graph. It can be interpreted when picking a randomly node, as the probability for two of its neighbors to be connected. Let us note gamma(G) the number of subgraph with 3 links and 3 nodes (triangles) and tau(G) the number of subgraphs with at least 2 links and 3 nodes (triangles and incomplete triangles. The global transitivity is:

\bar c(G)=\frac{\gamma(G)}{\tau(G)}

The transitivity ranges from 0.1 to 0.8 in the real world network. 

'''
