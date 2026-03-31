from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        freq = Counter(nums)
        res = []
        for key, value in freq.items():
            buckets[value].append(key)

        for i in range(n, 0, -1):
            if buckets[i]:
                res.extend(buckets[i])
                if len(res) >= k:
                    return res[:k]

        