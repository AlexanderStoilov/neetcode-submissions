# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


"""
Linked list cycle detection — Floyd's tortoise and hare, after a couple of false starts.

Went straight for the two-pointer approach: slow moves one step, fast moves two.
First version had both starting at head and used a first_turn flag so the loop
wouldn't bail immediately on slow == fast:

    slow = head
    fast = head
    first_turn = True
    while slow != fast or first_turn:
        first_turn = False
        if slow:
            slow = slow.next
        else:
            return False
        if fast and fast.next:
            fast = fast.next.next
        else:
            return False
    return True

It passed, but felt clunky — first_turn is basically patching the fact that both
pointers start on the same node, so equality at the start doesn't mean a cycle.

Before the guards were in place I was just doing slow = slow.next and
fast = fast.next.next blindly. That blew up on acyclic lists: fast eventually
hits None, and the next iteration tries fast.next on None → AttributeError. Same
reason you can't skip the null checks entirely; you need some way to detect
"we ran off the end, no cycle."

Drafted a cleaner second version that sidesteps the first_turn hack by starting
fast one step ahead and folding the null safety into the loop condition:

    if not head:
        return False
    slow = head
    fast = head.next
    while slow != fast and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow == fast

That also passed. The while condition does double duty — keep going while they
haven't met AND fast can still take two steps. The final return slow == fast
catches the single-node-self-loop case where they're already equal before the
loop body ever runs.

Ended up submitting the even more common variant instead — both start at head,
but only treat equality as a cycle after moving inside the loop:

    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

No first_turn, no offset start, no return slow == fast at the end. The while
guard (fast and fast.next) is the null safety; if fast can't advance two steps
we're at the tail of a list with no cycle. The if slow == fast inside the loop
is the only place we declare a cycle, so starting equal doesn't matter because
we move before we check.

Time complexity: O(n) — in a list with n nodes, fast moves at twice slow's
rate; either it hits the end in at most n steps (no cycle) or the two pointers
meet inside the cycle within O(n) steps.

Space complexity: O(1) — only two pointer variables, no hash set of visited
nodes.
"""

"""
Why slow and fast MUST meet within n steps if a cycle exists (Floyd's proof sketch).

Setup: n nodes total. If there's a cycle, split the list into:
  - L = nodes before the cycle starts (the "tail"), L >= 0
  - C = cycle length, C >= 1

  -  -  -  -  -  -
           |     |
            -  -

  So n = L + C (nodes in tail + nodes in cycle; cycle nodes are counted once).

Claim: from the start, slow and fast meet after at most n slow-steps.

Step 1 — slow reaches the cycle entrance in at most L steps.
  slow moves 1 per iteration, so after L iterations it's at the first cycle node.

Step 2 — once slow is inside the cycle, fast is already inside too.
  When slow has taken L steps, fast has taken 2L steps.
  2L >= L (for L >= 0), so fast is at least as far as the cycle entrance.
  It can't be "still on the tail" when slow has just entered the cycle.

Step 3 — inside the cycle, fast closes on slow by 1 node per iteration.
  Each loop body: slow += 1, fast += 2 (relative to slow, fast gains 1).
  View positions on the cycle as 0 .. C-1 clockwise.
  Let d = how many forward steps slow would need to reach fast's node (mod C).
  After one iteration, both advance, but fast advances one more than slow,
  so d shrinks by 1 (mod C): d, d-1, d-2, ... until d = 0 → they meet.

  d starts somewhere in {0, 1, ..., C-1}. It can't stay stuck above 0 forever
  because we subtract 1 each step. So they meet within at most C iterations
  after slow enters the cycle.

  (If d = 0 the moment slow enters, they're already meeting — that's the
  self-loop / already-aligned case; still ≤ C.)

Step 4 — add it up.
  At most L steps to enter the cycle + at most C steps inside = L + C = n.

So: no cycle → fast hits None within O(n) steps (fast reaches the end).
     cycle   → meet within at most n slow-steps.

That's O(n) time and O(1) space — no need to remember visited nodes.
"""