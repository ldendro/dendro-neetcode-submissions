class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxLeft = maxRight = maxContainer = 0
        while left < right:
            minheight = min(heights[right], heights[left])
            candidate = (right - left) * minheight
            maxContainer = max(maxContainer, candidate)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1

        return maxContainer
            

