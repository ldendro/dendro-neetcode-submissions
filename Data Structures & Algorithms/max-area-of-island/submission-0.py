class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()

        def dfs(r, c):
            if r < 0 or r > len(grid)-1 or c < 0 or c > len(grid[0])-1 or grid[r][c] == 0 or (r,c) in seen:
                return 0 

            seen.add((r,c))

            return dfs(r-1,c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1) + 1


        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res = max(res, dfs(r,c))

        return res

