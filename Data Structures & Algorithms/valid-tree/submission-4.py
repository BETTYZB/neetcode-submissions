class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) <= 0:
            return True

        tree = {i : [] for i in range(n)}

        for e1, e2 in edges:
            tree[e1].append(e2)
            tree[e2].append(e1)
# 0:1, 2, 3
# 1: 0,2, 4 ;;;;; 2: 0;;;;;3: 0;;;;; 4:1
        visit = set()
        def dfs(node, prev):
            visit.add(node)
            for edge in tree[node]:
                if edge == prev:
                    continue
                if edge in visit:
                    return False
                if not dfs(edge, node):
                    return False
            return True







        return (dfs(0, -1) and len(visit) == n)