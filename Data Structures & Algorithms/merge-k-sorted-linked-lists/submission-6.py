# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # t.c. O(n1 + n2) ~ O(n)    , where n1 = len(list1), n2 = len(list2)
        # unfortunately during the big loop in mergeKLists, every time list1 grows in size
        # s.c. O(1)
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
        return dummy.next # new head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        for i in range(1, len(lists)):
            newList = self.mergeTwoLists(lists[i - 1], lists[i])
            lists[i] = newList
        return lists[-1] if len(lists) >= 1 else None

# t.c. O(k * N) worst case, ~ O(N^2) when every list is short
# each merge walks one more list than the last:
# (n0 + n1) + (n0 + n1 + n2) + ... + (n0 + ... + n_{k-1})
# n0 shows up k-1 times, n1 shows up k-1 times, n2 shows up k-2 times, nj for j>= 1 shows up k-j times; last list shows up once
# worst case ~ N^2 / 2 when every list has 1 node

"""
Java:
Optional<T> is a real object on the heap. You wrap with Optional.ofNullable(x), then isPresent(), get(), orElse(...), etc. The value lives inside the box.

Python:
Optional[ListNode] is only a type hint (for you, the IDE, mypy). At runtime there is no Optional wrapper.

A parameter typed Optional[ListNode] is just:

    a ListNode instance,
or
    None

Same as if you wrote ListNode | None (Python 3.10+).
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
"""