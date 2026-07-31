# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(local_root):
            if not local_root:
                return
            if local_root.left:
                dfs(local_root.left)

            result.append(local_root.val)

            if local_root.right:
                dfs(local_root.right)
        
        dfs(root)

        return result