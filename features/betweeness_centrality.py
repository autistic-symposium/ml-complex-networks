'''
 Measures the number of shortest paths going through a node u. If we denote sigma_{vw} as  the total number of shortest paths between v and w, and sigma_{vw}(u), the total number of shortest paths between nodes v and w going though u, the betweenness centrality is:

betw(u) = \sum_{v<w\neq w} \frac{\sigma_{vw} (u)}{\sigma_{vw}}
'''
