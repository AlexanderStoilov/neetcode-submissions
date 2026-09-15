# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Two pointer approach (slow, fast)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
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

#  