class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        m=0
        for n in nums:
            if m<0:
                m=0
            m+=n
            res=max(res,m)
        return res

