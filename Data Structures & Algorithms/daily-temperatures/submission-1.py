class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]
        stack = [temperatures[-1]]
        # 30 38 36 35 40 28
        for i in range(len(temperatures)-2, -1, -1):
            for j in range(len(stack)-1, -1,  -1):
                if stack[j] > temperatures[i]:
                    res.append(len(stack) - j)
                    break
                elif j == 0:
                    res.append(0)
                    
            stack.append(temperatures[i])

        res.reverse()
        return res
