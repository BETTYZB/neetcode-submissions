class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # interate through the matrix
        # grid[r][c] == 1 recursive call
        # '' == 0 or visited ; conitune

        ROW = len(grid)
        COLS = len(grid[0])
        visit = set()
        count = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                drxn = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in drxn:
                    r = dr + row 
                    c = dc + col
                    if -1 < r < ROW and -1 < c < COLS and grid[r][c] == "1" and (r, c) not in visit:
                        q.append((r, c))
                        visit.add((r, c)) 

        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    count += 1
            
        return count

        