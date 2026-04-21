class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # 1 2 3 4 
        while l <= r:
            m = l + ((r-l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        if nums[r] > target:
            return l
        else:
            return r + 1

        
