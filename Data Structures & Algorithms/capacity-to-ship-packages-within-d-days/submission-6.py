class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Minimum possible weight is the max weight in weights, because we
        # can't have a situation where the maximum capacity weight is less than 
        # a weight in weights, we couldn't ship that weight. 
        # Maximum possible weight is the situation where we must ship all weights 
        # in one day, which is then just the sum of the weights in the array 
        l, r = max(weights), sum(weights)
        res = r
    
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
