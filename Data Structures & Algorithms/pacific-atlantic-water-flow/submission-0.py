class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visit, prevVal):
            if min(r, c) < 0 or r == ROWS or c == COLS or (r,c) in visit or heights[r][c] < prevVal:
                return

            visit.add((r,c))
            dfs(r-1, c, visit, heights[r][c])
            dfs(r+1, c, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, 0)
            dfs(r, COLS-1, atlantic, 0)

        for c in range(COLS):
            dfs(0, c, pacific, 0)
            dfs(ROWS-1, c, atlantic, 0)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res