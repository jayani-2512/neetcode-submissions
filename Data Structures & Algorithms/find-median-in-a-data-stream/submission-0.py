class MedianFinder:

    def __init__(self):
        self.heap=[]

    def addNum(self, num: int) -> None:
        self.heap.append(num)

    def findMedian(self) -> float:
        self.heap.sort()
        n=len(self.heap)
        return (self.heap[n//2] if n%2==1 else (self.heap[n//2]+        self.heap[n//2-1])/2 )
        