# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        left, right = p, q
        if q.val < p.val:
            left, right = q, p

        if not root:
            return root
        if root.val < left.val:
            return self.lowestCommonAncestor(root.right, left, right)
        if root.val > right.val:
            return self.lowestCommonAncestor(root.left, left, right)
        else:
            return root