class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashSet = set()
        l = r = 0
        while r < len(nums):
            if nums[r] in hashSet:
                return True
            else:
                hashSet.add(nums[r])
            r += 1

            if len(hashSet) > k:
                hashSet.remove(nums[l])
                l += 1

        return False