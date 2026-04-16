class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy, forward = ListNode(0, head), head
        while n>0:
            forward, n = forward.next, n-1

        prev = dummy
        while forward:
            prev, forward = prev.next, forward.next

        prev.next = prev.next.next
        return dummy.next
       