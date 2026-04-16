# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        overflow, looped = 0, 0
        ans = curr = ListNode()
        while l2 is not None or l1 is not None or overflow > 0:

            val1, val2 = 0, 0

            if l1 is not None:
                print(f"l1: {l1.val}")
                val1 = l1.val
                l1 = l1.next
            
            if l2 is not None:
                print(f"l2: {l2.val}")
                val2 = l2.val
                l2 = l2.next
            
            val = val1 + val2 + overflow
            digit = val % 10
            overflow = int((val - digit) / 10)

            curr.next = ListNode(digit)
            curr = curr.next

            print(f"val: {val}, overflow: {overflow}")
            looped += 1
            print(f"looped: {looped}")
        return ans.next
