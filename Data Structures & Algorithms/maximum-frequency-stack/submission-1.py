class FreqStack:

    def __init__(self):
        self.count={}
        self.maxc=0
        self.group={}

    def push(self, val: int) -> None:
        c=1+self.count.get(val,0)
        self.count[val]=c
        if c>self.maxc:
            self.maxc=c
            self.group[c]=[]
        self.group[c].append(val)

    def pop(self) -> int:
        res=self.group[self.maxc].pop()
        self.count[res]-=1
        if not self.group[self.maxc]:
            self.maxc-=1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()