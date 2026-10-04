# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappush, heappop
        
        heap = []
        counter = count()

        for lst in lists:
            head = lst
            while head:
                heappush(heap, (head.val, next(counter), head))
                head = head.next
        
        dummy = ListNode()
        tail = dummy
        while heap:
            _, _, tail.next = heappop(heap)
            tail = tail.next
        
        return dummy.next

            
