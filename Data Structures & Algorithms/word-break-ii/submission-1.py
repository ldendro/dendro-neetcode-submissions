class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        subset, res = [], []


        def dfs(i):
            if i == len(s):
                res.append(" ".join(subset))
                return 

            for word in wordDict:
                if s[i:i+len(word)] == word:
                    subset.append(word)
                    dfs(i+len(word))
                    subset.pop()
                
        dfs(0)
        return res