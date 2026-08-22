class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(num):
            no=1
            curr=0
            for n in nums:
                curr+=n
                if curr>num:
                    no+=1
                    if no>k:
                        return False
                    curr=n
            return True

        l=max(nums)
        r=sum(nums)
        res=r
        while l<=r:
            mid=l+(r-l)//2
            if cansplit(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
