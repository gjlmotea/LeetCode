class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.stack) == 1:
            self.min = x
        else:
            self.min = min(self.min, x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();
minStack.pop();
minStack.top();
minStack.getMin();

##class MinStack:
##    def __init__(self):
##        self.__a = []
##
##    def push(self, x: int) -> None:
##        m = x
##        if self.__a:
##            m = self.__a[-1][1]
##            if m > x:
##                m = x
##        self.__a.append((x, m))
##        print(self.__a)
##
##    def pop(self) -> None:
##        self.__a.pop()
##        print(self.__a)
##        
##    def top(self) -> int:
##        print(self.__a)
##        return self.__a[-1][0]
##
##    def getMin(self) -> int:
##        print(self.__a)
##        return self.__a[-1][1]
