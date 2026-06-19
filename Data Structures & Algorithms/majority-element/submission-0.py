class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for n in nums:
            if nums.count(n)>math.floor(len(nums)/2):
                return n