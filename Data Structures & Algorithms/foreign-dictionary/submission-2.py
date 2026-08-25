class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        res = []
        visit = {}
        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True 

            res.append(c)
            visit[c] = False

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)