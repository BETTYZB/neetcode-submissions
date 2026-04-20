class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # look for 0 and call dfs on it
        ROW = len(board)
        COLS = len(board[0])


        def dfs(r,c):
            if min(r, c) < 0 or r >= ROW or c >= COLS or board[r][c] != "O":
                return 
            board[r][c] = "T"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return 

        for r in range(ROW):
            for c in range(COLS):
                if (board[r][c] == "O" and (r in [0, ROW - 1] or c in [0, COLS - 1])):
                    dfs(r,c)
                 

        
        for r in range(ROW):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"

        