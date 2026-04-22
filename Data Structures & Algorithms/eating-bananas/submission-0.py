class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
        # piles=[25,10,23,4]
        # h=4
        # (14, 25) (20, 25) (23, 25) (25)
        # 19 22 24 
        while l <= r:
            k = l + (r-l) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        return res