from collections import deque
class Graph:
    
    def __init__(self):
        self.adj = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj:
            self.adj[src] = []
        if dst not in self.adj:
            self.adj[dst] = []

        self.adj[src].append(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj:
            return False
        arr = self.adj[src]
        for i in range(len(arr)):
            if  arr[i] == dst:
                arr[i] = arr[-1]
                arr.pop()
                return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.adj:
            return False

        q = deque()
        visit = set()
        q.append((src))
        visit.add(src)

        while q:
            val = q.popleft()
            if val == dst:
                return True
            neigh = self.adj[val]
            
            for n in neigh:
                if n not in visit:
                    q.append(n)
                    visit.add(n)
        return False