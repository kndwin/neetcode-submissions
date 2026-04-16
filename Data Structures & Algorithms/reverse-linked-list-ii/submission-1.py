# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev, curr, nhead, nTail, after, count = None, head, None, None, None, 1
        while curr:
            if count < left:
                print(f"count before: {count}")
                prev = curr

            if count == left:
                nTail, nHead = curr, prev
            
            if count >= left and count <= right:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                count += 1
                continue
            
            if count == right+1:
                after = curr

            count += 1
            curr = curr.next
        
        nTail.next = after
        if nHead:
            nHead.next = prev
        else:
            head = prev
        
        return head

