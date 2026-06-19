class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy=nums1[:m]
        i,j=0,0
        index=0

        while index<n+m:
            if j>=n or (i<m and copy[i]<=nums2[j]):
                nums1[index]=copy[i]
                i+=1
            else:
                nums1[index]=nums2[j]
                j+=1
            index+=1