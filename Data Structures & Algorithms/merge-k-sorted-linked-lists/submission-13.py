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

"""
Merge k sorted lists with a heap that only holds the current head of each list.

The lists are already sorted, so the next node in the result is always one of those heads. After I take one, the only new candidate is the next node from that same list. The heap therefore stays at most k items, not every node.

The tuple version needed a counter:

heappush(heap, (l.val, counter, l))
_, _, min_node = heappop(heap)

(l.val, l) is not enough. When two values are equal, the heap moves to the next part of the tuple and compares the two ListNode objects. ListNode has no less-than, so that raises TypeError. The counter is a plain increasing number sitting between the value and the node, so the tie is decided by the number. _, _, min_node is fine: the second _ overwrites the first, and neither one is used.

ListNode is created by the judge, so it is not in this file and I cannot add __lt__ to it. A wrapper around the node can own the comparison instead, and then the counter is gone:

class ListNodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

The heap stores wrappers and only calls __lt__. If both values are equal, __lt__ is False in both directions and the comparison stops. It never goes on to compare the nodes. Two heads with value 1 push and pop fine. I do not care which equal value comes out first.

class Solution:
    def mergeKLists(self, lists):
        heap = []
        for lst in lists:
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

if lst skips an empty list, since that entry is None. No lists, or every list empty, leaves the heap empty and returns None. One list just comes back out in order. [[1,2,4],[1,3,5],[3,6]] comes back [1,1,2,3,3,4,5,6]. Duplicates such as [1,2,2] and [2] come back [1,2,2,2].

Time: O(N log k). Every node is pushed once and popped once. The heap holds at most one live node from each list, so each push and pop costs log k. N is the total number of nodes. k is the number of lists.
Space: O(k). That is the largest the heap gets, when every list still has a node left. The result reuses the original nodes.
"""
        