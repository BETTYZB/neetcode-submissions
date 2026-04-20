class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        path = 0
        visit = set()
        if grid[0][0] == 1:
            return -1
        store = deque()
        store.append((0, 0))
        visit.add((0, 0))
        while store:
            for i in range(len(store)):
                r, c = store.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return path
                drxn = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in drxn:
                    nr, nc = dr + r, dc + c
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visit or grid[nr][nc] == 1:
                        continue
                    store.append((nr, nc))
                    visit.add((nr, nc))
                    
            path += 1

        return -1

        