class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mheap=nums
        heapq.heapify(mheap)
        while len(mheap)>k:
            heapq.heappop(mheap)
        return mheap[0]