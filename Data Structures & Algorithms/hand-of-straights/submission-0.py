class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        counts = {}
        for n in hand:
            counts[n] = 1 + counts.get(n, 0)
        
        minH = list(counts.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in counts:
                    return False
                counts[i] -= 1
                if counts[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
                
         