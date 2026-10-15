class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        M, N = len(matrix), len(matrix[0])
        D = [(1,0), (-1, 0), (0, 1), (0,-1)]
        def dfs(r, c, prev, seen):
            if min(r, c) < 0 or r == M or c == N or (r, c) in seen or prev >= matrix[r][c]:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            seen.add((r, c))
            res = 0
            for d1, d2 in D:
                res = max(res, 1 + dfs(r+d1, c+d2, matrix[r][c], seen))
            seen.remove((r,c))
            dp[(r, c)] = res
            return res

        res = 0
        for i in range(M):
            for j in range(N):
                res = max(res, dfs(i, j, float('-inf'), set())) 

        return res