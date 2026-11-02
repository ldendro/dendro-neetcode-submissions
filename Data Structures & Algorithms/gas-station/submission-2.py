class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank = res = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            if tank < 0 and diff > 0:
                res = i
                tank = diff
            else:
                tank += diff

        return res if tank >= 0 else -1
