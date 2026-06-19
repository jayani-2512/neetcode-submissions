class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        l=0
        for n in num:
            if (n-1) not in num:
                length=1
                while(n+length) in num:
                    length+=1
                l=max(length,l)
        return l
        
                