class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = nums[0], nums[0]
        for num in nums[1:]:
            tmp = curMax * num
            curMax = max(tmp, curMin * num, num)
            curMin = min(tmp, curMin * num, num)
            res = max(curMax, res)
        return res