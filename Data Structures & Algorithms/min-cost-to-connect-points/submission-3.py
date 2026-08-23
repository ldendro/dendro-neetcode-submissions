class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([j, cost])
                adj[j].append([i, cost])

        res = 0
        minHeap = [[0,0]]
        visit = set()
        while len(visit) != len(points):
            cost, point = heapq.heappop(minHeap)
            if point in visit:
                continue
            res += cost
            visit.add(point)
            for nei, neiCost in adj[point]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])

        return res