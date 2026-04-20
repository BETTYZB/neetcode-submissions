"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
            
        oldToNew = {}
        q = deque()
        oldToNew[node] = Node(node.val)
        q.append(node)

        while q:
            cur = q.popleft()
            for neigh in cur.neighbors:
                if neigh not in oldToNew:
                    oldToNew[neigh] = Node(neigh.val)
                    q.append(neigh)
                
                oldToNew[cur].neighbors.append(oldToNew[neigh])
                    
                
            
        return oldToNew[node]



        