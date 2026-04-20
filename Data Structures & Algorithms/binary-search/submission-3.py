class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            num = left + ((right - left) // 2)
            if nums[num] > target:
                right = num - 1
            elif nums[num] < target:
                left = num + 1
            else:
                return num 
        return -1