class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for n in nums2:
            nums1.append(n)
        nums1.sort()
        n=len(nums1)
        if n%2==1:
            return nums1[n//2]
        else:
            return (nums1[n//2-1]+nums1[n//2])/2