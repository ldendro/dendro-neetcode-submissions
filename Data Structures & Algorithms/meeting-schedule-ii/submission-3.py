"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        res = 1
        minHeap = [intervals[0].end]
        # [0 3] [1 2] [3 7] [3 8]
        for i in range(1, len(intervals)):
            if minHeap[0] > intervals[i].start:
                res += 1
            else:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, intervals[i].end)
            
        return res 