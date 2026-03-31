class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
            
        min_len = min(len(s) for s in strs)
        res = ""
        for j in range(min_len):
            for i in range(1, len(strs)):
                if strs[i][j] == strs[i-1][j]:
                    if i == (len(strs) - 1):
                        res += strs[i][j]
                else:
                    return res
        return res
