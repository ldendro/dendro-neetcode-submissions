from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        sCount = Counter(s)
        maxHeap = []
        for key, value in sCount.items():
            heapq.heappush(maxHeap, [-value, key])

        res = []
        prev = ""
        while maxHeap:
            value1, key1 = heapq.heappop(maxHeap)
            if key1 == prev:
                if maxHeap:
                    value2, key2 = heapq.heappop(maxHeap)
                else:
                    return ""
                if key2 == prev:
                    return ""
                heapq.heappush(maxHeap, [value1, key1])
                value1, key1 = value2, key2
            prev = key1
            res.append(key1)
            if value1 != -1:
                heapq.heappush(maxHeap, [value1+1, key1])

        return "".join(res)