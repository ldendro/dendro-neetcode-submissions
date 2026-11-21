class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)]
        used = []
        count = [0] * n

        for start, end in meetings:
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            if not available:
                endTime, firstRoom = heapq.heappop(used)
                end = endTime + (end - start)
                heapq.heappush(available, firstRoom)
            
            room = heapq.heappop(available)
            heapq.heappush(used, [end, room])
            count[room] += 1

        return count.index(max(count))