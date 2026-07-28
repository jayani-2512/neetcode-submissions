import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mheap=[]
        for x,y in points:
            d=(x**2)+(y**2)
            mheap.append([d,x,y])
        heapq.heapify(mheap)
        res=[]
        while k>0:
            d,x,y=heapq.heappop(mheap)
            res.append([x,y])
            k-=1
        return res
