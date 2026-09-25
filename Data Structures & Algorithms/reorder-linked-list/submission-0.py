# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        # Find the middle, at index 'slow'
        slow = head
        fast = head

        while fast and fast.next and fast.next.next: # so 'slow' lands at first half when nr of nodes is even, and at middle when nr of nodes is odd
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                raise ValueError("We have a cycle")
        
        if not slow.next:
            # nr of nodes is 1, so return that head
            return head
        
        # Reverse the second partition, starting from slow+1
        prev = None
        cur = slow.next 

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # Break connection between 1st and 2nd parts
        slow.next = None
        tail = prev

        # Zip the two partitions (zig-zag) - left to right in the left partition + right to left in the right partition, node by node

        dummy = ListNode()
        dummy_cpy = dummy

        while head and tail:
            head_nxt = head.next
            tail_nxt = tail.next
            
            dummy.next = head
            dummy.next.next = tail
            dummy = dummy.next.next

            head = head_nxt
            tail = tail_nxt

        while head: # when nr of elements is odd, head will have one more to take than tail
            dummy.next = head
            head = head.next

        head = dummy_cpy.next # the new head

"""
1 -> 2 -> 3 <-> 4      
     s
          f
                    

1 -> 2 -> 3 <-> 4 <-> 5 
          s
                      f
-----------------------------------------------
o   o   
s
f


o   o   o
    s
        f

o   o   o   o
    s
        f


o   o   o   o   o
        s
                f


o  ->  o  ->  o  <-  o


1 -> 2 -> 3 -> 4 <- 5 <- 6

1   6   2   5

"""