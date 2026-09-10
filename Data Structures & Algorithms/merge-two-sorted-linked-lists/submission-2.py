# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Choosing head
        newHead = None
        if ((list1 and list2) and (list1.val <= list2.val)) or (list1 and not list2):
            newHead = list1
            list1 = list1.next
        elif list2: # Fail guard, because if both lists are empty we should simply stop here
            newHead = list2
            list2 = list2.next
        else:
            return None

        newNode = newHead
        
        # Continuing with the each node taking from the smaller of the two
        while list1 or list2:
            if ((list1 and list2) and (list1.val <= list2.val)) or (list1 and not list2):
                newNode.next = list1
                list1 = list1.next
            else:
                newNode.next = list2
                list2 = list2.next
            newNode = newNode.next

        return newHead

        
