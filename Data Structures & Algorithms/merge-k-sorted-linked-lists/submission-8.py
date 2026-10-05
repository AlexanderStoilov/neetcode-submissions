# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            if not lists:
                return None

            i = 0
            level = []
            for list in lists:
                level.append(list)
            
            next_level = []          
            while len(level) >= 2:
                while level:
                    left = level.pop()
                    right = level.pop() if level else None
                    result = self.mergeTwoLists(left, right)
                    next_level.append(result)

                level = next_level # same references, ONLY ok cos we do next_level = [] below. Check comment below
                next_level = []
                
            return level[0]
        

"""
Merge k sorted lists by pairing them.

mergeTwoLists was already fine. It walks two sorted lists and rewires next pointers into one sorted list. If the second list is missing, the while never runs and it just returns the first list. If both are missing, it returns None.

The slow version merged list 0 into list 1, then that result into list 2, and so on. Early nodes got walked again on almost every later merge, so a lot of short lists timed out. Pairing fixes that. Merge 0 with 1, 2 with 3, and so on. Then do the same thing to those results. Each round cuts the number of lists in half, so a node is walked once per round instead of once per list.

First version of that:

level = []
for list in lists:
    level.append(list)
next_level = []
while level:
    while level:
        left = level.pop()
        right = level.pop() if level else None
        result = self.mergeTwoLists(left, right)
        next_level.append(result)
    level = next_level
    next_level = []
return level[0] if level else None

while level means "keep going while this array is not empty." One finished list is not empty. On [[1,2,4],[1,3,5],[3,6]] the rounds were:

3 lists -> [1,3,3,5,6] and [1,2,4]
2 lists -> [1,1,2,3,3,4,5,6]
1 list  -> mergeTwoLists(that list, None), which returns the same list

The answer was already sitting there. The outer loop put that one list back into level and merged it with None forever. The judge reports that as time limit exceeded.

The stop condition is "stop when a pair is no longer possible":

while len(level) >= 2:

An odd list has no partner, so right is None and mergeTwoLists gives it back unchanged. That is correct. One input list never enters the loop, and the function returns it. An empty input returns None before the loop. [[]] and [[],[]] come back as None.

The line I was nervous about:

level = next_level
next_level = []

A Python list variable is a name for a list object. It is not the nodes, and assigning it does not copy anything.

level = next_level makes both names point at one list. Right then, level is next_level is true. Anything that changes that object shows up under both names.

next_level.append(x) would also appear in level.
next_level.clear() would empty level too.
next_level[:] = [] would empty level too.

next_level = [] is different. It attaches the name next_level to a brand new empty list. The old list is untouched, and level is still pointing at it. After that line the two names are not the same object, so popping level and appending to next_level do not interfere.

Time: O(N log k). Each round walks every node once, and the rounds halve the list count, so there are about log k rounds. N is the total number of nodes. k is the number of lists.
Space: O(k). level and next_level store head references, at most one per list. The merge itself only keeps a few pointers. The result reuses the original nodes.
"""