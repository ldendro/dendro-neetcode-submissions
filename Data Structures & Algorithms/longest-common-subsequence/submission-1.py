class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text2), len(text1)
        dp = [[0] * N for _ in range(M)]

        def dfs(r, c):
            if r == M or c == N:
                return 0
            if dp[r][c] != 0:
                return dp[r][c]
            if text1[c] == text2[r]:
                dp[r][c] = 1 + dfs(r+1,c+1)
            else:
                dp[r][c] += max(dfs(r+1,c),dfs(r, c+1))
            return dp[r][c]

        return dfs(0,0)