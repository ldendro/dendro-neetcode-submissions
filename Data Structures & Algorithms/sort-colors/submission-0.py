from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        countColors = Counter(nums)
        for i in range(3):
            for j in range(idx, idx + countColors[i]):
                nums[j] = i
            idx += countColors[i]

        return nums