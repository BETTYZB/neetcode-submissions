class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights); COLS = len(heights[0])
        pacific = set() ; atlantic = set()
        def dfs(r, c, visit, preH):
            if min(r, c) < 0 or r >= ROW or c >= COLS or (r, c) in visit or heights[r][c] < preH:
                return
            visit.add((r, c)) 
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])

            return 

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROW - 1, c, atlantic, heights[ROW - 1][c])         
        
        for r in range(ROW):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1]) 

        res = []
        for r in range(ROW):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res
