class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        ROW = len(grid)
        COLS = len(grid[0])
        land = 0
        def dfs(grid, r, c, visit):
            if min(r, c) < 0 or r >= ROW or c >= COLS or grid[r][c] == "0" or (r, c) in visit:
                return 
            visit.add((r, c))
            dfs(grid, r + 1, c, visit)
            dfs(grid, r, c + 1, visit)
            dfs(grid, r - 1, c, visit)
            dfs(grid, r , c -1, visit)


        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    land += 1
                    dfs(grid, r, c, visit)

        return land

            
