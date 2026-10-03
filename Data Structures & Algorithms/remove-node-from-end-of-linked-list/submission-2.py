# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        cur = head
        cur_pos = 1

        if n == length: # element to be removed is head
            head = head.next
        else: 
            while cur_pos < length - n:
                cur = cur.next
                cur_pos += 1
        
            # the element after ours is the Nth and should be removed
            cur.next = cur.next.next

        return head