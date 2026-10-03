# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def rec(head, tail):
            if tail is None:
                return head

            head = rec(head, tail.next)
            if not head:
                return None

            if head == tail or head.next == tail: # If 'head' meets or crosses 'tail'
                tail.next = None
                return None        
            else:
                nxt_head = head.next

                # Tie the "far left -> far right -> left + 1" chain
                head.next = tail
                tail.next = nxt_head

                # Move to next on the left side
                return nxt_head


        rec(head, head.next)


"""
Reorder list, recursive version. Same result as the iterative one: L0, Ln, L1, Ln-1, ... The recursive idea is to walk to the end first, then on the way back pair a node from the back with a node from the front.

First attempt passed the even list [2,4,6,8] and died on the odd list [2,4,6,8,10]:

    def rec(head, cur_tail):
        if cur_tail is None:
            return head
        cur_head = rec(head, cur_tail.next)
        if cur_head == cur_tail or cur_tail.next == cur_head:
            cur_head.next = None
        else:
            nxt_head = cur_head.next
            cur_head.next = cur_tail
            cur_tail.next = nxt_head
            return nxt_head

    rec(head, head.next)

The crash was AttributeError: 'NoneType' object has no attribute 'next', on nxt_head = cur_head.next. I thought the way back was new calls, rec(2,10) then rec(4,8) then rec(6,6), and that 6 meeting 6 would end the whole thing. Those are pairs, not new calls. rec is only called on the way down, and every call is passed the original head. The left node moves because it is the return value.

For [2,4,6,8,10] the call stack is one frame per step toward the end. Indented means "this call is inside the one above it, and that one is paused":

    rec(2, 4)
        rec(2, 6)
            rec(2, 8)
                rec(2, 10)
                    rec(2, None)   return 2

Then Python unwinds. Each paused frame resumes, and head = the value just returned:

                rec(2, 10)   head becomes 2   link 2 → 10 → 4          return 4
            rec(2, 8)    head becomes 4   link 4 → 8 → 6           return 6
        rec(2, 6)    head becomes 6   6 == 6, set 6.next = None   return None
    rec(2, 4)    head becomes None   next line does None.next     crash

So the list was already 2 → 10 → 4 → 8 → 6 → None when it crashed. The 6 == 6 frame had finished its job and returned None, but returning from one frame does not cancel the frames above it. rec(2, 4) was still on the stack, woke up, and treated that None as a node. Even lists only looked fine because the stop happened on the outermost frame, so nobody above it tried to read .next.

The fix is to pass that "we are done" back up, and to cut the right node rather than the left one:

    def rec(head, tail):
        if tail is None:
            return head
        head = rec(head, tail.next)
        if not head:
            return None
        if head == tail or head.next == tail:
            tail.next = None
            return None
        nxt_head = head.next
        head.next = tail
        tail.next = nxt_head
        return nxt_head

if not head: return None is the line that stops the crash. Once some frame returns None, every frame still waiting does the same, until rec(head, head.next) itself returns. On a longer list those extra frames do not link anything. They just forward None. Writing return None in the meet branch is the same as falling off the end of the function. I write it so the stop is obvious.

head == tail is the odd middle: both pointers sit on the last node, so tail.next = None ends the list. head.next == tail is the even meet: the left node already points at the right one, as in 2 → 8 → 4 → 6 when head is 4 and tail is 6. Cutting tail.next keeps 6. Cutting head.next would drop 6.

Names I kept mixing up: the pile of unfinished rec calls is the call stack. One of those calls is a stack frame. if tail is None is the base case. The line head = rec(...) is the recursive call. Code before it is going down. Code after it is unwinding. A callback is a different thing. It is a function you hand off so something else can call it later.

Time complexity: O(n). One frame per node, and each frame does a constant amount of linking.

Space complexity: O(n). The call stack holds a frame for every node until the unwind finishes. The iterative version only keeps a few pointers, so its extra space stays O(1).
"""

"""
Names that match this code:

Call stack: the pile of rec calls that have started and not finished.
Stack frame: one entry on that pile. rec(2, 10) is one frame, rec(2, 8) is another.
Base case: if tail is None: return head. This frame does not call rec again.
Recursive call: head = rec(head, tail.next).
Going down: the calls before that line. tail walks toward the end. head is still the original first node.
Unwinding: the code after that line, as each frame resumes. This is your "getting back" journey.
Return value: what the inner call hands back. You store it in head, so on the way back head moves from the left.
"""


"""
first turn:
1   ->  2   ->  3   ->  4   ->  None
head
                       tail

===>
 1 -> 4 -> [2] ( -> 3 -> 4 -> (2 -> 3 -> 4 -> ...) & None)


second turn: 
1   ->  2   ->  3   ->  4   ->  None
      head
               tail

===>
 1 -> 4 -> [2] -> [[3]] -> 3 -> ...


third turn: 
1   ->  2   ->  3   ->  4   ->  None
               head
       tail

===>
 1 -> 4 -> 2 -> [[3]] -> 
"""
