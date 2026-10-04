# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # really crazy idea, but will be optimal - counting sort (which is O(N) due to the constraints of the values: -10k to 10k)
        SIZE = 20001 # 20001 elements: -10k ... 0 ... 10k included
        counter = [0 for _ in range(SIZE)]
        OFFSET = 10000
        for l in lists:
            while l:
                counter[l.val + OFFSET] += 1
                l = l.next
        
        for i in range(1, len(counter)):
            counter[i] += counter[i-1]
        
        new_arr = [None for _ in range(SIZE)]

        # we're not traversing the elements in reverse (which would require saving them in a big array), so we lose stable sort, but we dont care
        for l in lists:
            while l:
                el = l
                nr_of_lte_el = counter[el.val + OFFSET]
                new_arr[nr_of_lte_el - 1] = el
                counter[el.val + OFFSET] -= 1
                l = l.next

        dummy = ListNode()
        tail = dummy
        i = 0
        while i <= len(new_arr) - 1:
            while new_arr[i] is None:
                i += 1
                if i > len(new_arr) - 1:
                    tail.next = None # With duplicate maximum values, the node you place last is not always an original tail, so its old next points back at a node already in the result.
                    return dummy.next
            tail.next = new_arr[i]
            tail = tail.next
            i += 1
        tail.next = None # same as ^
        return dummy.next


        


