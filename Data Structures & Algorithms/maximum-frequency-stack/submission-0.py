class FreqStack:

    def __init__(self):
        self.stack=[]
        self.count=defaultdict(int)
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.count[val]+=1

    def pop(self) -> int:
        high=max(self.count.values())
        n=len(self.stack)-1
        while self.count[self.stack[n]]!=high:
            n-=1
        self.count[self.stack[n]]-=1
        return self.stack.pop(n)

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()