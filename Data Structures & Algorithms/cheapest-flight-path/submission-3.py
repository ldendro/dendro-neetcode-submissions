class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n 
        adj = [[] for _ in range(n)]
        for source, dest, price in flights:
            adj[source].append([dest, price])

        prices[src] = 0
        q = deque([(0,src,0)])
        while q:
            cst, p1, stops = q.popleft()
            if stops > k:
                continue
            for p2, newPrice in adj[p1]:
                if newPrice + cst < prices[p2]:
                    prices[p2] = newPrice + cst
                    q.append((cst + newPrice, p2, stops+1))

        return prices[dst] if prices[dst] != float('inf') else -1