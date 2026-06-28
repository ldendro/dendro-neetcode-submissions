class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort()
        time = tasks[0][0]
        minHeap = []
        idx = 0
        while idx < len(tasks) or minHeap:
            while idx < len(tasks) and tasks[idx][0] <= time:
                heapq.heappush(minHeap, [tasks[idx][1], tasks[idx][2]])
                idx += 1
            
            if minHeap:
                pTime, task = heapq.heappop(minHeap)
                time += pTime
                res.append(task)
            else:
                time += 1

        return res

            