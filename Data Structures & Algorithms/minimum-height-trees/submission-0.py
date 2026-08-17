class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        def findHeight(i, prev):
            height = 0
            for node in adj[i]:
                if node == prev:
                    continue
                height = max(height, findHeight(node, i))
            return height + 1

        res = []
        minHeight = float('inf')
        for i in range(n):
            temp = findHeight(i, -1)
            if temp < minHeight:
                minHeight = temp
                res = [i]
            elif temp == minHeight:
                res.append(i)

        return res 