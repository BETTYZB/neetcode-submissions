class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == 1:
                    return 0
            visit.add((r, c))
            length  = 0
            if r == ROWS - 1 and c == COLS - 1 and grid[r][c] == 0:
                length += 1
            length += dfs(r + 1, c)
            length += dfs(r - 1, c)
            length += dfs(r, c + 1)
            length += dfs(r, c - 1)
            visit.remove((r, c))
            return length 

        return dfs(0, 0) 