class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, multiSet, total):
            if total == target:
                res.append(multiSet.copy())
                return
            elif i == len(nums) or total > target:
                return
            
            multiSet.append(nums[i])
            dfs(i, multiSet, total + nums[i])
            multiSet.pop()
            dfs(i + 1, multiSet, total)

        dfs(0, [], 0)
        return res