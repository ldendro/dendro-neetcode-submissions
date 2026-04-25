class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # [3,4,5,6,1,2]
        # (0, 5) (3, 5) (3, 4) (4, 4)
        # m = 2, 4, 3
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1 
            else:
                r = m 
        return nums[l] 