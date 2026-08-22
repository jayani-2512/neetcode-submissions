class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n=mountainArr.length()
        cache={}
        def get(i):
            if i not in cache:
                cache[i]=mountainArr.get(i)
            return cache[i]
        
        l=0
        r=n-1
        while l<r:
            mid=(l+r)//2
            if get(mid)<get(mid+1):
                l=mid+1
            else:
                r=mid
        peak=l

        l=0
        r=peak
        while l<=r:
            mid=(l+r)//2
            if get(mid)==target:
                return mid
            elif get(mid)<target:
                l=mid+1
            else:
                r=mid-1
        l=peak+1
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if get(mid)==target:
                return mid
            elif get(mid)<target:
                r=mid-1
            else:
                l=mid+1
        return -1
