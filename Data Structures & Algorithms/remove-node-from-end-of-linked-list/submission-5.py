# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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

