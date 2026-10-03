# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def rec(head, tail):
            if tail is None:
                return head

            head = rec(head, tail.next)
            if not head:
                return None

            if head == tail or head.next == tail: # If 'head' meets or crosses 'tail'
                tail.next = None
                return None        
            else:
                nxt_head = head.next

                # Tie the "far left -> far right -> left + 1" chain
                head.next = tail
                tail.next = nxt_head

                # Move to next on the left side
                return nxt_head


        rec(head, head.next)


"""
first turn:
1   ->  2   ->  3   ->  4   ->  None
head
                       tail

===>
 1 -> 4 -> [2] ( -> 3 -> 4 -> (2 -> 3 -> 4 -> ...) & None)


second turn: 
1   ->  2   ->  3   ->  4   ->  None
      head
               tail

===>
 1 -> 4 -> [2] -> [[3]] -> 3 -> ...


third turn: 
1   ->  2   ->  3   ->  4   ->  None
               head
       tail

===>
 1 -> 4 -> 2 -> [[3]] -> 
"""
