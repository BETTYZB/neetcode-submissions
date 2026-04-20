from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        land = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            while q:
                r, c = q.popleft()
                drxn = [(0, 1), (1, 0), (-1, 0), (0, -1)]

                for dr, dc in drxn:
                    nr = dr + r
                    nc = dc + c
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0" or (nr, nc) in visit:
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    land += 1
                    bfs(r, c)


        return land