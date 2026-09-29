class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}
        def dfs(i):
            if i == len(stoneValue):
                return 0
            if i in dp:
                return dp[i]
            maxVal = float("-inf")
            for j in range(i, min(i+3, len(stoneValue))):
                maxVal = max(maxVal, sum(stoneValue[i:j+1]) - dfs(j+1))
            dp[i] = maxVal
            return maxVal

        score = dfs(0)
        if score < 0:
            return "Bob"
        elif score > 0:
            return "Alice"
        else:
            return "Tie"