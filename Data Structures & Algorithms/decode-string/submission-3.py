class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                temp = num = ""
                while stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)*temp) 
            else:
                stack.append(char)

        return "".join(stack)   
