"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        newHead = Node(head.val)
        mapOldToNew = { head: newHead }
        curr = head.next
        newCurr = newHead

        # First pass copies without random
        while curr is not None:
            newNode = Node(curr.val)
            mapOldToNew[curr] = newNode
            newCurr.next = newNode
            newCurr = newCurr.next
            curr = curr.next
        
        # Second pass updates random
        newCurr, curr = newHead, head
        while curr is not None:
            if curr.random is not None:
                newCurr.random = mapOldToNew[curr.random]
            newCurr = newCurr.next
            curr = curr.next

        return newHead
        

        