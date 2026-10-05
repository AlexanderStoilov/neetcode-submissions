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
                

        def divide(lists, l, r): # split the index range in 'lists'
            if l > r: # never happens due to the algorithm, fine as a safeguard
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
        return mergedList #  divide returns the head of the merged list for that range, so mergedList is the head of the whole result
            

"""
Merge k sorted lists by splitting the array of heads in half, recursively, then merging the two halves.

conquer is just the normal merge of two sorted lists. A dummy stays in front, tail links the smaller node, and whichever side remains is attached at the end. If one side is None, the while does not run and the other side is returned. If both are None, the result is None.

divide(lists, l, r) does not cut one linked list into two. It means "merge the heads stored at indexes l through r." (comment edited), The split is on the index range.

mid = l + (r - l) // 2
left = divide(lists, l, mid)
right = divide(lists, mid + 1, r)
return conquer(left, right)

When l == r there is only one head, so it returns lists[l]. That head may itself be None when that list is empty. conquer already knows what to do with None.

l > r is in the function, but the initial call never reaches it. mergeKLists only calls divide(lists, 0, len(lists) - 1) when lists is not empty, so the first call has l <= r. Recursion only happens when l < r. For that range, mid is at least l and at most r - 1, so the left call has l <= mid and the right call has mid + 1 <= r. Both sides still contain at least one index.

An empty input returns None before divide. One list never recurses and returns that head. An odd count just leaves one index on the right side of some call, and that call hits l == r.

divide returns the head of the merged list for its range, so the value that comes back to mergeKLists is already the head of the whole result.

Time: O(N log k). Each level of recursion walks every node once inside conquer, and the depth is about log k. N is the total number of nodes. k is the number of lists.
Space: O(log k). That is the call stack. conquer only keeps a dummy and tail. The result reuses the original nodes.
"""

        