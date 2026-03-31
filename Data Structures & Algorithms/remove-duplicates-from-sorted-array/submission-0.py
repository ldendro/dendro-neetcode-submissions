class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        maxNum = nums[-1] + 1
        counter = 0
        p = 1
        while p < len(nums):
            num = nums[p-1]
            while p < len(nums) and nums[p] == num:
                counter += 1
                nums[p] = maxNum
                p += 1
            p += 1
            
        nums.sort()
        return len(nums) - counter
