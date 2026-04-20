# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        copy_list = self.copyNode(head)
        reverse_list = self.reverseNode(head)
        res = ListNode()
        result = res
        size = self.length(copy_list)
        count = 0
        visit = False
        while count < size:
            if not visit:
                new_node = ListNode(copy_list.val)
                res.next = new_node
                res = new_node
                copy_list = copy_list.next
                visit = True
            else:
                new_node = ListNode(reverse_list.val)
                res.next = new_node
                res = new_node
                reverse_list = reverse_list.next
                visit = False
            count += 1

        
        head.val = result.next.val
        head.next = result.next.next
            
            
            

                


    def reverseNode(self, head):
        pre = None
        curr = head
        while head:
            head = head.next
            curr.next = pre
            pre = curr
            curr = head
        return pre

    def copyNode(self,head):
        node = ListNode()
        curr = node
        while head:
            new_nde = ListNode(head.val)
            node.next = new_nde
            node = new_nde
            head = head.next
        return curr.next

    def length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    
