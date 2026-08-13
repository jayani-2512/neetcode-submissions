class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        Max=1
        Min=1
        for n in nums:
            tmp=n*Max
            Max=max(tmp,n*Min,n)
            Min=min(tmp,n*Min,n)
            res=max(res,Max)
        return res