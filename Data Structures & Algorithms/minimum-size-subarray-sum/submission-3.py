class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,s=0,0
        minlen=float('inf')
        for r in range(len(nums)):
            s+=nums[r]
            while s>= target:
                minlen=min(minlen,r-l+1)
                s-=nums[l]
                l+=1
        return 0 if minlen==float('inf') else minlen