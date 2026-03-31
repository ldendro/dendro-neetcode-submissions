class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(n):
            idx = abs(nums[i]) - 1
            if idx < n and idx > -1:
                if nums[idx] == 0:
                    nums[idx] = -1 * (n + 1)
                elif nums[idx] > 0:
                    nums[idx] *= -1

        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        
        return n + 1
