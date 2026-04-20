class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            return n 
        # dict, adj list
        # dfs on each node
        # visit
        graph = {i:[] for i in range(n)}
        visit = set()
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        def dfs(node):
            if node in visit:
                return 
            visit.add(node)
            for neigh in graph[node]:
                dfs(neigh)
            return 


        count = 0
        for g in graph:
            if g not in visit:
                dfs(g)
                count += 1
            
        return count
        