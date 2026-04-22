class MinStack:

    def __init__(self):
        self.min_stck = []
        self.minstck = []

    def push(self, val: int) -> None:
        self.min_stck.append(val)
        if self.minstck:
            self.minstck.append(min(self.minstck[-1],val))  
        else:
            self.minstck.append(val)
            
            

    def pop(self) -> None:
        self.min_stck.pop(-1)
        self.minstck.pop(-1)

    def top(self) -> int:
        return self.min_stck[-1]

    def getMin(self) -> int:
        return self.minstck[-1]

        
