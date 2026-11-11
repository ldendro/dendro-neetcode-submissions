class Solution:
    def checkValidString(self, s: str) -> bool:
        openP = []
        stars = []

        for i in range(len(s)):
            if s[i] == '(':
                openP.append(i)
            elif s[i] == ')':
                if not openP:
                    if not stars:
                        return False
                    else:
                        stars.pop()
                else:
                    openP.pop()
            else:
                stars.append(i)

        while openP:
            if not stars or stars[-1] < openP[-1]:
                return False
            openP.pop()
            stars.pop()

        return True