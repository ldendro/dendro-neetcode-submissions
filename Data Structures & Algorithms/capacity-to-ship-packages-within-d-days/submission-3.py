class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxWeights = max(weights)
        l, r = maxWeights, maxWeights * len(weights)
        res = r
        # 1 1 1 1 1 1 1 1 1 1 days = 1
        while l <= r:
            w = l + (r-l) // 2
            tempDays = 1
            sumWeight = 0
            for i in range(len(weights)):
                if sumWeight + weights[i] > w:
                    sumWeight = weights[i]
                    tempDays += 1
                else:
                    sumWeight += weights[i]

            if tempDays <= days:
                r = w - 1
                res = min(res, w)
            else:
                l = w + 1

        return res
