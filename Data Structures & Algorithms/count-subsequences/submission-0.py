class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def dfs(i, j):
            if j == len(t):
                return 1 

            if (i, j) in dp:
                return dp[(i,j)]

            count = 0
            for idx in range(i, len(s)):
                if s[idx] == t[j]:
                    count += dfs(idx+1, j+1)

            dp[(i,j)] = count
            return count 

        return dfs(0,0)