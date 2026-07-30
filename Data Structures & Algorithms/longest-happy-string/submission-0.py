class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res=""
        mheap=[]
        for c, ch in [(-a,'a'),(-b,'b'),(-c,'c')]:
            if c!=0:
                heapq.heappush(mheap,(c,ch))
        while mheap:
            c,ch=heapq.heappop(mheap)
            if len(res)>1 and res[-1]==res[-2]==ch:
                if not mheap:
                    break
                c2,ch2=heapq.heappop(mheap)
                res+=ch2
                c2+=1
                if c2:
                    heapq.heappush(mheap,(c2,ch2))
                heapq.heappush(mheap,(c,ch))
            else:
                res+=ch
                c+=1
                if c:
                    heapq.heappush(mheap,(c,ch))
        return res