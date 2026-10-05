# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Divide and Conquer (Recursion)

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def conquer(left, right): # "conquer" = merge
            dummy = ListNode()
            tail = dummy
            while left and right:
                if left.val <= right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            if left:
                tail.next = left
            elif right:
                tail.next = right
            return dummy.next
                

        def divide(lists, l, r): # divide list into 2
            if l > r:
                return None
            elif l == r:
                return lists[l]
            else:
                mid = l + (r - l) // 2
                left = divide(lists, l, mid)
                right = divide(lists, mid+1, r)
                
                merged = conquer(left, right)
                return merged

        if not lists:
            return None
        
        mergedList = divide(lists, 0, len(lists)-1)
        return mergedList # pointer is its head, so that's it :)
            

        