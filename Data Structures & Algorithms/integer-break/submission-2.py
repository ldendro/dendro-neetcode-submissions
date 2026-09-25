class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [1] * (n+1)
        for i in range(1, n+1):
            for j in range(i-1, -1, -1):
                dp[i] = max(dp[i], dp[j]*(i-j))

        return dp[n]