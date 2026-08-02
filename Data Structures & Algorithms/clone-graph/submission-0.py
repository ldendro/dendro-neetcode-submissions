"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        hashMap = {}

        def dfs(node):
            newNode = Node(node.val)
            hashMap[node] = newNode
            for neighbor in node.neighbors:
                if neighbor not in hashMap:
                    dfs(neighbor)
                newNode.neighbors.append(hashMap[neighbor])

            return newNode

        return dfs(node)