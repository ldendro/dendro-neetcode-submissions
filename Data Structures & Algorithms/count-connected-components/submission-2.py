class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visit = set()
        def dfs(i):
            visit.add(i)
            for num in graph[i]:
                if num not in visit:
                    dfs(num)

        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1

        return res