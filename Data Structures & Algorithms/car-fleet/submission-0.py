class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Zip and sort by position, reverse loop and find min hours (minHours) throughout list
        # Adding to res for each new instance where hours < minHours. \
        # 0 1 4 7
        # 1 2 2 1
        # min = 3
        n = len(position)
        zipSorted = sorted(zip(position, speed))
        res = maxHours = 0
        for i in range(n-1,-1,-1):
            hours = (target - zipSorted[i][0]) / zipSorted[i][1]
            if hours > maxHours:
                res += 1
                maxHours = hours

        return res