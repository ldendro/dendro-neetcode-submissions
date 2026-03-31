from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countN = Counter(nums)
        for (key, value) in countN.items():
            if value > len(nums) // 2:
                return key

        return None