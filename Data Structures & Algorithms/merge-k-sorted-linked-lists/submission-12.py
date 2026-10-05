# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class ListNodeWrapper:
    def __init__(self, node: ListNode | None):
        self.node = node

    def __lt__(self, other: ListNodeWrapper):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for lst in lists: # lst, or the list, is just the first (head) node (of that list)
            if lst:
                heappush(heap, ListNodeWrapper(lst))
        
        dummy = ListNode()
        tail = dummy
        while heap:
            cur_min = heappop(heap).node
            tail.next = cur_min
            tail = tail.next

            if cur_min.next:
                heappush(heap, ListNodeWrapper(cur_min.next))

        return dummy.next


# t.c. O(N. log k) # N - each node will be processed; heap's push and pop are log M for M = size of heap. The size of the heap can be at most k (the number of lists)
# s.c. O(k) # the max size of the heap (if all the lists are non-empty)
        