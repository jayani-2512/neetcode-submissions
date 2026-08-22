class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxprofit=[]
        mincap=[(c,p) for c,p in zip(capital,profits)]
        heapq.heapify(mincap)

        for _ in range(k):
            while mincap and mincap[0][0]<=w:
                c,p=heapq.heappop(mincap)
                heapq.heappush(maxprofit,-p)
            if not maxprofit:
                break
            w+=-heapq.heappop(maxprofit)
        return w