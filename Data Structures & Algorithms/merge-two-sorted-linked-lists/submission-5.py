# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Merge two sorted linked lists — the walk to a clean solution.

First thing I wrote used a dummy node and a tail pointer, which is the standard
trick to avoid special-casing the head. Main loop peeled off the smaller of the
two current nodes:

    dummy = ListNode()
    tail = dummy
    while h1 and h2:
        if h1.val <= h2.val:
            tail.next = h1
            h1 = h1.next
        else:
            tail.next = h2
            h2 = h2.next
        tail = tail.next

Then, since only one list can have leftovers once the loop above ends, I bolted
on two more while loops to drain whichever one still had nodes:

    while h1:
        tail.next = h1
        h1 = h1.next
        tail = tail.next
    while h2:
        tail.next = h2
        h2 = h2.next
        tail = tail.next

    return dummy.next

Worked fine, passed everything, but it bugged me that there were three loops
doing basically the same "attach and advance" motion.

Right after that I tried a different shape just to see it from another angle:
pick the head manually up front instead of using a dummy, then keep going with
one loop:

    if ((list1 and list2) and (list1.val <= list2.val)) or (list1 and not list2):
        newHead = list1
        list1 = list1.next
    elif list2:
        newHead = list2
        list2 = list2.next
    else:
        return None

That elif/else at the bottom is the fail guard for both lists being empty at
the start — without it newHead would stay None and then newNode = newHead
would blow up trying to set .next on None. It worked, but that boolean
condition is nasty to read, and I'm repeating almost the exact same condition
again inside the main loop. Comparing the two approaches side by side made it
obvious the dummy-node version is just structurally simpler — no picking a
head, no fail guard, no repeated condition.

That pushed me to go back and clean up the leftover-draining part of the first
solution. Once the main while loop stops, whichever of h1/h2 is not None is
already a fully sorted chain by itself, so there's no need to walk it node by
node — I can just splice the whole remainder in one shot:

    tail.next = l1 if l1 else l2
    return dummy.next

That collapsed the two drain loops into a single line. Final version:

    dummy = ListNode()
    tail = dummy
    l1 = list1
    l2 = list2
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next

Also poked at the even shorter `tail.next = l1 or l2` form and had to remind
myself that `or` in Python isn't a boolean operator the way it is in C/Java —
it evaluates the first operand, returns it as-is if truthy, otherwise returns
the second operand, no boolean coercion involved. Since a ListNode is truthy
and None is falsy, `l1 or l2` naturally hands back the real remaining node (or
None if both are exhausted), so it's a legit drop-in for the `if/else` version.
Didn't switch to it in the final code, but good to actually understand why it
works instead of just pattern-matching it.

Time complexity: O(n + m), where n and m are the lengths of list1 and list2 —
every node from both lists gets visited and relinked exactly once.

Space complexity: O(1) extra space — no new nodes are allocated, the existing
nodes from list1 and list2 are just rewired into one chain; the dummy node is
a single constant-size helper, not proportional to input size.
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        l1 = list1
        l2 = list2
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return dummy.next
