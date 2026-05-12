# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseList(node):
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev
        
        cur = reverseList(head)
        dummy = ListNode(0, cur)
        count = 1
        prev = dummy
    
        while cur:
            if count == n:
                prev.next = cur.next
                break
            count += 1
            prev = cur
            cur = cur.next

        

        return reverseList(dummy.next)
        


            

