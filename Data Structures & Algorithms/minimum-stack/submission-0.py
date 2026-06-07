class MinStack:

    def __init__(self):
        self.MinStack = []
        

    def push(self, val: int) -> None:
        self.MinStack.append(val)

    def pop(self) -> None:
        self.MinStack.pop()
        

    def top(self) -> int:
        return self.MinStack[-1]
        

    def getMin(self) -> int:
        min = self.MinStack[0]
        for i in self.MinStack:
            if i < min:
                min = i
        return min
