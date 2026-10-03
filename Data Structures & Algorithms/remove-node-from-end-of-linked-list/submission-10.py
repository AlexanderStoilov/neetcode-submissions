# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # two pointer approach (both starting from left :))
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head 
        left = dummy
        right = head

        for i in range(n):
            right = right.next
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next


"""
Remove Nth Node From End of List, two pointers.

Right walks ahead, then left and right walk together until right falls off
the end. Left is then sitting on the node just before the one to delete, and
left.next = left.next.next skips it.

I started both pointers on the head:

class Solution:
    # two pointer approach (both starting from left :))
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head, head
        ...
        return head

Same edge case as the two-pass version. If the node to delete is the head,
left is already on it, so there is no node before it whose next I can change.
That is when n equals the length.

The fix is a dummy node in front of the real head. Left starts there, so even
the head has a node before it. I tried:

dummy = ListNode(head)

I thought the one argument would land in next. It does not. The constructor is:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

Arguments fill from the left. ListNode(head) sets val to the head node and
leaves next as None. The dummy is not in front of the list. val is a ListNode,
next is None.

An empty node, then a separate assignment, does put it in front:

dummy = ListNode()
dummy.next = head

ListNode(0, head) or ListNode(next=head) would also set next. I used the two
lines.

class Solution:
    # two pointer approach (both starting from left :))
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = head

        for i in range(n):
            right = right.next
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

Right starts on the first real node. The loop moves it n steps, so it begins
the paired walk n nodes ahead. Both then move until right becomes None. Left
stops on the node before the one to delete.

When n is the length, that first loop walks right off the end immediately.
The while never runs, left is still the dummy, and dummy.next = dummy.next.next
drops the old head. return dummy.next is the new head. One node with n = 1
returns None. Removing the tail leaves the node before it pointing at None.

Checked the head, the tail, the second node, one node, and a node in the middle.
[1, 2, 3, 4, 5] with n = 2 becomes [1, 2, 3, 5]. [1, 2, 3, 4] with n = 2
becomes [1, 2, 4].

Time: O(L). Right walks the list once, left walks the part behind it. L is
the length.
Space: O(1). Two pointers and one extra dummy node.
"""