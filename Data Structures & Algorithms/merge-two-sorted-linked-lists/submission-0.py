# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        ans = curr
        val = 0
        while list1 and list2:
            if list1.val <= list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next
            node = ListNode(val, None)
            curr.next = node
            curr = node

        if list2:
            curr.next = list2
        else:
            curr.next = list1
            
        return ans.next



