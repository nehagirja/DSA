class MinStack:

    def __init__(self):
        self.stack = []
        # we need two stacks so that we can perform getMin in O(1) time with O. (n) complexity
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # checking if minStack exists aka if we have any minimum value 
        if self.minStack:
            val = min(val, self.minStack[-1])
        else:
            val = val
        self.minStack.append(val)

    # you can use pop in this function, do not have to customise it    
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()