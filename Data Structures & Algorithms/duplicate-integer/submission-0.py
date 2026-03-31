class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for i in range(len(nums)):
            if nums[i] not in numSet:
                numSet.add(nums[i])
            else:
                return True
        return False