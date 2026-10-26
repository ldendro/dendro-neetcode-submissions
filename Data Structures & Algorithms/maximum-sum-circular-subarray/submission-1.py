class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax = currMax = float('-inf')
        globMin = currMin = float('inf')
        for num in nums:
            currMin = min(num, num + currMin)
            currMax = max(num, num + currMax)
            globMin = min(globMin, currMin)
            globMax = max(globMax, currMax)

        return max(sum(nums)-globMin, globMax) if globMax > 0 else globMax