class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k-1
        res=[]
        while r!=len(nums):
            arr = nums[l:r+1]
            res.append(max(arr))
            l+=1
            r+=1
        return res