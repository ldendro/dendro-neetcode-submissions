class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []
        for num in nums:
            heapq.heappush(maxheap, -num)

        while k != 1:
            heapq.heappop(maxheap)
            k -= 1

        return -(heapq.heappop(maxheap))