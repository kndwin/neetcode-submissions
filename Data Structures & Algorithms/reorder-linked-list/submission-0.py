class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Get mid point
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # Reverse
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev, second = second, temp
        # Merge
        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2