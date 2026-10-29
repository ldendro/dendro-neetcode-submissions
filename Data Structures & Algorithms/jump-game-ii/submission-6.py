class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [i for i in range(len(nums))]
        for i in range(len(nums)-1):
            if i + nums[i] >= len(nums):
                dp[-1] = min(dp[-1], dp[i]+1)
            else:
                dp[i+nums[i]] = min(dp[i+nums[i]], dp[i]+1)

        return dp[-1]