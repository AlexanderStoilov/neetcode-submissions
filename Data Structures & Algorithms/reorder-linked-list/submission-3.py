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
Reorder list: L0 → Ln → L1 → Ln-1 → …  Three steps in the end: find the split,
reverse the second half, weave. Getting there was mostly about not creating a
cycle, and not treating a singly linked list like you can walk it from both
ends without reversing first.

First draft found the middle with slow/fast, then reversed starting with
prev = slow (the middle node itself). That flips 4.next onto 3 while 3.next
is still 4:

    prev = slow
    cur = slow.next
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

Never cut slow.next, so you get 3 ↔ 4 before zip even starts. Zip used a
toggle and stopped when the two cursors met or were one apart:

    while head != tail and head.next != tail:
        ...
        take_from_left = not take_from_left

That only stops YOUR loop. It does not delete 3 → 4. Judge walks .next to
check the answer, never hits None → timeout. Thought the stop condition was
the safety net; it isn't.

Tried to break the leftover edge at the end instead:

    if head.next == tail:
        tail.next = None
    else:
        head.next = None

Assumed head.next == tail means even. On 1..5 the zip while exits with
head=3, tail=4 because 3.next == 4, so the "even" branch runs, 4.next = None,
and 3 falls off the list: 1 → 5 → 2 → 4 → None. Real issue under that: the
while refused one more iteration, so the middle node never got linked by zip
and only survived via the reverse edge 4 → 3. Wrong stop question (two
pointers closing a gap) for this problem (merge two chains).

Rewrite that actually passed: prev = None, reverse from slow.next, THEN cut,
dummy-zip while both halves exist, leftover first-half node for odd:

    prev, cur = None, slow.next
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    slow.next = None
    ...
    while head and tail:
        ...
    while head:
        dummy.next = head
        head = head.next
    head = dummy_cpy.next

Dummy works but is extra — result still starts at the original head node.
Rebinding local head does nothing for the caller; they still hold node 1.
Leftover while is at most one node, so it's really an if. Cycle raise in
middle-find was leftover from the other problem and never fires here.

In-place zip without dummy is the same merge. Hit a SyntaxError on
prev, cur: ListNode = None, slow.next (can't annotate an unpack), which hid
the actual bug: prev, cur = cur, next — next is the builtin, so reverse
silently pointed cur at a function. Needed nxt.

Also had the odd case wrong in my head: pictured 1 → 2 → 3 ← 4 ← 5 and a
third merge iteration doing 3.next = 3 then 3.next = None. After the cut
you have 1 → 2 → 3 → None and 5 → 4 → None. while second stops when
second is None; node 3 is never second. Getting the "point at the middle"
drawing is easy (reverse with prev = slow, then slow.next = None) but it
doesn't make zip simpler — still no prev pointers on the first half.

Final version:

    if not head or not head.next:
        return
    slow, fast = head, head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    prev, cur = None, slow.next
    slow.next = None
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    first, second = head, prev
    while second:
        nxt1, nxt2 = first.next, second.next
        first.next = second
        second.next = nxt1
        first, second = nxt1, nxt2

fast.next.next is so slow lands at end of first half (even) or on the middle
(odd). Second half is shorter-or-equal. Loop while second remains; odd
middle already sits at the end of first with .next is None.

Time complexity: O(n). One pass to the middle, one to reverse the back half,
one to weave — each node is touched a constant number of times.

Space complexity: O(1) extra. Only a handful of pointers. Nodes are relinked
in place, no array of values / nodes.
"""

"""
1   2   3   4
    s
        f

1   2   3   4   5
        s
                f

"""