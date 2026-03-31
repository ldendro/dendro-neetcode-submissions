class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preCount = defaultdict(int)
        preCount[0] = 1
        res = total = 0
        for i in range(n):
            total += nums[i]
            if (total - k) in preCount:
                res += preCount[total-k]
            preCount[total] += 1

        return res 
