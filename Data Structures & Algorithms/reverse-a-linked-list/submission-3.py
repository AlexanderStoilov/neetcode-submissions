# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Recursive

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head or not head.next:  # executes only once, at the end; 'not cur' is guard clause for None check
                return head
            new_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return new_head

"""
Did the iterative reverse first (stash nxt, point head at cur, slide both).
This is the same flip, but we walk to the end with recursion and rewire
on the way back.

First recursive try assigned the last node into a name that never left
the helper:

    def rec(cur):
        if not cur.next:
            new_head = cur
            return
        rec(cur.next)
        cur.next.next = cur

    new_head = None
    rec(head)
    head.next = None
    return new_head

The pointers were already 3 -> 2 -> 1 after that. new_head = cur inside
rec was a local. The outer new_head stayed None, so we returned None.

Fix was return the last node up the stack:

    def rec(cur):
        if not cur.next:
            return cur
        new_head = rec(cur.next)
        cur.next.next = cur
        return new_head

    new_head = rec(head)
    head.next = None
    return new_head

That worked on 1 -> 2 -> 3 locally. NeetCode also sends head = None.
if not cur.next does None.next and raises AttributeError. Local script
never built an empty list. Guard is if not head or not head.next —
None check first so the or short-circuits. Same if covers a single
node: already reversed, return it.

Dropped the nested helper and null each node's old next in its own
frame instead of only the original head at the end:

    if not head or not head.next:
        return head
    new_head = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return new_head

The part that stays hard: we do not reverse on the way down. We ask
"reverse everything after me" and only then touch this node.

    1 -> 2 -> 3 -> None

    reverseList(1) waits on reverseList(2)
    reverseList(2) waits on reverseList(3)
    reverseList(3) hits the guard, returns 3

    now head is 2: 2.next is still 3
        2.next.next = 2    →  3.next = 2
        2.next = None      →  3 -> 2 -> None
        return 3

    now head is 1: 1.next is still 2
        1.next.next = 1    →  2.next = 1
        1.next = None      →  3 -> 2 -> 1 -> None
        return 3

new_head is always that same last node. Each frame only turns one
forward link around and clears its own next so we do not leave a cycle
(2 <-> 3) sitting there.

Time:  O(n) — one call per node, constant work after it returns.
Space: O(n) — call stack is the whole list. Iterative was O(1) extra.
"""

""" # For testing:

from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    ...

c = ListNode(3)
b = ListNode(2, c)
a = ListNode(1, b)

s = Solution()
s.printList(a)
print()

newHead = s.reverseList(a)
s.printList(newHead)
print()
s.printList(a)
print()

"""