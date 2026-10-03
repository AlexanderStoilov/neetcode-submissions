# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # recursive
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def rec(cur):
            if cur is None:
                return None, 0

            cur.next, i = rec(cur.next)
            i += 1
            if i == n:
                return cur.next, i
            else:
                return cur, i

        head, i = rec(head)
        return head


"""
Remove Nth Node From End of List, recursive try.

I already had a working two-pass solution. This note is the recursive one,
because I kept losing the count.

The idea: walk to the end first, then count on the way back. When a node's
count equals n, return the node after it so the caller links past it.

First version passed i down and only returned the node:

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rec(cur, i):
            if cur is None:
                return None
            cur.next = rec(cur.next, i)

            i += 1
            if i == n:
                return cur.next
            else:
                return cur

        head = rec(head, 0)
        return head

[1, 2, 3, 4] with n = 2 should become [1, 2, 4]. It came back [1, 2, 3, 4].

i is a normal number, so each call gets its own copy. I called the next node
with the old i, then did i += 1 only in the current call. Every level was
entered with 0 and left with 1. n is 2, so i == n never happened and nothing
was removed. The skip (return cur.next) was fine. The count was not coming
back up.

A shared count outside the function also works, if you add 1 to that same
count on the way back. I did not want a variable living outside rec.

So the next version returns two things: the node to keep, and the count.
I still passed i in:

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rec(cur, i):
            if cur is None:
                return None, i

            cur.next, i = rec(cur.next, i)
            i += 1
            if i == n:
                return cur.next, i
            else:
                return cur, i

        head, i = rec(head, 0)
        return head

This one passes. The line cur.next, i = rec(cur.next, i) throws away the i
I passed down and keeps the i that came back. Then i += 1 and that new i is
returned to the caller. The end of the list just echoes the 0 it was given.
Every call passes 0, so the parameter is only a starting zero.

That means the argument can go. The empty spot returns 0 itself:

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rec(cur):
            if cur is None:
                return None, 0

            cur.next, i = rec(cur.next)
            i += 1
            if i == n:
                return cur.next, i
            else:
                return cur, i

        head, i = rec(head)
        return head

Same walk. For [1, 2, 3, 4] and n = 2: 4 comes back as count 1 and stays.
3 comes back as count 2, so it returns 4 and drops itself. 2 sets its next
to 4. 1 stays. Result is [1, 2, 4].

If the removed node is the head, the outer call gets cur.next back and that
becomes head. One node with n = 1 returns None. Removing the last node makes
the node before it point at None. Removing the second node stays on the head
and returns the head's next from that second call, so the head links over it.

Time: O(L), one walk to the end and back. L is the length of the list.
Space: O(L). Each node waits on the call stack until the end is reached.
The two-pass version only needs a few variables, so that one is O(1) extra memory.
"""