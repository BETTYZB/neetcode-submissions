class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COLS = len(grid[0])
        maxm_area = 0
        visit = set()

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROW or c >= COLS or grid[r][c] == 0 or (r, c) in visit:
                return 0
            visit.add((r, c))
            return 1 +  (dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1) + dfs(r - 1, c))
        
        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxm_area = max(dfs(r, c), maxm_area)
                    

        return maxm_area