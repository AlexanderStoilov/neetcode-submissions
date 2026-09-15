# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Merge Two Sorted Lists - dev log

First pass at this: dummy node, walk both lists with a while loop, whichever
node is smaller gets attached to tail.next, tail steps forward. Standard.
for the leftovers I did two extra while loops, one for whatever was left of h1
and one for h2, manually re-walking and re-attaching node by node:

    while h1:
        newH.next = h1
        h1 = h1.next
        newH = newH.next
    while h2:
        newH.next = h2
        h2 = h2.next
        newH = newH.next

worked fine, passed. also tried a second version without a dummy node at all -
manually picked whichever list's head was smaller to be newHead first, then
looped `while list1 or list2` using this condition to decide who to pull from:

    if ((list1 and list2) and (list1.val <= list2.val)) or (list1 and not list2):

also passed, but way uglier. no dummy node meant I had to hand-roll the
"which list starts first" logic AND handle both-empty as a guard clause
(`else: return None`). same boolean mess had to be repeated inside the loop.
simplified later to `list1 and (not list2 or list1.val <= list2.val)` but still,
way more surface area for bugs than just starting with a dummy.

the real realization: once the main while loop exits, one of the two lists is
empty and the other one is ALREADY a sorted chain of nodes with correct .next
pointers - i don't need to walk it node by node, i can just point tail.next at
whatever's left in one line and be done:

    tail.next = l1 if l1 else l2

so the two leftover while loops from the first version were pure waste.
collapsing that plus going back to the dummy-node structure (way less
annoying than picking a head manually) gave the final clean version.

side quest: got curious why `l1 or l2` would also work in place of the
if/else above. turns out `or`/`and` in python don't collapse to True/False -
they short-circuit and return the actual operand. `a or b` returns `a` if `a`
is truthy, otherwise returns `b`, whatever `b` is. a ListNode instance is
truthy, None is falsy, so `l1 or l2` returns a real node or None, never a bool.
same idiom as `name = user_input or "default"`. neat, filed away for later.

final:

    class Solution:
        def mergeTwoLists(self, list1, list2):
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

Time: O(n + m) - single pass, each node from both lists gets visited and
re-linked exactly once, the final splice is O(1) since it's just a pointer
assignment, not a walk.
Space: O(1) - no new nodes allocated, just rewiring .next pointers on the
existing nodes from list1/list2 (the dummy node itself is a constant, not
counted against input size).

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
