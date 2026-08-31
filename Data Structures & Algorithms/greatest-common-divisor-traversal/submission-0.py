class unionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return
        
        if self.rank[p1] < self.rank[p2]:
            p1, p2 = p2, p1
        self.par[p2] = p1
        self.rank[p1] += self.rank[p2]  
        self.count -= 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = unionFind(len(nums))
        factor_index = {}
        for i, num in enumerate(nums):
            f = 2
            while f * f <= num:
                if num % f == 0:
                    if f in factor_index:
                        uf.union(i, factor_index[f])
                    else:
                        factor_index[f] = i
                    while num % f == 0:
                        num = num // f
                f += 1
            if num > 1:
                if num in factor_index:
                    uf.union(i, factor_index[num])
                else:
                    factor_index[num] = i

        return uf.count == 1
