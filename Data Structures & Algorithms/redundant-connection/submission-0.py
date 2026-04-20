class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        r = [1] * (n + 1)

        def find(nd):  # find its par
            p = par[nd]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]

            return p

        def union(nd1,nd2):   #create the connection b/n graph
            p1, p2 = find(nd1), find(nd2)

            if p1 == p2:
                return False
            if r[p1] > r[p2]:
                par[p2] = p1
                r[p1] += r[p2] 
            else:
                par[p2] = p1
                r[p1] += r[p2]

            return True
        for i , j in edges:
            if not union(i, j):
                return [i, j]





