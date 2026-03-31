from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        repeats = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in repeats:
                if abs(repeats[nums[i]] - i) <= k:
                    return True
                else:
                    repeats[nums[i]] = i
            else:
                repeats[nums[i]] = i 
        return False