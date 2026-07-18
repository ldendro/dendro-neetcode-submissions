class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, comb = [], []
        ltrs = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(i):
            if i == len(digits):
                if comb:
                    res.append("".join(comb.copy()))
                return
            for ltr in ltrs[digits[i]]:
                comb.append(ltr)
                dfs(i+1)
                comb.pop()

        dfs(0)
        return res
