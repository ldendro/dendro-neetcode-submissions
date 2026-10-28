class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0
        for i in range(len(nums)-1):
            if nums[i] == 0 and maxIndex == i:
                return False
            else:
                maxIndex = max(maxIndex, i + nums[i])
        return True 