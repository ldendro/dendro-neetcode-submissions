class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1] * N for _ in range(M)]
        def dfs(r, c):
            if r == M or c == N or obstacleGrid[r][c] == 1:
                return 0
            if r == (M-1) and c == (N-1):
                return 1
            if dp[r][c] != -1:
                return dp[r][c]
            dp[r][c] = dfs(r+1, c) + dfs(r, c+1)
            return dp[r][c]

        return dfs(0,0)