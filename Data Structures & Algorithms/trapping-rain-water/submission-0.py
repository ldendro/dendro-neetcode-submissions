class Solution:
    def trap(self, height: List[int]) -> int:
        maxHeight = max(height)
        res = 0
        # 0, 2, 0, 3, 1, 0, 1, 3, 2, 1
        for i in range(1, maxHeight + 1):
            temp = 0
            contain = False
            for j in range(len(height)):
                if height[j] >= i: 
                    if contain == True:
                        res += temp
                        temp = 0
                    else:
                        contain = True
                elif height[j] < i and contain:
                    temp += 1
        
        return res