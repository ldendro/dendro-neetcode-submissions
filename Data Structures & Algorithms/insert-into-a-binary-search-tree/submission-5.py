# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def dfs(node):
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val, None, None)
                    return 
                else:
                    return dfs(node.right)
            else:
                if not node.left:
                    node.left = TreeNode(val, None, None)
                    return 
                else:
                    return dfs(node.left)


        if not root:
            return TreeNode(val)
        dfs(root)
        return root 
