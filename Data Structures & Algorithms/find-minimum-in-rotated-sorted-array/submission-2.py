class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Difference between min and max is len(nums) - 1
        # Consider nums[0] first min, then run binary search on nums and if
        # mid point of l and r is less than nums[0], set  r = m - 1 and min accordinly, else l = m + 1
        l, r = 0, len(nums) - 1
        minNum = min(nums[l], nums[r])
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < minNum:
                r = m - 1
                minNum = nums[m]
            else:
                l = m + 1
        
        return minNum
