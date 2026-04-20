class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid); COLS = len(grid[0])
        visit = set()
        q = deque()
        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        count = 1
        while q:
            for n in range(len(q)):
                r, c = q.popleft()
                drxn = [(r, c + 1), (r + 1, c), (r - 1, c), (r, c - 1)]

                for nr, nc in drxn:
                    if min(nr, nc) < 0 or nr >= ROW or nc >= COLS or grid[nr][nc] == -1 or (nr, nc) in visit:
                        continue
                    else:
                        grid[nr][nc] = count
                        q.append((nr, nc))
                        visit.add((nr, nc))

            count += 1
                    
        
                


        
 