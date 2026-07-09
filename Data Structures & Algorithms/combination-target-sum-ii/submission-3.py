class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(idx, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            elif idx == len(candidates) or total > target:
                return
            subset.append(candidates[idx])
            dfs(idx + 1, subset, total + candidates[idx])
            subset.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            dfs(idx + 1, subset, total)

        dfs(0, [], 0)
        return res