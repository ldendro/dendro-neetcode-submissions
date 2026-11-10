class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        sCount = Counter(s)
        res = []
        pool = set()
        for i in range(len(s)):
            sCount[s[i]] -= 1
            if sCount[s[i]] == 0:
                pool.discard(s[i])
                if not pool:
                    res.append((i + 1) - sum(res))
            else:
                pool.add(s[i])
            
        return res