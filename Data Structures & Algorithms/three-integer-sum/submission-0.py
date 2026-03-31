class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums)-2):
            if k > 0 and nums[k] == nums[k-1]:
                continue

            if nums[k] > 0:
                break

            i = k + 1
            j = len(nums) - 1
            while i < j:
                total = nums[k] + nums[i] + nums[j]
                if total < 0:
                    i += 1
                elif total > 0:
                    j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1

                    while i < j and nums[i] == nums[i-1]:
                        i += 1

                    while j > i and nums[j] == nums[j+1]:
                        j -= 1
                        
        return res

 