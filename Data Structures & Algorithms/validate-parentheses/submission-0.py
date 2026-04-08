class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')':'(',
            ']':'[',
            '}':'{',
        }

        stack = []
        for c in s:
            if c in brackets:
                if not stack or stack.pop() != brackets[c]:
                    return False
            else:
                stack.append(c)

        return not stack 