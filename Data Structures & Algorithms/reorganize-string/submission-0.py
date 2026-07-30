class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt=Counter(s)
        mheap=[[-c,ch] for ch,c in cnt.items()]
        heapq.heapify(mheap)
        pre=None
        res=""
        while mheap or pre:
            if pre and not mheap:
                return ""
            c,ch=heapq.heappop(mheap)
            res+=ch
            c+=1
            if pre:
                heapq.heappush(mheap,pre)
                pre=None
            if c!=0:
                pre=[c,ch]
        return res