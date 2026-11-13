class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COLS = len(grid[0])
        visit = set()
        count = 0

        def dfs(r, c, visit):
            if min(r, c) < 0 or ROW <= r or c >= COLS or (r, c) in visit or grid[r][c] == "0":
                return
            visit.add((r, c))

            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)
            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)

            return



        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c, visit)
                    count += 1

        return count
        