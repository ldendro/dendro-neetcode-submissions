class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        res = 0
        def dfs(r, c):
            if r < 0 or r > len(grid)-1 or c < 0 or c > len(grid[0])-1 or grid[r][c] == '0' or (r, c) in seen:
                return 

            seen.add((r,c))

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

            return True 

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if dfs(r, c):
                    res += 1

        return res 