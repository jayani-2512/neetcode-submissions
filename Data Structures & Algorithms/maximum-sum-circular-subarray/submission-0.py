class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gmax=nums[0]
        gmin=nums[0]
        cmax=0
        t=0
        cmin=0
        for n in nums:
            cmax=max(cmax+n,n)
            cmin=min(cmin+n,n)
            t+=n
            gmax=max(gmax,cmax)
            gmin=min(gmin,cmin)
        return max(gmax,t-gmin)if gmax>0 else gmax
      