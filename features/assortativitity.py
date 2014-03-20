'''

Measures the similarity of connections in the graph with respect to the node degree. Associative mixing by degree can be quantified in a number of ways, one of them is to use the correlation coefficient:

r =\frac{\sum_{ij}(A_{ij} -k_ik_j/2m)k_ik_j}{\sum_{ij}(k_i\delta_{ij} - k_ik_j/2m)k_ik_j},

instead we write:

r = \frac{S_1 S_e-S_2^2}{S_1S_3-S_2^2},

with 

S_e =\sum_{ij} A_{ij} k_ik_j = 2\sum_{edges(i,j)} k_ik_j,

where the second sum is over all distinct (unordered) pairs of vertices  (i,j) connected by an edge and

S_1=\sum_i k_i$m $S_2=sum_i k_i^2$ $S_3=\sum_i k_i^3.

Graphs that have only single edges between vertices tend in the absence of other biases to show disassortative mixing by degree because the number of edges that can fall between high-degree vertex pairs is limited. Since most networks are represented as simple graphs this implies that most should be disassortative.


'''
