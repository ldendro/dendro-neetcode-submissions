class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        for i in range(n+1):
            if math.floor(math.sqrt(i)) == math.sqrt(i):
                nums.append(i)

        dp = {0:0}
        for i in range(1, n+1):
            for num in nums:
                dp[i] = min(dp.get(i, n), 1 + dp.get(i - num, n))

        return dp[n]

        