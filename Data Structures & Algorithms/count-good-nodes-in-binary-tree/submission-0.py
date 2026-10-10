# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root,old_max):
            if not root:
                return 0
            good = 1 if root.val>=old_max else 0
            new_max = max(root.val, old_max)
            return good+dfs(root.left,new_max)+dfs(root.right,new_max)

        return dfs(root,root.val)