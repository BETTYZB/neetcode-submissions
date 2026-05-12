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
        map_node = {None:None}
        cur = head
        while cur:
            map_node[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            map_node[cur].next = map_node[cur.next]
            map_node[cur].random = map_node[cur.random]
            cur = cur.next

        return map_node[head]
            
