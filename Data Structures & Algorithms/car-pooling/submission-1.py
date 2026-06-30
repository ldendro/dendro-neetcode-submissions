from collections import Counter
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        capTime = Counter()
        for trip in trips:
            for i in range(trip[1], trip[2]):
                capTime[i] += trip[0]
                if capTime[i] > capacity:
                    return False
        return True
