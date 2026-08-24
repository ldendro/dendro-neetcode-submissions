class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        minHeap = [[grid[0][0], 0, 0]]

        visit.add((0,0))
        while minHeap:
            water, r1, c1 = heapq.heappop(minHeap)
            if r1 == len(grid)-1 and c1 == len(grid[0])-1:
                return water 
            for dr, dc in directions:
                r2, c2 = r1 + dr, c1 + dc
                if min(r2, c2) < 0 or r2 == len(grid) or c2 == len(grid[0]) or (r2, c2) in visit:
                    continue
                visit.add((r2, c2))
                heapq.heappush(minHeap, [max(grid[r2][c2], water), r2, c2])

        
