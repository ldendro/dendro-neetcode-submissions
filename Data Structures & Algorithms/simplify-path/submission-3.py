class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        l = r = 0
        while r < len(path):
            if path[r] != "/" and path[r] != ".":
                l = r
                while r < len(path) and path[r] != "/":
                    r += 1
                stack.append(path[l:r])
            elif path[r] == ".":
                l = r
                while r < len(path) and path[r] != "/":
                    r += 1
                if (r - l) > 2:
                    stack.append(path[l:r])
                elif stack and (r-l) == 2:
                    stack.pop()
            else:
                r += 1
                
        return f"/{"/".join(stack)}"
