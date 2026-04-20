class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COLS = len(grid), len(grid[0])
        visit = set()
        count = 0
        maxm = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            count = 1
            while q:
                nr, nc = q.popleft()
                drxn = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in drxn:
                    row, col = nr + dr, nc + dc
                    if -1 < row < ROW and -1 < col < COLS and (row, col) not in visit and grid[row][col] == 1:
                        count += 1
                        q.append((row, col))
                        visit.add((row, col))

            return count
        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxm = max(bfs(r, c), maxm)

        return maxm