class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def dfs(l, r, total):
            if l >= r:
                return 0
            if (l, r) in dp:
                return dp[(l,r)]
            total += max(piles[l]-dfs(l+1,r,total), piles[r]-dfs(l, r-1, total))
            dp[(l, r)] = total
            return dp[(l,r)]

        return dfs(0,len(piles)-1, 0) > 0