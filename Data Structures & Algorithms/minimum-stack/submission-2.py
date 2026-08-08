class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if len(self.stack) > 0:
            smallest = min(self.getMin(), val)
        else:
            smallest = val
        self.stack.append((val, smallest))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1][0]
        

    def getMin(self) -> int:
        return self.stack[len(self.stack) - 1][1]
        
