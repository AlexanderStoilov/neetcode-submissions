# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Heap of only the heads

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappush, heappop
        counter = 0 # to circumvent the heap requirement for a unique val comparator (sequential, left to right (Nodes cannot be compared by their definition above ^ (we could override __lt__ for them to be honest ( we need a new structure for that, like a wrapper, cos the ListNode structure isn't in this file, it comes from the solver judge automatically (spoiler: yes, a wrapper is exactly what sol. 4 "Heap" does))))). BTW another option is to use itertools.count() to initialize an iterator, and then call it via '.next()' 
        heap = []
        for l in lists:
            if l:
                heappush(heap, (l.val, counter, l))
                counter += 1

        # common "dummy, tail, tail connecting, return dummy.next" strategy
        dummy = ListNode()
        tail = dummy
        while heap:
            _, _, min_node = heappop(heap) # is it a problem to have 2 vals with "_", should we use "__" for second?
            tail.next = min_node
            tail = tail.next

            next_node = min_node.next
            if next_node:
                heappush(heap, (next_node.val, counter, next_node))
                counter += 1
        
        return dummy.next


# t.c. O(N.log k) # each node is processed -> N; pushing and popping into the heap is log X where X is size of heap. Size of heap can be at most k (see s.c. below) -> O(log k) ==> O(N.log k)
# s.c. O(k) # at most, the heap could contain the cur node of every one of the k lists