# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            list1, list2 = list2, list1

        prev = list1
        cur = list1
        # list1 is the smallest
        while list1 and list2:
            if list2.val < list1.val:
                nxt = list2.next
                prev.next = list2
                prev.next.next = list1
                prev = list2
                list2 = nxt
            else:
                prev = list1
                list1 = list1.next
        if list2:
            prev.next = list2

        return cur

                
