# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0

        def rec(cur):
            nonlocal i

            if cur is None:
                return None

            cur.next = rec(cur.next)
            i += 1
            if i == n:
                return cur.next
            else:
                return cur

        head = rec(head)
        return head

