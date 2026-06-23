class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStones = []
        for stone in stones:
            heapq.heappush(maxStones, -stone)

        while len(maxStones) > 1:
            first = -heapq.heappop(maxStones)
            second = -heapq.heappop(maxStones)
            res = first - second
            if res != 0:
                heapq.heappush(maxStones, -res)
            
        return -maxStones[0] if maxStones else 0