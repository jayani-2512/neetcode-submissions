class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        res=r
        def ship(mid):
            c=1
            curr=mid
            for n in weights:
                if curr-n<0:
                    c+=1
                    curr=mid
                curr-=n
            return c<=days
        while l<=r:
            mid=(l+r)//2
            if ship(mid):
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res
    

    
