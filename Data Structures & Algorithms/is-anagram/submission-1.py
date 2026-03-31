from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        sCount = Counter(s)
        tCount = Counter(t)
        for key in sCount.keys():
            if sCount[key] != tCount[key]:
                return False

        return True