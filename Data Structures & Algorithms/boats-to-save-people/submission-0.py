class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort()
        left, right = 0, len(people) - 1
        while left < right:
            while left < right and people[right] == 0:
                right -= 1

            while left < right and people[left] == 0:
                left += 1

            if people[left] + people[right] <= limit:
                res += 1
                people[left] = people[right] = 0
                left += 1
                right -= 1
            else:
                right -= 1

        for i in range(len(people)):
            if people[i] != 0:
                res += 1

        return res