class MinStack:
    def __init__(self) :
        self.stack = []
        self.minS = []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        LEN = len(self.minS)
        if not LEN or self.minS[LEN-1] > x :
            self.minS.append(x)
        else :
            self.minS.append(self.minS[LEN-1])
        self.stack.append(x)
        return x

    # @return nothing
    def pop(self):
        self.stack.pop()
        self.minS.pop()

    # @return an integer
    def top(self):
        LEN = len(self.stack) 
        return self.stack[LEN-1]

    # @return an integer
    def getMin(self):
        LEN = len(self.stack) 
        return self.minS[LEN-1]



