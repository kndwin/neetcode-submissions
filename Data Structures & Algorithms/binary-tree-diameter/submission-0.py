# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def maxHeight(node):
            if not node: return 0
            l,r = maxHeight(node.left), maxHeight(node.right)
            nonlocal res
            res = max(res, l + r)
            return 1 + max(l, r)
        maxHeight(root)
        return res