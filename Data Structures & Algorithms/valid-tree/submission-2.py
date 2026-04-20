class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        tree = {i : [] for i in range(n)}
        visit = set()
        prev = -1

        for r, c in edges:
            tree[r].append(c)
            tree[c].append(r)


        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for eg in tree[node]:
                if eg == prev:
                    continue
                if not dfs(eg, node):
                    return False
            
            return True

        return dfs(0, prev) and n == len(visit)

