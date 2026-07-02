class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap, maxHeap = [], []
        for i in range(len(profits)):
            heapq.heappush(minHeap, (capital[i], profits[i]))

        if w < minHeap[0][0]:
            return w
            
        while k > 0:
            while minHeap and w >= minHeap[0][0]:
                prof = heapq.heappop(minHeap)[1]
                heapq.heappush(maxHeap, -prof)

            w += -heapq.heappop(maxHeap)
            k -= 1

        return w 