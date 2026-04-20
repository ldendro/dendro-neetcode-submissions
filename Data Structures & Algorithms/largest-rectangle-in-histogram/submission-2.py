class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i in range(len(heights)):
            idx = i
            while stack and heights[i] < stack[-1][1]:
                idx = stack[-1][0]
                maxArea = max(maxArea, (i-stack[-1][0])*stack[-1][1])
                stack.pop()

            stack.append((idx, heights[i]))

        while stack:
            maxArea = max(maxArea, (len(heights)-stack[-1][0])*stack[-1][1])
            stack.pop()

        return maxArea
            
