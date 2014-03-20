
'''
Measures the quality of a community structure. It corresponds to the proportion of links located inside the communities, minus an estimation of the same quantity obtained for a null model. Consequently, its upper bound is 1, while 0 means the community structure is equivalent to a random one. Let us define the function delta such that delta(u,v) is equal to 1 if nodes $u$ and $v$ belong to the same community, and 0 otherwise:

Q(G)=\max \Bigg \{\frac{1}{2m} \sum_{u,v \in V} \Big [A_{uv} - \frac{k_v k_u}{2m}  \Big ] \delta(u,v) \Bigg \}

'''

