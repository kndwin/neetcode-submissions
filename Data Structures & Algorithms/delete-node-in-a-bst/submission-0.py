# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(lr, target):
            if not lr:
                return None
            if target < lr.val:
                lr.left = dfs(lr.left, target)
            elif target > lr.val:
                lr.right = dfs(lr.right, target)

            else:
                if not lr.left:
                    return lr.right
                if not lr.right:
                    return lr.left
                else:
                    successor = find_min(lr.right)
                    lr.val = successor.val
                    lr.right = dfs(lr.right, successor.val)
                    return lr
            return lr
        
        def find_min(node):
            if node.left:
                return find_min(node.left)
            return node

        return dfs(root, key)