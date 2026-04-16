# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], deque([(root, 0)])
        while stack:
            popped, depth = stack.popleft()
            if not popped: continue
            if len(res)-1 < depth:
                res.append(popped.val)
            else:
                res[depth] = popped.val
            if popped.left:
                stack.append((popped.left, 1 + depth))
            if popped.right:
                stack.append((popped.right, 1 + depth))
            print(popped.val)
        return res
        