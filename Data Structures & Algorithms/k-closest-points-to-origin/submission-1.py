class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mapping = {}
        minDistance = []
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            if dist in mapping:
                mapping[dist].append(point)
            else:
                mapping[dist] = [point]
            heapq.heappush(minDistance, dist)
        
        res = []
        while k != 0:
            dist = heapq.heappop(minDistance)
            idx = 0
            res.append(mapping[dist].pop())
            k -= 1

        return res