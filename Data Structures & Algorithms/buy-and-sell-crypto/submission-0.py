class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, minPrice = 0, prices[0]
        for sell in prices:
            res = max(res, sell - minPrice)
            minPrice = min(minPrice, sell)

        return res