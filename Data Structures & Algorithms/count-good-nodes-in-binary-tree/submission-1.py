# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 1

        def dfs(root, lmax):
            nonlocal count

            if root is None: 
                return
            if root.left:
                count += 1 if root.left.val >= lmax else 0
                dfs(root.left, max(lmax, root.left.val))
            if root.right:
                count += 1 if root.right.val >= lmax else 0
                dfs(root.right, max(lmax, root.right.val))

        if root is None: 
            return 0
        dfs(root, root.val)
        return count
        