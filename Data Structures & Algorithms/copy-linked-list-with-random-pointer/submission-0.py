"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 3 -> null -> next
        # 7 -> 4 -> 5

        dummy = Node(0, head)
        dict_new = {None : None}
        cur = head

        while cur:
            if cur not in dict_new:
                dict_new[cur] = Node(cur.val)

            cur = cur.next

        node = head
        while node:
            old = dict_new[node]
            old.next = dict_new[node.next]
            old.random = dict_new[node.random]

            node = node.next

        
        return dict_new[dummy.next]
            


            
