class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        u=sorted(set(nums))
        nums[:len(u)]=u
        return len(u)
