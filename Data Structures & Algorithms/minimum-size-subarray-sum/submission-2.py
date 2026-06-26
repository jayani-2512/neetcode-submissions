class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        prefixsum=[0]*(n+1)
        for i in range(n):
            prefixsum[i+1]=prefixsum[i] + nums[i]
        
        res=n+1
        for i in range(n):
            l,r=i,n
            while l<r:
                mid=(l+r)//2
                cursum=prefixsum[mid+1]-prefixsum[i]
                if cursum>=target:
                    r=mid
                else:
                    l=mid+1
            if l!=n:
                res=min(res,l-i+1)
        return res%(n+1)