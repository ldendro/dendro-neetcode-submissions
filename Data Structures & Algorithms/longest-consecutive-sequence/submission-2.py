class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0

        for num in nums:
            if num - 1 in numSet:
                continue
            else:
                p = num + 1
                while p in numSet:
                    p += 1
                maxLen = max(maxLen, p - num)

        return maxLen

 