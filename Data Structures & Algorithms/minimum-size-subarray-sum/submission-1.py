class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        count = l = 0
        for r in range(len(nums)):
            count += nums[r]
            if count >= target:
                while l <= r and count >= target:
                    res = min(res, (r - l + 1))
                    count -= nums[l]
                    l += 1

        return res if res != float('inf') else 0