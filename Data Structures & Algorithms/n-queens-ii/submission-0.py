class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiag = set()
        negDiag = set()
        self.res = 0
        def backTrack(r):
            if r == n:
                self.res += 1
                return
            for c in range(n):
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                backTrack(r+1)
                cols.remove(c) 
                posDiag.remove(r+c)
                negDiag.remove(r-c)
        backTrack(0)
        return self.res