class Solution:
    def candy(self, ratings: List[int]) -> int:
        dist = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                dist[i] = 1 + dist[i-1]

        for j in range(len(ratings)-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                dist[j] = max(dist[j], dist[j+1]+1)

        return sum(dist)