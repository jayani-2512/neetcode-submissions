class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for n in nums:
            c=nums.count(n)
            if c == 1:
                return n
                break