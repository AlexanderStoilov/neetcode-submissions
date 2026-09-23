# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev, cur = None, slow.next
        slow.next = None # Break connection between the 2 parts.
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt

        first, second = head, prev
        while second: # Stop when the reversed half is used up. Even: both halves same length. Odd: one extra node stays at the end of first; we never visit it here.
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first, second = nxt1, nxt2

        # No need to reassign the local 'head' var. Same first node, .next links are what change. Rebinding the local head wouldn’t matter to the caller anyway.

"""
1   2   3   4
    s
        f

1   2   3   4   5
        s
                f

"""