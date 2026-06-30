class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        minHeap = []
        curCap = 0
        for trip in trips:
            tripCap = trip[0]
            start = trip[1]
            end = trip[2]
            curCap += tripCap

            while minHeap and minHeap[0][0] <= start:
                curCap -= heapq.heappop(minHeap)[1]

            if curCap > capacity:
                return False

            heapq.heappush(minHeap, (end, tripCap))
        return True 