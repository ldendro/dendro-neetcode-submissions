class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]



        def dfs(i, prev):
            if visit[i]:
                return True
            visit[i] = True
            for node in graph[i]:
                if node != prev and dfs(node, i):
                    return True
            return False

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            visit = [False] * n

            if dfs(u, -1):
                return [u, v]
