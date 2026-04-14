class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        l = r = 0
        while r < len(path):
            if path[r] != "/":
                l = r
                while r < len(path) and path[r] != "/":
                    r += 1
                if stack and (r - l) == 2 and path[l] == "." and path[l+1] == ".":
                    stack.pop()
                elif (r - l) > 2 or path[l] != ".":
                    stack.append(path[l:r])
            else:
                r += 1
                
        return f"/{"/".join(stack)}"
