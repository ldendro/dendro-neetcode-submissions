class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[-1] * N for _ in range(M)]

        def dfs(r,c):
            if r == M or c == N:
                return float('inf')
            if r == (M-1) and c == (N-1):
                return grid[r][c]
            if dp[r][c] != -1:
                return dp[r][c]
            dp[r][c] = grid[r][c] + min(dfs(r+1,c), dfs(r, c+1))
            return dp[r][c]

        return dfs(0,0)