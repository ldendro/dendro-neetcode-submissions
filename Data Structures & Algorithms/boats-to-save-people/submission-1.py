class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res, left, right = 0, 0, len(people) - 1
        while left <= right:
            target = limit - people[right]
            right -= 1
            res += 1
            if people[left] <= target:
                left += 1

        return res