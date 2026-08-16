class unionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        x1, x2, = self.find(x1), self.find(x2)
        if x1 == x2:
            return False
        if self.rank[x1] > self.rank[x2]:
            self.rank[x1] += self.rank[x2]
            self.par[x2] = x1
        else:
            self.rank[x2] += self.rank[x1]
            self.par[x1] = x2

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = unionFind(len(accounts))
        emailToAcc = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(emailToAcc[e], i)
                else:
                    emailToAcc[e] = i

        emailGroup = defaultdict(list)
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)

        res = []
        for i, e in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))

        return res 



