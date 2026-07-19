class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        kSum = sum(nums) // k
        if kSum != sum(nums) / k:
            return False

        used = [False] * len(nums)
        nums.sort(reverse=True)

        def dfs(i, k, subTotal):
            if k == 0: 
                return True 
            if subTotal == kSum:
                return dfs(0, k - 1, 0)
            for j in range(i, len(nums)):
                if used[j] or subTotal + nums[j] > kSum:
                    continue
                used[j] = True 
                if dfs(i+1, k, subTotal + nums[j]):
                    return True 
                used[j] = False
                if subTotal == 0:
                    return False

        return dfs(0,k,0)

