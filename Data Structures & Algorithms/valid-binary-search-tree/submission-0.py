# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, maxVal, minVal):
            if not node:
                return True 
            if minVal < node.val < maxVal:
                return dfs(node.left, node.val, minVal) and dfs(node.right, maxVal, node.val)
            else:
                return False

        return dfs(root, float('inf'), float('-inf'))
                