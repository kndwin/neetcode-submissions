# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(node):
            if not node: return 0
            l,r = dfs(node.left), dfs(node.right)
            nonlocal balanced
            if l - r > 1 or r - l > 1:
                balanced = False
            return 1 + max(l, r)
        dfs(root)
        return balanced