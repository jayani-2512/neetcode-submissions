class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t:t[1])
        mheap=[]
        count=0
        for n,start,end in trips:
            while mheap and mheap[0][0]<=start:
                count-=heapq.heappop(mheap)[1]
            count+=n
            if count>capacity:
                return False
            heapq.heappush(mheap,[end,n])
        return True