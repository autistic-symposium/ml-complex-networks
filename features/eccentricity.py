'''
Represents, for a node $u$,  the maximum length of the shortest path between u and every other node in G:

e(u) = max_{v \in V} d(u,v).

If u is isolated, then e(u)=0. The average effective eccentricity is defined as:

\bar e(G) =\frac{1}{n} \sum^n_{i=1} e(u_i)

where n is the number of nodes of G.
'''

