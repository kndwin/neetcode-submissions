# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base edge cases
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        # Initialize vars
        h, c1, c2 = None, None, None
        if list1.val > list2.val:
            h, c1, c2 = list2, list1, list2.next
        else:
            h, c1, c2 = list1, list1.next, list2
        
        # Connect while looping
        c = h
        while c1 is not None and c2 is not None:
            if c1.val > c2.val:
                c.next = c2
                c = c2
                c2 = c2.next
            else:
                c.next = c1
                c = c1
                c1 = c1.next

        # Connect remaining nodes
        if c1 is not None:
            c.next = c1
        if c2 is not None:
            c.next = c2

        return h