class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = temp = float('-inf') 
        for num in nums:
            if num > temp and temp < 0:
                temp = num
            else:
                temp += num
            res = max(res, temp)
        return res