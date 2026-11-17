class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        interval = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] == interval[0] or intervals[i][0] < interval[1]:
                res += 1
                interval[1] = min(intervals[i][1], interval[1])
            else:
                interval = intervals[i]

        return res