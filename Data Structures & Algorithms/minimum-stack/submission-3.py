class MinStack:

    def __init__(self):
        self.m=float("inf")
        self.stack=[]

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.m=val
        else:
            self.stack.append(val-self.m)
            if val<self.m:
                self.m=val


    def pop(self) -> None:
        if not self.stack:
            return 
        p=self.stack.pop()

        if p<0:
            self.m=self.m-p

    def top(self) -> int:
        t=self.stack[-1]
        if t>0:
            return t+self.m
        else:
            return self.m

    def getMin(self) -> int:
        return self.m
