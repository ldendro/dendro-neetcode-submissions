from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = Counter(nums)
        res = []
        for (key, value) in counts.items():
            if value > (n//3):
                res.append(key)
        
        return res