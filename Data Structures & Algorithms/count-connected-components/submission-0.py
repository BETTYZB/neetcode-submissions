class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n < 2:
            return n
        graph = {i:[] for i in range(n)}
        visit = set()
        count = 0

        for r, c in edges:
            graph[r].append(c)
            graph[c].append(r)

        def dfs(node):
            if node in visit:
                return True
            visit.add(node)

            for eg in graph[node]:
                dfs(eg)
            
            return True

        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1

        return count


            
