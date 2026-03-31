class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        pflag = False

        for i in range(n):
            if nums[i] > 0 and not pflag:
                pflag = True
                if nums[i] > 1:
                    return 1
            if pflag:
                if i == (n-1) and nums[n-1] >= 0:
                    return nums[n-1] + 1
                elif nums[i] + 1 != nums[i+1] and nums[i] != nums[i+1]:
                    return nums[i] + 1

        return 1