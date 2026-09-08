class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * n
        def dfs(num):
            if num == n:
                return 1
            elif num > n:
                return 0
            elif dp[num] != 0:
                return dp[num]
            step1 = dfs(num+1)
            step2 = dfs(num+2)
            dp[num] = step1 + step2
            return dp[num]

        return dfs(0)