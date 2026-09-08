# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Reverse a singly linked list in place by flipping next pointers as we
walk. cur is the already-reversed prefix (None at the start, so the old
head will point at None and become the new tail). head is the next node
still in original order. Before we overwrite head.next we have to stash
the rest of the list, otherwise that pointer is gone:

    cur = None
    while head:
        nxt = head.next
        head.next = cur
        cur = head
        head = nxt
    return cur

Each step takes the current node off the front and pushes it onto the
front of cur. 1 -> 2 -> 3 becomes None <- 1, then None <- 1 <- 2, then
None <- 1 <- 2 <- 3, and we return 3. Empty list never enters the loop
and returns None. Single node sets next to None and returns itself.

Time:  O(n) — one visit and one rewire per node.
Space: O(1) — just nxt, cur, and head.
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = None
        while head:
            nxt = head.next
            head.next = cur
            cur = head
            head = nxt
        return cur
            