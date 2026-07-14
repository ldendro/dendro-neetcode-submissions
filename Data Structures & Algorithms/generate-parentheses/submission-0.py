class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []
        def dfs(openC, closeC):
            if openC == closeC == n:
                res.append("".join(stack))
                return
            
            if openC < n:
                stack.append("(")
                dfs(openC + 1, closeC)
                stack.pop()
            if closeC < openC:
                stack.append(")")
                dfs(openC, closeC+1)
                stack.pop()

        dfs(0,0)
        return res