class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        # heights=[3,6,5,7,4,8,1,0]
        # stack = (0, 3) (1, 5) (3, 7) ()
        # maxArea = 0, 6,
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
            
