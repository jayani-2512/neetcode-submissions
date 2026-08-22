class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=nums1
        b=nums2

        if len(b)<len(a):
            a,b=b,a
        t=len(nums1)+len(nums2)
        half=t//2
        l=0
        r=len(a)
        while True:
            i=(l+r)//2
            j=half-i
            al=a[i-1] if i>0 else float("-inf")
            ar=a[i] if i<len(a) else float("inf")
            bl=b[j-1] if j>0 else float("-inf")
            br=b[j] if j<len(b) else float("inf")
            if al<=br and bl<=ar:
                if t%2==1:
                    return min(ar,br)
                else:
                    return (max(al,bl)+min(ar,br))/2
            elif al>br:
                r=i-1
            else:
                l=i+1