class CustomStack:

    def __init__(self, maxSize: int):
        self.maxStack = []
        self.size = 0
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        
        if self.size>=self.maxSize:
            return None
        
        self.maxStack.append(x)
        self.size += 1

    def pop(self) -> int:
        if not self.maxStack:
            return -1

        self.size -= 1
        return self.maxStack.pop()

        
        

    def increment(self, k: int, val: int) -> None:
        for j in range(min(k, self.size)):
            self.maxStack[j] += val

        
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)