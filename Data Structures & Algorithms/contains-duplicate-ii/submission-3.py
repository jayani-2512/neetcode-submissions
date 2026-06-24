class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        w=set()
        i=0
        for j in range(len(nums)):
            if j-i>k:
                w.remove(nums[i])
                i+=1
            if nums[j] in w:
                return True
            w.add(nums[j])
        return False


        