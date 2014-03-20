''' 

 Measures how fast information spreads from a given node to other reachable nodes in the graphs. For a node u, it represents the reciprocal of the average shortest path length between $u$ and every other reachable node in the graph:

cc(u)= \frac{n-1}{\sum_{ v\in \{V_u \}}d(u,v)},

where d(u,v) is the length of the shortest path between the nodes u and v.

For a graph G we consider the average value of closeness centrality of all nodes:

\bar{cc}(G) = \frac{1}{n} \sum^n_{i=1} cc(u_i)

'''
