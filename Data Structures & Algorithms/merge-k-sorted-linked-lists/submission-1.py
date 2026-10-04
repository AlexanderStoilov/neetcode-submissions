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

# Using the problem’s symbols:
# k = lists.length (number of lists), 0 ≤ k ≤ 10 000
# nᵢ = length of lists[i], 0 ≤ nᵢ ≤ 500
# N = Σᵢ nᵢ (total nodes), N ≤ 10 000

# t.c. O(N log N) - pushing and popping into heap. Heap can grow to size N, meaning each push and pop could cost up to log N
# s.c. O(N)

            
