class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == '':
            return ""

        res = ''
        tCount, window = {}, {}

        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)

        have, need = 0, len(tCount)
        l = 0 
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in tCount and window[s[r]] == tCount[s[r]]:
                have += 1

            while have == need:
                if (res != '' and (r - l + 1) < len(res)) or res == '':
                    res = s[l:r+1]

                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1

        return res

        