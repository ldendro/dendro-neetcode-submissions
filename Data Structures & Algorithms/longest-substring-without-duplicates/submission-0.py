class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = l = 0
        subString = set()
        for r in range(len(s)):
            if s[r] not in subString:
                subString.add(s[r])
                maxLen = max(maxLen, len(subString))
            else:
                while s[r] in subString:
                    subString.remove(s[l])
                    l += 1
                subString.add(s[r])

        return maxLen