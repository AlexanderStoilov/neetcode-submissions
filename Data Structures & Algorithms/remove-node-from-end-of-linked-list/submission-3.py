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

        if n == length: # element to be removed is head
            head = head.next
        else: 
            cur = head
            cur_pos = 1
            while cur_pos < length - n:
                cur = cur.next
                cur_pos += 1
            # the element after ours is the Nth and should be removed
            cur.next = cur.next.next

        return head

"""
Remove Nth Node From End of List (NeetCode / Blind 75).

You get the head of a singly linked list and a number n. Delete the nth node
counting from the end, then return the head. n is always valid: at least 1,
and never bigger than the list.

I counted the nodes first, then walked to the node sitting just before the one
I want to delete, and skipped over it with cur.next = cur.next.next. Counting
from 1, that previous node is at position length - n. The node to delete is
at length - n + 1.

The first version counted correctly, but the delete step was wrong. I started
cur_pos at 0 and only walked while cur_pos + 1 < length - n. If that check
failed, I assumed the node to delete was the head and did head = head.next.

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        cur = head
        cur_pos = 0

        if cur_pos + 1 < length - n:
            while cur_pos + 1 < length - n:
                cur = cur.next
                cur_pos += 1
            cur.next = cur.next.next
        else:
            head = head.next

        return head

That passes a lot of cases. [1, 2, 3, 4, 5] with n = 2 becomes [1, 2, 3, 5].
Removing the real head (n == length) also works, and so does removing the tail.
It breaks when the node to delete is the second node, because then the node
before it is already the head and I do not need to walk. length - n is 1, the
if is false, and the else deletes the head anyway.

[1, 2] with n = 1 should become [1]. This returned [2].
[1, 2, 3, 4, 5] with n = 4 should become [1, 3, 4, 5]. This returned [2, 3, 4, 5].
[1, 2, 3] with n = 2 should become [1, 3]. This returned [2, 3].

The next try only changed the starting number. cur_pos began at 1, and the
check was cur_pos < length - n. Same else branch, same three failures. "I do
not walk forward" is not the same thing as "delete the head."

The fix was to ask the real question: is n equal to the length? Only then is
there no node before the one I am deleting, so I move the head forward. In
every other case I start at the head with cur_pos = 1 and walk while
cur_pos < length - n, then skip the next node. If length - n is 1, the loop
does not run, I stay on the head, and cur.next = cur.next.next removes the
second node. That is the case the earlier else branch was stealing.

One of the later pastes already had that n == length check, with cur and
cur_pos set before the if. It behaves the same as the version I kept. The
final one just creates the cursor inside the else, since the head branch
does not use it.

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        if n == length: # element to be removed is head
            head = head.next
        else:
            cur = head
            cur_pos = 1
            while cur_pos < length - n:
                cur = cur.next
                cur_pos += 1
            # the element after ours is the Nth and should be removed
            cur.next = cur.next.next

        return head

Checked the edges this kept missing, plus the obvious ones: one node, remove
the head, remove the tail, remove the second node, and a node in the middle.
All of those come back right.

Time: O(L), where L is the length of the list. One walk to count, one walk to
the node before the target. n does not add extra work.
Space: O(1). A few variables, no extra list.
"""