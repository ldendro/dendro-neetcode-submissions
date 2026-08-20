class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        network = defaultdict(list)
        for u, v, t in times:
            network[u].append([v, t])
            if u == k:
                heapq.heappush(minHeap, [t, v])

        visit = set()
        visit.add(k)
        while minHeap:
            t, v = heapq.heappop(minHeap)
            if v in visit:
                continue
            visit.add(v)
            if len(visit) == n:
                return t
            for nei, time in network[v]:
                if nei not in visit:
                    heapq.heappush(minHeap, [t + time, nei])

        return -1

