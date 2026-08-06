class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        safe = set()

        def dfs(r, c, safe):
            if min(r, c) < 0 or r == ROWS or c == COLS or board[r][c] == "X" or (r, c) in safe:
                return

            safe.add((r,c))
            dfs(r-1, c, safe)
            dfs(r+1, c, safe)
            dfs(r, c-1, safe)
            dfs(r, c+1, safe)

        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0, safe)
            if board[r][COLS-1] == "O":
                dfs(r, COLS-1, safe)

        for c in range(1, COLS-1):
            if board[0][c] == "O":
                dfs(0, c, safe)
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1, c, safe)

        for r in range(1, ROWS-1):
            for c in range(1, COLS-1):
                if board[r][c] == "O" and (r,c) not in safe:
                    board[r][c] = "X"

           