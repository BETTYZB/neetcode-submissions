class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COLS = len(grid[0])
        visit = set()
        max_count = 0
        count = 0

        def dfs(r, c, visit, count):
            if min(r, c) < 0 or ROW <= r or COLS <= c or (r, c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r,c))
            count = 1
            count += dfs(r + 1, c, visit, count)
            count += dfs(r - 1, c, visit, count)
            count += dfs(r, c + 1, visit, count)
            count += dfs(r, c - 1, visit, count)

            return count


        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    count = dfs(r, c, visit, 0)
                    if max_count < count:
                        max_count  = count

        return max_count


        