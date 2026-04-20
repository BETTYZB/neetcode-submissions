from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF =  2147483647
        visit = set()

        que = deque()
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    que.append((r, c))
                    visit.add((r, c))
        count = 1
        while que:
            siz = len(que)
            for i in range(siz):
                (r, c) = que.popleft()
                drxn = [(0, 1), (1, 0), (-1, 0),(0, -1)]

                for dr, dc in drxn:
                    if 0 <= dr + r < ROWS and 0 <= dc + c < COLS and (dr + r,dc + c) not in visit and grid[dr + r][dc + c] != -1:
                        grid[dr + r][dc + c] = count
                        que.append((dr + r,dc + c))
                        visit.add((dr + r,dc + c))

            count += 1



                

