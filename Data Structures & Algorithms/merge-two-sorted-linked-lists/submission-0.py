# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        newH = ListNode()
        copyNewH = newH
        while h1 and h2:
            if h1.val <= h2.val:
                newH.next = h1
                h1 = h1.next
            else:
                newH.next = h2
                h2 = h2.next
            newH = newH.next
        
        while h1:
            newH.next = h1
            h1 = h1.next
            newH = newH.next

        while h2:
            newH.next = h2
            h2 = h2.next
            newH = newH.next

        newH = copyNewH.next
        return newH

                
